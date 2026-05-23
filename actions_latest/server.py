"""MCP server exposing latest tracked GitHub Actions versions."""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from actions_latest.versions import (
    latest_for_action,
    load_versions_text,
    parse_versions,
    workflow_updates,
)

mcp = FastMCP("actions-latest")


@mcp.tool()
def latest_github_actions_versions(refresh: bool = True, include_untrusted: bool = False) -> str:
    """Return latest trusted GitHub Actions versions, optionally including community actions."""
    return load_versions_text(refresh=refresh, include_untrusted=include_untrusted)


@mcp.tool()
def latest_github_action_version(
    action: str,
    refresh: bool = True,
    include_untrusted: bool = False,
) -> str:
    """Return the latest stable major tag for one GitHub action."""
    versions = parse_versions(load_versions_text(refresh=refresh, include_untrusted=include_untrusted))
    result = latest_for_action(action, versions, refresh=refresh and include_untrusted)
    if result is None:
        return f"No stable major tag found for {action!r}."

    normalized, latest = result
    return f"{normalized}@{latest}"


@mcp.tool()
def check_github_actions_workflow(
    workflow: str,
    refresh: bool = True,
    include_untrusted: bool = False,
) -> str:
    """Check workflow YAML text and suggest stable major tag updates."""
    versions = parse_versions(load_versions_text(refresh=refresh, include_untrusted=include_untrusted))
    updates = workflow_updates(workflow, versions, refresh=refresh and include_untrusted)
    if not updates:
        return "No outdated stable GitHub Action references found."

    return "\n".join(
        f"{update.action}: {update.current} -> {update.latest} ({update.line.strip()})"
        for update in updates
    )


def main() -> None:
    """Run the stdio MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
