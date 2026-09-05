import sqlite3
from pathlib import Path
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from actions_latest.models import ActionRecord, CatalogEntry, Finding
from actions_latest.snapshot import SnapshotError, load_records, publish_snapshot, validate_snapshot
from actions_latest.versions import MetadataStore


def test_real_fts_search_and_literal_punctuation(tmp_path, record):
    path = tmp_path / "actions.db"
    publish_snapshot([record], path)
    store = MetadataStore(path)
    for query in ["node", "setup node", "example/setup-node", 'node"', "caching"]:
        assert [r.action for r in store.search(query)] == [record.action]
    assert store.search("unrelated") == []
    assert store.search("|+-") == []
    assert store.get_info("EXAMPLE/SETUP-NODE").action == record.action


def test_blocked_filter_and_exact_tags(tmp_path, record):
    blocked = record.model_copy(deep=True)
    blocked.catalog.action = "other/setup-node"
    blocked.state.scan.findings = [Finding(rule="injection", severity="error")]
    record.catalog.tags = ["nodejs"]
    path = tmp_path / "actions.db"
    publish_snapshot([record, blocked], path)
    store = MetadataStore(path)
    assert len(store.search("node")) == 1
    assert len(store.search("node", exclude_blocked=False)) == 2
    assert store.find_by_tag("node") == []
    assert len(store.find_by_tag("NODEJS")) == 1
    assert len(store.find_by_tag("node", exclude_blocked=False)) == 1
    assert store.find_by_tag("%") == []
    assert store.list_repos("%") == []


def test_missing_or_corrupt_database_is_not_no_results(tmp_path):
    path = tmp_path / "missing.db"
    with pytest.raises(sqlite3.Error):
        MetadataStore(path).search("node")
    assert not path.exists()
    path.write_text("not a database")
    with pytest.raises(sqlite3.Error):
        MetadataStore(path).search("node")


def test_snapshot_deterministic_and_atomic_on_failure(tmp_path, record):
    path = tmp_path / "actions.db"
    publish_snapshot([record], path)
    before = path.read_bytes()
    publish_snapshot(load_records(path), path)
    assert path.read_bytes() == before
    with patch(
        "actions_latest.snapshot.validate_snapshot", side_effect=SnapshotError("bad staging")
    ):
        with pytest.raises(SnapshotError):
            publish_snapshot([], path)
    assert path.read_bytes() == before
    with pytest.raises(ValueError, match="Duplicate"):
        publish_snapshot([record, record], path)
    assert path.read_bytes() == before
    assert not list(tmp_path.glob(".actions-*"))


def test_snapshot_tampering_detected(tmp_path, record):
    path = tmp_path / "actions.db"
    publish_snapshot([record], path)
    with sqlite3.connect(path) as conn:
        conn.execute("UPDATE snapshot_metadata SET value = 'bad' WHERE key = 'records_sha256'")
    with pytest.raises(SnapshotError, match="digest"):
        validate_snapshot(path)


def test_bundled_snapshot_matches_catalog():
    from actions_latest.discovery import combined_catalog
    from actions_latest.feed import decode_feed

    root = Path(__file__).resolve().parents[1]
    records = validate_snapshot(root / "actions_latest/actions.db")
    assert [r.catalog for r in records] == combined_catalog(
        root / "catalog.json", root / "data/discovered.json", root / "catalog-policy.json"
    )
    assert decode_feed((root / "data/snapshot-v2.json.gz").read_bytes()).records == records
    assert records


def test_model_rejects_mismatched_evidence_and_unsafe_paths(record):
    data = record.model_dump()
    data["state"]["scan"]["sha"] = "b" * 40
    with pytest.raises(ValidationError, match="selected SHA"):
        ActionRecord.model_validate(data)
    with pytest.raises(ValidationError):
        CatalogEntry(action="owner/repo/../other", description="invalid")
    data = record.model_dump()
    data["state"]["scan"]["scanned_at"] = "2026-01-01T00:00:00"
    with pytest.raises(ValidationError, match="timezone"):
        ActionRecord.model_validate(data)
