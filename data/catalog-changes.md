# Latest catalog changes

6 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## dtolnay/rust-toolchain

[Previous source](https://github.com/dtolnay/rust-toolchain/tree/6c977a6ca4077a0ceb28ffbe03f59d46e9ac8772/) · [Current source](https://github.com/dtolnay/rust-toolchain/tree/02cb101ec7c40f2c49e1d9714d64511d8e1b74de/) · [Upstream code diff](https://github.com/dtolnay/rust-toolchain/compare/6c977a6ca4077a0ceb28ffbe03f59d46e9ac8772...02cb101ec7c40f2c49e1d9714d64511d8e1b74de)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6c977a6ca4077a0ceb28ffbe03f59d46e9ac8772 | 02cb101ec7c40f2c49e1d9714d64511d8e1b74de |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/e354ba26ce66bb317aa30ec13e4bdff962373474/) · [Current source](https://github.com/pullfrog/pullfrog/tree/ce127b38d7f0c6c5e2c40ccd290adc4c5652357f/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/e354ba26ce66bb317aa30ec13e4bdff962373474...ce127b38d7f0c6c5e2c40ccd290adc4c5652357f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e354ba26ce66bb317aa30ec13e4bdff962373474 | ce127b38d7f0c6c5e2c40ccd290adc4c5652357f |
| Selected tag | v0.1.81 | v0.1.82 |

## Added: pypa/cibuildwheel

[Source](https://github.com/pypa/cibuildwheel) — Installs and runs cibuildwheel on the current runner

New entries still require observed stability and fresh scan evidence before usage.

## Added: rjstone/discord-webhook-notify

[Source](https://github.com/rjstone/discord-webhook-notify) — Send notifications to Discord using a webhook. Works with all execution environments including windows, macos, and linux. 

New entries still require observed stability and fresh scan evidence before usage.

## shaftoe/pi-coding-agent-action

[Previous source](https://github.com/shaftoe/pi-coding-agent-action) · [Current source](https://github.com/shaftoe/pi-coding-agent-action/tree/853a9af5ac64e79c79fa6bb3958314aa1acf7e92/)

| Changed | Before | After |
| --- | --- | --- |
| Input: auto\_compaction | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Enable automatic context compaction when the conversation grows too large for the model context window. When enabled, Pi will summarize older messages to free up context space, allowing longer sessions without hitting context limits.&quot;, &quot;required&quot;: false} |
| Input: base\_url | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional override for the provider base URL (e.g. to route OpenAI traffic through a proxy or use an OpenAI-compatible gateway).&quot;, &quot;required&quot;: false} |
| Input: branch\_name\_template | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Template for auto-generated branch names in create\_pull\_request. Supports variables: {number} (issue/PR number), {timestamp} (epoch ms), {title} (slugified PR title). Default: \\&quot;pi/issue{number}-{timestamp}\\&quot;&quot;, &quot;required&quot;: false} |
| Input: diff\_ignore\_patterns | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Space-separated list of file patterns to exclude from PR diffs by default (e.g. \\&quot;dist/ package-lock.json\\&quot;). The agent can still provide additional patterns at call time.&quot;, &quot;required&quot;: false} |
| Input: diff\_max\_bytes | null | {&quot;default&quot;: &quot;102400&quot;, &quot;description&quot;: &quot;Maximum diff size in bytes returned by the get\_pr\_diff tool. Defaults to 100KB.&quot;, &quot;required&quot;: false} |
| Input: diff\_max\_lines | null | {&quot;default&quot;: &quot;1000&quot;, &quot;description&quot;: &quot;Maximum number of diff lines returned by the get\_pr\_diff tool. Defaults to 1000.&quot;, &quot;required&quot;: false} |
| Input: export\_session\_html | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Export the Pi session as a self-contained HTML file and expose its path via the \`session\_html\_path\` output. Set to false to disable. Auto-enabled when share\_session is true.&quot;, &quot;required&quot;: false} |
| Input: export\_session\_jsonl | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Export the Pi session as a JSONL file (one JSON object per line) and expose its path via the \`session\_jsonl\_path\` output. Set to true to enable.&quot;, &quot;required&quot;: false} |
| Input: extensions | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Custom Pi extensions to load (one per line). Supports npm packages (npm:package-name), git repos (git:github.com/user/repo), or local file paths.&quot;, &quot;required&quot;: false} |
| Input: github\_token | null | {&quot;description&quot;: &quot;GitHub token for API access. The default \`GITHUB\_TOKEN\` works for all standard operations. To use \`share\_session\`, provide a classic PAT (\`gist\` scope), fine-grained PAT (Account → Gists: read/write), or GitHub App token instead — the default \`GITHUB\_TOKEN\` cannot create gists.&quot;, &quot;required&quot;: true} |
| Input: load\_builtin\_extensions | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether to load built-in GitHub extensions (see Custom Tools section in README for the full list)&quot;, &quot;required&quot;: false} |
| Input: loaded\_tools | null | {&quot;default&quot;: &quot;all&quot;, &quot;description&quot;: &quot;Controls which tools are loaded into the session. Defaults to &#x27;all&#x27; which loads all available tools (built-in + custom). Accepts a list of tool names (one per line) to load only those tools. Tool names must match exactly — unknown names cause the run to fail early.&quot;, &quot;required&quot;: false} |
| Input: model | null | {&quot;description&quot;: &quot;Model to use (e.g., gpt-5.4, gpt-4o, gemini-2.5-pro)&quot;, &quot;required&quot;: true} |
| Input: platform | null | {&quot;default&quot;: &quot;github&quot;, &quot;description&quot;: &quot;Git hosting platform the action is running on. One of github (default), codeberg, forgejo, or gitea (alias for forgejo). Determines platform-specific behaviour such as the action-run URL format used in the \\&quot;View action run\\&quot; footer. The platform is no longer auto-detected from the server URL, so set this explicitly when running on Forgejo/Codeberg/Gitea (e.g. platform: forgejo).&quot;, &quot;required&quot;: false} |
| Input: pr\_number | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Pull request number to target. Use this with workflow\_dispatch to run the agent on a specific PR without a triggering event. When set, the action fetches PR context and posts the result as a comment on the specified PR.&quot;, &quot;required&quot;: false} |
| Input: prompt | null | {&quot;description&quot;: &quot;Optional prompt to send to the agent. When provided, the trigger phrase is not required and the prompt is used as-is (useful for non-interactive workflows such as PR reviews, assignment triggers, or scheduled tasks). Falls back to extracting the prompt from the triggering comment if not set.&quot;, &quot;required&quot;: false} |
| Input: provider | null | {&quot;description&quot;: &quot;LLM provider (e.g. openai, google, anthropic, zai, etc.)&quot;, &quot;required&quot;: true} |
| Input: server\_url | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Override the forge server URL (e.g. https://git.example.com). Self-hosted runners (Forgejo/Gitea behind Docker or internal networking) may advertise a GITHUB\_SERVER\_URL that is only reachable from inside the host network (e.g. http://localhost:3000); set this to the externally-reachable URL so that derived links (commits, PRs, action runs) point at the right host. When unset, the runner-advertised GITHUB\_SERVER\_URL is used. Note: this only affects user-facing URLs — the API client keeps using the runner-advertised GITHUB\_API\_URL, and platform selection is controlled by the platform input.&quot;, &quot;required&quot;: false} |
| Input: share\_gist\_api\_url | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;API URL for the share gist provider. Required when share\_gist\_provider is \`opengist\`: the instance&#x27;s create endpoint, e.g. \`https://gist.l3x.in/api/gists\` (Opengist&#x27;s REST API lives under /api/, not /api/v1/). Optional override for the github provider (defaults to https://api.github.com/gists).&quot;, &quot;required&quot;: false} |
| Input: share\_gist\_expiration | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Time-to-live for shared gists (opengist provider only; GitHub Gists have no expiry). One of \`1hour\`, \`12hours\`, \`1day\`, \`7days\`, \`15days\`, or \`never\`. Defaults to \`7days\` — shared sessions are ephemeral CI artifacts. Set to \`never\` to keep them indefinitely.&quot;, &quot;required&quot;: false} |
| Input: share\_gist\_provider | null | {&quot;default&quot;: &quot;github&quot;, &quot;description&quot;: &quot;Storage backend for session sharing. Defaults to \`github\` (GitHub Gists + pi.dev viewer). Set to \`opengist\` to upload to a self-hosted Opengist instance instead — in that case also set share\_gist\_api\_url (and a share\_gist\_token or github\_token with gist:write access). When opengist is used, share\_url points at a self-rendering raw-HTML link (the pi.dev viewer cannot read non-GitHub gists).&quot;, &quot;required&quot;: false} |
| Input: share\_gist\_token | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Token used to create the shared gist. For opengist, an Opengist access token (og\_…) with the gist:write scope — this is required (there is no github\_token fallback, since a GitHub token cannot authenticate against a self-hosted Opengist instance). For the github provider, falls back to github\_token when unset, so it keeps working with a single token.&quot;, &quot;required&quot;: false} |
| Input: share\_session | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Share the session like pi&#x27;s /share command: upload the exported session HTML to a secret GitHub Gist and surface a pi.dev-style viewer link. Uses the github\_token input to create the gist, so provide a PAT/App token with gist scope there (the default GITHUB\_TOKEN cannot create gists). Auto-enables export\_session\_html.&quot;, &quot;required&quot;: false} |
| Input: thinking\_level | null | {&quot;default&quot;: &quot;off&quot;, &quot;description&quot;: &quot;Thinking level (e.g. off, low, medium, high, etc.)&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;description&quot;: &quot;API token for the LLM provider. Required for most providers, but can be omitted when using providers that support alternative auth mechanisms (e.g. google-vertex with Application Default Credentials).&quot;, &quot;required&quot;: false} |
| Input: trigger | null | {&quot;default&quot;: &quot;/pi &quot;, &quot;description&quot;: &quot;Trigger phrase for the pi agent (e.g. /pi )&quot;, &quot;required&quot;: false} |
| Input: update\_comment | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to update/overwrite the bot&#x27;s previous comment on the issue/PR instead of creating a new one.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;cost&quot;, &quot;duration\_seconds&quot;, &quot;gist\_id&quot;, &quot;gist\_url&quot;, &quot;input\_tokens&quot;, &quot;output\_tokens&quot;, &quot;response&quot;, &quot;session\_html\_path&quot;, &quot;session\_jsonl\_path&quot;, &quot;share\_url&quot;, &quot;success&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 853a9af5ac64e79c79fa6bb3958314aa1acf7e92 |
| Selected tag | null | v2.28.1 |

## zgosalvez/github-actions-ensure-sha-pinned-actions

[Previous source](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/tree/60e3a74c7b74a319e8e53e46bc455205f7173e1a/) · [Current source](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/tree/62574f011e0d1967d555a862bd28a7abba8684fe/) · [Upstream code diff](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/compare/60e3a74c7b74a319e8e53e46bc455205f7173e1a...62574f011e0d1967d555a862bd28a7abba8684fe)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 60e3a74c7b74a319e8e53e46bc455205f7173e1a | 62574f011e0d1967d555a862bd28a7abba8684fe |
| Selected tag | v5.0.8 | v5.0.9 |
