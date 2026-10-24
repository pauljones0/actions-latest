# Latest catalog changes

14 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## Added: Akimiya-z/codex-guard

[Source](https://github.com/Akimiya-z/codex-guard) — Quality gate for AI-generated pull requests: blocks TODO leftovers, leaked secrets, sloppy commits and red CI.

New entries still require observed stability and fresh scan evidence before usage.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/374f254f5efaf968abfe15d399fd90972e8138b9/) · [Current source](https://github.com/anthropics/claude-code-action/tree/f27be6b65a4652f08a2ba3cff79114829b588967/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/374f254f5efaf968abfe15d399fd90972e8138b9...f27be6b65a4652f08a2ba3cff79114829b588967)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 374f254f5efaf968abfe15d399fd90972e8138b9 | f27be6b65a4652f08a2ba3cff79114829b588967 |
| Selected tag | v1.0.251 | v1.0.252 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/183e1289224ed627c6c28a4535875f940e9ecfe2/) · [Current source](https://github.com/asklokesh/loki-mode/tree/72d4d8bfabfca37ccde4a37f25826e62fa719041/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/183e1289224ed627c6c28a4535875f940e9ecfe2...72d4d8bfabfca37ccde4a37f25826e62fa719041)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 183e1289224ed627c6c28a4535875f940e9ecfe2 | 72d4d8bfabfca37ccde4a37f25826e62fa719041 |
| Selected tag | v11.15.0 | v11.17.38 |

## cycjimmy/semantic-release-action

[Previous source](https://github.com/cycjimmy/semantic-release-action/tree/9e1f8a3ef91f1097285028e799a5fb8bb90e8899/) · [Current source](https://github.com/cycjimmy/semantic-release-action/tree/03595b5eaf44910cf239ff20904cc52d410f97d4/) · [Upstream code diff](https://github.com/cycjimmy/semantic-release-action/compare/9e1f8a3ef91f1097285028e799a5fb8bb90e8899...03595b5eaf44910cf239ff20904cc52d410f97d4)

| Changed | Before | After |
| --- | --- | --- |
| Input: tag\_format | {&quot;description&quot;: &quot;The default tag format on semantic-release is v{version}. You can override that behavior using this option.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The default tag format on semantic-release is v${version}. You can override that behavior using this option.&quot;, &quot;required&quot;: false} |
| Selected SHA | 9e1f8a3ef91f1097285028e799a5fb8bb90e8899 | 03595b5eaf44910cf239ff20904cc52d410f97d4 |
| Selected tag | v8.1.0 | v8.1.2 |

## egor-tensin/setup-gcc

[Previous source](https://github.com/egor-tensin/setup-gcc/tree/a2861a8b8538f49cf2850980acccf6b05a1b2ae4/) · [Current source](https://github.com/egor-tensin/setup-gcc/tree/eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08/) · [Upstream code diff](https://github.com/egor-tensin/setup-gcc/compare/a2861a8b8538f49cf2850980acccf6b05a1b2ae4...eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\]\] | \[\] |
| Security | blocked | clean |
| Selected SHA | a2861a8b8538f49cf2850980acccf6b05a1b2ae4 | eb5588a28b96aaa4ca1c9aa8858f30b9e59b1a08 |
| Selected tag | v2.0 | v2.0.2 |

## egor-tensin/setup-wireguard

[Previous source](https://github.com/egor-tensin/setup-wireguard) · [Current source](https://github.com/egor-tensin/setup-wireguard/tree/0c34af0f8ab752230aa963e763d97f3bec8422ec/)

| Changed | Before | After |
| --- | --- | --- |
| Input: allowed\_ips | null | {&quot;description&quot;: &quot;Comma-separated list of netmasks&quot;, &quot;required&quot;: true} |
| Input: endpoint | null | {&quot;description&quot;: &quot;Endpoint in the HOST:PORT format&quot;, &quot;required&quot;: true} |
| Input: endpoint\_public\_key | null | {&quot;description&quot;: &quot;Public key of the endpoint&quot;, &quot;required&quot;: true} |
| Input: ips | null | {&quot;description&quot;: &quot;Comma-separated list of IP addresses&quot;, &quot;required&quot;: true} |
| Input: keepalive | null | {&quot;description&quot;: &quot;Useful for NAT traversal&quot;, &quot;required&quot;: false} |
| Input: preshared\_key | null | {&quot;description&quot;: &quot;Preshared key&quot;, &quot;required&quot;: false} |
| Input: private\_key | null | {&quot;description&quot;: &quot;Private key&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | composite |
| Security | unknown | clean |
| Selected SHA | null | 0c34af0f8ab752230aa963e763d97f3bec8422ec |
| Selected tag | null | v1.2.2 |

## jdx/mise-action

[Previous source](https://github.com/jdx/mise-action/tree/08ae2a091c038e1e05ec6f5115dc5c69d5a2a6b8/) · [Current source](https://github.com/jdx/mise-action/tree/9b200bcecbfd6303e69a4a261b2e09e3757440a7/) · [Upstream code diff](https://github.com/jdx/mise-action/compare/08ae2a091c038e1e05ec6f5115dc5c69d5a2a6b8...9b200bcecbfd6303e69a4a261b2e09e3757440a7)

| Changed | Before | After |
| --- | --- | --- |
| Input: cache\_key | {&quot;description&quot;: &quot;Override the complete cache key (ignores all other cache key options).\\nSupports template variables: {{version}}, {{cache\_key\_prefix}}, {{platform}}, {{file\_hash}},\\n{{mise\_env}}, {{install\_args\_hash}}, {{bootstrap\_hash}}, {{default}}, {{env.VAR\_NAME}} for environment variables,\\nand conditional logic like {{#if version}}...{{/if}}\\n&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Override the complete cache key (ignores all other cache key options).\\nSupports template variables: {{version}}, {{cache\_key\_prefix}}, {{platform}}, {{file\_hash}},\\n{{mise\_env}}, {{install\_args\_hash}}, {{bootstrap\_hash}}, {{cache\_period}}, {{default}}, {{env.VAR\_NAME}} for environment variables,\\nand conditional logic like {{#if version}}...{{/if}}\\n&quot;, &quot;required&quot;: false} |
| Input: cache\_max\_age\_days | null | {&quot;default&quot;: &quot;30&quot;, &quot;description&quot;: &quot;Rebuild the cache from scratch at least this often, so a frequently used cache still picks up the latest mise and tools. Adds a period number to the default cache key. Set 0 to disable.&quot;, &quot;required&quot;: false} |
| Input: cache\_restore\_retry\_budget | null | {&quot;default&quot;: &quot;0s&quot;, &quot;description&quot;: &quot;Total time to keep retrying a cache restore that GitHub throttles with HTTP 429, as a duration like \`60s\`. Each wait is at least the advertised Retry-After plus up to 2s of jitter and counts against the budget. \`0s\` disables retries. A cache miss is never retried.&quot;, &quot;required&quot;: false} |
| Input: cache\_save\_retry\_budget | null | {&quot;default&quot;: &quot;0s&quot;, &quot;description&quot;: &quot;Total time to keep retrying a cache save that GitHub throttles with HTTP 429, as a duration like \`60s\`. Each wait is at least the advertised Retry-After plus up to 2s of jitter and counts against the budget. \`0s\` disables retries. A reservation conflict (another job is saving the same key) is never retried.&quot;, &quot;required&quot;: false} |
| Input: fetch\_from\_github | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;If true (default), fetch the mise binary from GitHub. If false and using the latest version, fetch from mise.jdx.dev instead.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;If true (default), fetch the mise binary from GitHub, falling back to mise.jdx.dev when the latest version is requested and the GitHub download fails. If false and using the latest version, fetch from mise.jdx.dev first and fall back to GitHub. A pinned version is only ever fetched from GitHub. Downloads are verified against the signed checksums either way.&quot;, &quot;required&quot;: false} |
| Input: monorepo | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Automatically pass \`--monorepo\` to \`mise install\` when the mise configuration has \`monorepo.config\_roots\`. Set to false to opt out.&quot;, &quot;required&quot;: false} |
| Selected SHA | 08ae2a091c038e1e05ec6f5115dc5c69d5a2a6b8 | 9b200bcecbfd6303e69a4a261b2e09e3757440a7 |
| Selected tag | v5.1.2 | v5.2.0 |

## KengoTODA/actions-setup-docker-compose

[Previous source](https://github.com/KengoTODA/actions-setup-docker-compose/tree/3365b3ff2fc7b4e5ffa2d9ddbb3c2bd73727d443/) · [Current source](https://github.com/KengoTODA/actions-setup-docker-compose/tree/b09fb2b902df45b91982bc46858188f2a714ee5f/) · [Upstream code diff](https://github.com/KengoTODA/actions-setup-docker-compose/compare/3365b3ff2fc7b4e5ffa2d9ddbb3c2bd73727d443...b09fb2b902df45b91982bc46858188f2a714ee5f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3365b3ff2fc7b4e5ffa2d9ddbb3c2bd73727d443 | b09fb2b902df45b91982bc46858188f2a714ee5f |
| Selected tag | v1.2.10 | v1.2.11 |

## ls-lint/action

[Previous source](https://github.com/ls-lint/action/tree/02e380fe8733d499cbfc9e22276de5085508a5bd/) · [Current source](https://github.com/ls-lint/action/tree/a87c5eb4fb26d7af1bd0adba203dd1e76f7e94eb/) · [Upstream code diff](https://github.com/ls-lint/action/compare/02e380fe8733d499cbfc9e22276de5085508a5bd...a87c5eb4fb26d7af1bd0adba203dd1e76f7e94eb)

| Changed | Before | After |
| --- | --- | --- |
| Runtime | node20 | node24 |
| Selected SHA | 02e380fe8733d499cbfc9e22276de5085508a5bd | a87c5eb4fb26d7af1bd0adba203dd1e76f7e94eb |
| Selected tag | v2.3.1 | v2.3.2 |

## macalbert/envilder

[Previous source](https://github.com/macalbert/envilder/tree/5f7258aaeb6aff4c998e4361897037926f30abb8/) · [Current source](https://github.com/macalbert/envilder/tree/181ea06aed55af1dd5ba1d89007629bb1f5324cc/) · [Upstream code diff](https://github.com/macalbert/envilder/compare/5f7258aaeb6aff4c998e4361897037926f30abb8...181ea06aed55af1dd5ba1d89007629bb1f5324cc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5f7258aaeb6aff4c998e4361897037926f30abb8 | 181ea06aed55af1dd5ba1d89007629bb1f5324cc |
| Selected tag | v0.14.0 | v0.15.0 |

## Added: MishaKav/pytest-coverage-comment

[Source](https://github.com/MishaKav/pytest-coverage-comment) — GitHub Action that adds pytest coverage reports as comments to pull requests with badges, test statistics, and direct file links. Requires pull-requests: write permission.

New entries still require observed stability and fresh scan evidence before usage.

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/3cbf14efd750961dba35fccbf00f9e14028cb1f5/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/b76d06f8570118465db3190c9a08f1b29d341aa1/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/3cbf14efd750961dba35fccbf00f9e14028cb1f5...b76d06f8570118465db3190c9a08f1b29d341aa1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3cbf14efd750961dba35fccbf00f9e14028cb1f5 | b76d06f8570118465db3190c9a08f1b29d341aa1 |
| Selected tag | v1.80.2 | v1.80.3 |

## Songmu/tagpr

[Previous source](https://github.com/Songmu/tagpr/tree/0c4eb5a3b0862693702acea436a7c68bd586530d/) · [Current source](https://github.com/Songmu/tagpr/tree/1fcd7292d1fe8ea9a8313eef46b8d80b7a15d227/) · [Upstream code diff](https://github.com/Songmu/tagpr/compare/0c4eb5a3b0862693702acea436a7c68bd586530d...1fcd7292d1fe8ea9a8313eef46b8d80b7a15d227)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;v1.21.2&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v1.21.3&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} |
| Selected SHA | 0c4eb5a3b0862693702acea436a7c68bd586530d | 1fcd7292d1fe8ea9a8313eef46b8d80b7a15d227 |
| Selected tag | v1.21.2 | v1.21.3 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/1168f6810a3cb30a3514bf5756a3b7f0422c6df8/) · [Current source](https://github.com/taiki-e/install-action/tree/8cca0918f8471c33515202b73f56ab27f2bed283/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/1168f6810a3cb30a3514bf5756a3b7f0422c6df8...8cca0918f8471c33515202b73f56ab27f2bed283)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 1168f6810a3cb30a3514bf5756a3b7f0422c6df8 | 8cca0918f8471c33515202b73f56ab27f2bed283 |
| Selected tag | v2.87.28 | v2.87.29 |
