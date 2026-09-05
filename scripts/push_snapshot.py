"""Normal fast-forward push with credentials available only for this operation."""

import os
import subprocess
import tempfile
from pathlib import Path


def main():
    if not os.environ.get("GITHUB_TOKEN"):
        raise SystemExit("GITHUB_TOKEN is required for the snapshot push")
    with tempfile.TemporaryDirectory(prefix="actions-push-") as directory:
        askpass = Path(directory) / "askpass.sh"
        askpass.write_text('#!/bin/sh\nprintf "%s\\n" "$GITHUB_TOKEN"\n')
        askpass.chmod(0o700)
        env = dict(os.environ, GIT_ASKPASS=str(askpass), GIT_TERMINAL_PROMPT="0")
        # The helper prints only to Git's credential pipe. No credential is
        # embedded in the helper file, Git config, URL, or command arguments.
        subprocess.run(
            [
                "git",
                "-c",
                "credential.helper=",
                "-c",
                "credential.username=x-access-token",
                "push",
                "origin",
                "HEAD:main",
            ],
            env=env,
            check=True,
            timeout=60,
        )


if __name__ == "__main__":
    main()
