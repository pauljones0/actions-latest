# GitHub Actions Navigator

An MCP server for discovering curated GitHub Actions and inspecting their pinned revisions. Search runs locally against a bundled SQLite snapshot. A scheduled updater observes version tags and scans action manifests.

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

CI tests Python 3.10, 3.12, and 3.14. The package supports MCP SDK 1.x; the dependency constraint prevents incompatible SDK 2.x installations. Installing from Git uses the catalog snapshot at the fetched commit. An installed server does not download newer snapshots automatically: reinstall or refresh the tool installation to get repository updates.

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
| `help` | Commands and examples |

```text
run "grep setup | grep node | cat"
run "find --tag docker | cat | audit"
run "help && ls"
```

Search returns up to ten candidates and excludes known blocked revisions. Candidates may still be unverified, unscanned, or stale; inspect them with `cat`. Search treats punctuation as word separators and combines words with AND. A pipe refines the full preceding search before applying the result limit. Pipes preserve action identities through formatted summaries. `&&` continues on success; `;` continues regardless. Operators work without surrounding spaces and are literal inside quotes. This is not a system shell.

`man` and `audit` require network access. `audit` additionally requires **zizmor 1.30.0** on PATH. For a tool installation, add `"--with", "zizmor==1.30.0"` to the `uvx` arguments before the command. `GITHUB_TOKEN` is optional for public manifests and useful for higher API limits; configure it through your client's secret/environment settings.

## What a recommendation means

A usage snippet is emitted only when the selected tag-to-SHA mapping has been observed unchanged at least seven days apart, its manifest was parsed at that SHA, and its scan succeeded within the last fourteen days without high-severity findings. The snippet uses the **full commit SHA**, with the version tag as a comment. Warning findings remain visible.

Unknown, failed, stale, and blocked scans have separate statuses. A failed rescan preserves existing blocking findings. Changing the selected SHA invalidates prior manifest and scan evidence. Manifest checks do **not** audit the action's JavaScript, scripts, Docker image, transitive dependencies, or behavior at runtime. See [the security model](docs/architecture.md#security-policy) for the exact scope.

The initial migrated snapshot retains the original 541 catalog entries and their historical pins. Historical blocking findings are preserved conservatively; old clean claims and runtime/output fields without verifiable provenance are discarded. Imported pins are marked `unverified` until the new observation gate completes. They are inspectable, but do not produce vetted usage snippets during that interval.

## Maintain the catalog

Edit **`catalog.json`** to add or remove actions or improve editorial descriptions, categories, tags, and usage guidance. Action identifiers support `owner/repo` and `owner/repo/subdirectory`. Runtime, inputs, outputs, popularity, observations, and scans are generated state in **`actions_latest/actions.db`**. The updater never edits the catalog or removes an entry because an API request failed or a repository became inactive.

```sh
uv run python update.py             # Fetch observations and scan selected manifests
uv run python update.py --check     # Validate the bundled snapshot
uv run python update.py --rebuild   # Rebuild locally without network calls
uv run pytest -q
```

The daily workflow uses bounded concurrency and prioritizes entries with the oldest successful check. Rate limits can produce partial refreshes; the summary reports update and scan errors, and affected entries retain their prior evidence. A rejected Git push fails the job: rerun from current `main` to incorporate concurrent edits. The workflow never force-pushes or merges generated snapshots.

See [CONTRIBUTING.md](CONTRIBUTING.md) for development and verification, and [the architecture](docs/architecture.md) for data flow and failure handling.
