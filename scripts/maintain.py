#!/usr/bin/env python3
"""Prepare compatible tooling updates; CI validates before a normal push."""

import json
import re
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


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


def main() -> None:
    changes = []
    project = ROOT / "pyproject.toml"
    content = project.read_text()
    for package in ("ruff", "zizmor"):
        current = re.search(rf'"{package}==([0-9.]+)"', content).group(1)
        latest = pypi_version(package, current)
        content = content.replace(f"{package}=={current}", f"{package}=={latest}")
        if package == "zizmor":
            model = ROOT / "actions_latest/models.py"
            model.write_text(
                model.read_text().replace(
                    f'SCANNER_VERSION = "{current}"', f'SCANNER_VERSION = "{latest}"'
                )
            )
        changes.append(f"{package}: {current} -> {latest}")
    project.write_text(content)
    tooling = ROOT / "tooling.json"
    settings = json.loads(tooling.read_text())
    current_uv = settings["uv"]
    latest_uv = pypi_version("uv", current_uv)
    settings["uv"] = latest_uv
    tooling.write_text(json.dumps(settings, indent=2) + "\n")
    changes.append(f"uv: {current_uv} -> {latest_uv}")
    subprocess.run(["uv", "lock", "--upgrade"], cwd=ROOT, check=True, timeout=300)
    print("\n".join(changes))


if __name__ == "__main__":
    main()
