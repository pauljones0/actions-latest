"""Data access layer for the Action Navigator."""

from __future__ import annotations

import sqlite3
import subprocess
import os
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import List, Optional

@dataclass(frozen=True)
class ActionMetadata:
    action: str
    latest_tag: str
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

class MetadataStore:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def search(self, query: str, limit: int = 10) -> List[ActionMetadata]:
        """Search actions using BM25 and Robustness Score."""
        conn = self._get_conn()
        cursor = conn.cursor()
        try:
            # Rank by BM25 ranking (rank) first, then authority (robustness_score)
            cursor.execute("""
                SELECT actions.action, actions.latest_tag, actions.description, 
                       actions.category, actions.tags, actions.best_use_case,
                       actions.robustness_score, actions.stars,
                       actions.runtime, actions.requires, actions.conflicts,
                       actions.permissions, actions.auth, actions.outputs,
                       actions.side_effects, actions.performance, actions.match_logic
                FROM actions_fts
                JOIN actions ON actions.rowid = actions_fts.rowid
                WHERE actions_fts MATCH ?
                ORDER BY rank, actions.robustness_score DESC
                LIMIT ?
            """, (query, limit))
            results = cursor.fetchall()
            return [ActionMetadata(*r) for r in results]
        except sqlite3.OperationalError:
            return []
        finally:
            conn.close()

    def find_by_tag(self, tag: str, limit: int = 10) -> List[ActionMetadata]:
        """Find actions by tag, sorted by robustness."""
        conn = self._get_conn()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT action, latest_tag, description, category, tags, best_use_case, robustness_score, stars,
                   runtime, requires, conflicts, permissions, auth, outputs, side_effects, performance, match_logic
            FROM actions 
            WHERE tags LIKE ? 
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
        cursor.execute("""
            SELECT action, latest_tag, description, category, tags, best_use_case, robustness_score, stars,
                   runtime, requires, conflicts, permissions, auth, outputs, side_effects, performance, match_logic
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
        cursor.execute("""
            SELECT action, latest_tag, description, category, tags, best_use_case, robustness_score, stars,
                   runtime, requires, conflicts, permissions, auth, outputs, side_effects, performance, match_logic
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
    except:
        return Path(__file__).resolve().parent / "actions.db"

def fetch_action_manifest(action: str, timeout: float = 10.0) -> str:
    """Fetch action.yml or action.yaml from the repository."""
    token = os.environ.get("GITHUB_TOKEN")
    headers = ["-H", "Accept: application/vnd.github.v3.raw"]
    if token:
        headers.extend(["-H", f"Authorization: Bearer {token}"])
    
    for filename in ["action.yml", "action.yaml"]:
        url = f"https://api.github.com/repos/{action}/contents/{filename}"
        try:
            result = subprocess.run(
                ["curl", "-sL", *headers, url],
                capture_output=True, text=True, timeout=timeout
            )
            if result.returncode == 0 and not result.stdout.startswith("{"):
                return result.stdout
        except:
            continue
    return f"[error] Could not find action.yml or action.yaml for {action}."

def generate_usage_snippet(action: str, version: str) -> str:
    """Generate a simple YAML usage snippet."""
    return f"- uses: {action}@{version}\n  with:\n    # Pass inputs here"
