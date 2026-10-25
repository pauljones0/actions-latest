# Latest catalog changes

8 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/72d4d8bfabfca37ccde4a37f25826e62fa719041/) · [Current source](https://github.com/asklokesh/loki-mode/tree/c22c19b7b6ff7560cac4868fb29da77e771ae7fd/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/72d4d8bfabfca37ccde4a37f25826e62fa719041...c22c19b7b6ff7560cac4868fb29da77e771ae7fd)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 72d4d8bfabfca37ccde4a37f25826e62fa719041 | c22c19b7b6ff7560cac4868fb29da77e771ae7fd |
| Selected tag | v11.17.38 | v11.17.58 |

## cucuwang/geoptimize

[Previous source](https://github.com/cucuwang/geoptimize/tree/9b12be12a912243728667b5447391dd1a20cb69d/) · [Current source](https://github.com/cucuwang/geoptimize/tree/3a567d9d3fd94177bd668dfa0ced334fc3d40d33/) · [Upstream code diff](https://github.com/cucuwang/geoptimize/compare/9b12be12a912243728667b5447391dd1a20cb69d...3a567d9d3fd94177bd668dfa0ced334fc3d40d33)

| Changed | Before | After |
| --- | --- | --- |
| Description | Run the deterministic geoptimize readiness lint against a build directory | Lint content quality in CI for documentation and static-site builds, with optional regression blocking |
| Input: package-spec | {&quot;default&quot;: &quot;geoptimize@0.11.0&quot;, &quot;description&quot;: &quot;npm package spec to install; keep the default outside prerelease testing&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;geoptimize@0.12.0&quot;, &quot;description&quot;: &quot;npm package spec to install; keep the default outside prerelease testing&quot;, &quot;required&quot;: false} |
| Selected SHA | 9b12be12a912243728667b5447391dd1a20cb69d | 3a567d9d3fd94177bd668dfa0ced334fc3d40d33 |
| Selected tag | v0.11.0 | v0.12.0 |

## egor-tensin/setup-gcc

[Previous source](https://github.com/egor-tensin/setup-gcc/tree/eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08/) · [Current source](https://github.com/egor-tensin/setup-gcc/tree/e06c44b6df51fa631dbc917dfb0ebcc5cec0aa5b/) · [Upstream code diff](https://github.com/egor-tensin/setup-gcc/compare/eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08...e06c44b6df51fa631dbc917dfb0ebcc5cec0aa5b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08 | e06c44b6df51fa631dbc917dfb0ebcc5cec0aa5b |
| Selected tag | v2.0.2 | v2.0.3 |

## julia-actions/setup-julia

[Previous source](https://github.com/julia-actions/setup-julia/tree/fa02766e078afaaf09b14210362cee14137e6a32/) · [Current source](https://github.com/julia-actions/setup-julia/tree/da908477b5db94c10ffce8cfea9f2b3b9d5db687/) · [Upstream code diff](https://github.com/julia-actions/setup-julia/compare/fa02766e078afaaf09b14210362cee14137e6a32...da908477b5db94c10ffce8cfea9f2b3b9d5db687)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | fa02766e078afaaf09b14210362cee14137e6a32 | da908477b5db94c10ffce8cfea9f2b3b9d5db687 |
| Selected tag | v3.0.2 | v3.0.3 |

## kerlenton/mcpsnoop

[Previous source](https://github.com/kerlenton/mcpsnoop/tree/a82bd3858e8ac6df324ea0cba9b7532d27be1390/) · [Current source](https://github.com/kerlenton/mcpsnoop/tree/3ceaf6fc26807f72978ca0e1ef80653938688dd4/) · [Upstream code diff](https://github.com/kerlenton/mcpsnoop/compare/a82bd3858e8ac6df324ea0cba9b7532d27be1390...3ceaf6fc26807f72978ca0e1ef80653938688dd4)

| Changed | Before | After |
| --- | --- | --- |
| Input: replay | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to a recorded capture, relative to the repository root, to replay\\nagainst server instead of checking a capture you made yourself. The\\naction drives the server with the recorded client&#x27;s side of the session,\\nchecks the capture that produces, and also fails when the server got\\nworse than in the recording: a tool removed or changed, a call that\\nfailed or went unanswered, a call that got notably slower.\\n&quot;} |
| Input: replay-args | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Any other mcpsnoop replay flags, for example: --read-only --wait 30s\\n--out is not accepted: the action decides where the replayed capture goes.\\n&quot;} |
| Input: server | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;The command that starts the server under test, quoted the way it would\\nbe on a command line, for example: node dist/index.js\\nRequired with replay for a stdio server. With target it starts an HTTP\\nserver first, and can be left out when one is already running.\\n&quot;} |
| Input: session | {&quot;description&quot;: &quot;Path to the .jsonl capture to check, relative to the repository root.\\nRecord one by wrapping your server with mcpsnoop in an earlier step.\\n&quot;, &quot;required&quot;: true} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to the .jsonl capture to check, or to a directory of them, relative\\nto the repository root. Record one by wrapping your server with mcpsnoop\\nin an earlier step. Give this or replay, not both.\\n&quot;} |
| Input: target | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;The URL of a Streamable HTTP server to replay against, for example\\nhttp://localhost:3000/mcp. A credential goes in replay-args as\\n--header \\&quot;Authorization: Bearer ...\\&quot;, which the step log shows hidden.\\n&quot;} |
| Input: version | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Which mcpsnoop to install, for example v0.27.0. Defaults to the release you\\npinned the action to, so normally there is nothing to set. Needed only when\\npinning a branch or a commit, which names no release.\\n&quot;} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Which mcpsnoop to install, for example v0.28.0. Defaults to the release you\\npinned the action to, so normally there is nothing to set. Needed only when\\npinning a branch or a commit, which names no release.\\n&quot;} |
| Outputs | \[&quot;exit-code&quot;, &quot;outcome&quot;, &quot;sarif&quot;\] | \[&quot;capture&quot;, &quot;exit-code&quot;, &quot;outcome&quot;, &quot;sarif&quot;\] |
| Selected SHA | a82bd3858e8ac6df324ea0cba9b7532d27be1390 | 3ceaf6fc26807f72978ca0e1ef80653938688dd4 |
| Selected tag | v0.27.0 | v0.28.0 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/b23c8aaafd4d372c24ccfabb67e412c709a522ad/) · [Current source](https://github.com/tmatens/compose-lint/tree/02651c8ce343efb293e9735695126dc47071b50f/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/b23c8aaafd4d372c24ccfabb67e412c709a522ad...02651c8ce343efb293e9735695126dc47071b50f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b23c8aaafd4d372c24ccfabb67e412c709a522ad | 02651c8ce343efb293e9735695126dc47071b50f |
| Selected tag | v0.36.0 | v0.36.1 |

## upptime/uptime-monitor

[Previous source](https://github.com/upptime/uptime-monitor/tree/a284d6064bcbf89db3f1e2a6c533d0e69111573b/) · [Current source](https://github.com/upptime/uptime-monitor/tree/c34c41a9fc6fc6852ca94c66ae83f54dbe7063ae/) · [Upstream code diff](https://github.com/upptime/uptime-monitor/compare/a284d6064bcbf89db3f1e2a6c533d0e69111573b...c34c41a9fc6fc6852ca94c66ae83f54dbe7063ae)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a284d6064bcbf89db3f1e2a6c533d0e69111573b | c34c41a9fc6fc6852ca94c66ae83f54dbe7063ae |
| Selected tag | v1.46.0 | v1.46.1 |

## Added: yu-iskw/action-sqlfluff

[Source](https://github.com/yu-iskw/action-sqlfluff) — 🐶 Run sqlfluff with reviewdog on pull requests to improve code review experience.

New entries still require observed stability and fresh scan evidence before usage.
