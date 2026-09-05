"""Deliver a failed, fully prepared upgrade as one draft PR, using only stdlib."""

import json
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "maintenance/failed-upgrade-"
FILES = {"pyproject.toml", "uv.lock", "actions_latest/models.py", "tooling.json"}


def run(*args, cwd=ROOT):
    return subprocess.check_output(args, cwd=cwd, text=True, timeout=120).strip()


def proposal(root):
    report = json.loads((root / "data/dependency-review.json").read_text())
    patch = root / "data/maintenance-proposal.patch"
    if not report.get("prepared") or report.get("validated") or not patch.exists():
        return None
    if not patch.read_bytes().strip():
        return None
    if not re.fullmatch(r"[0-9a-f]{40}", report["base_commit"]):
        raise ValueError("Invalid proposal base commit")
    return report


def body(report_text, run_url):
    return f"""Compatible upgrades failed validation, so automatic publication stopped.
Main keeps its existing dependencies. This draft contains the exact candidate;
there is no artifact to download or patch to reconstruct.

**Next action:** inspect the [failed validation step]({run_url}), fix the cause
on this branch, and mark ready only after the checks pass. If a rerun passes,
verify the original failure was transient before accepting the upgrade.
Closing this PR declines this attempt; the next weekly run tries current releases.

CI is dispatched automatically for this branch. Further commits run normal PR CI.
The dependency report records the original failed attempt; current checks show
whether subsequent fixes work. Automation never overwrites this branch.

{report_text}
"""


def main():
    report = proposal(ROOT)
    if report is None:
        print("No unpublished candidate changes; no review PR needed.")
        return
    repo = os.environ["GITHUB_REPOSITORY"]
    run_id = os.environ["GITHUB_RUN_ID"]
    if not run_id.isdecimal():
        raise ValueError("Invalid workflow run ID")
    prs = json.loads(
        run(
            "gh",
            "pr",
            "list",
            "--repo",
            repo,
            "--state",
            "open",
            "--limit",
            "100",
            "--json",
            "headRefName,url",
        )
    )
    for pr in prs:
        if pr["headRefName"].startswith(PREFIX):
            print(f"An upgrade already needs attention: {pr['url']}. Preserving its edits.")
            return
    branch = PREFIX + run_id
    with tempfile.TemporaryDirectory(prefix="maintenance-pr-") as directory:
        checkout = Path(directory) / "checkout"
        run("git", "worktree", "add", "--detach", str(checkout), report["base_commit"])
        try:
            run("git", "apply", str(ROOT / "data/maintenance-proposal.patch"), cwd=checkout)
            changed = set(run("git", "diff", "--name-only", cwd=checkout).splitlines())
            if not changed or changed - FILES:
                raise ValueError("Proposal must change only managed dependency files")
            (checkout / "data").mkdir(exist_ok=True)
            for name in ("dependency-review.json", "dependency-review.md"):
                (checkout / "data" / name).write_bytes((ROOT / "data" / name).read_bytes())
            run(
                "git",
                "add",
                "--",
                *sorted(FILES),
                "data/dependency-review.json",
                "data/dependency-review.md",
                cwd=checkout,
            )
            run(
                "git",
                "-c",
                "user.name=github-actions[bot]",
                "-c",
                "user.email=github-actions[bot]@users.noreply.github.com",
                "commit",
                "-m",
                "Prepare failed dependency upgrade for repair",
                cwd=checkout,
            )
            run(
                "git",
                "-c",
                "credential.helper=",
                "-c",
                "credential.helper=!gh auth git-credential",
                "push",
                "origin",
                f"HEAD:refs/heads/{branch}",
                cwd=checkout,
            )
            # Explicit dispatch avoids making the owner approve bot-triggered CI.
            run("gh", "workflow", "run", "test.yml", "--repo", repo, "--ref", branch)
            description = Path(directory) / "body.md"
            description.write_text(
                body(
                    (ROOT / "data/dependency-review.md").read_text(),
                    f"https://github.com/{repo}/actions/runs/{run_id}",
                )
            )
            print(
                run(
                    "gh",
                    "pr",
                    "create",
                    "--repo",
                    repo,
                    "--base",
                    "main",
                    "--head",
                    branch,
                    "--draft",
                    "--title",
                    "Repair dependency upgrade that failed validation",
                    "--body-file",
                    str(description),
                )
            )
        finally:
            run("git", "worktree", "remove", "--force", str(checkout))


if __name__ == "__main__":
    main()
