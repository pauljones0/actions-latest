"""Dependency-free, actionable failure summary even when project bootstrap fails."""

import argparse
import os

URL = "https://github.com/pauljones0/actions-latest"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["refresh", "maintain", "health"])
    operation = parser.parse_args().operation
    workflow = {"refresh": "update", "maintain": "maintenance", "health": "health"}[operation]
    report = f"""## {operation.title()} needs attention

Open the first failed step above; subsequent skipped steps are consequences.

| Failure | What to do |
| --- | --- |
| Git push rejected | Another commit won the race. Rerun from current main; never force-push generated data. |
| GitHub rate limit, network outage, or 5xx | Keep the working snapshot. Retry after the upstream service recovers. |
| Authentication or 403 | Check token permissions/expiry. Data and maintenance writes use the workflow token; GH_PAT is read-only. |
| Dependency validation | Main keeps its existing dependencies. Open the draft repair PR linked in this run's summary; its changes and CI are already prepared. The proposal artifact is a fallback if PR creation failed. |
| Dependency resolution or bootstrap | No complete upgrade candidate exists yet. Inspect the first failing step; rerun after resolving its cause. |
| Snapshot/feed validation | Do not bypass it. Rebuild with `uv run python update.py --rebuild`, then run `--check`. |
| Publication/observation coverage | Inspect [prioritized issues]({URL}/blob/main/data/maintenance.md). The health monitor can retry stalled refreshes. |

[Open the workflow and choose Run workflow]({URL}/actions/workflows/{workflow}.yml), or:

```sh
gh workflow run {workflow}.yml --repo pauljones0/actions-latest --ref main
```

[Review and rollback guide]({URL}/blob/main/MAINTENANCE.md). A failed run is not proof that upstream data is unsafe; investigate its evidence before accepting that conclusion.
"""
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as handle:
            handle.write(report)


if __name__ == "__main__":
    main()
