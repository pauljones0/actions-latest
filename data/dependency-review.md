# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| iniconfig | \[&quot;2.3.0&quot;\] | \[&quot;2.3.1&quot;\] | [2.3.1](https://pypi.org/project/iniconfig/2.3.1/) |
| pycparser | \[&quot;3.0&quot;\] | \[&quot;3.11&quot;\] | [3.11](https://pypi.org/project/pycparser/3.11/) |
| pydantic | \[&quot;2.13.5&quot;\] | \[&quot;2.14.1&quot;\] | [2.14.1](https://pypi.org/project/pydantic/2.14.1/) |
| pydantic-core | \[&quot;2.46.5&quot;\] | \[&quot;2.50.1&quot;\] | [2.50.1](https://pypi.org/project/pydantic-core/2.50.1/) |
| ruff | \[&quot;0.16.10&quot;\] | \[&quot;0.17.0&quot;\] | [0.17.0](https://pypi.org/project/ruff/0.17.0/) |
| tomli | \[&quot;2.4.1&quot;\] | \[&quot;2.5.0&quot;\] | [2.5.0](https://pypi.org/project/tomli/2.5.0/) |
| uv | \[&quot;0.12.23&quot;\] | \[&quot;0.13.0&quot;\] | [0.13.0](https://pypi.org/project/uv/0.13.0/) |

**Proposal base commit:** `675ba5a4b62c8826bafd47eca11312c00d0dafa7`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.

[Checks and publication result](https://github.com/pauljones0/actions-latest/actions/runs/38229178365)

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
