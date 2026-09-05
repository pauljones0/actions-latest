import json
import subprocess
from datetime import timedelta
from unittest.mock import patch

import pytest
from conftest import MANIFEST, NOW, SHA

from actions_latest.models import Finding
from actions_latest.security import SCANNER_VERSION, ScanError, Scanner, parse_manifest
from actions_latest.versions import generate_usage_snippet


@pytest.fixture
def scanner():
    scanner = Scanner.__new__(Scanner)
    scanner.command = "mock-zizmor"
    scanner.version = SCANNER_VERSION
    scanner.timeout = 1
    return scanner


@pytest.mark.parametrize(
    "code,output", [(3, ""), (1, ""), (2, "[]"), (0, ""), (0, "{}"), (14, "[]"), (0, "invalid")]
)
def test_bad_scanner_output_never_clean(scanner, code, output):
    with patch(
        "actions_latest.security.subprocess.run",
        return_value=subprocess.CompletedProcess([], code, output, "failed"),
    ):
        with pytest.raises(ScanError):
            scanner.scan(MANIFEST, SHA)


def test_timeout_and_unknown_severity_fail(scanner):
    with patch(
        "actions_latest.security.subprocess.run", side_effect=subprocess.TimeoutExpired("zizmor", 1)
    ):
        with pytest.raises(ScanError, match="execution failed"):
            scanner.scan(MANIFEST, SHA)
    payload = [{"ident": "new-rule", "determinations": {"severity": "FutureSeverity"}}]
    with patch(
        "actions_latest.security.subprocess.run",
        return_value=subprocess.CompletedProcess([], 0, json.dumps(payload), ""),
    ):
        with pytest.raises(ScanError, match="contract"):
            scanner.scan(MANIFEST, SHA)


def test_scanner_version_must_match_tested_contract(scanner):
    scanner.version = "999.0.0"
    with pytest.raises(ScanError, match="Unsupported"):
        scanner.scan(MANIFEST, SHA)


def test_real_scanner_clean_invalid_and_vulnerable():
    scanner = Scanner()
    assert scanner.version == SCANNER_VERSION, "Run uv sync --group dev"
    assert scanner.scan(MANIFEST, SHA).findings == []
    with pytest.raises(ScanError):
        scanner.scan("name: [invalid yaml", SHA)
    content = """name: example
description: example
inputs:
  command:
    description: untrusted input
runs:
  using: composite
  steps:
    - shell: bash
      run: echo '${{ inputs.command }}'
"""
    result = scanner.scan(content, SHA)
    assert any(f.rule == "template-injection" and f.severity == "error" for f in result.findings)
    assert all(f.line is None or f.line >= 1 for f in result.findings)


def test_manifest_fields_are_derived_from_revision():
    parsed = parse_manifest(MANIFEST, SHA)
    assert parsed.runtime == "node24"
    assert parsed.outputs == ["installed-version"]
    assert parsed.inputs["version"]["required"] is True
    assert parsed.name == "example"
    assert parsed.description == "example action"


def test_compatible_new_scanner_evidence_can_refresh_older_clients(record):
    record.state.scan.scanner_version = "1.999.0"
    assert record.security_status(NOW) == "clean"
    record.state.scan.scanner_version = "2.0.0"
    assert record.security_status(NOW) == "stale"


def test_usage_requires_fresh_scanned_observed_sha(record):
    assert f"@{SHA} # v1.0.0" in generate_usage_snippet(record)
    record.state.scan.scanned_at = NOW - timedelta(days=15)
    assert record.security_status(NOW) == "stale"
    assert "uses:" not in generate_usage_snippet(record)
    record.state.scan.scanned_at = NOW
    record.state.scan_error = "timeout"
    assert record.security_status(NOW) == "error"
    record.state.scan.findings = [Finding(rule="injection", severity="error")]
    assert record.security_status(NOW) == "blocked"
    record.state.scan = None
    record.state.scan_error = None
    assert record.security_status(NOW) == "unknown"
    assert "uses:" not in generate_usage_snippet(record)


@pytest.mark.parametrize("field,value", [("scanner_version", "old-version"), ("policy_version", 0)])
def test_changed_scanner_policy_invalidates_clean_evidence(record, field, value):
    setattr(record.state.scan, field, value)
    assert record.security_status(NOW) == "stale"
    assert "uses:" not in generate_usage_snippet(record)
    record.state.scan.findings = [Finding(rule="injection", severity="error")]
    assert record.security_status(NOW) == "blocked"
