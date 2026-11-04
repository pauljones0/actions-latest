# Latest catalog changes

18 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/8041f1d17e0e7d2f2cfe35002962e9f26237c0bb/) · [Current source](https://github.com/anthropics/claude-code-action/tree/d70510b174a1244958df0b03166a54912811f3e6/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/8041f1d17e0e7d2f2cfe35002962e9f26237c0bb...d70510b174a1244958df0b03166a54912811f3e6)

| Changed | Before | After |
| --- | --- | --- |
| Input: plugins | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Newline-separated list of Claude Code plugin names to install (e.g., &#x27;code-review@claude-code-plugins\\nfeature-dev@claude-code-plugins&#x27;)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Newline-separated list of Claude Code plugin names to install (e.g., &#x27;code-review@claude-plugins-official\\nfeature-dev@claude-plugins-official&#x27;)&quot;, &quot;required&quot;: false} |
| Selected SHA | 8041f1d17e0e7d2f2cfe35002962e9f26237c0bb | d70510b174a1244958df0b03166a54912811f3e6 |
| Selected tag | v1.0.263 | v1.0.264 |

## apple-actions/upload-testflight-build

[Previous source](https://github.com/apple-actions/upload-testflight-build/tree/acf1166e95edc302069b74b258a788004fe39a08/) · [Current source](https://github.com/apple-actions/upload-testflight-build/tree/958b2fe4969e2ab1824f79f07c270b950f06bb3a/) · [Upstream code diff](https://github.com/apple-actions/upload-testflight-build/compare/acf1166e95edc302069b74b258a788004fe39a08...958b2fe4969e2ab1824f79f07c270b950f06bb3a)

| Changed | Before | After |
| --- | --- | --- |
| Input: groups | null | {&quot;description&quot;: &quot;Optional comma- or newline-separated exact TestFlight beta group names to add the uploaded build to. Mutually exclusive with groups-file. Requires wait-for-processing.&quot;, &quot;required&quot;: false} |
| Input: groups-file | null | {&quot;description&quot;: &quot;Optional path to a text file of exact TestFlight beta group names (one per line; # comments allowed). Mutually exclusive with groups. Requires wait-for-processing.&quot;, &quot;required&quot;: false} |
| Input: wait-for-processing | {&quot;description&quot;: &quot;Boolean string. Set to \\&quot;false\\&quot; to skip waiting for App Store processing (metadata updates will be skipped when waiting is disabled).&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Boolean string. Set to \\&quot;false\\&quot; to skip waiting for App Store processing (metadata updates are skipped; groups/groups-file cannot be used when waiting is disabled).&quot;, &quot;required&quot;: false} |
| Selected SHA | acf1166e95edc302069b74b258a788004fe39a08 | 958b2fe4969e2ab1824f79f07c270b950f06bb3a |
| Selected tag | v5.7.0 | v5.8.0 |

## Added: coactions/setup-xvfb

[Source](https://github.com/coactions/setup-xvfb) — Run your headless tests with XVFB

New entries still require observed stability and fresh scan evidence before usage.

## cycjimmy/semantic-release-action

[Previous source](https://github.com/cycjimmy/semantic-release-action/tree/d9bf53a078bd2f86aaffaec796dbb3d28f1b6f34/) · [Current source](https://github.com/cycjimmy/semantic-release-action/tree/ad51787758d9654d5a75150a89a6fa9b3ccef95e/) · [Upstream code diff](https://github.com/cycjimmy/semantic-release-action/compare/d9bf53a078bd2f86aaffaec796dbb3d28f1b6f34...ad51787758d9654d5a75150a89a6fa9b3ccef95e)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | d9bf53a078bd2f86aaffaec796dbb3d28f1b6f34 | ad51787758d9654d5a75150a89a6fa9b3ccef95e |
| Selected tag | v8.1.3 | v8.1.4 |

## docker/scout-action

[Previous source](https://github.com/docker/scout-action/tree/a4119c5a8c5076236a54e4ce99531f7e4dd2ef84/) · [Current source](https://github.com/docker/scout-action/tree/4bbf17a9da65a7b5497361bb407e88cc9548f69c/) · [Upstream code diff](https://github.com/docker/scout-action/compare/a4119c5a8c5076236a54e4ce99531f7e4dd2ef84...4bbf17a9da65a7b5497361bb407e88cc9548f69c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a4119c5a8c5076236a54e4ce99531f7e4dd2ef84 | 4bbf17a9da65a7b5497361bb407e88cc9548f69c |
| Selected tag | v1.27.0 | v1.28.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/90ddb7f21a3af4163cd722882cfd8844b07ea96e/) · [Current source](https://github.com/duriantaco/skylos/tree/e90c3c9b08d00d89aa77807d3943ee1dc41fceb5/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/90ddb7f21a3af4163cd722882cfd8844b07ea96e...e90c3c9b08d00d89aa77807d3943ee1dc41fceb5)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 90ddb7f21a3af4163cd722882cfd8844b07ea96e | e90c3c9b08d00d89aa77807d3943ee1dc41fceb5 |
| Selected tag | v5.1.2 | v5.1.4 |

## helm/chart-releaser-action

[Previous source](https://github.com/helm/chart-releaser-action/tree/cae68fefc6b5f367a0275617c9f83181ba54714f/) · [Current source](https://github.com/helm/chart-releaser-action/tree/df287104677278f869ca5480bd260358397cc3f9/) · [Upstream code diff](https://github.com/helm/chart-releaser-action/compare/cae68fefc6b5f367a0275617c9f83181ba54714f...df287104677278f869ca5480bd260358397cc3f9)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\]\] | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\]\] |
| Input: mark\_as\_latest | {&quot;default&quot;: true, &quot;description&quot;: &quot;Mark the created GitHub release as &#x27;latest&#x27;&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Mark the created GitHub release as &#x27;latest&#x27;&quot;, &quot;required&quot;: false} |
| Input: match\_tags | null | {&quot;description&quot;: &quot;The glob to use to filter Git tags (default: all tags)&quot;, &quot;required&quot;: false} |
| Input: oci\_password | null | {&quot;description&quot;: &quot;Password or token for OCI registry authentication. Falls back to the local registry credential store when unset.&quot;, &quot;required&quot;: false} |
| Input: oci\_registry\_url | null | {&quot;description&quot;: &quot;OCI registry URL (e.g. oci://ghcr.io/myorg/charts). When set, chart packages are pushed to this OCI registry using &#x27;cr push&#x27;.&quot;, &quot;required&quot;: false} |
| Input: oci\_username | null | {&quot;description&quot;: &quot;Username for OCI registry authentication. Falls back to the local registry credential store (e.g. ~/.docker/config.json populated by helm/docker login) when unset.&quot;, &quot;required&quot;: false} |
| Input: packages\_with\_index | {&quot;default&quot;: false, &quot;description&quot;: &quot;Upload chart packages directly into publishing branch&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Upload chart packages directly into publishing branch&quot;, &quot;required&quot;: false} |
| Input: version | {&quot;default&quot;: &quot;v1.7.0&quot;, &quot;description&quot;: &quot;The chart-releaser version to use (default: v1.7.0)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v1.9.0&quot;, &quot;description&quot;: &quot;The chart-releaser version to use (default: v1.9.0)&quot;, &quot;required&quot;: false} |
| Selected SHA | cae68fefc6b5f367a0275617c9f83181ba54714f | df287104677278f869ca5480bd260358397cc3f9 |
| Selected tag | v1.7.0 | v1.8.0 |

## jdx/mise-action

[Previous source](https://github.com/jdx/mise-action/tree/82a612c5ab8bcda7cc5db6b7e81a8e7584c3dc6e/) · [Current source](https://github.com/jdx/mise-action/tree/6be3c7ed4c21d4f76b208d351d95aac273ebb76d/) · [Upstream code diff](https://github.com/jdx/mise-action/compare/82a612c5ab8bcda7cc5db6b7e81a8e7584c3dc6e...6be3c7ed4c21d4f76b208d351d95aac273ebb76d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 82a612c5ab8bcda7cc5db6b7e81a8e7584c3dc6e | 6be3c7ed4c21d4f76b208d351d95aac273ebb76d |
| Selected tag | v5.2.3 | v5.2.4 |

## macalbert/envilder

[Previous source](https://github.com/macalbert/envilder/tree/12b022c17902fdd38182b18378057b9b1b95f836/) · [Current source](https://github.com/macalbert/envilder/tree/83f4fb314b1f9c69c31cc6bc8635dbafdd7724bc/) · [Upstream code diff](https://github.com/macalbert/envilder/compare/12b022c17902fdd38182b18378057b9b1b95f836...83f4fb314b1f9c69c31cc6bc8635dbafdd7724bc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 12b022c17902fdd38182b18378057b9b1b95f836 | 83f4fb314b1f9c69c31cc6bc8635dbafdd7724bc |
| Selected tag | v0.16.0 | v0.17.1 |

## openqodex/openqodex

[Previous source](https://github.com/openqodex/openqodex/tree/7c3e5924b7c2a08fb2154a98106f188ded596942/) · [Current source](https://github.com/openqodex/openqodex/tree/6d879d65de94ab201bddd9ccad76e1d1bcff70ca/) · [Upstream code diff](https://github.com/openqodex/openqodex/compare/7c3e5924b7c2a08fb2154a98106f188ded596942...6d879d65de94ab201bddd9ccad76e1d1bcff70ca)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.15.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.16.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} |
| Selected SHA | 7c3e5924b7c2a08fb2154a98106f188ded596942 | 6d879d65de94ab201bddd9ccad76e1d1bcff70ca |
| Selected tag | v0.15.0 | v0.16.0 |

## oras-project/setup-oras

[Previous source](https://github.com/oras-project/setup-oras/tree/005458ad77f1c8facd38a094e4af2e69e5607ff4/) · [Current source](https://github.com/oras-project/setup-oras/tree/5e2f2482b30b0cb3e14e67f89a80c88c659a7c63/) · [Upstream code diff](https://github.com/oras-project/setup-oras/compare/005458ad77f1c8facd38a094e4af2e69e5607ff4...5e2f2482b30b0cb3e14e67f89a80c88c659a7c63)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 005458ad77f1c8facd38a094e4af2e69e5607ff4 | 5e2f2482b30b0cb3e14e67f89a80c88c659a7c63 |
| Selected tag | v2.0.2 | v2.0.3 |

## plengauer/Thoth

[Previous source](https://github.com/plengauer/Thoth/tree/cae29061ec48de46feefdc8131c776a9af11da6f/) · [Current source](https://github.com/plengauer/Thoth/tree/93ce0b69b0f9f22a50cc67b08f4a55c84616b5bd/) · [Upstream code diff](https://github.com/plengauer/Thoth/compare/cae29061ec48de46feefdc8131c776a9af11da6f...93ce0b69b0f9f22a50cc67b08f4a55c84616b5bd)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | cae29061ec48de46feefdc8131c776a9af11da6f | 93ce0b69b0f9f22a50cc67b08f4a55c84616b5bd |
| Selected tag | v5.64.0 | v5.65.0 |

## pypa/cibuildwheel

[Previous source](https://github.com/pypa/cibuildwheel/tree/b9e566a2b284570af229f6c2a33673410d0389a3/) · [Current source](https://github.com/pypa/cibuildwheel/tree/f9b966cfadf4109556cadc5bb39ddb72d0ce664e/) · [Upstream code diff](https://github.com/pypa/cibuildwheel/compare/b9e566a2b284570af229f6c2a33673410d0389a3...f9b966cfadf4109556cadc5bb39ddb72d0ce664e)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b9e566a2b284570af229f6c2a33673410d0389a3 | f9b966cfadf4109556cadc5bb39ddb72d0ce664e |
| Selected tag | v4.3.4 | v4.3.5 |

## reviewdog/action-misspell

[Previous source](https://github.com/reviewdog/action-misspell/tree/3467363dab5b42db2b1372c5fd2b1771fea2ea48/) · [Current source](https://github.com/reviewdog/action-misspell/tree/840bfbe9f804da9afb0bd739dc4689012f3fdd2d/) · [Upstream code diff](https://github.com/reviewdog/action-misspell/compare/3467363dab5b42db2b1372c5fd2b1771fea2ea48...840bfbe9f804da9afb0bd739dc4689012f3fdd2d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3467363dab5b42db2b1372c5fd2b1771fea2ea48 | 840bfbe9f804da9afb0bd739dc4689012f3fdd2d |
| Selected tag | v1.30.3 | v1.30.4 |

## ruzickap/action-my-broken-link-checker

[Previous source](https://github.com/ruzickap/action-my-broken-link-checker/tree/4b27aca6c7fe3290645ad406d86e61c688515eae/) · [Current source](https://github.com/ruzickap/action-my-broken-link-checker/tree/5c84b4ee7ae993f10d8e5c7898ab669d4432f269/) · [Upstream code diff](https://github.com/ruzickap/action-my-broken-link-checker/compare/4b27aca6c7fe3290645ad406d86e61c688515eae...5c84b4ee7ae993f10d8e5c7898ab669d4432f269)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 4b27aca6c7fe3290645ad406d86e61c688515eae | 5c84b4ee7ae993f10d8e5c7898ab669d4432f269 |
| Selected tag | v3.0.2 | v3.0.3 |

## SonarSource/sonarqube-scan-action

[Previous source](https://github.com/SonarSource/sonarqube-scan-action/tree/d209202bc7d53ff1cc128f7f907dac145c9d6ae9/) · [Current source](https://github.com/SonarSource/sonarqube-scan-action/tree/4d1dc0c91ee400dcf8a6dddf2f705ac36542e304/) · [Upstream code diff](https://github.com/SonarSource/sonarqube-scan-action/compare/d209202bc7d53ff1cc128f7f907dac145c9d6ae9...4d1dc0c91ee400dcf8a6dddf2f705ac36542e304)

| Changed | Before | After |
| --- | --- | --- |
| Input: scannerVersion | {&quot;default&quot;: &quot;8.1.0.6389&quot;, &quot;description&quot;: &quot;Version of the Sonar Scanner CLI to use&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;8.3.0.16463&quot;, &quot;description&quot;: &quot;Version of the Sonar Scanner CLI to use&quot;, &quot;required&quot;: false} |
| Selected SHA | d209202bc7d53ff1cc128f7f907dac145c9d6ae9 | 4d1dc0c91ee400dcf8a6dddf2f705ac36542e304 |
| Selected tag | v8.3.0 | v8.4.0 |

## step-security/harden-runner

[Previous source](https://github.com/step-security/harden-runner/tree/dc2769abcc0fcfbadfc1df54081c1608579ef6b2/) · [Current source](https://github.com/step-security/harden-runner/tree/46b06cea07f9e64621fdf066ba77ac6915163d43/) · [Upstream code diff](https://github.com/step-security/harden-runner/compare/dc2769abcc0fcfbadfc1df54081c1608579ef6b2...46b06cea07f9e64621fdf066ba77ac6915163d43)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | dc2769abcc0fcfbadfc1df54081c1608579ef6b2 | 46b06cea07f9e64621fdf066ba77ac6915163d43 |
| Selected tag | v2.22.2 | v2.22.3 |

## vladopajic/go-test-coverage

[Previous source](https://github.com/vladopajic/go-test-coverage/tree/239670d50ed072bfce8b9ab1765227a53429d664/) · [Current source](https://github.com/vladopajic/go-test-coverage/tree/249eda999ac7e91238727277beec9b32b28a19b0/) · [Upstream code diff](https://github.com/vladopajic/go-test-coverage/compare/239670d50ed072bfce8b9ab1765227a53429d664...249eda999ac7e91238727277beec9b32b28a19b0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 239670d50ed072bfce8b9ab1765227a53429d664 | 249eda999ac7e91238727277beec9b32b28a19b0 |
| Selected tag | v2.20.1 | v2.21.0 |
