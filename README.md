# actions-latest

Keeping track of the latest versions of various GitHub Actions

https://simonw.github.io/actions-latest/versions.txt

Access that URL for a list of all of the official Actions belonging to the [GitHub Actions](https://github.com/actions) organization along with their latest version tags.

You can point coding agents such as Claude Code and Codex CLI at this URL so they know the most recent Actions versions to use in their workflow files.

## MCP server

This fork can also run as a stdio MCP server for coding agents:

```json
{
  "mcpServers": {
    "actions-latest": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/pauljones0/actions-latest.git@codex/actions-latest-mcp",
        "actions-latest-mcp"
      ]
    }
  }
}
```

Available tools:

- `latest_github_actions_versions`: returns the full `versions.txt` content.
- `latest_github_action_version`: looks up one official action, such as `checkout` or `actions/checkout@v4`.
- `check_github_actions_workflow`: checks workflow YAML text for outdated official `actions/*` references.

Set `ACTIONS_LATEST_URL` to override the versions source, or set `ACTIONS_LATEST_OFFLINE=1` to use the packaged snapshot instead of fetching the live URL.

<!-- VERSIONS_START -->
## Latest versions

```
actions/actions-sync@v202601271539
actions/attest@v4
actions/cache@v5
actions/checkout@v6
actions/configure-pages@v6
actions/create-github-app-token@v3
actions/create-release@v1
actions/delete-package-versions@v5
actions/dependency-review-action@v3
actions/deploy-pages@v5
actions/download-artifact@v8
actions/first-interaction@v3
actions/github-script@v9
actions/go-dependency-submission@v2
actions/hello-world-docker-action@v2
actions/hello-world-javascript-action@v1
actions/javascript-action@v1
actions/jekyll-build-pages@v1
actions/labeler@v6
actions/publish-immutable-action@v0
actions/setup-dotnet@v5
actions/setup-elixir@v1
actions/setup-go@v6
actions/setup-haskell@v1
actions/setup-java@v5
actions/setup-node@v6
actions/setup-python@v6
actions/setup-ruby@v1
actions/stale@v10
actions/upload-artifact@v7
actions/upload-code-coverage@v1
actions/upload-pages-artifact@v5
actions/upload-release-asset@v1
```
<!-- VERSIONS_END -->
