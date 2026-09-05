# Maintenance: start here

**Most days, do nothing.** Catalog refresh, candidate discovery, client data refresh, and compatible Python/tool upgrades run automatically. Tests and freshness checks run before a change is treated as successful.

| What you need | Open this |
| --- | --- |
| Is anything actionable? | [Prioritized overview](data/maintenance.md) |
| What changed in the catalog? | [Readable before/after changes](data/catalog-changes.md) |
| What dependencies changed? | [Latest dependency review](data/dependency-review.md) |
| Is an upgrade waiting for review? | [Open upgrade PRs](https://github.com/pauljones0/actions-latest/pulls?q=is%3Apr+is%3Aopen+author%3Aapp%2Fdependabot) |
| Did an operation fail? | [Workflow runs](https://github.com/pauljones0/actions-latest/actions) — open the failed run's summary |

## Review an upgrade

Routine workflow minor/patch updates are grouped; major upgrades get separate PRs so one breaking change cannot hide among routine updates. Dependabot supplies old/new versions, source links, and release notes. CI supplies three Python versions, fresh installation/MCP checks, snapshot consistency, and workflow scanning.

1. Read the release notes for removed inputs, runtime/runner changes, and changed defaults. Check whether this repo uses the affected behavior. Green tests support compatibility but do not replace that decision.
2. Check that the diff contains the expected immutable action pins and that all checks passed for the PR's current commit.
3. Merge if the change is understood and compatible. If not, leave it open and investigate the concrete mismatch; do not accept a failed result without checking its cause.

Routine Python/tool updates already follow declared compatibility bounds and publish after validation; they do not need another approval. Their review report includes every changed resolved package (including transitive dependencies), version links, validation state, and the run containing the publication result.

## Review one action's guidance

```sh
uv run python manage.py status
uv run python manage.py review actions/checkout
```

The review packet contains the immutable source, parsed facts, each human claim, the previous reviewed revision when available, and the exact acknowledgement command. Fix unsupported claims in `catalog.json` before acknowledging. The command requires the selected SHA and refuses stale acknowledgements. It rebuilds the publication artifacts for you; review and commit the resulting diff normally. Editorial acknowledgement never clears scanner findings or bypasses the seven-day stability gate.

Failures come first, then previously reviewed guidance invalidated by a changed revision, then historical unreviewed entries ordered by popularity. The full queue is linked from the overview; you do not need to work through hundreds of historical entries before operating the repo.

## Rerun or diagnose

These commands dispatch the operation on current GitHub `main`; they do not run an expensive update locally:

```sh
uv run python manage.py refresh
uv run python manage.py maintain
uv run python manage.py health
```

Without a checkout, open [Refresh](https://github.com/pauljones0/actions-latest/actions/workflows/update.yml), [Maintenance](https://github.com/pauljones0/actions-latest/actions/workflows/maintenance.yml), or [Health](https://github.com/pauljones0/actions-latest/actions/workflows/health.yml) and choose **Run workflow**.

Failure summaries explain common causes and the correct next operation. A rejected push usually needs a rerun from current main. An outage needs upstream recovery, not deleting catalog entries. Persistent manifest failures need inspection at the selected immutable SHA; a repository can contain subdirectory actions without having a root action.

For failed dependency maintenance, download the **maintenance-proposal** artifact from that run (retained 14 days). It contains the exact proposed patch and before/after report. In a clean checkout of that run's commit, inspect it, then:

```sh
git apply --check maintenance-proposal.patch
git apply maintenance-proposal.patch
python scripts/install_tooling.py
uv sync --locked --group dev
uv run pytest -q
```

Use the first failing check from the run to narrow the investigation. You do not have to reconstruct the candidate from an index that has since changed. Bootstrap or resolver failures may happen before a proposal exists; the original error remains in the failed step.

## Undo a bad accepted maintenance change

Pause maintenance first so the next run does not immediately reapply the upgrade:

```sh
gh workflow disable maintenance.yml --repo pauljones0/actions-latest
```

In a clean checkout of latest main, run `git show <maintenance-commit>` and confirm that it is the dependency maintenance commit you intend to undo. Then use `git revert <maintenance-commit>`, test, and publish the revert through the normal review/push path. Before resuming, prevent the bad version from being selected again:

- For uv, Ruff, or zizmor, add `"hold": ["ruff"]` (substitute the affected tool) to `tooling.json`. The reverted tool pin stays fixed while other maintenance continues. Remove the hold after resolving the incompatibility.
- For a Python dependency, constrain the known-good version in `pyproject.toml` (for example, `constraint-dependencies = ["package==known-good-version"]` under `[tool.uv]`) and regenerate the lock. Existing dependency bounds and uv constraints remain authoritative.

Then resume:

```sh
gh workflow enable maintenance.yml --repo pauljones0/actions-latest
uv run python manage.py maintain
```

Daily catalog freshness continues while dependency maintenance is paused. For a workflow upgrade, revert its PR's commit and investigate the breaking behavior before merging a replacement. Do not restore arbitrary old binary snapshots or force-push over concurrent changes.

## Compare any snapshot revision

```sh
uv run python manage.py changes --base HEAD~1
```

This reads the old SQLite from Git and compares meaningful facts to the working snapshot. It does not alter the checkout or require manual binary inspection. Choose a base from the same snapshot schema; schema migrations require their migration notes. The daily report compares the current run with its starting snapshot and omits timestamp and popularity churn.
