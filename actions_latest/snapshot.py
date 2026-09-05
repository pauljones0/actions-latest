"""Deterministic, validated SQLite snapshots, published with one atomic rename."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import tempfile
from contextlib import closing
from pathlib import Path

from .models import SCHEMA_VERSION, ActionRecord, CatalogEntry


class SnapshotError(RuntimeError):
    pass


def canonical(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value) -> str:
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def fts_fields(record: ActionRecord) -> tuple[str, ...]:
    catalog, state = record.catalog, record.state
    return (
        record.action,
        catalog.description,
        catalog.category,
        " ".join(sorted({tag.casefold() for tag in catalog.tags})),
        catalog.match_logic,
        state.manifest.runtime if state.manifest else "",
        catalog.auth,
        " ".join(state.manifest.outputs) if state.manifest else "",
    )


def load_catalog(path: Path) -> list[CatalogEntry]:
    entries = [CatalogEntry.model_validate(item) for item in json.loads(path.read_text())]
    names = [entry.action.casefold() for entry in entries]
    if len(names) != len(set(names)):
        raise ValueError("Catalog contains duplicate action names (case insensitive)")
    return sorted(entries, key=lambda entry: entry.action.casefold())


def connect(path: Path | str) -> sqlite3.Connection:
    conn = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True)
    if conn.execute("PRAGMA user_version").fetchone()[0] != SCHEMA_VERSION:
        conn.close()
        raise SnapshotError("Unsupported snapshot schema; regenerate or reinstall the package")
    return conn


def load_records(path: Path) -> list[ActionRecord]:
    with closing(connect(path)) as conn:
        return [
            ActionRecord.model_validate_json(row[0])
            for row in conn.execute("SELECT record FROM actions ORDER BY action COLLATE NOCASE")
        ]


def validate_snapshot(path: Path) -> list[ActionRecord]:
    records = load_records(path)
    with closing(connect(path)) as conn:
        if conn.execute("PRAGMA integrity_check").fetchone() != ("ok",):
            raise SnapshotError("SQLite integrity check failed")
        stored = dict(conn.execute("SELECT key, value FROM snapshot_metadata"))
        if stored.get("records_sha256") != digest([r.model_dump(mode="json") for r in records]):
            raise SnapshotError("Snapshot record digest mismatch")
        if stored.get("catalog_sha256") != digest(
            [r.catalog.model_dump(mode="json") for r in records]
        ):
            raise SnapshotError("Snapshot catalog digest mismatch")
        if conn.execute("SELECT COUNT(*) FROM actions_fts").fetchone()[0] != len(records):
            raise SnapshotError("FTS row count mismatch")
        if conn.execute("PRAGMA foreign_key_check").fetchall():
            raise SnapshotError("Snapshot foreign key check failed")
        actual = conn.execute(
            "SELECT action, category, robustness_score, blocked FROM actions ORDER BY action COLLATE NOCASE"
        ).fetchall()
        expected = [
            (
                r.action,
                r.catalog.category,
                r.state.robustness_score,
                int(r.security_status() == "blocked"),
            )
            for r in records
        ]
        if actual != expected:
            raise SnapshotError("Snapshot query columns disagree with record evidence")
        actual_fts = conn.execute(
            "SELECT actions_fts.action, description, actions_fts.category, tags, match_logic, runtime, auth, outputs FROM actions_fts JOIN actions ON actions.rowid = actions_fts.rowid ORDER BY actions.action COLLATE NOCASE"
        ).fetchall()
        if actual_fts != [fts_fields(r) for r in records]:
            raise SnapshotError("Snapshot FTS content disagrees with records")
        actual_tags = set(conn.execute("SELECT action, tag FROM action_tags"))
        expected_tags = {(r.action, tag.casefold()) for r in records for tag in r.catalog.tags}
        if actual_tags != expected_tags:
            raise SnapshotError("Snapshot tags disagree with records")
    return records


def publish_snapshot(records: list[ActionRecord], destination: Path) -> None:
    records = sorted(
        (ActionRecord.model_validate(r.model_dump()) for r in records),
        key=lambda r: r.action.casefold(),
    )
    names = [r.action.casefold() for r in records]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate action names")
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=".actions-", suffix=".db", dir=destination.parent)
    os.close(descriptor)
    staging = Path(name)
    try:
        with closing(sqlite3.connect(staging)) as conn:
            conn.executescript(f"""
                PRAGMA user_version = {SCHEMA_VERSION};
                PRAGMA foreign_keys = ON;
                CREATE TABLE snapshot_metadata (key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE actions (
                    action TEXT PRIMARY KEY COLLATE NOCASE,
                    category TEXT NOT NULL,
                    robustness_score INTEGER NOT NULL,
                    blocked INTEGER NOT NULL CHECK (blocked IN (0, 1)),
                    record TEXT NOT NULL
                );
                CREATE TABLE action_tags (
                    action TEXT NOT NULL REFERENCES actions(action),
                    tag TEXT NOT NULL COLLATE NOCASE,
                    PRIMARY KEY (action, tag)
                );
                CREATE INDEX tags_lookup ON action_tags(tag);
                CREATE VIRTUAL TABLE actions_fts USING fts5(
                    action, description, category, tags, match_logic, runtime, auth, outputs,
                    tokenize='porter unicode61'
                );
            """)
            for rowid, record in enumerate(records, 1):
                catalog, state = record.catalog, record.state
                conn.execute(
                    "INSERT INTO actions(rowid, action, category, robustness_score, blocked, record) VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        rowid,
                        record.action,
                        catalog.category,
                        state.robustness_score,
                        int(record.security_status() == "blocked"),
                        canonical(record.model_dump(mode="json")),
                    ),
                )
                tags = sorted({tag.casefold() for tag in catalog.tags})
                conn.executemany(
                    "INSERT INTO action_tags VALUES (?, ?)", ((record.action, tag) for tag in tags)
                )
                conn.execute(
                    "INSERT INTO actions_fts(rowid, action, description, category, tags, match_logic, runtime, auth, outputs) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (rowid, *fts_fields(record)),
                )
            conn.executemany(
                "INSERT INTO snapshot_metadata VALUES (?, ?)",
                [
                    ("records_sha256", digest([r.model_dump(mode="json") for r in records])),
                    (
                        "catalog_sha256",
                        digest([r.catalog.model_dump(mode="json") for r in records]),
                    ),
                ],
            )
            conn.execute("INSERT INTO actions_fts(actions_fts) VALUES ('integrity-check')")
            conn.commit()
        validate_snapshot(staging)
        staging.chmod(0o644)
        with staging.open("rb") as handle:
            os.fsync(handle.fileno())
        os.replace(staging, destination)
        if os.name == "posix":
            descriptor = os.open(destination.parent, os.O_RDONLY)
            try:
                os.fsync(descriptor)
            finally:
                os.close(descriptor)
    finally:
        staging.unlink(missing_ok=True)
