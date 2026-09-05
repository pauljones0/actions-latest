#!/usr/bin/env python3
"""Refresh, validate, and publish source-backed action observations."""

import argparse
import json
from pathlib import Path

from actions_latest.discovery import combined_catalog, discover
from actions_latest.feed import decode_feed, export_feed
from actions_latest.github import GitHubClient
from actions_latest.health import health_report, include_discovery
from actions_latest.models import ActionRecord, ActionState
from actions_latest.reports import change_report, maintenance_summary, review_queue
from actions_latest.security import Scanner
from actions_latest.snapshot import digest, publish_snapshot, validate_snapshot
from actions_latest.updater import update

ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "catalog.json")
    parser.add_argument("--snapshot", type=Path, default=ROOT / "actions_latest/actions.db")
    parser.add_argument("--discovered", type=Path)
    parser.add_argument("--policy", type=Path)
    parser.add_argument("--feed", type=Path)
    parser.add_argument("--discover", action="store_true")
    parser.add_argument("--workers", type=int, choices=range(1, 17), default=6)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--rebuild", action="store_true")
    modes.add_argument("--health", action="store_true")
    args = parser.parse_args()
    standard = (
        args.catalog == ROOT / "catalog.json"
        and args.snapshot == ROOT / "actions_latest/actions.db"
    )
    registry = args.discovered or (ROOT / "data/discovered.json" if standard else None)
    policy = args.policy or (ROOT / "catalog-policy.json" if standard else None)
    feed = args.feed or (ROOT / "data/snapshot-v2.json.gz" if standard else None)
    catalog = combined_catalog(args.catalog, registry, policy)
    if args.check or args.health:
        records = validate_snapshot(args.snapshot)
        if [r.catalog for r in records] != catalog:
            raise SystemExit("Snapshot catalog differs from inputs; run update.py --rebuild")
        if feed:
            published = decode_feed(feed.read_bytes())
            if published.records_sha256 != digest([r.model_dump(mode="json") for r in records]):
                raise SystemExit("Published feed differs from snapshot")
        if args.health:
            report = health_report(records, published.published_at if feed else None)
            if standard:
                discovery_path = ROOT / "data/discovery-report.json"
                include_discovery(
                    report,
                    json.loads(discovery_path.read_text()) if discovery_path.exists() else {},
                )
            print(json.dumps(report, indent=2))
            if not report["healthy"]:
                raise SystemExit(1)
        else:
            print(f"Validated {len(records)} actions and publication inputs")
        return
    before = validate_snapshot(args.snapshot) if standard and args.snapshot.exists() else []
    if args.rebuild:
        previous = (
            {r.action.casefold(): r.state for r in validate_snapshot(args.snapshot)}
            if args.snapshot.exists()
            else {}
        )
        publish_snapshot(
            [
                ActionRecord(catalog=c, state=previous.get(c.action.casefold(), ActionState()))
                for c in catalog
            ],
            args.snapshot,
        )
    else:
        client, scanner = GitHubClient(), Scanner()
        if args.discover:
            if not registry or not policy:
                raise SystemExit("Discovery requires --discovered and --policy with custom paths")
            discover(
                args.catalog,
                registry,
                registry.with_name("discovery-report.json"),
                policy,
                client,
                scanner,
            )
        print(
            json.dumps(
                update(
                    args.catalog,
                    args.snapshot,
                    workers=args.workers,
                    client=client,
                    scanner=scanner,
                    discovered_path=registry,
                    policy_path=policy,
                ),
                indent=2,
            )
        )
    if feed:
        export_feed(args.snapshot, feed)
    if standard:
        from actions_latest.feed import atomic_write

        records = validate_snapshot(args.snapshot)
        report = health_report(records, decode_feed(feed.read_bytes()).published_at)
        discovery_path = ROOT / "data/discovery-report.json"
        include_discovery(
            report, json.loads(discovery_path.read_text()) if discovery_path.exists() else {}
        )
        atomic_write(ROOT / "data/health.json", (json.dumps(report, indent=2) + "\n").encode())
        atomic_write(ROOT / "data/catalog-changes.md", change_report(before, records).encode())
        atomic_write(ROOT / "data/maintenance.md", maintenance_summary(records, report).encode())
        atomic_write(
            ROOT / "data/review-queue.json",
            (json.dumps(review_queue(records), indent=2) + "\n").encode(),
        )


if __name__ == "__main__":
    main()
