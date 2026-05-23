"""Load, parse, and compare latest stable GitHub Actions versions."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

DEFAULT_VERSIONS_URL = "https://raw.githubusercontent.com/pauljones0/actions-latest/main/versions.txt"
GITHUB_API_URL = "https://api.github.com"
VERSION_TOKEN_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+@v[0-9][A-Za-z0-9_.-]*$")
MAJOR_TAG_RE = re.compile(r"^v(\d+)$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
USES_RE = re.compile(r"^\s*-?\s*uses:\s*['\"]?([^'\"#\s]+)", re.MULTILINE)


@dataclass(frozen=True)
class WorkflowUpdate:
    """A workflow action reference that can be updated."""

    action: str
    current: str
    latest: str
    line: str


def bundled_versions_text() -> str:
    """Return the packaged versions snapshot."""
    return resources.files("actions_latest").joinpath("versions.txt").read_text()


def fetch_versions_text(url: str | None = None, timeout: float = 10.0) -> str:
    """Fetch the latest versions text from the configured URL."""
    request = Request(
        url or os.environ.get("ACTIONS_LATEST_URL", DEFAULT_VERSIONS_URL),
        headers={"User-Agent": "actions-latest-mcp"},
    )
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def github_api_json(path: str, timeout: float = 10.0) -> object:
    """Fetch JSON from the GitHub API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "actions-latest-mcp",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(f"{GITHUB_API_URL}{path}", headers=headers)
    with urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def load_versions_text(refresh: bool = True) -> str:
    """Return remote versions text, falling back to the packaged snapshot."""
    if not refresh or os.environ.get("ACTIONS_LATEST_OFFLINE"):
        return bundled_versions_text()

    try:
        return fetch_versions_text()
    except (OSError, URLError):
        return bundled_versions_text()


def parse_versions(text: str) -> dict[str, str]:
    """Parse versions text into {action_name: version_ref}."""
    versions: dict[str, str] = {}
    for token in text.split():
        token = token.strip()
        if not VERSION_TOKEN_RE.match(token):
            continue
        action, version = token.split("@", 1)
        versions[action] = version
    return dict(sorted(versions.items()))


def latest_major_tag(tags: list[str]) -> str | None:
    """Return the highest floating major tag, matching Simon's vINTEGER style."""
    major_tags: list[tuple[int, str]] = []
    for tag in tags:
        match = MAJOR_TAG_RE.match(tag.strip())
        if match:
            major_tags.append((int(match.group(1)), tag.strip()))

    if not major_tags:
        return None

    major_tags.sort(reverse=True, key=lambda item: item[0])
    return major_tags[0][1]


def normalize_action_name(action: str) -> str:
    """Normalize an action input to owner/name form."""
    name = action.strip().strip("'\"")
    if name.startswith("uses:"):
        name = name.split(":", 1)[1].strip()
    if "@" in name:
        name = name.split("@", 1)[0]
    if "/" not in name:
        name = f"actions/{name}"
    return name


def action_repo(action: str) -> str | None:
    """Return owner/repo for an action reference."""
    parts = normalize_action_name(action).split("/")
    if len(parts) < 2:
        return None
    return "/".join(parts[:2])


def fetch_action_tags(action: str) -> list[str]:
    """Fetch all tags for an action repository."""
    repo = action_repo(action)
    if repo is None:
        return []

    tags: list[str] = []
    page = 1
    per_page = 100
    while True:
        page_tags = github_api_json(f"/repos/{repo}/tags?per_page={per_page}&page={page}")
        if not isinstance(page_tags, list):
            raise RuntimeError(f"Unexpected tags response for {repo}")
        if not page_tags:
            break

        for tag in page_tags:
            if isinstance(tag, dict) and isinstance(tag.get("name"), str):
                tags.append(tag["name"])

        if len(page_tags) < per_page:
            break
        page += 1

    return tags


def latest_for_action(action: str, versions: dict[str, str], refresh: bool = True) -> tuple[str, str] | None:
    """Return (normalized_action, latest stable ref) for an action, if known."""
    normalized = normalize_action_name(action)
    latest = versions.get(normalized)
    if latest is not None:
        return normalized, latest

    if not refresh:
        return None

    try:
        latest = latest_major_tag(fetch_action_tags(normalized))
    except (OSError, URLError, RuntimeError):
        return None

    if latest is None:
        return None
    return normalized, latest


def workflow_updates(workflow: str, versions: dict[str, str], refresh: bool = True) -> list[WorkflowUpdate]:
    """Find action references that do not use the latest stable major tag."""
    updates: list[WorkflowUpdate] = []
    for match in USES_RE.finditer(workflow):
        ref = match.group(1).strip()
        if ref.startswith(("./", "docker://")) or "@" not in ref:
            continue

        action, current = ref.split("@", 1)
        if SHA_RE.match(current) or current == "stable":
            continue

        result = latest_for_action(action, versions, refresh=refresh)
        if result is None:
            continue

        normalized, latest = result
        if current == latest:
            continue

        line_start = workflow.rfind("\n", 0, match.start()) + 1
        line_end = workflow.find("\n", match.start())
        if line_end == -1:
            line_end = len(workflow)

        updates.append(
            WorkflowUpdate(
                action=normalized,
                current=current,
                latest=latest,
                line=workflow[line_start:line_end],
            )
        )
    return updates


def repo_versions_file() -> Path:
    """Return the root versions.txt path for this repository checkout."""
    return Path(__file__).resolve().parent.parent / "versions.txt"
