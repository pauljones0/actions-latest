#!/usr/bin/env python3
"""Prepare compatible tooling/action-pin updates; CI validates before a normal push."""

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


def gh_json(endpoint: str):
    return json.loads(subprocess.check_output(["gh", "api", endpoint], text=True, timeout=60))


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
    workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
    current_uv = re.search(r"uv==([0-9.]+)", "\n".join(p.read_text() for p in workflows)).group(1)
    latest_uv = pypi_version("uv", current_uv)
    pins = {}
    for path in workflows:
        content = path.read_text().replace(f"uv=={current_uv}", f"uv=={latest_uv}")
        pattern = r"uses: ([\w.-]+/[\w.-]+)@([a-f0-9]{40}) # v([0-9.]+)"
        for match in list(re.finditer(pattern, content)):
            repository, old_sha, current = match.groups()
            key = (repository, current)
            if key not in pins:
                releases = gh_json(f"repos/{repository}/releases?per_page=100")
                versions = [
                    r["tag_name"].removeprefix("v")
                    for r in releases
                    if not r["draft"] and not r["prerelease"]
                ]
                latest = latest_compatible(current, [current, *versions])
                # Commit API peels annotated tags; never pin the tag object itself.
                sha = gh_json(f"repos/{repository}/commits/v{latest}")["sha"]
                if not re.fullmatch(r"[a-f0-9]{40}", sha):
                    raise ValueError("Invalid resolved action SHA")
                pins[key] = (latest, sha)
                changes.append(f"{repository}: {current} -> {latest}")
            latest, sha = pins[key]
            content = content.replace(match.group(), f"uses: {repository}@{sha} # v{latest}")
        path.write_text(content)
    changes.append(f"uv: {current_uv} -> {latest_uv}")
    subprocess.run(["uv", "lock", "--upgrade"], cwd=ROOT, check=True, timeout=300)
    print("\n".join(changes))


if __name__ == "__main__":
    main()
