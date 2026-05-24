# GitHub Actions Navigator (MCP)

A high-fidelity, Unix-style discovery engine for GitHub Actions. Designed for AI agents to find, understand, and version-lock the best actions with zero fuss.

### Radical Simplicity
This repository does one thing: it maintains a **ranked, fresh, and audited index** of the GitHub Actions universe.

### Installation

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

### Discovery Engine (`run`)
Follows the Unix philosophy of progressive disclosure via a single tool.

- `run browse`: List action categories (Security, Setup, CD, etc.).
- `run ls <owner>`: Explore actions by organization.
- `run grep <query>`: Search by intent (e.g., "setup rust with caching").
- `run find --tag <T>`: Filter by high-signal tags (e.g., #aws, #node).
- `run cat <action>`: Get a summary, popularity (stars), and usage snippet.
- `run man <action>`: Read the live `action.yml` manifest for full API details.

### Set and Forget (Auto-Pilot)
The index is self-healing and self-maintaining via a daily GitHub Workflow:
*   **Auto-Update**: Every action is checked for new `vN` version tags.
*   **Auto-Rank**: Star counts are refreshed to prioritize authoritative tools.
*   **Auto-Prune**: Stale actions (no push in >1 year) are automatically purged.
*   **Audit-Driven**: Redundant or low-quality duplicates are filtered out.

### Architecture
- **Single Source of Truth**: `actions-metadata.json`.
- **Unified Engine**: `update.py` handles the entire lifecycle (Fetch -> Enrich -> Index).
- **Search Backend**: SQLite FTS5 for fast, BM25-ranked discovery.
