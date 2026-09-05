# Review resolution and verification

The overhaul addresses the original review through these implementation boundaries and regression checks. See `CONTRIBUTING.md` for the commands that run them.

| Requirement | Implementation | Evidence |
| --- | --- | --- |
| Fresh installations and MCP startup | Compatible SDK range; packaged SQLite; thin transport adapter | Fresh wheel/console-entry-point smoke test outside the checkout; real stdio protocol test |
| Functional search without swallowed errors | Qualified SQL projection, literal FTS terms, read-only connections | Real FTS queries, punctuation, exact tags, blocked filtering, missing/corrupt database errors |
| Discovery of newer releases | Enumerate tags on every successful refresh | Unchanged old tag plus newer release test; selection after the observation interval |
| Observed tag stability | SHA mappings with first/last observations | Moved/reappearing tags, clock rollback, prerelease exclusion, no silent downgrade |
| Reliable security states | Shared versioned scanner adapter; SHA-bound evidence; independent attempt errors | Real clean/vulnerable manifests; invalid YAML; exit/JSON/timeout failures; stale/unknown and scanner-policy changes |
| SHA-pinned consumption | Snippets require eligible evidence; manifests/audits request stored SHA | Snippet eligibility test; piped cat/audit identity checks; manifest request assertions |
| Correct operational metadata | Parse runtime, inputs, outputs at selected SHA | Manifest extraction and revision-change tests; live checks on checkout and setup-node |
| Outage recovery without catalog loss | Curated membership separate from generated state | Complete updater tests for missing resources, outages, rate limits, recovery, and catalog additions |
| Safe snapshot publication | Validate staged SQLite, projections, tags, FTS, and content digests; atomic replacement | Byte-equivalent rebuild; failed build retaining original bytes; catalog drift and offline reconciliation tests |
| Concurrent edits survive automation | Update-only database writes; ordinary fast-forward Git push | Two-clone/bare-remote race test rejecting the outdated generated snapshot |
| Predictable command chains | Quote-aware parser; action identities separate from display text | Refine-before-limit, empty pipes, cat-to-audit, conditionals, sequences, quoted operators, invalid syntax |
| Maintainability and reproducibility | Explicit models/adapters; locked tooling; focused modules | Ruff, Python version matrix, workflow scan, architecture and contributor documentation |

## Intentional limits

- The initial migrated dataset retains historical pins but cannot retrospectively prove seven days of observations. Usage stays withheld until real updates satisfy the gate. Historical blocks are preserved; old clean claims are not assumed valid.
- Zizmor checks manifests offline. It does not establish the safety of referenced implementation code or dependencies.
- GitHub rate limits can leave a snapshot partially refreshed. Errors remain visible and previous evidence is retained; subsequent runs prioritize older checks.
- Consumers receive the snapshot packaged at installation. Refreshing the installed tool is required to receive later generated snapshots.
- Repository changes, tests, and workflow definitions are local until a maintainer publishes them. Remote CI execution and branch-protection settings require that separate publication/configuration step.
