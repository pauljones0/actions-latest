#!/usr/bin/env python3
"""Prepare compatible tooling updates; CI validates before a normal push."""

import argparse
import json
import os
import re
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from actions_latest.reports import dependency_report

ROOT = Path(__file__).resolve().parents[1]


def locked_versions(content: str) -> dict[str, list[str]]:
    versions = {}
    for package in tomllib.loads(content).get("package", []):
        if package["name"] != "actions-latest":
            versions.setdefault(package["name"], set()).add(package["version"])
    return {name: sorted(values) for name, values in versions.items()}


def version_changes(before: dict, after: dict) -> list[dict]:
    return [
        {"package": name, "before": before.get(name, []), "after": after.get(name, [])}
        for name in sorted(before.keys() | after.keys())
        if before.get(name) != after.get(name)
    ]


def save_report(changes: list[dict], validated: bool, *, prepared: bool = True) -> None:
    run = os.environ.get("GITHUB_RUN_ID")
    report = {
        "changes": changes,
        "validated": validated,
        "prepared": prepared,
        "base_commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, timeout=10
        ).strip(),
        "held_tools": json.loads((ROOT / "tooling.json").read_text()).get("hold", []),
        "run_url": f"https://github.com/pauljones0/actions-latest/actions/runs/{run}"
        if run
        else None,
    }
    (ROOT / "data/dependency-review.json").write_text(json.dumps(report, indent=2) + "\n")
    text = dependency_report(report)
    (ROOT / "data/dependency-review.md").write_text(text)
    print(text)


def stable_version(value: str) -> tuple[int, ...] | None:
    return tuple(map(int, value.split("."))) if re.fullmatch(r"\d+\.\d+\.\d+", value) else None


def latest_compatible(current: str, releases: list[str]) -> str:
    baseline = stable_version(current)
    candidates = [(stable_version(v), v) for v in releases]
    return max(
        (key, v) for key, v in candidates if key and key[0] == baseline[0] and key >= baseline
    )[1]


def pypi_version(package: str, current: str) -> str:
    with urlopen(Request(f"https://pypi.org/pypi/{package}/json"), timeout=20) as response:
        data = json.load(response)
    supported = [
        v for v, files in data["releases"].items() if any(not f.get("yanked") for f in files)
    ]
    return latest_compatible(current, [current, *supported])


def managed_version(package: str, current: str, held: set[str]) -> str:
    return current if package in held else pypi_version(package, current)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--finalize", action="store_true", help="Record validation after the workflow's checks pass"
    )
    if parser.parse_args().finalize:
        report = json.loads((ROOT / "data/dependency-review.json").read_text())
        if not report.get("prepared"):
            raise ValueError("Cannot finalize an incomplete dependency proposal")
        save_report(report["changes"], True)
        return
    save_report([], False, prepared=False)
    (ROOT / "data/maintenance-proposal.patch").unlink(missing_ok=True)
    before = locked_versions((ROOT / "uv.lock").read_text())
    tooling = ROOT / "tooling.json"
    settings = json.loads(tooling.read_text())
    held = set(settings.get("hold", []))
    if held - {"uv", "ruff", "zizmor"}:
        raise ValueError(
            "Tool holds support uv, ruff, and zizmor; use dependency constraints for other packages"
        )
    project = ROOT / "pyproject.toml"
    content = project.read_text()
    for package in ("ruff", "zizmor"):
        current = re.search(rf'"{package}==([0-9.]+)"', content).group(1)
        latest = managed_version(package, current, held)
        content = content.replace(f"{package}=={current}", f"{package}=={latest}")
        if package == "zizmor":
            model = ROOT / "actions_latest/models.py"
            model.write_text(
                model.read_text().replace(
                    f'SCANNER_VERSION = "{current}"', f'SCANNER_VERSION = "{latest}"'
                )
            )
    project.write_text(content)
    current_uv = settings["uv"]
    latest_uv = managed_version("uv", current_uv, held)
    settings["uv"] = latest_uv
    tooling.write_text(json.dumps(settings, indent=2) + "\n")
    subprocess.run(["uv", "lock", "--upgrade"], cwd=ROOT, check=True, timeout=300)
    after = locked_versions((ROOT / "uv.lock").read_text())
    before["uv"], after["uv"] = [current_uv], [latest_uv]
    save_report(version_changes(before, after), False)
    patch = subprocess.check_output(
        [
            "git",
            "diff",
            "--binary",
            "--",
            "pyproject.toml",
            "uv.lock",
            "actions_latest/models.py",
            "tooling.json",
        ],
        cwd=ROOT,
        timeout=30,
    )
    (ROOT / "data/maintenance-proposal.patch").write_bytes(patch)


if __name__ == "__main__":
    main()
