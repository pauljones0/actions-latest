# Easier maintenance: verification

Implemented through [PR #5](https://github.com/pauljones0/actions-latest/pull/5), with follow-up improvements verified against a real shared API quota failure.

## Code and review checks

[Final code CI](https://github.com/pauljones0/actions-latest/actions/runs/33992079119) passed all 101 tests on Python 3.10, 3.12, and 3.14. CI also checks formatting, snapshot/feed consistency, a fresh wheel/MCP installation, and workflow security.

The new tests exercise semantic changes without timestamp/popularity churn, added and removed inputs, safe rendering of upstream text, review prioritization, SHA-guarded acknowledgements, preserved security state, explicitly pending unobserved entries, all platform-specific resolved dependency versions, tool holds, bounded summaries, dependency-free failure instructions, failed pipeline propagation, and grouping/recovery of shared service failures without hiding independent manifest errors. The documented uv dependency constraint was also verified against the actual resolver, and the prepared maintenance patch was checked against Git.

## Production evidence

- [Maintenance](https://github.com/pauljones0/actions-latest/actions/runs/33991213956) passed, published the dependency review, and automatically dispatched a refresh. Its report records the actual checkout base commit `ed014b9c4e279aabe30b00305dddedf06e546fa9`, validation state, and the run containing the publication result.
- [Health](https://github.com/pauljones0/actions-latest/actions/runs/33991215046) passed through the new `manage.py health` entry point and generated the maintainer overview.
- [Catalog refresh](https://github.com/pauljones0/actions-latest/actions/runs/33991242539) exercised the new published reports. Repeated verification runs then reached the shared GitHub API quota, revealing that hundreds of related errors needed one recovery item rather than hundreds of source reviews. That behavior was corrected and tested.
- The follow-up reports distinguish overall freshness checks, stored-observation age, and last-refresh success. They group API quota/access/transport failures while keeping malformed manifests and invalidated editorial reviews actionable. Meaningful change reports also group service-error transitions.
- [Recovery refresh](https://github.com/pauljones0/actions-latest/actions/runs/33992155740) succeeded after the authoritative reset time, followed by a [successful independent health check](https://github.com/pauljones0/actions-latest/actions/runs/33992237629). All 549 repository observations succeeded; update errors and stale observations returned to zero. The readable change report represents 549 recovered request errors as one shared-service transition, while the five previously verified upstream manifest issues remain explicit.
- A live limited API response was checked using the new HTTP adapter. Its authoritative reset header was preserved as `2026-09-05T21:08:15+00:00`, including subsequent requests skipped by the same client. This is the timestamp future recovery reports display when GitHub provides it.

Routine maintenance succeeded in production, so its failed-proposal artifact step was correctly skipped. Candidate patch generation and consistency were verified locally; the artifact is configured to upload only after preparation succeeded, avoiding accidentally presenting a previous run's report as the failed candidate. Resolver/bootstrap failures before that point remain explicit in the first failed step.

Use [MAINTENANCE.md](../MAINTENANCE.md) for the operational interface. Historical reports remain accessible through Git history and immutable links from job summaries. Human review remains necessary for workflow executable changes and editorial claims; the system supplies the evidence and next action instead of fabricating that judgment.
