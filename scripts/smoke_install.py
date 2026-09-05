"""Build a wheel, install into a fresh environment, and exercise packaged MCP."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SMOKE = """
import asyncio
import os
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from actions_latest.versions import MetadataStore, get_db_path

assert get_db_path().is_file(), 'wheel omitted the snapshot'
assert MetadataStore(get_db_path()).search('checkout'), 'packaged search is broken'
async def check():
    executable = Path(sys.executable).parent / ('actions-latest-mcp.exe' if os.name == 'nt' else 'actions-latest-mcp')
    assert executable.is_file(), 'wheel omitted the console entry point'
    parameters = StdioServerParameters(command=str(executable), env={'ACTIONS_LATEST_AUTO_REFRESH': '0'})
    async with stdio_client(parameters) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            assert [tool.name for tool in (await session.list_tools()).tools] == ['run']
            result = await session.call_tool('run', {'command': 'grep checkout'})
            assert not result.isError
            assert 'actions/checkout' in ''.join(item.text for item in result.content)
asyncio.run(asyncio.wait_for(check(), 20))
print('Fresh wheel installation, bundled database, and MCP protocol passed')
"""


def main():
    with tempfile.TemporaryDirectory(prefix="actions-install-") as directory:
        temporary = Path(directory)
        subprocess.run(
            ["uv", "build", "--wheel", "--out-dir", str(temporary)],
            cwd=ROOT,
            check=True,
            timeout=120,
        )
        environment = temporary / "venv"
        subprocess.run(
            ["uv", "venv", "--python", sys.executable, str(environment)], check=True, timeout=60
        )
        python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
        wheel = next(temporary.glob("*.whl"))
        subprocess.run(
            ["uv", "pip", "install", "--python", str(python), str(wheel)], check=True, timeout=120
        )
        env = os.environ.copy()
        env.pop("PYTHONPATH", None)
        env["ACTIONS_LATEST_AUTO_REFRESH"] = "0"
        subprocess.run([str(python), "-c", SMOKE], cwd=temporary, env=env, check=True, timeout=30)


if __name__ == "__main__":
    main()
