#!/usr/bin/env python3
"""Run the update engine from a source checkout. See docs/architecture.md."""

import argparse
import json
from pathlib import Path

from actions_latest.models import ActionRecord, ActionState
from actions_latest.snapshot import load_catalog, publish_snapshot, validate_snapshot
from actions_latest.updater import update

ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=ROOT / "catalog.json")
    parser.add_argument("--snapshot", type=Path, default=ROOT / "actions_latest/actions.db")
    parser.add_argument("--workers", type=int, choices=range(1, 17), default=6)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="Validate the snapshot offline")
    modes.add_argument("--rebuild", action="store_true", help="Rebuild the snapshot offline")
    args = parser.parse_args()
    if args.check:
        records = validate_snapshot(args.snapshot)
        if [r.catalog for r in records] != load_catalog(args.catalog):
            raise SystemExit("Snapshot catalog differs from inputs; run update.py --rebuild")
        print(f"Validated {len(records)} actions")
    elif args.rebuild:
        previous = (
            {r.action.casefold(): r.state for r in validate_snapshot(args.snapshot)}
            if args.snapshot.exists()
            else {}
        )
        records = [
            ActionRecord(catalog=c, state=previous.get(c.action.casefold(), ActionState()))
            for c in load_catalog(args.catalog)
        ]
        publish_snapshot(records, args.snapshot)
    else:
        print(json.dumps(update(args.catalog, args.snapshot, workers=args.workers), indent=2))


if __name__ == "__main__":
    main()
