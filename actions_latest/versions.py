"""Load, parse, and compare latest official GitHub Actions versions."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

DEFAULT_VERSIONS_URL = "https://simonw.github.io/actions-latest/versions.txt"
VERSION_TOKEN_RE = re.compile(r"^actions/[A-Za-z0-9_.-]+@v[0-9][A-Za-z0-9_.-]*$")
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


def latest_for_action(action: str, versions: dict[str, str]) -> tuple[str, str] | None:
    """Return (normalized_action, latest_ref) for an action, if known."""
    normalized = normalize_action_name(action)
    latest = versions.get(normalized)
    if latest is None:
        return None
    return normalized, latest


def workflow_updates(workflow: str, versions: dict[str, str]) -> list[WorkflowUpdate]:
    """Find official actions in a workflow that do not use the latest major tag."""
    updates: list[WorkflowUpdate] = []
    for match in USES_RE.finditer(workflow):
        ref = match.group(1).strip()
        if ref.startswith("./") or "@" not in ref:
            continue

        action, current = ref.split("@", 1)
        latest = versions.get(action)
        if latest is None or current == latest:
            continue

        line_start = workflow.rfind("\n", 0, match.start()) + 1
        line_end = workflow.find("\n", match.start())
        if line_end == -1:
            line_end = len(workflow)

        updates.append(
            WorkflowUpdate(
                action=action,
                current=current,
                latest=latest,
                line=workflow[line_start:line_end],
            )
        )
    return updates


def repo_versions_file() -> Path:
    """Return the root versions.txt path for this repository checkout."""
    return Path(__file__).resolve().parent.parent / "versions.txt"
