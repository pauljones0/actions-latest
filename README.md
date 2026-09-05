# GitHub Actions Navigator

An MCP server for discovering curated and automatically discovered GitHub Actions and inspecting their pinned revisions. Search runs locally against a validated SQLite snapshot. Daily automation discovers candidates, observes version tags, scans manifests, and publishes a portable feed. Installed clients refresh their data in the background.

## Install

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then add this configuration to an MCP client:

```json
{
  "mcpServers": {
    "actions-latest": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/pauljones0/actions-latest.git",
        "actions-latest-mcp"
      ]
    }
  }
}
```

CI tests Python 3.10, 3.12, and 3.14. The package supports MCP SDK 1.x; the dependency constraint prevents incompatible SDK 2.x installations. Installing from Git includes a working snapshot. The server checks for compatible data updates at startup and during use, at most once every six hours, without blocking searches. Failed downloads retain the last working cache or bundled snapshot. Set `ACTIONS_LATEST_AUTO_REFRESH=0` for network-free local search. Application code upgrades still require refreshing the installation.

For a local checkout:

```sh
uv sync --locked --group dev
uv run actions-latest-mcp
```

## Use

The server exposes one tool, `run`, with a small command language:

| Command | Result |
| --- | --- |
| `browse` | Available categories |
| `ls actions` | Actions maintained by an owner |
| `grep setup rust caching` | Search descriptions, names, tags, and guidance |
| `find --tag node` | Exact tag matches |
| `cat actions/checkout` | Selected SHA, observation/scan status, and usage when eligible |
| `man actions/checkout` | Live manifest at the stored SHA |
| `audit actions/checkout` | On-demand scan of that same SHA |
| `status` | Snapshot source, last refresh, publication age warning, and errors |
| `help` | Commands and examples |

```text
run "grep setup | grep node | cat"
run "find --tag docker | cat | audit"
run "help && ls"
```

Search returns up to ten candidates and excludes known blocked revisions. Candidates may still be unverified, unscanned, or stale; inspect them with `cat`. Search treats punctuation as word separators and combines words with AND. A pipe refines the full preceding search before applying the result limit. Pipes preserve action identities through formatted summaries. `&&` continues on success; `;` continues regardless. Operators work without surrounding spaces and are literal inside quotes. This is not a system shell.

`man` and `audit` require network access. `audit` additionally requires the zizmor version pinned in `pyproject.toml` on PATH. For a tool installation, add `"--with", "zizmor==<pinned-version>"` to the `uvx` arguments before the command. `GITHUB_TOKEN` is optional for public manifests and useful for higher API limits; configure it through your client's secret/environment settings.

## What a recommendation means

A usage snippet is emitted only when the selected tag-to-SHA mapping has been observed unchanged at least seven days apart, its manifest was parsed at that SHA, and its scan succeeded within the last fourteen days without high-severity findings. The snippet uses the **full commit SHA**, with the version tag as a comment. Warning findings remain visible.

Unknown, failed, stale, and blocked scans have separate statuses. A failed rescan preserves existing blocking findings. Changing the selected SHA invalidates prior manifest and scan evidence. Manifest checks do **not** audit the action's JavaScript, scripts, Docker image, transitive dependencies, or behavior at runtime. See [the security model](docs/architecture.md#security-policy) for the exact scope.

The initial migrated snapshot retains the original 541 catalog entries and their historical pins. Historical blocking findings are preserved conservatively; old clean claims and runtime/output fields without verifiable provenance are discarded. Imported pins are marked `unverified` until the new observation gate completes. They are inspectable, but do not produce vetted usage snippets during that interval.

## Maintain the catalog

Start with **[MAINTENANCE.md](MAINTENANCE.md)** for the prioritized overview, readable changes, upgrade reviews, and recovery commands.

Edit **`catalog.json`** to add or remove actions or improve editorial descriptions, categories, tags, and usage guidance. Action identifiers support `owner/repo` and `owner/repo/subdirectory`. Manifest descriptions, runtime, inputs, outputs, popularity, observations, and scans are generated state in **`actions_latest/actions.db`**. The updater never edits the catalog or removes an entry because an API request failed or a repository became inactive.

```sh
uv run python update.py --discover  # Discover candidates, refresh observations, publish feed
uv run python update.py --check     # Validate the bundled snapshot
uv run python update.py --rebuild   # Rebuild locally without network calls
uv run pytest -q
```

The daily workflow uses bounded concurrency and prioritizes entries with the oldest successful check. Rate limits can produce partial refreshes; the summary reports update and scan errors, and affected entries retain their prior evidence. A rejected Git push fails the job: rerun from current `main` to incorporate concurrent edits. The workflow never force-pushes or merges generated snapshots.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development and verification, and [the architecture](docs/architecture.md) for data flow and failure handling.

## Automatic freshness

- **Daily, 04:51 UTC:** inspect at most 40 search results and admit at most 10 maintained, public, nonfork action repositories with at least 50 stars, a valid root manifest, numeric version tags, and no blocking manifest scan findings. `catalog-policy.json` controls these limits and exclusions. Discovery is bounded and topic based; it does not claim exhaustive Marketplace coverage.
- **Source facts:** descriptions, runtime, required inputs, and outputs come from the selected immutable manifest. Human recommendations remain explicit editorial claims, labelled unreviewed or needing review after the SHA changes. Automation never invents permissions or authentication advice. `data/health.json` includes the editorial review queue.
- **Weekly maintenance:** resolve compatible stable tool releases, and Python dependency locks; update the scanner contract together; run all three Python test versions, lint, real scanner checks, and a fresh wheel installation. Publish only after these pass, then dispatch the updater. Incompatible direct major upgrades require an intentional migration. Dependabot separately proposes workflow action SHA updates through PRs, which run the same CI and require review.
- **Every six hours:** an independent monitor checks publication age and successful observation/scan coverage. Stale or degraded coverage fails the job with a report and can dispatch one recovery update after six hours without an active/recent updater.
- **Installed clients:** download schema-specific compressed JSON over HTTPS, enforce size/schema/model/digest/rollback checks, build SQLite locally, and atomically cache it under `$XDG_CACHE_HOME/actions-latest/schema-2` (default `~/.cache`). A process lock coordinates multiple clients. `status` exposes failures; no network success is required to search.

The GitHub workflows and their job summaries are the operational monitoring surface. Repository Actions notifications follow your GitHub settings; this does not configure an external paging service. See [operations](docs/operations.md) for recovery and trust boundaries.
