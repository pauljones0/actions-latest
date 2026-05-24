#!/usr/bin/env python3
"""
The Action Navigator Engine.
Does one thing: Keeps the GitHub Actions index fresh, robust, and ranked.
"""

import json
import os
import re
import subprocess
import sqlite3
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

# --- Configuration ---
SCRIPT_DIR = Path(__file__).parent.resolve()
METADATA_FILE = SCRIPT_DIR / "actions-metadata.json"
DB_FILE = SCRIPT_DIR / "actions_latest" / "actions.db"
GITHUB_API_URL = "https://api.github.com"

VERIFIED_ORGS = [
    "actions", "github", "google-github-actions", "aws-actions", 
    "Azure", "docker", "microsoft", "astral-sh", "hashicorp",
    "cloudflare", "snyk", "codecov", "getsentry"
]

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
                print("!! Rate limit reached !!")
                return "RATE_LIMIT"
            return None
        return data
    except:
        return None

def get_latest_tag(owner, repo):
    tags = github_api_request(f"/repos/{owner}/{repo}/tags", {"per_page": 100})
    if not isinstance(tags, list): return None
    
    version_pattern = re.compile(r"^v(\d+)$")
    v_tags = []
    for t in tags:
        match = version_pattern.match(t.get("name", ""))
        if match:
            v_tags.append((int(match.group(1)), t["name"]))
    
    if not v_tags: return None
    v_tags.sort(reverse=True, key=lambda x: x[0])
    return v_tags[0][1]

# --- Core Engine Logic ---
def update_engine():
    if not METADATA_FILE.exists():
        print("Error: metadata file missing.")
        return

    with open(METADATA_FILE, "r") as f:
        actions = json.load(f)

    today = datetime.now(timezone.utc)
    one_year_ago = today - timedelta(days=365)
    
    fresh_actions = []
    updated_count = 0
    purged_stale = 0
    
    print(f"Syncing {len(actions)} actions...")

    for i, entry in enumerate(actions):
        repo_name = entry["action"]
        owner, repo = repo_name.split("/")
        
        # 1. Fetch Repository Vital Signs
        repo_data = github_api_request(f"/repos/{repo_name}")
        if repo_data == "RATE_LIMIT": break
        if not repo_data:
            print(f"!! Skipping {repo_name} (Not found or error)")
            continue
            
        # 2. Enforce Freshness (1-year rule)
        pushed_at_str = repo_data.get("pushed_at")
        pushed_at = datetime.fromisoformat(pushed_at_str.replace("Z", "+00:00"))
        if pushed_at < one_year_ago:
            print(f"-- Purging {repo_name} (Stale since {pushed_at_str[:10]})")
            purged_stale += 1
            continue
            
        # 3. Update Popularity & Robustness
        stars = repo_data.get("stargazers_count", 0)
        forks = repo_data.get("forks_count", 0)
        
        score = stars + (forks * 0.5)
        if owner in VERIFIED_ORGS: score *= 10
        if owner == "actions": score *= 2
        
        entry["stars"] = stars
        entry["robustness_score"] = int(score)
        
        # 4. Check for New Versions
        latest_tag = get_latest_tag(owner, repo)
        if latest_tag and latest_tag != entry["latest_tag"]:
            print(f"++ Updated {repo_name}: {entry['latest_tag']} -> {latest_tag}")
            entry["latest_tag"] = latest_tag
            updated_count += 1
            
        fresh_actions.append(entry)
        
        if (i+1) % 50 == 0:
            print(f"Progress: {i+1}/{len(actions)} processed...")

    # Save Fresh Metadata
    with open(METADATA_FILE, "w") as f:
        json.dump(fresh_actions, f, indent=2)

    # Re-build SQLite Index
    build_index(fresh_actions)
    
    print(f"\n--- Update Summary ---")
    print(f"Total: {len(fresh_actions)} | Updated: {updated_count} | Purged: {purged_stale}")

def build_index(actions):
    print("Re-indexing SQLite database...")
    if DB_FILE.exists(): DB_FILE.unlink()
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE actions (
            action TEXT PRIMARY KEY, latest_tag TEXT, description TEXT,
            category TEXT, tags TEXT, best_use_case TEXT,
            robustness_score INTEGER, stars INTEGER,
            runtime TEXT, requires TEXT, conflicts TEXT, permissions TEXT,
            auth TEXT, outputs TEXT, side_effects TEXT, performance TEXT, match_logic TEXT
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
        cursor.execute(
            """INSERT INTO actions VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )""",
            (
                entry["action"], entry["latest_tag"], entry.get("description", ""),
                entry.get("category", "General"), 
                ", ".join(entry["tags"]) if isinstance(entry["tags"], list) else entry.get("tags", ""),
                entry.get("best_use_case", ""),
                entry.get("robustness_score", 0), entry.get("stars", 0),
                entry.get("runtime", ""),
                json.dumps(entry.get("requires", [])),
                json.dumps(entry.get("conflicts", [])),
                json.dumps(entry.get("permissions", {})),
                entry.get("auth", ""),
                json.dumps(entry.get("outputs", [])),
                json.dumps(entry.get("side_effects", [])),
                entry.get("performance", ""),
                entry.get("match_logic", "")
            )
        )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_engine()
