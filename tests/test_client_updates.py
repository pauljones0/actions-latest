import gzip
import json
from datetime import timedelta
from unittest.mock import Mock

import pytest
from conftest import NOW
from filelock import FileLock

from actions_latest.client_updates import SnapshotManager
from actions_latest.feed import decode_feed, encode_feed
from actions_latest.models import SCHEMA_VERSION
from actions_latest.snapshot import publish_snapshot
from actions_latest.versions import RefreshingMetadataStore


@pytest.fixture
def bundled(tmp_path, record):
    path = tmp_path / "bundled.db"
    publish_snapshot([record], path)
    return path


def test_download_refreshes_live_store_and_survives_offline_restart(tmp_path, record, bundled):
    new = record.model_copy(deep=True)
    new.catalog.action = "fresh/action"
    fetch = Mock(return_value=encode_feed([record, new], NOW))
    manager = SnapshotManager(bundled, tmp_path / "cache", fetch=fetch)
    store = RefreshingMetadataStore(manager)
    assert store.get_info("fresh/action") is None
    assert manager.refresh(now=NOW)
    assert store.get_info("fresh/action") is not None
    assert manager.status()["source"] == "cache"
    restarted = SnapshotManager(
        bundled, tmp_path / "cache", fetch=Mock(side_effect=OSError("offline"))
    )
    assert not restarted.refresh(force=True, now=NOW + timedelta(hours=7))
    assert RefreshingMetadataStore(restarted).get_info("fresh/action") is not None
    assert "offline" in restarted.status()["error"]


@pytest.mark.parametrize("kind", ["corrupt", "schema", "digest", "duplicate", "future"])
def test_bad_download_never_replaces_working_snapshot(tmp_path, record, bundled, kind):
    payload = encode_feed([record], NOW)
    data = json.loads(gzip.decompress(payload))
    if kind == "schema":
        data["schema_version"] = SCHEMA_VERSION + 1
    elif kind == "digest":
        data["records_sha256"] = "0" * 64
    elif kind == "duplicate":
        data["records"].append(data["records"][0])
    elif kind == "future":
        data["published_at"] = (NOW + timedelta(days=1)).isoformat()
    payload = b"not gzip" if kind == "corrupt" else gzip.compress(json.dumps(data).encode())
    manager = SnapshotManager(bundled, tmp_path / "cache", fetch=Mock(return_value=payload))
    before = bundled.read_bytes()
    assert not manager.refresh(now=NOW)
    assert manager.path == bundled
    assert bundled.read_bytes() == before
    assert manager.status()["error"]


def test_rollback_and_retry_cooldown(tmp_path, record, bundled):
    fetch = Mock(
        side_effect=[encode_feed([record], NOW), encode_feed([record], NOW - timedelta(days=1))]
    )
    manager = SnapshotManager(bundled, tmp_path / "cache", fetch=fetch)
    assert manager.refresh(now=NOW)
    before = manager.database.read_bytes()
    assert not manager.refresh(now=NOW + timedelta(minutes=20))
    assert fetch.call_count == 1
    assert not manager.refresh(force=True, now=NOW + timedelta(hours=7))
    assert "older" in manager.status()["error"]
    assert manager.database.read_bytes() == before
    assert not manager.refresh(now=NOW + timedelta(hours=7, minutes=15))
    assert fetch.call_count == 2


def test_offline_opt_out_and_cache_lock(tmp_path, record, bundled):
    fetch = Mock(return_value=encode_feed([record], NOW))
    manager = SnapshotManager(bundled, tmp_path / "cache", enabled=False, fetch=fetch)
    assert not manager.refresh(force=True, now=NOW)
    manager.kick()
    fetch.assert_not_called()
    manager.enabled = True
    manager.cache.mkdir(parents=True)
    with FileLock(str(manager.cache / "refresh.lock")):
        assert not manager.refresh(now=NOW)
    fetch.assert_not_called()


def test_corrupt_cache_and_metadata_fall_back_then_repair(tmp_path, record, bundled):
    cache = tmp_path / "cache"
    cache.mkdir()
    (cache / "actions.db").write_bytes(b"corrupt")
    (cache / "refresh.json").write_text('{"published_at": 1, "last_attempt": "invalid"}')
    manager = SnapshotManager(bundled, cache, fetch=Mock(return_value=encode_feed([record], NOW)))
    assert manager.path == bundled
    assert manager.refresh(now=NOW)
    assert manager.path == manager.database


def test_expansion_limit_rejects_compression_bombs(monkeypatch, record):
    monkeypatch.setattr("actions_latest.feed.MAX_UNPACKED", 100)
    with pytest.raises(ValueError, match="expands"):
        decode_feed(encode_feed([record], NOW), NOW)


def test_existing_client_notices_another_process_cache(tmp_path, record, bundled):
    first = SnapshotManager(bundled, tmp_path / "cache", fetch=Mock())
    second = SnapshotManager(
        bundled, tmp_path / "cache", fetch=Mock(return_value=encode_feed([record], NOW))
    )
    assert second.refresh(now=NOW)
    first.kick()
    assert first.path == second.database
    first.fetch.assert_not_called()
