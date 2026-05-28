"""Data access layer for the Action Navigator."""

from __future__ import annotations

import sqlite3
import subprocess
import os
from dataclasses import dataclass, field
from importlib import resources
from pathlib import Path
from typing import List, Optional

@dataclass(frozen=True)
class ActionMetadata:
    action: str
    latest_tag: str
    latest_sha: str        # Commit SHA the tag currently points to (for determinism)
    description: str
    category: str = "General"
    tags: str = ""
    best_use_case: str = ""
    robustness_score: int = 0
    stars: int = 0
    runtime: str = ""
    requires: str = "[]"
    conflicts: str = "[]"
    permissions: str = "{}"
    auth: str = ""
    outputs: str = "[]"
    side_effects: str = "[]"
    performance: str = ""
    match_logic: str = ""
    # zizmor security scan results
    zizmor_ok: int = 1              # 0 = has WARNING+ findings
    zizmor_blocked: int = 0         # 1 = has ERROR findings → EXCLUDED from recommendations
    zizmor_findings: str = "[]"     # All findings (JSON list)
    zizmor_error_findings: str = "[]"
    zizmor_warning_findings: str = "[]"
    zizmor_scanned_at: str = ""     # ISO timestamp of last scan


# Columns selected in all queries — must match ActionMetadata field order exactly.
_SELECT_COLS = """
    action, latest_tag, COALESCE(latest_sha, ''), description,
    category, tags, best_use_case, robustness_score, stars,
    runtime, requires, conflicts, permissions, auth, outputs,
    side_effects, performance, match_logic,
    COALESCE(zizmor_ok, 1), COALESCE(zizmor_blocked, 0),
    COALESCE(zizmor_findings, '[]'),
    COALESCE(zizmor_error_findings, '[]'),
    COALESCE(zizmor_warning_findings, '[]'),
    COALESCE(zizmor_scanned_at, '')
""".strip()


class MetadataStore:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def search(self, query: str, limit: int = 10, exclude_blocked: bool = True) -> List[ActionMetadata]:
        """Search actions using BM25 and Robustness Score.

        Args:
            exclude_blocked: If True (default), actions with ERROR-level zizmor
                             findings are excluded from results entirely.
        """
        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            blocked_clause = "AND COALESCE(actions.zizmor_blocked, 0) = 0" if exclude_blocked else ""
            cursor.execute(f"""
                SELECT {_SELECT_COLS.replace(chr(10), ' ')}
                FROM actions_fts
                JOIN actions ON actions.rowid = actions_fts.rowid
                WHERE actions_fts MATCH ?
                {blocked_clause}
                ORDER BY rank, actions.robustness_score DESC
                LIMIT ?
            """, (query, limit))
            results = cursor.fetchall()
            return [ActionMetadata(*r) for r in results]
        except sqlite3.OperationalError:
            return []
        finally:
            conn.close()

    def find_by_tag(self, tag: str, limit: int = 10, exclude_blocked: bool = True) -> List[ActionMetadata]:
        """Find actions by tag, sorted by robustness."""
        conn = self._get_conn()
        cursor = conn.cursor()
        blocked_clause = "AND COALESCE(zizmor_blocked, 0) = 0" if exclude_blocked else ""
        cursor.execute(f"""
            SELECT {_SELECT_COLS.replace(chr(10), ' ')}
            FROM actions
            WHERE tags LIKE ?
            {blocked_clause}
            ORDER BY robustness_score DESC
            LIMIT ?
        """, (f"%{tag}%", limit))
        results = cursor.fetchall()
        conn.close()
        return [ActionMetadata(*r) for r in results]

    def list_categories(self) -> List[str]:
        """List available categories."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT category FROM actions")
        categories = [r[0] for r in cursor.fetchall()]
        conn.close()
        return sorted(categories)

    def list_owners(self, category: str = "all") -> List[str]:
        """List owners (simulated directories)."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT SUBSTR(action, 1, INSTR(action, '/') - 1) FROM actions")
        owners = [r[0] for r in cursor.fetchall()]
        conn.close()
        return sorted(owners)

    def list_repos(self, owner: str) -> List[ActionMetadata]:
        """List repos for a specific owner."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT {_SELECT_COLS.replace(chr(10), ' ')}
            FROM actions
            WHERE action LIKE ?
        """, (f"{owner}/%",))
        results = cursor.fetchall()
        conn.close()
        return [ActionMetadata(*r) for r in results]

    def get_info(self, action: str) -> Optional[ActionMetadata]:
        """Get metadata for a specific action."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT {_SELECT_COLS.replace(chr(10), ' ')}
            FROM actions
            WHERE action = ?
        """, (action,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return ActionMetadata(*result)
        return None


def get_db_path() -> Path:
    """Return the path to the actions.db file."""
    package_db = resources.files("actions_latest").joinpath("actions.db")
    try:
        with resources.as_file(package_db) as f:
            return f
    except Exception:
        return Path(__file__).resolve().parent / "actions.db"


def fetch_action_manifest(action: str, timeout: float = 10.0, ref: str = "") -> str:
    """
    Fetch action.yml or action.yaml from the repository.

    Args:
        action: "owner/repo" string.
        timeout: HTTP timeout in seconds.
        ref: Optional git ref (tag, branch, or SHA) to fetch at.
             SHA is preferred for determinism. Defaults to the repo's default branch.
    """
    token = os.environ.get("GITHUB_TOKEN")
    headers = ["-H", "Accept: application/vnd.github.v3.raw"]
    if token:
        headers.extend(["-H", f"Authorization: Bearer {token}"])

    ref_suffix = f"?ref={ref}" if ref else ""
    for filename in ["action.yml", "action.yaml"]:
        url = f"https://api.github.com/repos/{action}/contents/{filename}{ref_suffix}"
        try:
            result = subprocess.run(
                ["curl", "-sL", *headers, url],
                capture_output=True, text=True, timeout=timeout
            )
            if result.returncode == 0 and result.stdout.strip() and not result.stdout.startswith("{"):
                return result.stdout
        except Exception:
            continue
    return f"[error] Could not find action.yml or action.yaml for {action}."


def generate_usage_snippet(action: str, version: str) -> str:
    """Generate a simple YAML usage snippet."""
    return f"- uses: {action}@{version}\n  with:\n    # Pass inputs here"
