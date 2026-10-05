# Latest catalog changes

13 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/1975cd732a95d5db19012195ecc3531800fe2fd1/) · [Current source](https://github.com/asklokesh/loki-mode/tree/b60ca0ef35273b3553ca99ec530011ae0d33413f/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/1975cd732a95d5db19012195ecc3531800fe2fd1...b60ca0ef35273b3553ca99ec530011ae0d33413f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 1975cd732a95d5db19012195ecc3531800fe2fd1 | b60ca0ef35273b3553ca99ec530011ae0d33413f |
| Selected tag | v9.55.0 | v10.1.0 |

## bridgecrewio/checkov-action

[Previous source](https://github.com/bridgecrewio/checkov-action/tree/444c9db6fa75e2d9c19ebf1fde7322089be9009e/) · [Current source](https://github.com/bridgecrewio/checkov-action/tree/5798bad4f6dd9c1fb67ae3ec10d42d8fb67037c4/) · [Upstream code diff](https://github.com/bridgecrewio/checkov-action/compare/444c9db6fa75e2d9c19ebf1fde7322089be9009e...5798bad4f6dd9c1fb67ae3ec10d42d8fb67037c4)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 444c9db6fa75e2d9c19ebf1fde7322089be9009e | 5798bad4f6dd9c1fb67ae3ec10d42d8fb67037c4 |
| Selected tag | v12.3125.0 | v12.3126.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/6d1ac3de35dfff5b53b840b9080f5fa44db6b29e/) · [Current source](https://github.com/duriantaco/skylos/tree/0a42d5c3432221951cc6ab3024916811041b78cf/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/6d1ac3de35dfff5b53b840b9080f5fa44db6b29e...0a42d5c3432221951cc6ab3024916811041b78cf)

| Changed | Before | After |
| --- | --- | --- |
| Input: sarif-category | null | {&quot;default&quot;: &quot;skylos&quot;, &quot;description&quot;: &quot;Code scanning category for the uploaded SARIF (distinguishes multiple Skylos runs in one repo)&quot;, &quot;required&quot;: false} |
| Input: upload-sarif | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Also write skylos.sarif and upload it to GitHub code scanning (source scans only; needs permissions: security-events: write)&quot;, &quot;required&quot;: false} |
| Selected SHA | 6d1ac3de35dfff5b53b840b9080f5fa44db6b29e | 0a42d5c3432221951cc6ab3024916811041b78cf |
| Selected tag | v4.39.2 | v4.40.0 |

## flatt-security/setup-takumi-guard-npm

[Previous source](https://github.com/flatt-security/setup-takumi-guard-npm/tree/6d4182745c1e474c35a023573c2612c085be45a4/) · [Current source](https://github.com/flatt-security/setup-takumi-guard-npm/tree/3d2e7e64161c6fb76c74abd6600e4248d4859153/) · [Upstream code diff](https://github.com/flatt-security/setup-takumi-guard-npm/compare/6d4182745c1e474c35a023573c2612c085be45a4...3d2e7e64161c6fb76c74abd6600e4248d4859153)

| Changed | Before | After |
| --- | --- | --- |
| Description | Authenticate to the Takumi byGMO Guard npm registry via OIDC. Works with npm, pnpm, and yarn. | Authenticate to the Takumi byGMO Guard npm registry via OIDC. Works with npm, pnpm, yarn, and bun. |
| Findings | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\]\] | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\]\] |
| Input: always-auth | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Also send the token for unscoped packages with Yarn Classic. npm 11 and later warn about this setting on every command.&quot;, &quot;required&quot;: false} |
| Input: set-registry | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Set the registry URL in .npmrc. Set to false if you manage the registry yourself.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Set the registry URL. Set to false if you manage the registry yourself.&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;registry-url&quot;, &quot;token&quot;, &quot;token-expires-at&quot;\] | \[&quot;npmrc-path&quot;, &quot;registry-url&quot;, &quot;token&quot;, &quot;token-expires-at&quot;\] |
| Selected SHA | 6d4182745c1e474c35a023573c2612c085be45a4 | 3d2e7e64161c6fb76c74abd6600e4248d4859153 |
| Selected tag | v1.2.0 | v1.3.0 |

## jianruntech/geo-score

[Previous source](https://github.com/jianruntech/geo-score) · [Current source](https://github.com/jianruntech/geo-score/tree/884c4725841b5b3f67b8a54458030e1a5c76d0d7/)

| Changed | Before | After |
| --- | --- | --- |
| Input: annotations | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Annotate the run with checks at zero (gates as errors, others as warnings). Set to false to turn off.&quot;, &quot;required&quot;: false} |
| Input: fail-under | null | {&quot;description&quot;: &quot;Fail the job if the normalised score is below this. Omit to report without failing.&quot;, &quot;required&quot;: false} |
| Input: json-out | null | {&quot;description&quot;: &quot;Write the machine-readable report (schema/report.v2.json) to this path.&quot;, &quot;required&quot;: false} |
| Input: junit | null | {&quot;description&quot;: &quot;Write JUnit XML to this path, for CI test-report tools.&quot;, &quot;required&quot;: false} |
| Input: sample | null | {&quot;default&quot;: &quot;8&quot;, &quot;description&quot;: &quot;How many pages to sample (default 8).&quot;, &quot;required&quot;: false} |
| Input: sarif | null | {&quot;description&quot;: &quot;Write SARIF 2.1.0 to this path, for github/codeql-action/upload-sarif or any SARIF viewer. Each result points at its check&#x27;s line in the JSON report (json-out, or geo-score-report.json in the workspace).&quot;, &quot;required&quot;: false} |
| Input: url | null | {&quot;description&quot;: &quot;The URL to score.&quot;, &quot;required&quot;: true} |
| Input: urls-from | null | {&quot;description&quot;: &quot;Score the pages an earlier JSON report sampled instead of drawing a new sample, so two runs compare the same pages.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;band&quot;, &quot;gate-capped&quot;, &quot;report&quot;, &quot;report-path&quot;, &quot;score&quot;\] |
| Runtime | null | composite |
| Security | unknown | clean |
| Selected SHA | null | 884c4725841b5b3f67b8a54458030e1a5c76d0d7 |
| Selected tag | null | v1.4.0 |

## korthout/backport-action

[Previous source](https://github.com/korthout/backport-action/tree/6b65649031ac6d18ffdfd0c0820e9436f3fde22b/) · [Current source](https://github.com/korthout/backport-action/tree/8560fb503c275d433c56f05a2f64850093baa9f7/) · [Upstream code diff](https://github.com/korthout/backport-action/compare/6b65649031ac6d18ffdfd0c0820e9436f3fde22b...8560fb503c275d433c56f05a2f64850093baa9f7)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6b65649031ac6d18ffdfd0c0820e9436f3fde22b | 8560fb503c275d433c56f05a2f64850093baa9f7 |
| Selected tag | v4.6.1 | v4.7.0 |

## Added: lukka/get-cmake

[Source](https://github.com/lukka/get-cmake) — Installs CMake and Ninja, and caches them on cloud based GitHub cache, and/or on the local GitHub runner cache.

New entries still require observed stability and fresh scan evidence before usage.

## msys2/setup-msys2

[Previous source](https://github.com/msys2/setup-msys2/tree/66cd2cce69caa17b53920067426061ca1de3a884/) · [Current source](https://github.com/msys2/setup-msys2/tree/ec48f7c5447b3140e2b088413ae3a55687bccb6e/) · [Upstream code diff](https://github.com/msys2/setup-msys2/compare/66cd2cce69caa17b53920067426061ca1de3a884...ec48f7c5447b3140e2b088413ae3a55687bccb6e)

| Changed | Before | After |
| --- | --- | --- |
| Input: suppress-deprecation-warnings | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Whitespace-separated deprecation warning IDs to acknowledge and suppress&quot;, &quot;required&quot;: false} |
| Selected SHA | 66cd2cce69caa17b53920067426061ca1de3a884 | ec48f7c5447b3140e2b088413ae3a55687bccb6e |
| Selected tag | v2.32.0 | v2.33.0 |

## owenthereal/action-upterm

[Previous source](https://github.com/owenthereal/action-upterm/tree/eec00cabd6cdaa61f61ca9f4939852fcfd2b285f/) · [Current source](https://github.com/owenthereal/action-upterm/tree/41ec120391a17f0dbc38ba074d19245e925855bf/) · [Upstream code diff](https://github.com/owenthereal/action-upterm/compare/eec00cabd6cdaa61f61ca9f4939852fcfd2b285f...41ec120391a17f0dbc38ba074d19245e925855bf)

| Changed | Before | After |
| --- | --- | --- |
| Input: known-hosts | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;known\_hosts entry for the upterm server, pinning its host key. Required when upterm-server is not the default. The default server&#x27;s key is bundled with the action. A relay that presents a host certificate needs an &#x27;@cert-authority &lt;host&gt; &lt;type&gt; &lt;key&gt;&#x27; line.&quot;, &quot;required&quot;: false} |
| Selected SHA | eec00cabd6cdaa61f61ca9f4939852fcfd2b285f | 41ec120391a17f0dbc38ba074d19245e925855bf |
| Selected tag | v2.2.0 | v2.3.0 |

## renovatebot/github-action

[Previous source](https://github.com/renovatebot/github-action/tree/f3a31a786096ba6b40d0f0ffe11a494ef73bfa7c/) · [Current source](https://github.com/renovatebot/github-action/tree/1cd96b855fee0da6f230617e89dbff0e06ea393a/) · [Upstream code diff](https://github.com/renovatebot/github-action/compare/f3a31a786096ba6b40d0f0ffe11a494ef73bfa7c...1cd96b855fee0da6f230617e89dbff0e06ea393a)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f3a31a786096ba6b40d0f0ffe11a494ef73bfa7c | 1cd96b855fee0da6f230617e89dbff0e06ea393a |
| Selected tag | v46.3.4 | v46.3.5 |

## shaftoe/pi-coding-agent-action

[Previous source](https://github.com/shaftoe/pi-coding-agent-action/tree/8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4/) · [Current source](https://github.com/shaftoe/pi-coding-agent-action/tree/babaa1a909dd7021abc538be6f20c1757b3b8fb7/) · [Upstream code diff](https://github.com/shaftoe/pi-coding-agent-action/compare/8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4...babaa1a909dd7021abc538be6f20c1757b3b8fb7)

| Changed | Before | After |
| --- | --- | --- |
| Input: refresh\_model\_catalog | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether to refresh the provider&#x27;s model catalog from pi.dev at startup so models newer than the bundled SDK resolve. Set to \`false\` to skip the network round-trip and shorten boot time (the bundled model list is used instead).&quot;, &quot;required&quot;: false} |
| Selected SHA | 8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4 | babaa1a909dd7021abc538be6f20c1757b3b8fb7 |
| Selected tag | v2.29.0 | v2.29.1 |

## suzuki-shunsuke/tfaction

[Previous source](https://github.com/suzuki-shunsuke/tfaction/tree/9fdf06dabe8e3d9acb003939af57e477a0d3090e/) · [Current source](https://github.com/suzuki-shunsuke/tfaction/tree/935e0d2db39178f46045c678519a05eefb5c4f52/) · [Upstream code diff](https://github.com/suzuki-shunsuke/tfaction/compare/9fdf06dabe8e3d9acb003939af57e477a0d3090e...935e0d2db39178f46045c678519a05eefb5c4f52)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9fdf06dabe8e3d9acb003939af57e477a0d3090e | 935e0d2db39178f46045c678519a05eefb5c4f52 |
| Selected tag | v2.2.0 | v2.3.0 |

## upsidr/merge-gatekeeper

[Previous source](https://github.com/upsidr/merge-gatekeeper) · [Current source](https://github.com/upsidr/merge-gatekeeper/tree/09af7a82c1666d0e64d2bd8c01797a0bcfd3bb5d/)

| Changed | Before | After |
| --- | --- | --- |
| Input: ignored | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;set ignored jobs (comma-separated list)&quot;, &quot;required&quot;: false} |
| Input: interval | null | {&quot;default&quot;: &quot;5&quot;, &quot;description&quot;: &quot;set validate interval second (default 5)&quot;, &quot;required&quot;: false} |
| Input: ref | null | {&quot;default&quot;: &quot;${{ github.event.pull\_request.head.sha }}&quot;, &quot;description&quot;: &quot;set ref of github repository. the ref can be a SHA, a branch name, or tag name&quot;, &quot;required&quot;: false} |
| Input: self | null | {&quot;default&quot;: &quot;merge-gatekeeper&quot;, &quot;description&quot;: &quot;set self job name&quot;, &quot;required&quot;: false} |
| Input: timeout | null | {&quot;default&quot;: &quot;600&quot;, &quot;description&quot;: &quot;set validate timeout second (default 600)&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;description&quot;: &quot;set github token&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 09af7a82c1666d0e64d2bd8c01797a0bcfd3bb5d |
| Selected tag | null | v1.2.1 |
