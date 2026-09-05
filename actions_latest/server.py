"""MCP transport adapter; command semantics live in commands.py."""

import asyncio

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError

from .commands import Navigator
from .versions import MetadataStore, get_db_path

mcp = FastMCP("actions-latest")
navigator = Navigator(MetadataStore(get_db_path()))


@mcp.tool()
async def run(command: str) -> str:
    """Discover GitHub Actions with browse, ls, grep, find, cat, man, audit, help.

    Search returns candidates: inspect security and stability with cat before use.
    Pipe identities with |, chain successful commands with &&, or sequence with ;.
    Examples: grep setup | grep node | cat; find --tag docker | cat.
    """
    result = await asyncio.to_thread(navigator.run, command)
    if result.code:
        raise ToolError(result.text)
    return result.text


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
