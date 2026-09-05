"""One manifest parser and scanner policy for updates and on-demand audits."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

import yaml

from .models import POLICY_VERSION, SCANNER_VERSION, Finding, Manifest, ScanEvidence, utc_now


class ScanError(RuntimeError):
    pass


def parse_manifest(content: str, sha: str) -> Manifest:
    try:
        data = yaml.safe_load(content)
        if not isinstance(data, dict) or not isinstance(data.get("runs"), dict):
            raise ValueError("manifest must contain a runs mapping")
        runtime = data["runs"].get("using")
        if not isinstance(runtime, str) or not runtime:
            raise ValueError("manifest must specify runs.using")
        inputs = data.get("inputs") or {}
        outputs = data.get("outputs") or {}
        if not isinstance(inputs, dict) or not isinstance(outputs, dict):
            raise ValueError("inputs and outputs must be mappings")
        return Manifest(
            sha=sha,
            name=data.get("name", ""),
            description=data.get("description", ""),
            runtime=runtime,
            inputs=inputs,
            outputs=sorted(outputs),
        )
    except (yaml.YAMLError, ValueError, TypeError) as exc:
        raise ScanError(f"Invalid action manifest: {exc}") from exc


class Scanner:
    def __init__(self, command: str = "zizmor", timeout: float = 30):
        self.command = shutil.which(command)
        self.timeout = timeout
        self.version: str | None = None
        if self.command:
            try:
                result = subprocess.run(
                    [self.command, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=True,
                )
                self.version = result.stdout.strip().removeprefix("zizmor ")
            except (OSError, subprocess.SubprocessError):
                pass

    def scan(self, content: str, sha: str, now: datetime | None = None) -> ScanEvidence:
        parse_manifest(content, sha)
        if not self.command or not self.version:
            raise ScanError("zizmor is unavailable; install the pinned dev dependencies")
        if self.version != SCANNER_VERSION:
            raise ScanError(f"Unsupported zizmor {self.version}; expected {SCANNER_VERSION}")
        with tempfile.TemporaryDirectory(prefix="actions-scan-") as directory:
            path = Path(directory) / "action.yml"
            path.write_text(content, encoding="utf-8")
            try:
                result = subprocess.run(
                    [
                        self.command,
                        "--offline",
                        "--strict-collection",
                        "--format=json-v1",
                        str(path),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=self.timeout,
                )
            except (OSError, subprocess.SubprocessError) as exc:
                raise ScanError(f"Scanner execution failed: {type(exc).__name__}") from exc
        if result.returncode not in {0, 11, 12, 13, 14}:
            raise ScanError(f"zizmor failed with exit {result.returncode}")
        try:
            data = json.loads(result.stdout)
            if not isinstance(data, list):
                raise ValueError("expected a JSON findings array")
            findings = []
            severity_map = {
                "informational": "info",
                "low": "warning",
                "medium": "warning",
                "high": "error",
            }
            for item in data:
                severity = severity_map[item["determinations"]["severity"].lower()]
                locations = item.get("locations", [])
                row = (
                    (
                        locations[0]
                        .get("concrete", {})
                        .get("location", {})
                        .get("start_point", {})
                        .get("row")
                    )
                    if locations
                    else None
                )
                findings.append(
                    Finding(
                        rule=item["ident"],
                        severity=severity,
                        message=item.get("desc", ""),
                        line=row + 1 if isinstance(row, int) else None,
                    )
                )
            if result.returncode != 0 and not findings:
                raise ValueError("finding exit code without findings")
        except (ValueError, KeyError, TypeError, AttributeError) as exc:
            raise ScanError(f"Invalid scanner JSON contract: {exc}") from exc
        return ScanEvidence(
            sha=sha,
            scanner_version=self.version,
            policy_version=POLICY_VERSION,
            scanned_at=now or utc_now(),
            findings=findings,
        )
