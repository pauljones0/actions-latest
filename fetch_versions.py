#!/usr/bin/env python3
"""
Fetch all repos from the GitHub actions organization and their tags via the API,
and generate a versions.txt file with the latest vINTEGER tags.

No git cloning required - uses GitHub REST API only.

Repos known to have no vINTEGER tags are cached in unversioned.txt to skip
API calls on future runs.
"""

import json
import os
import re
import subprocess
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
VERSIONS_FILE = SCRIPT_DIR / "versions.txt"
COMMUNITY_VERSIONS_FILE = SCRIPT_DIR / "community-versions.txt"
PACKAGE_VERSIONS_FILE = SCRIPT_DIR / "actions_latest" / "versions.txt"
PACKAGE_COMMUNITY_VERSIONS_FILE = SCRIPT_DIR / "actions_latest" / "community-versions.txt"
UNVERSIONED_FILE = SCRIPT_DIR / "unversioned.txt"
TRUSTED_ACTIONS_FILE = SCRIPT_DIR / "trusted-actions.txt"
COMMUNITY_ACTIONS_FILE = SCRIPT_DIR / "community-actions.txt"
README_FILE = SCRIPT_DIR / "README.md"

# Markers for the README section
README_START_MARKER = "<!-- VERSIONS_START -->"
README_END_MARKER = "<!-- VERSIONS_END -->"
COMMUNITY_README_START_MARKER = "<!-- COMMUNITY_VERSIONS_START -->"
COMMUNITY_README_END_MARKER = "<!-- COMMUNITY_VERSIONS_END -->"
ORG_NAME = "actions"
GITHUB_API_URL = "https://api.github.com"
ACTION_NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def github_api_headers() -> list[str]:
    """Return curl headers for GitHub API requests."""
    headers = ["-H", "Accept: application/vnd.github+json"]
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers.extend(
            [
                "-H",
                f"Authorization: Bearer {token}",
                "-H",
                "X-GitHub-Api-Version: 2022-11-28",
            ]
        )
    return headers


def load_unversioned() -> set[str]:
    """Load the set of repos known to have no vINTEGER tags."""
    if not UNVERSIONED_FILE.exists():
        return set()
    return set(line.strip() for line in UNVERSIONED_FILE.read_text().splitlines() if line.strip())


def save_unversioned(repos: set[str]) -> None:
    """Save the set of repos known to have no vINTEGER tags."""
    with open(UNVERSIONED_FILE, "w") as f:
        for repo_name in sorted(repos):
            f.write(f"{repo_name}\n")


def load_actions_file(path: Path) -> list[str]:
    """Load owner/repo action names from a text file."""
    if not path.exists():
        return []

    actions = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        action = line.split("#", 1)[0].strip()
        if not action:
            continue
        if not ACTION_NAME_RE.match(action):
            raise ValueError(
                f"Invalid action name in {path}:{line_number}: {line!r}"
            )
        actions.append(action)

    return sorted(set(actions), key=str.lower)


def load_trusted_actions() -> list[str]:
    """Load curated trusted owner/repo actions to include in generated versions."""
    return load_actions_file(TRUSTED_ACTIONS_FILE)


def load_community_actions() -> list[str]:
    """Load broader community owner/repo actions to include in generated versions."""
    return load_actions_file(COMMUNITY_ACTIONS_FILE)


def replace_readme_section(text: str, start_marker: str, end_marker: str, section: str) -> str:
    """Replace one generated README section, or append it when absent."""
    if start_marker in text and end_marker in text:
        pattern = re.compile(
            re.escape(start_marker) + r".*?" + re.escape(end_marker),
            re.DOTALL,
        )
        return pattern.sub(section, text)

    return text.rstrip() + "\n\n" + section + "\n"


def update_readme(versions_content: str, community_versions_content: str = "") -> None:
    """Update the README.md with the latest versions in a fenced code block."""
    if not README_FILE.exists():
        print(f"Warning: {README_FILE} not found, skipping README update")
        return

    readme_text = README_FILE.read_text()

    trusted_section = f"""{README_START_MARKER}
## Latest trusted versions

```
{versions_content}```
{README_END_MARKER}"""

    new_readme = replace_readme_section(
        readme_text,
        README_START_MARKER,
        README_END_MARKER,
        trusted_section,
    )

    if community_versions_content:
        community_section = f"""{COMMUNITY_README_START_MARKER}
## Latest community versions

```
{community_versions_content}```
{COMMUNITY_README_END_MARKER}"""
        new_readme = replace_readme_section(
            new_readme,
            COMMUNITY_README_START_MARKER,
            COMMUNITY_README_END_MARKER,
            community_section,
        )

    README_FILE.write_text(new_readme)
    print(f"Updated {README_FILE} with latest versions")


def fetch_repos(org: str) -> list[dict]:
    """Fetch all repos for an organization using curl."""
    repos = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API_URL}/orgs/{org}/repos?per_page={per_page}&page={page}"
        result = subprocess.run(
            ["curl", "-s", *github_api_headers(), url],
            capture_output=True,
            text=True,
            check=True,
        )

        page_repos = json.loads(result.stdout)
        if isinstance(page_repos, dict) and "message" in page_repos:
            raise RuntimeError(f"API error fetching repos for {org}: {page_repos['message']}")

        if not page_repos:
            break

        repos.extend(page_repos)

        if len(page_repos) < per_page:
            break

        page += 1

    return repos


def fetch_tags(org: str, repo_name: str) -> list[str]:
    """Fetch all tags for a repository using the GitHub API."""
    tags = []
    page = 1
    per_page = 100

    while True:
        url = f"{GITHUB_API_URL}/repos/{org}/{repo_name}/tags?per_page={per_page}&page={page}"
        result = subprocess.run(
            ["curl", "-s", *github_api_headers(), url],
            capture_output=True,
            text=True,
            check=True,
        )

        page_tags = json.loads(result.stdout)

        if isinstance(page_tags, dict) and "message" in page_tags:
            raise RuntimeError(f"API error for {repo_name}: {page_tags['message']}")

        if not page_tags:
            break

        tags.extend(tag["name"] for tag in page_tags)

        if len(page_tags) < per_page:
            break

        page += 1

    return tags


def get_latest_version_tag(tags: list[str]) -> str | None:
    """Get the latest vINTEGER tag from a list of tags."""
    # Filter to vINTEGER tags (e.g., v1, v2, v10)
    version_pattern = re.compile(r"^v(\d+)$")
    version_tags = []

    for tag in tags:
        match = version_pattern.match(tag.strip())
        if match:
            version_tags.append((int(match.group(1)), tag.strip()))

    if not version_tags:
        return None

    # Sort by version number descending and return the latest
    version_tags.sort(reverse=True, key=lambda x: x[0])
    return version_tags[0][1]


def fetch_tracked_action_versions(
    actions: list[str],
    label: str,
    skip_actions: set[str] | None = None,
) -> list[tuple[str, str]]:
    """Fetch latest vINTEGER tags for a list of owner/repo actions."""
    if actions:
        print(f"\nFetching tags for {len(actions)} {label} actions...")

    versions = []
    versioned_actions = set(skip_actions or set())
    for action in actions:
        if action in versioned_actions:
            print(f"Skipping {action} (already fetched)")
            continue

        owner, repo_name = action.split("/", 1)
        print(f"Fetching tags for {action}...", end=" ")
        tags = fetch_tags(owner, repo_name)
        latest_tag = get_latest_version_tag(tags)

        if latest_tag:
            versions.append((action, latest_tag))
            versioned_actions.add(action)
            print(f"{latest_tag}")
        else:
            print("no vINTEGER tag")

    return versions


def versions_content(versions: list[tuple[str, str]]) -> str:
    """Build versions.txt content from action version tuples."""
    versions.sort(key=lambda x: x[0].lower())
    if not versions:
        return ""
    return "\n".join(f"{action}@{tag}" for action, tag in versions) + "\n"


def main():
    """Main function to fetch repos, get tags via API, and generate versions.txt."""
    # Load cached unversioned repos
    unversioned = load_unversioned()
    if unversioned:
        print(f"Loaded {len(unversioned)} known unversioned repos from cache")

    print(f"Fetching repos for {ORG_NAME}...")
    repos = fetch_repos(ORG_NAME)
    print(f"Found {len(repos)} repos")

    versions = []
    new_unversioned = set()

    for repo in repos:
        repo_name = repo["name"]

        # Skip repos known to have no vINTEGER tags
        if repo_name in unversioned:
            print(f"Skipping {repo_name} (cached as unversioned)")
            new_unversioned.add(repo_name)
            continue

        print(f"Fetching tags for {repo_name}...", end=" ")
        tags = fetch_tags(ORG_NAME, repo_name)
        latest_tag = get_latest_version_tag(tags)

        if latest_tag:
            versions.append((f"{ORG_NAME}/{repo_name}", latest_tag))
            print(f"{latest_tag}")
        else:
            print("no vINTEGER tag")
            new_unversioned.add(repo_name)

    trusted_actions = load_trusted_actions()
    trusted_versioned = {action for action, _ in versions}
    versions.extend(
        fetch_tracked_action_versions(
            trusted_actions,
            "trusted",
            skip_actions=trusted_versioned,
        )
    )
    trusted_versioned = {action for action, _ in versions}

    community_versions = fetch_tracked_action_versions(
        load_community_actions(),
        "community",
        skip_actions=trusted_versioned,
    )

    trusted_versions_content = versions_content(versions)
    community_versions_content = versions_content(community_versions)

    # Write versions snapshots
    with open(VERSIONS_FILE, "w") as f:
        f.write(trusted_versions_content)
    with open(COMMUNITY_VERSIONS_FILE, "w") as f:
        f.write(community_versions_content)
    if PACKAGE_VERSIONS_FILE.parent.exists():
        PACKAGE_VERSIONS_FILE.write_text(trusted_versions_content)
        PACKAGE_COMMUNITY_VERSIONS_FILE.write_text(community_versions_content)

    # Update README.md with the versions
    update_readme(trusted_versions_content, community_versions_content)

    # Update unversioned.txt
    save_unversioned(new_unversioned)

    print(f"\nWrote {len(versions)} trusted versions to {VERSIONS_FILE}")
    print(f"Wrote {len(community_versions)} community versions to {COMMUNITY_VERSIONS_FILE}")
    print(f"Cached {len(new_unversioned)} unversioned repos to {UNVERSIONED_FILE}")


if __name__ == "__main__":
    main()
