"""Read-only metadata queries and SHA-pinned usage rendering."""

from __future__ import annotations

import re
from contextlib import closing
from pathlib import Path

from .models import ActionRecord
from .snapshot import connect


class MetadataStore:
    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)

    def _query(self, sql: str, parameters: tuple = ()) -> list[ActionRecord]:
        with closing(connect(self.db_path)) as conn:
            return [
                ActionRecord.model_validate_json(row[0]) for row in conn.execute(sql, parameters)
            ]

    def search(
        self, query: str, limit: int = 10, exclude_blocked: bool = True
    ) -> list[ActionRecord]:
        # Punctuation in owner/repo, setup-node, etc. is not FTS expression syntax.
        words = re.findall(r"[^\W_]+", query, flags=re.UNICODE)
        if not words:
            return []
        expression = " AND ".join('"' + word + '"' for word in words)
        return self._query(
            """
            SELECT actions.record FROM actions_fts
            JOIN actions ON actions.rowid = actions_fts.rowid
            WHERE actions_fts MATCH ? AND (? = 0 OR actions.blocked = 0)
            ORDER BY bm25(actions_fts, 4, 1, 2, 3, 2, 1, 1, 1),
                     actions.robustness_score DESC, actions.action COLLATE NOCASE
            LIMIT ?
        """,
            (expression, int(exclude_blocked), limit),
        )

    def find_by_tag(
        self, tag: str, limit: int = 10, exclude_blocked: bool = True
    ) -> list[ActionRecord]:
        return self._query(
            """
            SELECT actions.record FROM actions
            JOIN action_tags ON action_tags.action = actions.action
            WHERE action_tags.tag = ? COLLATE NOCASE AND (? = 0 OR actions.blocked = 0)
            ORDER BY actions.robustness_score DESC, actions.action COLLATE NOCASE LIMIT ?
        """,
            (tag, int(exclude_blocked), limit),
        )

    def list_categories(self) -> list[str]:
        with closing(connect(self.db_path)) as conn:
            return [
                row[0]
                for row in conn.execute("SELECT DISTINCT category FROM actions ORDER BY category")
            ]

    def list_owners(self) -> list[str]:
        with closing(connect(self.db_path)) as conn:
            return [
                row[0]
                for row in conn.execute(
                    "SELECT DISTINCT substr(action, 1, instr(action, '/') - 1) AS owner FROM actions ORDER BY owner COLLATE NOCASE"
                )
            ]

    def list_repos(self, owner: str) -> list[ActionRecord]:
        return self._query(
            """
            SELECT record FROM actions
            WHERE substr(action, 1, instr(action, '/') - 1) = ? COLLATE NOCASE
            ORDER BY robustness_score DESC, action COLLATE NOCASE
        """,
            (owner.rstrip("/"),),
        )

    def get_info(self, action: str) -> ActionRecord | None:
        rows = self._query("SELECT record FROM actions WHERE action = ? COLLATE NOCASE", (action,))
        return rows[0] if rows else None


def get_db_path() -> Path:
    # Wheels install as directories; this path has the package's lifetime.
    return Path(__file__).resolve().with_name("actions.db")


def generate_usage_snippet(record: ActionRecord) -> str:
    if not record.usage_ready():
        return "Usage withheld: this revision needs observed stability and a fresh successful manifest scan."
    selected = record.state.selected
    assert selected is not None
    return f"- uses: {record.action}@{selected.sha} # {selected.tag}"
