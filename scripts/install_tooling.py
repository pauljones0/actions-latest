"""Bootstrap the centrally pinned uv version without project dependencies."""

import json
import re
import subprocess
import sys
from pathlib import Path


def main():
    version = json.loads((Path(__file__).resolve().parents[1] / "tooling.json").read_text())["uv"]
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid uv version pin")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", f"uv=={version}"], check=True, timeout=120
    )


if __name__ == "__main__":
    main()
