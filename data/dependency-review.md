# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| pyjwt | \[&quot;2.14.0&quot;\] | \[&quot;2.15.0&quot;\] | [2.15.0](https://pypi.org/project/pyjwt/2.15.0/) |
| ruff | \[&quot;0.16.8&quot;\] | \[&quot;0.16.9&quot;\] | [0.16.9](https://pypi.org/project/ruff/0.16.9/) |
| starlette | \[&quot;1.6.0&quot;\] | \[&quot;1.7.0&quot;\] | [1.7.0](https://pypi.org/project/starlette/1.7.0/) |
| uv | \[&quot;0.12.17&quot;\] | \[&quot;0.12.19&quot;\] | [0.12.19](https://pypi.org/project/uv/0.12.19/) |
| uvicorn | \[&quot;0.53.0&quot;\] | \[&quot;0.54.0&quot;\] | [0.54.0](https://pypi.org/project/uvicorn/0.54.0/) |

**Proposal base commit:** `e8cfa5cc4798d96694a59ba79da8dfaaba34c7a3`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.

[Checks and publication result](https://github.com/pauljones0/actions-latest/actions/runs/36399219646)

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
