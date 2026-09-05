# Deployment verification — 2026-09-05

The overhaul and automatic freshness implementation were merged through [PR #3](https://github.com/pauljones0/actions-latest/pull/3), followed by verified production fixes for queued checkouts and scoped maintenance credentials.

- [PR CI](https://github.com/pauljones0/actions-latest/actions/runs/33989538089) and [current implementation CI](https://github.com/pauljones0/actions-latest/actions/runs/33989840555): 84 tests on Python 3.10, 3.12, and 3.14, Ruff, snapshot/feed validation, fresh wheel MCP installation; current CI also scans workflows.
- [Production daily updater](https://github.com/pauljones0/actions-latest/actions/runs/33989610593): successful refresh and normal push; all 547 records checked, no update errors, 65 blocked revisions, five explicit upstream manifest errors. The initial live discovery admitted six actions. New tag observations retain the seven-day gate.
- [Independent health monitor](https://github.com/pauljones0/actions-latest/actions/runs/33989710615): passed publication-age and actual observation/scan-coverage checks.
- [Production maintenance](https://github.com/pauljones0/actions-latest/actions/runs/33989840572): resolved compatible updates, passed all three Python versions and fresh installation, pushed lockfile commit `bebfc95` using the workflow token, and explicitly dispatched [the next refresh](https://github.com/pauljones0/actions-latest/actions/runs/33989886364).
- A separately installed wheel outside the source tree fetched the public feed through the running MCP server, switched to `source: cache`, and reported `schema_version: 2`, a successful refresh, no error, and no stale-publication warning. Reproduce after deployment with `uv run python scripts/smoke_install.py --online-refresh`. Ordinary CI uses the offline smoke mode.

The five remaining scan errors were checked against immutable upstream trees: `actions/actions-sync` contains no action manifest; `asdf-vm/actions`, `bitwarden/gh-actions`, and `bytecodealliance/actions` expose subdirectory manifests instead of a root action; `ansible/ansible-content-actions` has a root composite manifest without steps. These are retained as explicit errors; none are converted to clean evidence or silently removed.

## Dependabot activation verified

The user enabled version updates for this fork. [Dependabot's first check](https://github.com/pauljones0/actions-latest/actions/runs/33989963205) succeeded and opened [PR #4](https://github.com/pauljones0/actions-latest/pull/4) for checkout 7.0.1 and setup-python 7.0.0. [Its CI](https://github.com/pauljones0/actions-latest/actions/runs/33989990311) passed all three Python versions, installation, and workflow security checks. The changes were reviewed against the release notes and immutable tag commits and merged. Weekly workflow-pin proposals are active; future proposals require review, while supported Python/tool maintenance publishes automatically after validation.
