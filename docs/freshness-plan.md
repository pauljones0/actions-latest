# Automatic freshness implementation plan

This tracks the active follow-up goal. Completion requires publication and real workflow/runtime verification, not just local tests.

- [x] Checkpoint the previous overhaul and integrate latest remote generated data without losing catalog membership or blocking evidence.
- [x] Publish a versioned, compressed, validated snapshot feed.
- [x] Refresh installed clients in the background, with a compatible-schema cache, integrity validation, offline fallback, rollback protection, bounded downloads, and visible refresh status.
- [x] Refresh manifest-backed descriptions and operational facts; preserve explicit curated overrides and label outdated/unreviewed editorial claims instead of inventing guidance.
- [x] Discover qualifying maintained action repositories automatically; validate manifests, apply scanning and observation gates, retain curated overrides and explicit exclusions, and publish admission/rejection provenance.
- [x] Automate supported dependency/tool/scanner/workflow-pin upgrades, with coordinated scanner-version updates and full validation before publication or review proposals.
- [x] Produce freshness/coverage metrics and run an independent scheduled health check with bounded recovery dispatch.
- [x] Update operations documentation and test every new success/failure path.
- [ ] Publish changes, run CI and maintenance workflows, inspect actual results, and verify an installed client updates from the published feed.

Design constraints: no untrusted action code execution; no fabricated release ages or editorial claims; preserve SHA-pinned recommendations; never turn failed scans into clean results; prevent generated snapshots from overwriting concurrent human edits; do not silently auto-upgrade incompatible executable client code.
