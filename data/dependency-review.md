# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| No package version changes | — | — | Lock format/metadata may still change. |

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
