# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| filelock | \[&quot;3.32.5&quot;\] | \[&quot;3.32.6&quot;\] | [3.32.6](https://pypi.org/project/filelock/3.32.6/) |
| mcp | \[&quot;1.29.1&quot;\] | \[&quot;1.30.0&quot;\] | [1.30.0](https://pypi.org/project/mcp/1.30.0/) |
| pyjwt | \[&quot;2.13.0&quot;\] | \[&quot;2.14.0&quot;\] | [2.14.0](https://pypi.org/project/pyjwt/2.14.0/) |
| ruff | \[&quot;0.16.6&quot;\] | \[&quot;0.16.7&quot;\] | [0.16.7](https://pypi.org/project/ruff/0.16.7/) |
| uv | \[&quot;0.12.10&quot;\] | \[&quot;0.12.13&quot;\] | [0.12.13](https://pypi.org/project/uv/0.12.13/) |
| uvicorn | \[&quot;0.52.4&quot;\] | \[&quot;0.53.0&quot;\] | [0.53.0](https://pypi.org/project/uvicorn/0.53.0/) |
| zizmor | \[&quot;1.30.0&quot;\] | \[&quot;1.30.1&quot;\] | [1.30.1](https://pypi.org/project/zizmor/1.30.1/) |

**Proposal base commit:** `c6de647958584ea869146d7e13cc98195e82781e`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.

[Checks and publication result](https://github.com/pauljones0/actions-latest/actions/runs/34820212664)

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
