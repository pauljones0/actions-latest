# Contributing

## Development

Use Python 3.10 or newer and the uv version pinned in `tooling.json`:

```sh
uv sync --locked --group dev
uv run ruff check .
uv run ruff format --check .
uv run pytest -q
uv run python update.py --check
uv run python scripts/smoke_install.py
```

The test suite runs offline. It uses real SQLite databases, a real pinned zizmor binary, mocked HTTP boundaries for failure and rate-limit cases, controlled observation times, and a real MCP stdio client/server exchange. The installation smoke test needs package-index access: it builds a wheel, installs into a separate environment, and checks the bundled database and MCP server outside the source tree.

CI repeats the tests on Python 3.10, 3.12, and 3.14. Run the same checks before proposing changes. Investigate a failing test or unexpected empty result before accepting it as expected behavior.

## Maintainer workflow

Use [MAINTENANCE.md](MAINTENANCE.md) as the starting point. `manage.py status` shows priorities; `manage.py review <action>` produces a source-linked review packet; `manage.py changes --base <commit>` makes snapshot changes readable. The `reviewed` command records completed human review only and requires an exact selected SHA.

## Catalog edits

`catalog.json` is the curated input. Use a unique action name, a concrete description, one category, and specific tags. Subdirectory actions use the complete path, such as `owner/repo/setup`. Human guidance about authentication, permissions, side effects, and matching intent is editorial; do not represent it as scanner output.

Rebuild the snapshot after catalog edits. Offline rebuilds preserve observations for retained actions and initialize newly added actions without a selected revision. Network updates begin observing their tags; the first eligible revision requires observations at least seven days apart. Remove an entry only by an intentional catalog edit, never as an outage response.

Do not hand-edit `actions_latest/actions.db`. `update.py --rebuild` also exports the matching versioned feed and health report. `update.py --check` rejects mismatched inputs, database, and feed.

## Code changes

Keep HTTP and subprocess calls at the adapter boundaries. Version selection accepts explicit timestamps; tests should advance those timestamps instead of sleeping. Preserve old state on recoverable external errors, but let programming errors fail publication. Any new security state needs tests covering how it appears in search, summaries, audits, and usage generation.

Update the SQLite schema version if an incompatible format changes. Update the package version in `pyproject.toml` and `actions_latest/__init__.py` together. The database shipped in the wheel must match the current reader.

## Dependency updates

`uv.lock` fixes development and CI dependencies. Package consumers use the supported ranges in `pyproject.toml`; therefore the fresh installation smoke test is required after dependency changes. MCP is constrained to `<2` until a deliberate migration is implemented and tested.

Zizmor is pinned in the dev dependency group and `models.SCANNER_VERSION`. Update both together and exercise the real scanner fixtures before accepting a new version. The adapter selects `json-v1`, rejects unknown severity values, and treats execution/collection/parse failures as errors. Changing the classification policy also requires incrementing `POLICY_VERSION`, which forces a rescan. Evidence from an older/incompatible scanner or a different policy version is stale until rescanned; known blocks remain enforced.

## Publishing and automation

The update job writes the database, feed, discovery registry/provenance report, and health report. Git's normal fast-forward push protects concurrent changes. Do not add `-X theirs`, force pushes, or binary merge drivers to resolve conflicts. Rerun on the latest catalog instead.

Weekly maintenance tests compatible Python/tool updates before a normal push to main using the scoped workflow token. The uv bootstrap reads `tooling.json`. Dependabot proposes workflow-action pin updates as tested PRs for review; maintenance never needs a personal token to edit workflow files. The independent monitor can recover missed updates, but credential failures require maintainer repair. See [operations](docs/operations.md).
