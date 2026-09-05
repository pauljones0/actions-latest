import json
import runpy
from datetime import timedelta
from pathlib import Path

import pytest
from conftest import NOW, SHA

from actions_latest.reports import (
    action_review,
    change_report,
    dependency_report,
    maintenance_summary,
    review_queue,
)
from actions_latest.snapshot import publish_snapshot, validate_snapshot

ROOT = Path(__file__).resolve().parents[1]
manage = runpy.run_path(str(ROOT / "manage.py"))
maintain = runpy.run_path(str(ROOT / "scripts/maintain.py"))


def test_catalog_report_ignores_timestamp_and_popularity_churn(record):
    later = record.model_copy(deep=True)
    later.state.checked_at = NOW + timedelta(hours=1)
    later.state.scan.scanned_at = NOW + timedelta(hours=1)
    later.state.stars += 100
    later.state.robustness_score += 100
    report = change_report([record], [later], NOW + timedelta(hours=2))
    assert "No meaningful catalog changes" in report


def test_catalog_report_explains_semantic_changes_and_escapes_upstream_text(record):
    later = record.model_copy(deep=True)
    later.state.manifest.runtime = "node26"
    later.state.manifest.description = "<script>alert(1)</script> | [fake](https://example.invalid)"
    later.state.scan_error = "timeout"
    report = change_report([record], [later], NOW)
    assert "node24" in report and "node26" in report
    assert "Scan error" in report and "timeout" in report
    assert "<script>" not in report
    assert "\\[fake\\]" in report and "\\|" in report
    assert f"/tree/{SHA}" in report
    assert "Added:" in change_report([], [later], NOW)
    assert "Removed from published catalog" in change_report([later], [], NOW)


def test_queue_prioritizes_failures_then_invalidated_reviews(record):
    failed = record.model_copy(deep=True)
    failed.catalog.action = "low/popularity"
    failed.state.scan_error = "missing manifest"
    changed = record.model_copy(deep=True)
    changed.catalog.action = "changed/review"
    changed.catalog.reviewed_sha = "b" * 40
    record.state.stars = 100000
    assert [item["action"] for item in review_queue([record, changed, failed])] == [
        failed.action,
        changed.action,
        record.action,
    ]
    report = maintenance_summary([record, changed, failed], {"healthy": True, "reasons": []})
    assert "1 action-specific fetch/scan failures" in report
    assert "1 reviews invalidated" in report
    assert "manage.py review" in report


def test_review_packet_has_source_claims_decision_and_immutable_acknowledgement(record):
    record.catalog.reviewed_sha = "b" * 40
    report = action_review(record)
    assert "Human claims to check" in report
    assert f"--sha {SHA}" in report
    assert f"/compare/{'b' * 40}...{SHA}" in report
    assert "cannot clear findings" in report


def test_review_acknowledgement_refuses_changed_revision_and_preserves_security(tmp_path, record):
    database = tmp_path / "actions_latest/actions.db"
    database.parent.mkdir()
    publish_snapshot([record], database)
    catalog = tmp_path / "catalog.json"
    catalog.write_text(json.dumps([record.catalog.model_dump()]))
    before = catalog.read_bytes()
    with pytest.raises(ValueError, match="changed"):
        manage["mark_reviewed"](tmp_path, record.action, "b" * 40)
    assert catalog.read_bytes() == before
    manage["mark_reviewed"](tmp_path, record.action, SHA)
    assert json.loads(catalog.read_text())[0]["reviewed_sha"] == SHA
    assert validate_snapshot(database)[0].state == record.state


def test_resolved_dependency_report_includes_all_platform_versions_and_validation():
    before = maintain["locked_versions"]("""[[package]]
name = "example"
version = "1.0.0"
[[package]]
name = "example"
version = "2.0.0"
""")
    assert before == {"example": ["1.0.0", "2.0.0"]}
    changes = maintain["version_changes"](before, {"example": ["2.0.0"], "added": ["1.0.0"]})
    report = dependency_report({"changes": changes, "validated": False, "run_url": None})
    assert "Validation: pending" in report
    assert "/project/example/2.0.0/" in report
    assert "maintenance-proposal" in report
    assert "Validation: passed" in dependency_report({"changes": changes, "validated": True})


def test_catalog_report_shows_added_removed_inputs_without_markdown_injection(record):
    record.state.manifest.inputs = {"version": {"required": False}}
    changed = record.model_copy(deep=True)
    changed.state.manifest.inputs = {"bad|name": {"required": True}}
    report = change_report([record], [changed], NOW)
    assert "Input: bad\\|name" in report
    assert "Input: version" in report
    assert "null" in report


def test_failure_summary_works_without_project_environment(tmp_path):
    import os
    import subprocess
    import sys

    summary = tmp_path / "summary.md"
    result = subprocess.run(
        [sys.executable, "-I", str(ROOT / "scripts/job_failure.py"), "maintain"],
        cwd=tmp_path,
        env=dict(os.environ, GITHUB_STEP_SUMMARY=str(summary)),
        text=True,
        capture_output=True,
        timeout=10,
        check=True,
    )
    assert "maintenance.yml --repo pauljones0/actions-latest" in result.stdout
    assert "never force-push" in summary.read_text()


def test_job_summary_bounds_large_reports_at_section_boundaries():
    summarize = runpy.run_path(str(ROOT / "scripts/render_summary.py"))["summarize_changes"]
    report = "# Changes\n\n50 actions changed.\n" + "\n## action\n" + "x" * 20000
    summary = summarize(report, 1000)
    assert len(summary) < 1000
    assert "50 actions" in summary
    assert "complete change report" in summary
    assert "x" * 10 not in summary


def test_tool_hold_prevents_reapplying_a_bad_upgrade(monkeypatch):
    from unittest.mock import Mock

    resolver = Mock(return_value="1.9.0")
    function = maintain["managed_version"]
    monkeypatch.setitem(function.__globals__, "pypi_version", resolver)
    assert function("ruff", "1.2.0", {"ruff"}) == "1.2.0"
    resolver.assert_not_called()
    assert function("zizmor", "1.2.0", {"ruff"}) == "1.9.0"


def test_logged_workflow_failures_cannot_be_hidden_by_tee(tmp_path):
    import subprocess

    import yaml

    for name in ("update", "maintenance"):
        workflow = yaml.safe_load((ROOT / f".github/workflows/{name}.yml").read_text())
        shell = workflow.get("defaults", {}).get("run", {}).get("shell")
        # Match GitHub's explicit bash behavior versus its implicit bash -e default.
        flags = ["-e", "-o", "pipefail"] if shell == "bash" else ["-e"]
        result = subprocess.run(
            ["bash", *flags, "-c", "false | tee failure.log"], cwd=tmp_path, capture_output=True
        )
        assert result.returncode != 0, f"{name}: tee masked the failed maintenance command"


def test_shared_rate_limit_is_one_recovery_item_not_hundreds_of_reviews(record):
    affected = []
    before = []
    for index in range(30):
        item = record.model_copy(deep=True)
        item.catalog.action = f"owner/action-{index}"
        before.append(item.model_copy(deep=True))
        item.state.update_error = "GitHub rate limit reached; retry in a later update"
        affected.append(item)
    summary = maintenance_summary(affected, {"healthy": True, "reasons": []})
    assert "partial (30 fetch failures)" in summary
    assert summary.count("| GitHub API rate limit | 30 |") == 1
    assert "manage.py review owner/" not in summary
    assert "30 historical guidance reviews" in summary
    report = change_report(before, affected, NOW)
    assert "30 request-error transitions affected" in report
    assert "## owner/action-" not in report
    assert "30 request-error transitions recovered" in change_report(affected, before, NOW)


def test_shared_outage_does_not_hide_an_independent_manifest_failure(record):
    record.state.update_error = "GitHub rate limit reached; retaining previous state"
    record.state.scan_error = "Invalid action manifest"
    queue = review_queue([record])
    assert queue[0]["priority"] == 0
    assert queue[0]["detail"] == "Invalid action manifest"


def test_error_grouping_never_hides_a_new_action_specific_failure(record):
    previous = record.model_copy(deep=True)
    previous.state.scan_error = "GitHub rate limit reached; retaining previous state"
    record.state.scan_error = "Invalid action manifest"
    report = change_report([previous], [record], NOW)
    assert "Invalid action manifest" in report
    assert "## example/setup-node" in report
