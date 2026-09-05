import json
import runpy
from datetime import timedelta
from pathlib import Path
from unittest.mock import Mock

from conftest import MANIFEST, NOW, SHA

from actions_latest.discovery import combined_catalog, discover
from actions_latest.github import TransientError
from actions_latest.health import health_report
from actions_latest.models import SCANNER_VERSION, Finding, ScanEvidence

latest_compatible = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / "scripts/maintain.py")
)["latest_compatible"]


def discovery_setup(tmp_path):
    curated, registry, report, policy = [
        tmp_path / name
        for name in ("curated.json", "discovered.json", "report.json", "policy.json")
    ]
    curated.write_text("[]")
    policy.write_text('{"admissions_per_run": 1}')
    client, scanner = Mock(), Mock()
    client.search_repositories.return_value = [
        dict(
            full_name="owner/action",
            stargazers_count=100,
            pushed_at=NOW.isoformat(),
            default_branch="main",
            topics=["ci"],
        )
    ]
    client.default_sha.return_value = SHA
    client.manifest.return_value = MANIFEST
    client.tags.return_value = {"v1": SHA}
    scanner.scan.return_value = ScanEvidence(
        sha=SHA, scanner_version=SCANNER_VERSION, scanned_at=NOW
    )
    return (curated, registry, report, policy), client, scanner


def test_discovery_admits_source_facts_once_without_claiming_review(tmp_path):
    paths, client, scanner = discovery_setup(tmp_path)
    result = discover(*paths, client, scanner, NOW)
    assert result["admitted"] == ["owner/action"]
    entries = combined_catalog(paths[0], paths[1], paths[3])
    assert entries[0].origin == "discovered"
    assert entries[0].reviewed_sha is None
    assert entries[0].source_url.endswith(SHA)
    assert entries[0].description == "example action"
    client.manifest.assert_called_once_with("owner/action", SHA)
    assert not discover(*paths, client, scanner, NOW)["admitted"]


def test_discovery_rejects_blocked_and_recovers_transient_errors(tmp_path):
    paths, client, scanner = discovery_setup(tmp_path)
    scanner.scan.return_value.findings = [Finding(rule="injection", severity="error")]
    assert not discover(*paths, client, scanner, NOW)["admitted"]
    assert json.loads(paths[2].read_text())["candidates"]["owner/action"]["status"] == "rejected"
    scanner.scan.return_value.findings = []
    client.manifest.side_effect = TransientError("offline")
    assert not discover(*paths, client, scanner, NOW + timedelta(days=8))["admitted"]
    client.manifest.side_effect = None
    assert discover(*paths, client, scanner, NOW + timedelta(days=8, hours=7))["admitted"]


def test_curated_override_and_explicit_exclusion(tmp_path):
    paths, client, scanner = discovery_setup(tmp_path)
    discover(*paths, client, scanner, NOW)
    paths[0].write_text('[{"action":"owner/action","description":"curated override"}]')
    assert combined_catalog(paths[0], paths[1])[0].description == "curated override"
    paths[3].write_text('{"excluded_actions":["OWNER/ACTION"]}')
    assert combined_catalog(paths[0], paths[1], paths[3]) == []
    assert not discover(*paths, client, scanner, NOW + timedelta(days=8))["admitted"]


def test_new_publication_cannot_hide_old_observations_or_scanner_failure(record):
    record.state.checked_at = NOW
    assert health_report([record], NOW, NOW)["healthy"]
    assert not health_report([record], NOW - timedelta(days=3), NOW)["healthy"]
    record.state.checked_at = NOW - timedelta(days=4)
    assert not health_report([record], NOW, NOW)["healthy"]
    record.state.checked_at = NOW
    record.state.scan_error = "scanner broken"
    assert not health_report([record], NOW, NOW)["healthy"]


def test_editorial_review_invalidated_on_revision_change(record):
    assert record.guidance_status() == "unreviewed"
    record.catalog.reviewed_sha = SHA
    assert record.guidance_status() == "reviewed for selected SHA"
    record.catalog.reviewed_sha = "b" * 40
    assert record.guidance_status() == "needs review after revision change"


def test_maintenance_never_adopts_prerelease_or_major():
    assert latest_compatible("1.2.3", ["1.2.3", "1.9.0", "2.0.0", "1.99.0rc1"]) == "1.9.0"


def test_discovery_outage_cannot_hide_behind_fresh_publication(record):
    from actions_latest.health import include_discovery

    record.state.checked_at = NOW
    report = health_report([record], NOW, NOW)
    assert not include_discovery(
        report, {"checked_at": NOW.isoformat(), "errors": ["rate limited"]}, NOW
    )["healthy"]
