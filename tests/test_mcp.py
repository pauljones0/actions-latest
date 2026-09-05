import asyncio
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def test_stdio_protocol_discovery_search_and_errors():
    async def check():
        parameters = StdioServerParameters(
            command=sys.executable,
            args=["-m", "actions_latest.server"],
            cwd=str(Path(__file__).resolve().parents[1]),
            env={"PATH": os.environ["PATH"]},
        )
        async with stdio_client(parameters) as (reader, writer):
            async with ClientSession(reader, writer) as session:
                initialized = await session.initialize()
                assert initialized.serverInfo.name == "actions-latest"
                assert [tool.name for tool in (await session.list_tools()).tools] == ["run"]
                result = await session.call_tool("run", {"command": "grep checkout"})
                assert not result.isError
                assert "actions/checkout" in "".join(item.text for item in result.content)
                failed = await session.call_tool("run", {"command": "cat nonexistent/action"})
                assert failed.isError

    asyncio.run(asyncio.wait_for(check(), 20))
