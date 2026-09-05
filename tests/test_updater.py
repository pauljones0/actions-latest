import json
from datetime import timedelta
from unittest.mock import Mock

import pytest
from conftest import MANIFEST, NEW_SHA, NOW, SHA

from actions_latest.github import GitHubError, NotFound, RateLimited, TransientError
from actions_latest.models import ActionState, Finding, Revision, ScanEvidence
from actions_latest.security import SCANNER_VERSION, ScanError
from actions_latest.snapshot import load_records, publish_snapshot
from actions_latest.updater import observe_tags, refresh_action, select_revision, update


def client_and_scanner(tags=None):
    client = Mock()
    client.repository.return_value = {
        "archived": False,
        "stargazers_count": 10,
        "forks_count": 2,
        "pushed_at": NOW.isoformat(),
    }
    client.tags.return_value = tags or {"v1.0.0": SHA}
    client.is_prerelease.return_value = False
    client.manifest.return_value = MANIFEST
    scanner = Mock()
    scanner.scan.side_effect = lambda content, sha, now: ScanEvidence(
        sha=sha, scanner_version=SCANNER_VERSION, scanned_at=now
    )
    return client, scanner


def test_new_release_discovered_while_previous_tag_is_unchanged(record):
    client, scanner = client_and_scanner({"v1.0.0": SHA, "v2.0.0": NEW_SHA})
    first = refresh_action(record.catalog, record.state, client, scanner, NOW)
    assert first.state.selected.sha == SHA
    assert first.state.observations["v2.0.0"].first_seen == NOW
    later = refresh_action(record.catalog, first.state, client, scanner, NOW + timedelta(days=7))
    assert later.state.selected.tag == "v2.0.0"
    assert later.state.selected.sha == NEW_SHA
    assert later.state.selected.stability == "observed"
    assert later.state.manifest.sha == later.state.scan.sha == NEW_SHA
    assert later.state.manifest.runtime == "node24"
    client.manifest.assert_called_with(record.action, NEW_SHA)


def test_moved_tag_requires_observed_age_not_commit_or_release_date(record):
    record.state.observations = observe_tags({"v1.0.0": SHA}, {}, NOW - timedelta(days=100))
    client, scanner = client_and_scanner({"v1.0.0": NEW_SHA})
    first = refresh_action(record.catalog, record.state, client, scanner, NOW)
    assert first.state.selected.sha == SHA
    assert first.state.observations["v1.0.0"].first_seen == NOW
    client.is_prerelease.assert_not_called()
    later = refresh_action(record.catalog, first.state, client, scanner, NOW + timedelta(days=7))
    assert later.state.selected.sha == NEW_SHA


def test_disappeared_tag_and_clock_rollback_reset_observation():
    original = observe_tags({"v1": SHA}, {}, NOW)
    assert observe_tags({}, original, NOW + timedelta(days=1)) == {}
    reappeared = observe_tags({"v1": SHA}, {}, NOW + timedelta(days=8))
    assert reappeared["v1"].first_seen == NOW + timedelta(days=8)
    rollback = observe_tags({"v1": SHA}, original, NOW - timedelta(days=1))
    assert rollback["v1"].first_seen == NOW - timedelta(days=1)


def test_no_downgrade_and_prerelease_exclusion():
    old = Revision(tag="v2", sha=SHA, stability="observed")
    observations = observe_tags(
        {"v1": SHA, "v3": NEW_SHA, "v4-rc.1": NEW_SHA}, {}, NOW - timedelta(days=8)
    )
    observations = observe_tags({"v1": SHA, "v3": NEW_SHA}, observations, NOW)
    assert select_revision(observations, old, NOW, lambda tag: tag == "v3") == old
    assert select_revision(observations, old, NOW, lambda tag: False).tag == "v3"


@pytest.mark.parametrize(
    "failure",
    [
        TransientError("outage"),
        NotFound("missing"),
        RateLimited("limited"),
        GitHubError("bad response"),
    ],
)
def test_api_failures_preserve_entry_and_recover(tmp_path, record, failure):
    catalog_path, path = tmp_path / "catalog.json", tmp_path / "actions.db"
    catalog_path.write_text(json.dumps([record.catalog.model_dump()]))
    publish_snapshot([record], path)
    client, scanner = client_and_scanner()
    client.repository.side_effect = failure
    summary = update(catalog_path, path, client=client, scanner=scanner, now=NOW)
    assert summary["actions"] == 1 and summary["update_errors"] == 1
    failed = load_records(path)[0]
    assert failed.state.selected == record.state.selected
    assert failed.state.scan == record.state.scan
    client.repository.side_effect = None
    update(catalog_path, path, client=client, scanner=scanner, now=NOW + timedelta(days=1))
    assert load_records(path)[0].state.update_error is None


def test_failed_rescan_preserves_blocking_evidence(record):
    record.state.scan.findings = [Finding(rule="injection", severity="error")]
    record.state.scan.scanned_at = NOW - timedelta(days=8)
    client, scanner = client_and_scanner()
    scanner.scan.side_effect = ScanError("timed out")
    result = refresh_action(record.catalog, record.state, client, scanner, NOW)
    assert result.security_status(NOW) == "blocked"
    assert result.state.scan_error == "timed out"
    assert result.state.scan == record.state.scan


def test_failed_scan_after_sha_change_cannot_reuse_clean_evidence(record):
    record.state.observations = observe_tags({"v2": NEW_SHA}, {}, NOW - timedelta(days=8))
    client, scanner = client_and_scanner({"v2": NEW_SHA})
    client.manifest.side_effect = NotFound("manifest unavailable")
    result = refresh_action(record.catalog, record.state, client, scanner, NOW)
    assert result.state.selected.sha == NEW_SHA
    assert result.state.scan is None and result.state.manifest is None
    assert result.security_status(NOW) == "error"
    assert not result.usage_ready(NOW)


def test_programmer_error_does_not_publish_partial_snapshot(tmp_path, record):
    catalog_path, path = tmp_path / "catalog.json", tmp_path / "actions.db"
    catalog_path.write_text(json.dumps([record.catalog.model_dump()]))
    publish_snapshot([record], path)
    before = path.read_bytes()
    client, scanner = client_and_scanner()
    client.tags.side_effect = TypeError("bug")
    with pytest.raises(TypeError):
        update(catalog_path, path, client=client, scanner=scanner, now=NOW)
    assert path.read_bytes() == before


def test_catalog_change_during_update_aborts_publication(tmp_path, record):
    catalog_path, path = tmp_path / "catalog.json", tmp_path / "actions.db"
    catalog_path.write_text(json.dumps([record.catalog.model_dump()]))
    publish_snapshot([record], path)
    before = path.read_bytes()
    client, scanner = client_and_scanner()

    def change_catalog(repository):
        catalog_path.write_text("[]")
        return {"v1": SHA}

    client.tags.side_effect = change_catalog
    with pytest.raises(RuntimeError, match="Catalog changed"):
        update(catalog_path, path, client=client, scanner=scanner, now=NOW)
    assert path.read_bytes() == before


def test_catalog_addition_is_independent_of_generated_state(tmp_path, record):
    catalog_path, path = tmp_path / "catalog.json", tmp_path / "actions.db"
    added = record.catalog.model_copy(update={"action": "new/setup-node"})
    catalog_path.write_text(json.dumps([record.catalog.model_dump(), added.model_dump()]))
    publish_snapshot([record], path)
    client, scanner = client_and_scanner()
    update(catalog_path, path, client=client, scanner=scanner, now=NOW)
    rows = load_records(path)
    assert len(rows) == 2
    assert rows[1].state.selected is None  # A new entry must earn its initial revision.
    assert rows[1].state.observations


def test_update_prioritizes_entries_not_recently_checked(tmp_path, record):
    catalog_path, path = tmp_path / "catalog.json", tmp_path / "actions.db"
    record.state.checked_at = NOW
    older = record.model_copy(deep=True)
    older.catalog.action = "zebra/setup-node"
    older.state = ActionState()
    catalog_path.write_text(json.dumps([r.catalog.model_dump() for r in [record, older]]))
    publish_snapshot([record, older], path)
    client, scanner = client_and_scanner()
    update(catalog_path, path, client=client, scanner=scanner, now=NOW, workers=1)
    assert client.repository.call_args_list[0].args == ("zebra/setup-node",)
