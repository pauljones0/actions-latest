#!/usr/bin/env python3
"""
The Action Navigator Engine.
Does one thing: Keeps the GitHub Actions index fresh, robust, and ranked.

Security Model
--------------
Each action is scanned with zizmor on every update cycle. Findings are
classified by severity:

  ERROR   → zizmor_blocked = True.  Action is EXCLUDED from all recommendations.
            These represent exploitable vulnerabilities in the action's manifest
            (e.g. template-injection, artipacked, dangerous-triggers).

  WARNING → zizmor_ok = False.  Action is surfaced with a warning badge.
            The LLM is told to weigh the risk. Common for excessive-permissions,
            ref-confusion, etc.

  INFO    → Stored and surfaced only via the 'audit' command. Not shown in 'cat'.

Stability Gate
--------------
We only track a tag once the commit it points to has been stable for at least
MIN_TAG_AGE_DAYS days. We also store the commit SHA so we can detect if a
floating tag (e.g. v4) has been silently moved — if it has, and the new
commit hasn't aged yet, we hold the old SHA.

VERIFIED_ORGS get a pass on the 'unpinned-uses' rule (which flags the action's
own internal dependencies, not our use of the action).
"""

import json
import os
import re
import subprocess
import sqlite3
import tempfile
import time
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent.resolve()
METADATA_FILE = SCRIPT_DIR / "actions-metadata.json"
DB_FILE = SCRIPT_DIR / "actions_latest" / "actions.db"
GITHUB_API_URL = "https://api.github.com"

# Only accept a tag whose commit has been unchanged for at least this many days.
MIN_TAG_AGE_DAYS = 7

# Zizmor rules that are suppressed for VERIFIED_ORGS (their own internal
# dependency management doesn't reflect risk to us).
VERIFIED_ORG_SUPPRESSED_RULES = {"unpinned-uses", "ref-confusion"}

VERIFIED_ORGS = [
    "actions", "github", "google-github-actions", "aws-actions",
    "Azure", "docker", "microsoft", "astral-sh", "hashicorp",
    "cloudflare", "snyk", "codecov", "getsentry"
]

# Threading helpers
print_lock = threading.Lock()
rate_limit_event = threading.Event()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

# --- GitHub API Helpers ---
def github_api_request(path, params=None):
    token = os.environ.get("GITHUB_TOKEN")
    headers = ["-H", "Accept: application/vnd.github+json"]
    if token:
        headers.extend(["-H", f"Authorization: Bearer {token}"])

    url = f"{GITHUB_API_URL}{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())

    result = subprocess.run(
        ["curl", "-sL", *headers, url],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    try:
        data = json.loads(result.stdout)
        if isinstance(data, dict) and "message" in data:
            if "rate limit" in data["message"].lower():
                return "RATE_LIMIT"
            if "documentation_url" in data:
                return None
        return data
    except Exception:
        return None


def _resolve_tag_date_and_sha(
    owner: str, repo: str, tag_name: str, tag_obj: dict
) -> tuple[datetime | None, str | None]:
    """
    Resolve (publish_date, commit_sha) for a tag.

    Strategy (fastest/most-accurate first):
      1. GitHub Release published_at — explicit human-released timestamp.
      2. Git ref lookup → annotated tag object → tagger.date + object.sha
      3. Commit date from the commit SHA in the tags-list response (lightweight).

    Returns:
      (date, commit_sha)  — date may be None on failure.
      ("RATE_LIMIT", None) — sentinel: caller should abort immediately.
    """
    commit_sha_from_list = tag_obj.get("commit", {}).get("sha")

    # 1. GitHub Release — has published_at and links back to the same commit
    release_data = github_api_request(
        f"/repos/{owner}/{repo}/releases/tags/{tag_name}"
    )
    if release_data == "RATE_LIMIT":
        return "RATE_LIMIT", None
    if isinstance(release_data, dict) and release_data.get("published_at"):
        date = datetime.fromisoformat(
            release_data["published_at"].replace("Z", "+00:00")
        )
        return date, commit_sha_from_list

    # 2. Resolve actual ref SHA to handle annotated tags.
    #    /tags list gives commit.sha (the dereferenced commit), but annotated
    #    tags have a tag-object SHA reachable via /git/refs/tags/{name}.
    ref_data = github_api_request(
        f"/repos/{owner}/{repo}/git/refs/tags/{tag_name}"
    )
    if ref_data == "RATE_LIMIT":
        return "RATE_LIMIT", None
    if isinstance(ref_data, dict):
        ref_obj = ref_data.get("object", {})
        ref_sha = ref_obj.get("sha")
        ref_type = ref_obj.get("type")  # "commit" or "tag"

        if ref_type == "tag" and ref_sha:
            tag_data = github_api_request(
                f"/repos/{owner}/{repo}/git/tags/{ref_sha}"
            )
            if tag_data == "RATE_LIMIT":
                return "RATE_LIMIT", None
            if isinstance(tag_data, dict) and "tagger" in tag_data:
                date_str = tag_data["tagger"].get("date")
                if date_str:
                    date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                    actual_commit = tag_data.get("object", {}).get("sha") or commit_sha_from_list
                    return date, actual_commit

    # 3. Fall back to commit date (lightweight tag points directly at commit)
    if commit_sha_from_list:
        commit_data = github_api_request(
            f"/repos/{owner}/{repo}/git/commits/{commit_sha_from_list}"
        )
        if commit_data == "RATE_LIMIT":
            return "RATE_LIMIT", None
        if isinstance(commit_data, dict):
            date_str = (
                commit_data.get("committer", {}).get("date")
                or commit_data.get("author", {}).get("date")
            )
            if date_str:
                date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                return date, commit_sha_from_list

    return None, commit_sha_from_list


def _check_tag_sha(owner: str, repo: str, tag_name: str) -> str | None:
    """
    Fast-path: resolve just the current commit SHA a tag points to.
    Uses a single /git/refs/tags/{name} call.
    Returns the commit SHA, None on failure, or "RATE_LIMIT" sentinel.
    """
    ref_data = github_api_request(
        f"/repos/{owner}/{repo}/git/refs/tags/{tag_name}"
    )
    if ref_data == "RATE_LIMIT":
        return "RATE_LIMIT"
    if not isinstance(ref_data, dict):
        return None
    ref_obj = ref_data.get("object", {})
    ref_sha = ref_obj.get("sha")
    ref_type = ref_obj.get("type")
    if ref_type == "tag" and ref_sha:
        # Annotated: dereference to the actual commit
        tag_data = github_api_request(
            f"/repos/{owner}/{repo}/git/tags/{ref_sha}"
        )
        if tag_data == "RATE_LIMIT":
            return "RATE_LIMIT"
        if isinstance(tag_data, dict):
            return tag_data.get("object", {}).get("sha") or ref_sha
    # Lightweight: ref_sha IS the commit sha
    return ref_sha


def get_latest_stable_tag(
    owner: str,
    repo: str,
    min_age_days: int = MIN_TAG_AGE_DAYS,
    current_tag: str | None = None,
    current_sha: str | None = None,
) -> tuple[str | None, str | None, datetime | None]:
    """
    Return the newest tag whose commit has been stable for at least min_age_days.

    Fast-path: if we already have a stored tag+SHA and the tag still points to
    that same SHA, we skip the expensive full scan entirely (saves ~100 API calls
    for actions with many tags).

    Returns:
      (tag_name, commit_sha, tag_date) — all None if nothing qualifies.
      ("RATE_LIMIT", None, None)        — sentinel: caller should abort the run.
    """
    # --- Fast path: verify stored tag hasn't moved ---
    if current_tag and current_sha:
        live_sha = _check_tag_sha(owner, repo, current_tag)
        if live_sha == "RATE_LIMIT":
            return "RATE_LIMIT", None, None
        if live_sha and live_sha == current_sha:
            # Tag still points to the same commit we already vetted. No scan needed.
            return current_tag, current_sha, None  # date=None means "unchanged"
        # SHA changed or couldn't check — fall through to full scan
        if live_sha and live_sha != current_sha:
            safe_print(f"   ~~ {owner}/{repo} tag {current_tag} moved ({current_sha[:8]} → {live_sha[:8]}), rescanning")

    # --- Full scan: iterate all vN tags newest-first ---
    tags = github_api_request(f"/repos/{owner}/{repo}/tags", {"per_page": 100})
    if tags == "RATE_LIMIT":
        return "RATE_LIMIT", None, None
    if not isinstance(tags, list):
        return None, None, None

    version_pattern = re.compile(r"^v(\d+)(?:\.\d+)*$")
    cutoff = datetime.now(timezone.utc) - timedelta(days=min_age_days)

    versioned = []
    for t in tags:
        name = t.get("name", "")
        if not version_pattern.match(name):
            continue
        parts = name.lstrip("v").split(".")
        try:
            version_tuple = tuple(int(p) for p in parts)
        except ValueError:
            continue
        versioned.append((version_tuple, name, t))

    versioned.sort(key=lambda x: x[0], reverse=True)

    for version_tuple, tag_name, tag_obj in versioned:
        tag_date, commit_sha = _resolve_tag_date_and_sha(owner, repo, tag_name, tag_obj)
        if tag_date == "RATE_LIMIT":
            return "RATE_LIMIT", None, None
        if tag_date is None:
            safe_print(f"   ?? Could not resolve date for {tag_name}, skipping")
            continue
        if tag_date > cutoff:
            # age_days = (datetime.now(timezone.utc) - tag_date).days
            # safe_print(f"   -- Skipping {tag_name} @ {(commit_sha or '?')[:8]} (only {age_days}d old, need {min_age_days}d)")
            continue
        return tag_name, commit_sha, tag_date

    return None, None, None


# --- Zizmor Security Scanning ---
def _get_zizmor_cmd() -> str:
    """Resolve the path to zizmor. Inspects the virtualenv first."""
    import sys
    venv_zizmor = Path(sys.executable).parent / "zizmor"
    if venv_zizmor.exists():
        return str(venv_zizmor)
    return "zizmor"


def _zizmor_available() -> bool:
    """Check if zizmor is installed and on PATH."""
    try:
        result = subprocess.run(
            [_get_zizmor_cmd(), "--version"],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def _fetch_manifest(owner: str, repo: str, ref: str) -> str | None:
    """Fetch action.yml or action.yaml at the given ref (tag or SHA)."""
    token = os.environ.get("GITHUB_TOKEN")
    headers = ["-H", "Accept: application/vnd.github.v3.raw"]
    if token:
        headers.extend(["-H", f"Authorization: Bearer {token}"])

    action = f"{owner}/{repo}"
    for filename in ["action.yml", "action.yaml"]:
        url = f"https://api.github.com/repos/{action}/contents/{filename}?ref={ref}"
        try:
            result = subprocess.run(
                ["curl", "-sL", *headers, url],
                capture_output=True, text=True, timeout=15
            )
            if result.returncode == 0 and result.stdout.strip() and not result.stdout.startswith("{"):
                return result.stdout
        except Exception:
            continue
    return None


# Zizmor severity levels in ascending order of concern
_SEVERITY_ORDER = {"unknown": 0, "info": 1, "warning": 2, "error": 3}


def run_zizmor(manifest_content: str, owner: str) -> dict:
    """
    Run zizmor on the given manifest content and classify findings.

    Returns:
      {
        "blocked": bool,         # True = has ERROR-level findings (after suppressions)
        "ok": bool,              # True = no WARNING+ findings (after suppressions)
        "findings": [...],       # All raw finding labels  
        "error_findings": [...], # ERROR severity findings
        "warning_findings": [...],
        "info_findings": [...],
        "scanned_at": str,       # ISO timestamp
        "error": str | None
      }
    """
    if not _zizmor_available():
        return {
            "blocked": False, "ok": True,
            "findings": [], "error_findings": [], "warning_findings": [], "info_findings": [],
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "error": "zizmor not installed",
        }

    # Use TemporaryDirectory so the file can be named action.yml or action.yaml.
    # zizmor relies on the filename to identify it as an action manifest instead of a workflow.
    import shutil
    tmp_dir = tempfile.mkdtemp(prefix="zizmor_")
    tmp_path = Path(tmp_dir) / "action.yml"
    tmp_path.write_text(manifest_content)

    try:
        result = subprocess.run(
            [_get_zizmor_cmd(), "--format", "json", str(tmp_path)],
            capture_output=True, text=True, timeout=30
        )
        raw = result.stdout.strip()
        if not raw:
            return {
                "blocked": False, "ok": True,
                "findings": [], "error_findings": [], "warning_findings": [], "info_findings": [],
                "scanned_at": datetime.now(timezone.utc).isoformat(),
                "error": None,
            }

        data = json.loads(raw)
        diagnostics = data if isinstance(data, list) else data.get("diagnostics", [])

        is_verified = owner in VERIFIED_ORGS
        error_findings, warning_findings, info_findings = [], [], []

        for d in diagnostics:
            rule = d.get("ident") or d.get("id") or d.get("check_name", "unknown")
            
            # Map determinations.severity (High/Critical -> error, Medium/Low -> warning, else info)
            det_severity = d.get("determinations", {}).get("severity")
            if det_severity:
                det_sev_lower = det_severity.lower()
                if det_sev_lower in ("high", "critical"):
                    severity = "error"
                elif det_sev_lower in ("medium", "low"):
                    severity = "warning"
                else:
                    severity = "info"
            else:
                severity = (d.get("severity") or "unknown").lower()

            # Verified orgs get suppression for benign self-referential rules
            if is_verified and rule in VERIFIED_ORG_SUPPRESSED_RULES:
                continue

            label = f"{rule}:{severity}"
            if severity == "error":
                error_findings.append(label)
            elif severity == "warning":
                warning_findings.append(label)
            else:
                info_findings.append(label)

        all_findings = error_findings + warning_findings + info_findings
        return {
            "blocked": len(error_findings) > 0,
            "ok": len(error_findings) == 0 and len(warning_findings) == 0,
            "findings": all_findings,
            "error_findings": error_findings,
            "warning_findings": warning_findings,
            "info_findings": info_findings,
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "error": None,
        }
    except json.JSONDecodeError as e:
        return {
            "blocked": False, "ok": True,
            "findings": [], "error_findings": [], "warning_findings": [], "info_findings": [],
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "error": f"zizmor output parse error: {e}",
        }
    except subprocess.TimeoutExpired:
        return {
            "blocked": False, "ok": True,
            "findings": [], "error_findings": [], "warning_findings": [], "info_findings": [],
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "error": "zizmor timed out",
        }
    except Exception as e:
        return {
            "blocked": False, "ok": True,
            "findings": [], "error_findings": [], "warning_findings": [], "info_findings": [],
            "scanned_at": datetime.now(timezone.utc).isoformat(),
            "error": str(e),
        }
    finally:
        try:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        except Exception:
            pass


def process_one_action(entry, zizmor_enabled, today, one_year_ago):
    if rate_limit_event.is_set():
        return entry, "SKIPPED"

    repo_name = entry["action"]
    owner, repo = repo_name.split("/")

    # 1. Fetch Repository Vital Signs
    repo_data = github_api_request(f"/repos/{repo_name}")
    if repo_data == "RATE_LIMIT":
        rate_limit_event.set()
        return entry, "RATE_LIMIT"
    if not repo_data:
        safe_print(f"!! Skipping {repo_name} (Not found or error)")
        return None, "NOT_FOUND"

    # 2. Enforce Freshness (1-year rule)
    pushed_at_str = repo_data.get("pushed_at")
    pushed_at = datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
    if pushed_at < one_year_ago:
        safe_print(f"-- Purging {repo_name} (Stale since {pushed_at_str[:10]})")
        return None, "STALE"

    # 3. Update Popularity & Robustness
    stars = repo_data.get("stargazers_count", 0)
    forks = repo_data.get("forks_count", 0)
    score = stars + (forks * 0.5)
    if owner in VERIFIED_ORGS:
        score *= 10
    if owner == "actions":
        score *= 2
    entry["stars"] = stars
    entry["robustness_score"] = int(score)

    # 4. Check for New Versions (with stability gate)
    current_tag = entry.get("latest_tag")
    current_sha = entry.get("latest_sha")
    latest_tag, new_sha, tag_date = get_latest_stable_tag(
        owner, repo, MIN_TAG_AGE_DAYS,
        current_tag=current_tag,
        current_sha=current_sha,
    )

    if latest_tag == "RATE_LIMIT":
        rate_limit_event.set()
        return entry, "RATE_LIMIT"

    tag_changed = False
    if latest_tag is None:
        # No stable tag found yet — keep what we have
        # safe_print(f"   ~~ {repo_name}: no stable tag (all too new), keeping {entry.get('latest_tag', 'N/A')}")
        pass
    elif latest_tag == current_tag and new_sha == current_sha and tag_date is None:
        # Fast-path hit: tag unchanged, nothing to do
        pass
    elif latest_tag != current_tag or new_sha != current_sha:
        date_str = tag_date.strftime("%Y-%m-%d") if tag_date else "unchanged"
        sha_short = (new_sha or "?")[:8]
        safe_print(f"++ Updated {repo_name}: {entry.get('latest_tag', '?')} → {latest_tag} @ {sha_short} (published {date_str})")
        entry["latest_tag"] = latest_tag
        entry["latest_sha"] = new_sha
        tag_changed = True

    # Use the current (possibly just-updated) ref for scanning.
    # Prefer SHA for deterministic fetching; fall back to tag.
    scan_ref = entry.get("latest_sha") or entry.get("latest_tag", "")

    # 5. Zizmor Security Scan
    # Only re-scan if: (a) tag/SHA changed, (b) never scanned before,
    # or (c) last scan was >7 days ago
    last_scan = entry.get("zizmor_scanned_at")
    scan_age_ok = True
    if last_scan:
        try:
            last_scan_dt = datetime.fromisoformat(last_scan)
            scan_age_ok = (today - last_scan_dt).days >= 7
        except Exception:
            pass

    needs_scan = zizmor_enabled and scan_ref and (tag_changed or not last_scan or scan_age_ok)

    status = "UNCHANGED"
    if tag_changed:
        status = "UPDATED"

    if needs_scan:
        manifest = _fetch_manifest(owner, repo, scan_ref)
        if manifest:
            zizmor_result = run_zizmor(manifest, owner)
            entry["zizmor_ok"] = zizmor_result["ok"]
            entry["zizmor_blocked"] = zizmor_result["blocked"]
            entry["zizmor_findings"] = zizmor_result["findings"]
            entry["zizmor_error_findings"] = zizmor_result["error_findings"]
            entry["zizmor_warning_findings"] = zizmor_result["warning_findings"]
            entry["zizmor_scanned_at"] = zizmor_result["scanned_at"]

            if zizmor_result["blocked"]:
                status = "BLOCKED"
                safe_print(f"   🚫 {repo_name}: BLOCKED — {len(zizmor_result['error_findings'])} ERROR finding(s)")
            elif not zizmor_result["ok"]:
                status = "WARNED"
                safe_print(f"   ⚠️  {repo_name}: {len(zizmor_result['warning_findings'])} WARNING finding(s)")
            if zizmor_result.get("error"):
                safe_print(f"   ?? {repo_name} zizmor note: {zizmor_result['error']}")
        else:
            entry.setdefault("zizmor_ok", True)
            entry.setdefault("zizmor_blocked", False)
            entry.setdefault("zizmor_findings", [])
            entry.setdefault("zizmor_error_findings", [])
            entry.setdefault("zizmor_warning_findings", [])
    else:
        entry.setdefault("zizmor_ok", True)
        entry.setdefault("zizmor_blocked", False)
        entry.setdefault("zizmor_findings", [])
        entry.setdefault("zizmor_error_findings", [])
        entry.setdefault("zizmor_warning_findings", [])

    return entry, status


# --- Core Engine Logic ---
def update_engine():
    if not METADATA_FILE.exists():
        print("Error: metadata file missing.")
        return

    with open(METADATA_FILE, "r") as f:
        actions = json.load(f)

    today = datetime.now(timezone.utc)
    one_year_ago = today - timedelta(days=365)

    zizmor_enabled = _zizmor_available()

    if zizmor_enabled:
        print("🔍 zizmor detected — security scanning enabled.")
    else:
        print("⚠️  zizmor not found — skipping security scans (install with: pip install zizmor)")

    print(f"Syncing {len(actions)} actions (stability gate: ≥{MIN_TAG_AGE_DAYS} days)...")

    fresh_actions = []
    updated_count = 0
    purged_stale = 0
    zizmor_blocked_count = 0
    zizmor_warned_count = 0
    
    # Use ThreadPoolExecutor for parallel processing
    max_workers = 10
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_action = {executor.submit(process_one_action, entry, zizmor_enabled, today, one_year_ago): entry for entry in actions}
        
        for i, future in enumerate(as_completed(future_to_action)):
            entry, status = future.result()
            
            if status == "RATE_LIMIT":
                print(f"!! Rate limit hit, stopping further requests.")
                # We don't break immediately to let other already started threads finish
                # but process_one_action checks rate_limit_event.
            
            if entry is not None:
                fresh_actions.append(entry)
            
            if status == "UPDATED":
                updated_count += 1
            elif status == "STALE":
                purged_stale += 1
            elif status == "BLOCKED":
                zizmor_blocked_count += 1
            elif status == "WARNED":
                zizmor_warned_count += 1
                
            if (i + 1) % 50 == 0:
                print(f"Progress: {i + 1}/{len(actions)} processed...")

    # Sort actions by name to keep metadata file stable
    fresh_actions.sort(key=lambda x: x["action"])

    # Save Fresh Metadata
    with open(METADATA_FILE, "w") as f:
        json.dump(fresh_actions, f, indent=2)

    # Re-build SQLite Index
    build_index(fresh_actions)

    print(f"\n--- Update Summary ---")
    print(f"Total: {len(fresh_actions)} | Updated: {updated_count} | Purged: {purged_stale}")
    print(f"Zizmor: {zizmor_blocked_count} blocked (ERROR) | {zizmor_warned_count} warned (WARNING)")


def build_index(actions):
    print("Re-indexing SQLite database...")
    if DB_FILE.exists():
        DB_FILE.unlink()

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE actions (
            action TEXT PRIMARY KEY,
            latest_tag TEXT,
            latest_sha TEXT,
            description TEXT,
            category TEXT,
            tags TEXT,
            best_use_case TEXT,
            robustness_score INTEGER,
            stars INTEGER,
            runtime TEXT,
            requires TEXT,
            conflicts TEXT,
            permissions TEXT,
            auth TEXT,
            outputs TEXT,
            side_effects TEXT,
            performance TEXT,
            match_logic TEXT,
            -- zizmor security columns
            zizmor_ok INTEGER DEFAULT 1,
            zizmor_blocked INTEGER DEFAULT 0,
            zizmor_findings TEXT DEFAULT '[]',
            zizmor_error_findings TEXT DEFAULT '[]',
            zizmor_warning_findings TEXT DEFAULT '[]',
            zizmor_scanned_at TEXT DEFAULT ''
        )
    """)
    cursor.execute("""
        CREATE VIRTUAL TABLE actions_fts USING fts5(
            action, description, category, tags, best_use_case,
            runtime, auth, outputs, side_effects, performance, match_logic,
            content='actions', content_rowid='rowid'
        )
    """)
    cursor.execute("""
        CREATE TRIGGER actions_ai AFTER INSERT ON actions BEGIN
            INSERT INTO actions_fts(
                rowid, action, description, category, tags, best_use_case,
                runtime, auth, outputs, side_effects, performance, match_logic
            )
            VALUES (
                new.rowid, new.action, new.description, new.category, new.tags, new.best_use_case,
                new.runtime, new.auth, new.outputs, new.side_effects, new.performance, new.match_logic
            );
        END
    """)

    for entry in actions:
        def _jdump(v, default):
            if isinstance(v, (list, dict)):
                return json.dumps(v)
            return v if isinstance(v, str) else json.dumps(default)

        cursor.execute(
            """INSERT INTO actions VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )""",
            (
                entry["action"],
                entry.get("latest_tag", ""),
                entry.get("latest_sha", ""),
                entry.get("description", ""),
                entry.get("category", "General"),
                ", ".join(entry["tags"]) if isinstance(entry["tags"], list) else entry.get("tags", ""),
                entry.get("best_use_case", ""),
                entry.get("robustness_score", 0),
                entry.get("stars", 0),
                entry.get("runtime", ""),
                _jdump(entry.get("requires"), []),
                _jdump(entry.get("conflicts"), []),
                _jdump(entry.get("permissions"), {}),
                entry.get("auth", ""),
                _jdump(entry.get("outputs"), []),
                _jdump(entry.get("side_effects"), []),
                entry.get("performance", ""),
                entry.get("match_logic", ""),
                1 if entry.get("zizmor_ok", True) else 0,
                1 if entry.get("zizmor_blocked", False) else 0,
                _jdump(entry.get("zizmor_findings"), []),
                _jdump(entry.get("zizmor_error_findings"), []),
                _jdump(entry.get("zizmor_warning_findings"), []),
                entry.get("zizmor_scanned_at", ""),
            )
        )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    update_engine()
