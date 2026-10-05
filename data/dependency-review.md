# Dependency maintenance review

**Validation: passed** — the workflow may publish these changes.

Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.

| Package | Before | After | Upstream details |
| --- | --- | --- | --- |
| cryptography | \[&quot;50.0.1&quot;\] | \[&quot;50.0.2&quot;\] | [50.0.2](https://pypi.org/project/cryptography/50.0.2/) |
| pyjwt | \[&quot;2.15.0&quot;\] | \[&quot;2.15.1&quot;\] | [2.15.1](https://pypi.org/project/pyjwt/2.15.1/) |
| python-dotenv | \[&quot;1.2.3&quot;\] | \[&quot;1.2.4&quot;\] | [1.2.4](https://pypi.org/project/python-dotenv/1.2.4/) |
| rpds-py | \[&quot;0.30.0&quot;, &quot;2026.6.3&quot;\] | \[&quot;0.30.0&quot;, &quot;2026.9.1&quot;\] | [0.30.0](https://pypi.org/project/rpds-py/0.30.0/) · [2026.9.1](https://pypi.org/project/rpds-py/2026.9.1/) |
| ruff | \[&quot;0.16.9&quot;\] | \[&quot;0.16.10&quot;\] | [0.16.10](https://pypi.org/project/ruff/0.16.10/) |
| sse-starlette | \[&quot;3.4.11&quot;\] | \[&quot;3.5.0&quot;\] | [3.5.0](https://pypi.org/project/sse-starlette/3.5.0/) |
| uv | \[&quot;0.12.19&quot;\] | \[&quot;0.12.23&quot;\] | [0.12.23](https://pypi.org/project/uv/0.12.23/) |

**Proposal base commit:** `4926fb354d8dd21478c016880737e24505e538c2`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.

[Checks and publication result](https://github.com/pauljones0/actions-latest/actions/runs/37288290338)

## Decision

No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.

If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.

For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).
