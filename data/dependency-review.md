# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| filelock | \[&quot;3.32.6&quot;\] | \[&quot;3.32.7&quot;\] | [3.32.7](https://pypi.org/project/filelock/3.32.7/) |
| idna | \[&quot;3.19&quot;\] | \[&quot;3.20&quot;\] | [3.20](https://pypi.org/project/idna/3.20/) |
| ruff | \[&quot;0.16.7&quot;\] | \[&quot;0.16.8&quot;\] | [0.16.8](https://pypi.org/project/ruff/0.16.8/) |
| uv | \[&quot;0.12.13&quot;\] | \[&quot;0.12.17&quot;\] | [0.12.17](https://pypi.org/project/uv/0.12.17/) |

**Proposal base commit:** `0cd139553e3d4e70d19c38cc7873e833fb7352d6`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.

[Checks and publication result](https://github.com/pauljones0/actions-latest/actions/runs/35575643677)

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
