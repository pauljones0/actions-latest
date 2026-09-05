#!/usr/bin/env python3
"""One entry point for maintenance: status, changes, review, and recovery dispatch."""

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from actions_latest.feed import atomic_write, decode_feed
from actions_latest.health import health_report, include_discovery
from actions_latest.models import utc_now
from actions_latest.reports import action_review, change_report, maintenance_summary
from actions_latest.snapshot import validate_snapshot

ROOT = Path(__file__).resolve().parent
REPOSITORY = "pauljones0/actions-latest"


def mark_reviewed(root: Path, action: str, sha: str) -> None:
    records = validate_snapshot(root / "actions_latest/actions.db")
    record = next((r for r in records if r.action.casefold() == action.casefold()), None)
    if not record or not record.state.selected or record.state.selected.sha != sha:
        raise ValueError(
            "Selected revision changed or is missing. Run review again; no acknowledgement saved."
        )
    if not record.state.manifest or record.catalog.origin != "curated":
        raise ValueError(
            "Review acknowledgement requires a curated entry with a parsed selected manifest."
        )
    catalog_path = root / "catalog.json"
    entries = json.loads(catalog_path.read_text())
    entry = next(item for item in entries if item["action"].casefold() == action.casefold())
    entry.update(reviewed_sha=sha, reviewed_at=utc_now().isoformat())
    atomic_write(catalog_path, (json.dumps(entries, indent=2, ensure_ascii=False) + "\n").encode())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("status", help="Show the prioritized maintenance overview")
    changes = commands.add_parser("changes", help="Compare readable facts with a Git revision")
    changes.add_argument(
        "--base", default="HEAD", help="Commit/ref to compare with the working snapshot"
    )
    review = commands.add_parser(
        "review", help="Show immutable facts, human claims, and the exact review decision"
    )
    review.add_argument("action")
    reviewed = commands.add_parser(
        "reviewed", help="Record completed human review for an exact selected SHA"
    )
    reviewed.add_argument("action")
    reviewed.add_argument("--sha", required=True)
    for name in ("refresh", "maintain", "health"):
        commands.add_parser(name, help=f"Dispatch {name} on GitHub main")
    args = parser.parse_args()
    if args.command in {"refresh", "maintain", "health"}:
        workflow = {"refresh": "update", "maintain": "maintenance", "health": "health"}[
            args.command
        ]
        subprocess.run(
            ["gh", "workflow", "run", workflow + ".yml", "--repo", REPOSITORY, "--ref", "main"],
            check=True,
            timeout=60,
        )
        print(
            f"Opened a {args.command} run: https://github.com/{REPOSITORY}/actions/workflows/{workflow}.yml"
        )
        return
    records = validate_snapshot(ROOT / "actions_latest/actions.db")
    if args.command == "status":
        feed = decode_feed((ROOT / "data/snapshot-v2.json.gz").read_bytes())
        report = health_report(records, feed.published_at)
        include_discovery(report, json.loads((ROOT / "data/discovery-report.json").read_text()))
        print(maintenance_summary(records, report))
    elif args.command == "changes":
        commit = subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", args.base + "^{commit}"],
            cwd=ROOT,
            text=True,
            timeout=20,
        ).strip()
        content = subprocess.check_output(
            ["git", "show", commit + ":actions_latest/actions.db"], cwd=ROOT, timeout=30
        )
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "before.db"
            database.write_bytes(content)
            print(change_report(validate_snapshot(database), records))
    elif args.command == "review":
        record = next((r for r in records if r.action.casefold() == args.action.casefold()), None)
        if not record:
            raise ValueError("Action not found")
        print(action_review(record))
    else:
        mark_reviewed(ROOT, args.action, args.sha)
        subprocess.run(
            [sys.executable, str(ROOT / "update.py"), "--rebuild"], cwd=ROOT, check=True, timeout=60
        )
        print(
            "Review recorded and publication artifacts rebuilt. Inspect git diff, then commit the catalog and data together."
        )


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        raise SystemExit(str(exc)) from exc
