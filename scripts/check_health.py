#!/usr/bin/env python3
"""Independent age/coverage check with bounded recovery for a stalled updater."""

import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

from actions_latest.feed import decode_feed
from actions_latest.health import health_report, include_discovery
from actions_latest.models import utc_now


def main():
    now = utc_now()
    feed = decode_feed(Path("data/snapshot-v2.json.gz").read_bytes())
    report = health_report(feed.records, feed.published_at, now)
    include_discovery(report, json.loads(Path("data/discovery-report.json").read_text()), now)
    text = json.dumps(report, indent=2)
    print(text)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as handle:
            handle.write("```json\n" + text + "\n```\n")
    if report["healthy"]:
        return
    runs = json.loads(
        subprocess.check_output(
            [
                "gh",
                "run",
                "list",
                "--workflow",
                "update.yml",
                "--branch",
                "main",
                "--limit",
                "5",
                "--json",
                "status,createdAt",
            ],
            text=True,
            timeout=60,
        )
    )
    active = any(
        run["status"] in {"queued", "in_progress", "waiting", "pending", "requested"}
        for run in runs
    )
    recent = any(
        now - datetime.fromisoformat(run["createdAt"].replace("Z", "+00:00")) < timedelta(hours=6)
        for run in runs
    )
    if not active and not recent:
        subprocess.run(
            ["gh", "workflow", "run", "update.yml", "--ref", "main"], check=True, timeout=60
        )
        print("Dispatched one recovery update; next monitor run will verify recovery.")
    print("::error::Freshness degraded. Inspect the job summary and Refresh workflow logs.")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
