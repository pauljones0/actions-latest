# Operating automatic freshness

Routine upgrades run automatically or arrive as prepared PRs. This document describes the operating guarantees; [the maintenance guide](../MAINTENANCE.md) is optional troubleshooting reference. Completed milestones and verification links are in [implementation history](history.md).

## Published state and review

`catalog.json` contains curated membership and human guidance. `data/discovered.json` contains automatic admissions. Curated entries override machine entries with the same case-insensitive identifier. To permanently exclude an entry, add its identifier to `catalog-policy.json`; merely removing a curated entry can allow rediscovery. An excluded machine record is retained as history but omitted from the combined catalog. Discovery does not remove existing actions on API failure or archive status.

Discovery checks repository maintenance and popularity, a root action manifest at the default branch's immutable SHA, numeric tags, and an offline manifest scan. It admits at most the configured number per run. New actions start without a selected revision; the regular updater must observe stable mappings at least seven days apart. Root-only, topic-based discovery deliberately has incomplete coverage; add subdirectory actions or overlooked projects to the curated catalog. Rejections retry after seven days, transport/scanner errors after six hours. Search errors appear in `data/discovery-report.json`.

Manifest-backed descriptions supersede historical catalog descriptions in search and summaries. Operational facts are refreshed at the selected SHA when rescanned (at least weekly). Curated categorization and advice remain human inputs, not inferred safety guarantees. Record `reviewed_sha` and `reviewed_at` after reviewing human guidance against an immutable revision; a later revision marks it for review. Existing historical guidance starts unreviewed. The health report lists outstanding editorial reviews without treating human judgment as something automation can fabricate.

## Schedules and failures

The daily updater publishes `actions_latest/actions.db`, `data/snapshot-v2.json.gz`, discovery results, and `data/health.json` together. It runs tests before fetching and verifies all publication inputs before pushing. A final health check fails if publication is older than 48 hours, more than 20% of actions lack a successful check in 72 hours, or more than 20% have scan failures. Healthy partial results are retained even when coverage fails; a new feed timestamp alone cannot satisfy health.

The independent six-hour monitor calculates these metrics from the feed at its current checkout. It dispatches a recovery only when no update is active and no update was created in the preceding six hours. The monitor remains failed until a later check confirms actual recovery. Inspect Actions job summaries and individual record errors. Discovery search failures and weekly maintenance failures have their own workflow status; none are silently marked successful.

To recover after correcting credentials, a Git conflict, or an upstream outage:

```sh
gh workflow run update.yml --repo pauljones0/actions-latest --ref main
gh workflow run health.yml --repo pauljones0/actions-latest --ref main
```

The updater and maintenance workflow share a concurrency group. Every generated-state push is a normal fast-forward push: concurrent human changes cause failure and require rerunning from current main. No binary conflict merge or force push is allowed. The existing read-only `GH_PAT` supports higher read limits; all maintenance and data pushes use the scoped workflow token. Secrets are passed only to the steps that need them. Git credentials go through temporary askpass code reading the environment, not token-bearing command arguments or repository configuration.

Weekly maintenance resolves the newest stable release within the current direct tool major, refreshes the dependency lock inside declared ranges, updates the scanner version contract, and tests before publication. Transitive versions follow their upstream constraints. Test or resolution failures prevent publication to main. Fully prepared candidates that fail validation arrive as draft repair PRs with version comparisons, failure links, and explicitly dispatched CI. Bootstrap/resolution failures without a complete candidate remain visible in the maintenance job. Incompatible upgrades require an explicit migration. To undo a bad accepted maintenance change, revert its commit normally and correct/pin the offending dependency before the next maintenance run. Maintenance dispatches the daily updater explicitly because token-created pushes may not trigger other workflows. `tooling.json` centralizes the uv bootstrap pin so a routine tool upgrade never needs workflow-file write permission. [Dependabot](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates) checks GitHub Actions pins weekly and groups minor/patch updates while leaving major upgrades in individual PRs; these run the full CI matrix and workflow scanner before maintainer review. Workflow pins were brought to their current releases during deployment.

## Client cache and trust

The application bundles a validated snapshot so first use and offline search work. Background refresh uses a fixed HTTPS URL on this repository's main branch, a five-second socket timeout, a 32 MiB compressed limit, and a 128 MiB decompression limit. It validates schema, Pydantic models, duplicate identifiers, SHA/evidence relationships, future publication dates, and the canonical record digest before building a local SQLite database. The digest detects corruption; authenticity relies on HTTPS and control of the GitHub repository, not an independent signature.

Successful checks are spaced six hours apart, failed attempts one hour apart. Checks happen on startup and tool requests; an idle or stopped process is not a scheduler. Atomic replacement keeps active readers on a complete snapshot. An interprocess file lock prevents overlapping cache writers. Failed downloads retain the previous usable cache or bundle. Cache metadata is validated and corrupt caches can be rebuilt. `status` reports source, attempt/success/publication times, errors, and a publication-age warning. Cached data may be stale while offline; per-action eligibility still enforces scan age.

Set `ACTIONS_LATEST_AUTO_REFRESH=0` to disable snapshot network requests. `man` and `audit` are separately explicit online commands. Refresh only replaces data, not executable code or dependencies. Schema-major migrations and application fixes require reinstalling/updating the tool; keep old schema feeds available during future migrations, and expect old clients to report stale publication when a feed is retired.

## Review artifacts

The daily updater commits a semantic before/after catalog report, a prioritized overview, and a complete machine-readable review queue. It excludes timestamp and popularity churn. `manage.py changes` can compare arbitrary commits from the same schema without altering the working tree. Review priorities put fetch/scan failures first, invalidated prior reviews next, and historical unreviewed guidance last, ordered by popularity.

Dependency maintenance records all changed resolved versions, upstream package links, candidate/validated state, and the GitHub run proving validation and publication. Failed validation candidates are delivered through one draft repair PR without overwriting human edits. A downloadable patch/report artifact is retained for 14 days as a fallback when preparation reached that stage. Failure summaries work without project dependencies and point directly to the relevant recovery operation. Tests or schema validation must not be bypassed to obtain a successful status.
