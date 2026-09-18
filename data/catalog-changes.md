# Latest catalog changes

13 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## affaan-m/agentshield

[Previous source](https://github.com/affaan-m/agentshield/tree/9bbc007cf5afb562c324bbad4ce6c544420f49f6/) · [Current source](https://github.com/affaan-m/agentshield/tree/b0891303bdcd6037376a94263d45cfd2ff3dfb98/) · [Upstream code diff](https://github.com/affaan-m/agentshield/compare/9bbc007cf5afb562c324bbad4ce6c544420f49f6...b0891303bdcd6037376a94263d45cfd2ff3dfb98)

| Changed | Before | After |
| --- | --- | --- |
| Input: baseline | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to an AgentShield baseline JSON file for drift comparison&quot;, &quot;required&quot;: false} |
| Input: evidence-pack | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to write an AgentShield evidence pack for audit and security-review handoffs&quot;, &quot;required&quot;: false} |
| Input: fail-on-policy | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Fail the action when the organization policy is non-compliant&quot;, &quot;required&quot;: false} |
| Input: fail-on-policy-promotion | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Fail the action when policy promotion review items still require action&quot;, &quot;required&quot;: false} |
| Input: fail-on-supply-chain | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Fail the action when supply-chain verification finds critical or high package risks; defaults to fail-on-findings when unset&quot;, &quot;required&quot;: false} |
| Input: format | {&quot;default&quot;: &quot;terminal&quot;, &quot;description&quot;: &quot;Output format: terminal, json, markdown&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;terminal&quot;, &quot;description&quot;: &quot;Output format: terminal, json, markdown, sarif&quot;, &quot;required&quot;: false} |
| Input: policy | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to an AgentShield organization policy JSON file&quot;, &quot;required&quot;: false} |
| Input: policy-promotion-dry-run | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Verify promotion review evidence without writing the active policy&quot;, &quot;required&quot;: false} |
| Input: policy-promotion-manifest | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to an AgentShield policy export manifest to verify and promote or dry-run&quot;, &quot;required&quot;: false} |
| Input: policy-promotion-output | null | {&quot;default&quot;: &quot;.agentshield/policy.json&quot;, &quot;description&quot;: &quot;Path to write the promoted active policy when policy-promotion-dry-run is false&quot;, &quot;required&quot;: false} |
| Input: policy-promotion-pack | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Policy pack id to select when the promotion manifest contains multiple packs&quot;, &quot;required&quot;: false} |
| Input: sarif-output | null | {&quot;default&quot;: &quot;agentshield-results.sarif&quot;, &quot;description&quot;: &quot;Path to write SARIF results when format is sarif&quot;, &quot;required&quot;: false} |
| Input: save-baseline | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to write the current scan as a new AgentShield baseline JSON file&quot;, &quot;required&quot;: false} |
| Input: supply-chain | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Verify MCP npm/git package provenance and known malicious package risk&quot;, &quot;required&quot;: false} |
| Input: supply-chain-online | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Query npm registry metadata during supply-chain verification&quot;, &quot;required&quot;: false} |
| Input: verify-evidence-pack | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Verify evidence-pack artifact hashes and bundle digest after writing&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;critical-count&quot;, &quot;grade&quot;, &quot;score&quot;, &quot;total-findings&quot;\] | \[&quot;baseline-path&quot;, &quot;baseline-status&quot;, &quot;critical-count&quot;, &quot;evidence-pack-digest&quot;, &quot;evidence-pack-path&quot;, &quot;evidence-pack-status&quot;, &quot;grade&quot;, &quot;new-findings&quot;, &quot;package-manager-hardening-critical-count&quot;, &quot;package-manager-hardening-findings&quot;, &quot;package-manager-hardening-high-count&quot;, &quot;package-manager-hardening-lifecycle-scripts&quot;, &quot;package-manager-hardening-registry-credentials&quot;, &quot;package-manager-hardening-release-age-gates&quot;, &quot;package-manager-hardening-status&quot;, &quot;policy-promotion-action-required-count&quot;, &quot;policy-promotion-digest&quot;, &quot;policy-promotion-pack&quot;, &quot;policy-promotion-review-items&quot;, &quot;policy-promotion-status&quot;, &quot;policy-status&quot;, &quot;policy-violations&quot;, &quot;resolved-findings&quot;, &quot;sarif-path&quot;, &quot;score&quot;, &quot;score-delta&quot;, &quot;supply-chain-critical-count&quot;, &quot;supply-chain-high-count&quot;, &quot;supply-chain-risky-packages&quot;, &quot;supply-chain-status&quot;, &quot;total-findings&quot;, &quot;unchanged-findings&quot;\] |
| Runtime | node20 | node24 |
| Selected SHA | 9bbc007cf5afb562c324bbad4ce6c544420f49f6 | b0891303bdcd6037376a94263d45cfd2ff3dfb98 |
| Selected tag | v1.4.0 | v1.6.0 |

## Aletheore/Aletheore

[Previous source](https://github.com/Aletheore/Aletheore) · [Current source](https://github.com/Aletheore/Aletheore/tree/d6f20beaa2257046abf501b4233a77e444e876c0/)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\] | \[\[&quot;artipacked&quot;, &quot;warning&quot;, &quot;credential persistence through GitHub Actions artifacts&quot;\], \[&quot;artipacked&quot;, &quot;warning&quot;, &quot;credential persistence through GitHub Actions artifacts&quot;\]\] |
| Input: base-ref | null | {&quot;default&quot;: &quot;${{ github.event.pull\_request.base.sha }}&quot;, &quot;description&quot;: &quot;Git ref/sha to treat as the base&quot;, &quot;required&quot;: false} |
| Input: fail-on-new-layer-violations | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Exit non-zero if a new layer-convention violation is found&quot;, &quot;required&quot;: false} |
| Input: fail-on-new-secrets | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Exit non-zero if a new real (non-placeholder) secret is found&quot;, &quot;required&quot;: false} |
| Input: fail-on-new-vulnerabilities | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Exit non-zero if a new dependency vulnerability is found&quot;, &quot;required&quot;: false} |
| Input: full | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Show the full raw diff instead of the curated summary&quot;, &quot;required&quot;: false} |
| Input: head-ref | null | {&quot;default&quot;: &quot;${{ github.event.pull\_request.head.sha }}&quot;, &quot;description&quot;: &quot;Git ref/sha to treat as the head&quot;, &quot;required&quot;: false} |
| Input: post-pr-comment | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Post the diff as a PR comment (requires pull-requests: write permission)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;diff-json&quot;\] |
| Runtime | null | composite |
| Security | unknown | warning |
| Selected SHA | null | d6f20beaa2257046abf501b4233a77e444e876c0 |
| Selected tag | null | v0.9.15 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/19dda84776b3518d98b8798e591daee763049ed3/) · [Current source](https://github.com/anthropics/claude-code-action/tree/0a8d3c9443bbff909ab973b6a17a340b913f229f/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/19dda84776b3518d98b8798e591daee763049ed3...0a8d3c9443bbff909ab973b6a17a340b913f229f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 19dda84776b3518d98b8798e591daee763049ed3 | 0a8d3c9443bbff909ab973b6a17a340b913f229f |
| Selected tag | v1.0.220 | v1.0.221 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/95a6f54149a82f0d54d9f6d3275461cad18f0fc0/) · [Current source](https://github.com/asklokesh/loki-mode/tree/7c6be7414ca46b6b678b882e284541c41b8ab092/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/95a6f54149a82f0d54d9f6d3275461cad18f0fc0...7c6be7414ca46b6b678b882e284541c41b8ab092)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 95a6f54149a82f0d54d9f6d3275461cad18f0fc0 | 7c6be7414ca46b6b678b882e284541c41b8ab092 |
| Selected tag | v9.26.3 | v9.35.0 |

## astral-sh/setup-uv

[Previous source](https://github.com/astral-sh/setup-uv/tree/20cfd1bf945f4377ade1205e4dbc17946fc9a30d/) · [Current source](https://github.com/astral-sh/setup-uv/tree/bec219d24cd3e171d82865faccec33120bb574f4/) · [Upstream code diff](https://github.com/astral-sh/setup-uv/compare/20cfd1bf945f4377ade1205e4dbc17946fc9a30d...bec219d24cd3e171d82865faccec33120bb574f4)

| Changed | Before | After |
| --- | --- | --- |
| Outputs | \[&quot;cache-hit&quot;, &quot;cache-key&quot;, &quot;python-cache-hit&quot;, &quot;python-version&quot;, &quot;uv-path&quot;, &quot;uv-version&quot;, &quot;uvx-path&quot;, &quot;venv&quot;\] | \[&quot;cache-hit&quot;, &quot;cache-key&quot;, &quot;python-cache-hit&quot;, &quot;python-runtime-id&quot;, &quot;python-version&quot;, &quot;uv-path&quot;, &quot;uv-version&quot;, &quot;uvx-path&quot;, &quot;venv&quot;\] |
| Selected SHA | 20cfd1bf945f4377ade1205e4dbc17946fc9a30d | bec219d24cd3e171d82865faccec33120bb574f4 |
| Selected tag | v10.0.1 | v10.1.0 |

## dawidd6/action-homebrew-bump-formula

[Previous source](https://github.com/dawidd6/action-homebrew-bump-formula/tree/a0e064e08103c01870c6d1b05168d1b726aab119/) · [Current source](https://github.com/dawidd6/action-homebrew-bump-formula/tree/b12d2bc99c46444125e606142f28200ec71a1214/) · [Upstream code diff](https://github.com/dawidd6/action-homebrew-bump-formula/compare/a0e064e08103c01870c6d1b05168d1b726aab119...b12d2bc99c46444125e606142f28200ec71a1214)

| Changed | Before | After |
| --- | --- | --- |
| Input: branch | null | {&quot;description&quot;: &quot;Tap branch to bump against.\\n\\nDefaults to the tap&#x27;s default branch.\\n\\nExample: dev\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | a0e064e08103c01870c6d1b05168d1b726aab119 | b12d2bc99c46444125e606142f28200ec71a1214 |
| Selected tag | v8 | v10 |

## dawidd6/action-send-mail

[Previous source](https://github.com/dawidd6/action-send-mail/tree/ca8dbb4d4f91ca7f75e7f2feea5339e76ce70c90/) · [Current source](https://github.com/dawidd6/action-send-mail/tree/03a02a49409134de07636216fb379a026c52991e/) · [Upstream code diff](https://github.com/dawidd6/action-send-mail/compare/ca8dbb4d4f91ca7f75e7f2feea5339e76ce70c90...03a02a49409134de07636216fb379a026c52991e)

| Changed | Before | After |
| --- | --- | --- |
| Input: require\_tls | null | {&quot;description&quot;: &quot;When &#x27;secure&#x27; is false, refuse to send if the server does not support STARTTLS (prevents credentials from ever being sent in clear text)&quot;, &quot;required&quot;: false} |
| Selected SHA | ca8dbb4d4f91ca7f75e7f2feea5339e76ce70c90 | 03a02a49409134de07636216fb379a026c52991e |
| Selected tag | v20 | v21 |

## Added: hermes-labs-ai/lintlang

[Source](https://github.com/hermes-labs-ai/lintlang) — Statically lint AI agent configs, tool definitions, and prompts with LintLang.

New entries still require observed stability and fresh scan evidence before usage.

## juliangruber/approve-pull-request-action

[Previous source](https://github.com/juliangruber/approve-pull-request-action/tree/68fcc9a5a73b5641cadf757cf99d73720dcb05d0/) · [Current source](https://github.com/juliangruber/approve-pull-request-action/tree/1cecaf0206ba34c4fddd072ded0b42e28ee68dd9/) · [Upstream code diff](https://github.com/juliangruber/approve-pull-request-action/compare/68fcc9a5a73b5641cadf757cf99d73720dcb05d0...1cecaf0206ba34c4fddd072ded0b42e28ee68dd9)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 68fcc9a5a73b5641cadf757cf99d73720dcb05d0 | 1cecaf0206ba34c4fddd072ded0b42e28ee68dd9 |
| Selected tag | v2.1.0 | v2.1.1 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/e6d5add383f6fa331f36f35a7ae3977c0c0a1971/) · [Current source](https://github.com/pullfrog/pullfrog/tree/59433521bdff32d700bbd62f729754fa34e948d8/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/e6d5add383f6fa331f36f35a7ae3977c0c0a1971...59433521bdff32d700bbd62f729754fa34e948d8)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e6d5add383f6fa331f36f35a7ae3977c0c0a1971 | 59433521bdff32d700bbd62f729754fa34e948d8 |
| Selected tag | v0.1.70 | v0.1.75 |

## shogo82148/actions-setup-mysql

[Previous source](https://github.com/shogo82148/actions-setup-mysql/tree/62da9377d83991fce27b6ed2a397d3306121e41d/) · [Current source](https://github.com/shogo82148/actions-setup-mysql/tree/083ec148d28e62f2b24b8f4541693dfe1d50488d/) · [Upstream code diff](https://github.com/shogo82148/actions-setup-mysql/compare/62da9377d83991fce27b6ed2a397d3306121e41d...083ec148d28e62f2b24b8f4541693dfe1d50488d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 62da9377d83991fce27b6ed2a397d3306121e41d | 083ec148d28e62f2b24b8f4541693dfe1d50488d |
| Selected tag | v1.53.1 | v1.54.0 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/c3ec0de9ae7f1019cea21aa96aa0a895b9552063/) · [Current source](https://github.com/taiki-e/install-action/tree/fa23953489c080190314742a9b907f8e97c6767c/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/c3ec0de9ae7f1019cea21aa96aa0a895b9552063...fa23953489c080190314742a9b907f8e97c6767c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | c3ec0de9ae7f1019cea21aa96aa0a895b9552063 | fa23953489c080190314742a9b907f8e97c6767c |
| Selected tag | v2.87.9 | v2.87.10 |

## Added: UiPath/coder\_eval

[Source](https://github.com/UiPath/coder_eval) — Install a pinned coder-eval and run evaluation tasks as a CI gate, with JUnit XML output.

New entries still require observed stability and fresh scan evidence before usage.
