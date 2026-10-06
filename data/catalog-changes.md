# Latest catalog changes

16 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## actions/upload-code-coverage

[Previous source](https://github.com/actions/upload-code-coverage/tree/d8e329117199404bba6fc81efe8093dc7c015e34/) · [Current source](https://github.com/actions/upload-code-coverage/tree/bfa741d815a28cb064a8e3a0837e577457a017d5/) · [Upstream code diff](https://github.com/actions/upload-code-coverage/compare/d8e329117199404bba6fc81efe8093dc7c015e34...bfa741d815a28cb064a8e3a0837e577457a017d5)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\]\] | \[\] |
| Security | blocked | clean |
| Selected SHA | d8e329117199404bba6fc81efe8093dc7c015e34 | bfa741d815a28cb064a8e3a0837e577457a017d5 |
| Selected tag | v1.4.2 | v1.4.3 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/756cc22e19660d20e8cc9496b4f242475a7f7790/) · [Current source](https://github.com/anthropics/claude-code-action/tree/8ce9314fa9a404564fa7e954cd84f25bcba2b829/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/756cc22e19660d20e8cc9496b4f242475a7f7790...8ce9314fa9a404564fa7e954cd84f25bcba2b829)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 756cc22e19660d20e8cc9496b4f242475a7f7790 | 8ce9314fa9a404564fa7e954cd84f25bcba2b829 |
| Selected tag | v1.0.235 | v1.0.236 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/b60ca0ef35273b3553ca99ec530011ae0d33413f/) · [Current source](https://github.com/asklokesh/loki-mode/tree/21b7becda67fa6742e1151e461e3a21d0c064d71/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/b60ca0ef35273b3553ca99ec530011ae0d33413f...21b7becda67fa6742e1151e461e3a21d0c064d71)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b60ca0ef35273b3553ca99ec530011ae0d33413f | 21b7becda67fa6742e1151e461e3a21d0c064d71 |
| Selected tag | v10.1.0 | v10.5.5 |

## calibreapp/image-actions

[Previous source](https://github.com/calibreapp/image-actions) · [Current source](https://github.com/calibreapp/image-actions/tree/9d037c06280028c110ff61c433ad4dc7d33c3c43/)

| Changed | Before | After |
| --- | --- | --- |
| Input: GITHUB\_TOKEN | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;The token that the action will use to create and update the pull request.&quot;} |
| Input: avifQuality | null | {&quot;default&quot;: &quot;75&quot;, &quot;description&quot;: &quot;AVIF quality level&quot;, &quot;required&quot;: false} |
| Input: compressOnly | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Images will be compressed. No commit, or comments will be added to your Pull Request&quot;, &quot;required&quot;: false} |
| Input: ignorePaths | null | {&quot;default&quot;: &quot;node\_modules/\*\*&quot;, &quot;description&quot;: &quot;Paths to ignore during search&quot;, &quot;required&quot;: false} |
| Input: jpegProgressive | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Use progressive (interlaced) scan for JPEG&quot;, &quot;required&quot;: false} |
| Input: jpegQuality | null | {&quot;default&quot;: &quot;85&quot;, &quot;description&quot;: &quot;JPEG quality level&quot;, &quot;required&quot;: false} |
| Input: minAbsChange | null | {&quot;default&quot;: &quot;1024&quot;, &quot;description&quot;: &quot;Minimun bytes reduction to be committed&quot;, &quot;required&quot;: false} |
| Input: minPctChange | null | {&quot;default&quot;: &quot;5&quot;, &quot;description&quot;: &quot;Minimun percentage reduction to be committed&quot;, &quot;required&quot;: false} |
| Input: pngQuality | null | {&quot;default&quot;: &quot;80&quot;, &quot;description&quot;: &quot;PNG quality level&quot;, &quot;required&quot;: false} |
| Input: webpQuality | null | {&quot;default&quot;: &quot;85&quot;, &quot;description&quot;: &quot;WEBP quality level&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;markdown&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 9d037c06280028c110ff61c433ad4dc7d33c3c43 |
| Selected tag | null | 1.5.0 |

## CodelyTV/pr-size-labeler

[Previous source](https://github.com/CodelyTV/pr-size-labeler) · [Current source](https://github.com/CodelyTV/pr-size-labeler/tree/4e3aa0f77f348c8066513d453515316ffa01a607/)

| Changed | Before | After |
| --- | --- | --- |
| Input: GITHUB\_TOKEN | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;GitHub token needed to interact with the repository&quot;, &quot;required&quot;: false} |
| Input: fail\_if\_xl | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Report GitHub Workflow failure if the PR size is xl allowing to forbid PR merge&quot;, &quot;required&quot;: false} |
| Input: files\_to\_ignore | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Whitespace separated list of files to ignore when calculating the PR size (sum of changes)&quot;, &quot;required&quot;: false} |
| Input: github\_api\_url | null | {&quot;default&quot;: &quot;${{ github.api\_url }}&quot;, &quot;description&quot;: &quot;URL to the API of your Github Server, only necessary for Github Enterprise customers&quot;, &quot;required&quot;: false} |
| Input: ignore\_file\_deletions | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to ignore files which are deleted when calculating the PR size. If set to \\&quot;true\\&quot;, deleted files will be ignored.&quot;, &quot;required&quot;: false} |
| Input: ignore\_line\_deletions | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to ignore lines which are deleted when calculating the PR size. If set to \\&quot;true\\&quot;, deleted lines will be ignored.&quot;, &quot;required&quot;: false} |
| Input: l\_label | null | {&quot;default&quot;: &quot;size/l&quot;, &quot;description&quot;: &quot;Label for l PR&quot;, &quot;required&quot;: false} |
| Input: l\_max\_size | null | {&quot;default&quot;: &quot;1000&quot;, &quot;description&quot;: &quot;Max size for a PR to be considered l&quot;, &quot;required&quot;: false} |
| Input: m\_label | null | {&quot;default&quot;: &quot;size/m&quot;, &quot;description&quot;: &quot;Label for m PR&quot;, &quot;required&quot;: false} |
| Input: m\_max\_size | null | {&quot;default&quot;: &quot;500&quot;, &quot;description&quot;: &quot;Max size for a PR to be considered m&quot;, &quot;required&quot;: false} |
| Input: message\_if\_xl | null | {&quot;default&quot;: &quot;This PR exceeds the recommended size of 1000 lines. Please make sure you are NOT addressing multiple issues with one PR. Note this PR might be rejected due to its size.\\n&quot;, &quot;description&quot;: &quot;Message to show if the PR size is xl&quot;, &quot;required&quot;: false} |
| Input: s\_label | null | {&quot;default&quot;: &quot;size/s&quot;, &quot;description&quot;: &quot;Label for s PR&quot;, &quot;required&quot;: false} |
| Input: s\_max\_size | null | {&quot;default&quot;: &quot;100&quot;, &quot;description&quot;: &quot;Max size for a PR to be considered s&quot;, &quot;required&quot;: false} |
| Input: xl\_label | null | {&quot;default&quot;: &quot;size/xl&quot;, &quot;description&quot;: &quot;Label for xl PR&quot;, &quot;required&quot;: false} |
| Input: xs\_label | null | {&quot;default&quot;: &quot;size/xs&quot;, &quot;description&quot;: &quot;Label for xs PR&quot;, &quot;required&quot;: false} |
| Input: xs\_max\_size | null | {&quot;default&quot;: &quot;10&quot;, &quot;description&quot;: &quot;Max size for a PR to be considered xs&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 4e3aa0f77f348c8066513d453515316ffa01a607 |
| Selected tag | null | v1.11.1 |

## dawidd6/action-download-artifact

[Previous source](https://github.com/dawidd6/action-download-artifact/tree/634d83b91986fcec9be314054943fa5c976aeb0e/) · [Current source](https://github.com/dawidd6/action-download-artifact/tree/27e4ae67c24b67d3b54bc6d6a45475be1e28031b/) · [Upstream code diff](https://github.com/dawidd6/action-download-artifact/compare/634d83b91986fcec9be314054943fa5c976aeb0e...27e4ae67c24b67d3b54bc6d6a45475be1e28031b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 634d83b91986fcec9be314054943fa5c976aeb0e | 27e4ae67c24b67d3b54bc6d6a45475be1e28031b |
| Selected tag | v25 | v26 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/81c06b499c0c4e9b8a4c583542f2e0cce8b4bd1f/) · [Current source](https://github.com/duriantaco/skylos/tree/041e872c9189c131a6b75b3f9007594ec800bb11/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/81c06b499c0c4e9b8a4c583542f2e0cce8b4bd1f...041e872c9189c131a6b75b3f9007594ec800bb11)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 81c06b499c0c4e9b8a4c583542f2e0cce8b4bd1f | 041e872c9189c131a6b75b3f9007594ec800bb11 |
| Selected tag | v4.41.0 | v4.42.0 |

## flatt-security/setup-takumi-guard-npm

[Previous source](https://github.com/flatt-security/setup-takumi-guard-npm/tree/3d2e7e64161c6fb76c74abd6600e4248d4859153/) · [Current source](https://github.com/flatt-security/setup-takumi-guard-npm/tree/14f07d0cbc739b42a1b7c70a04c2b84cd1318ddd/) · [Upstream code diff](https://github.com/flatt-security/setup-takumi-guard-npm/compare/3d2e7e64161c6fb76c74abd6600e4248d4859153...14f07d0cbc739b42a1b7c70a04c2b84cd1318ddd)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3d2e7e64161c6fb76c74abd6600e4248d4859153 | 14f07d0cbc739b42a1b7c70a04c2b84cd1318ddd |
| Selected tag | v1.3.0 | v1.4.0 |

## gradle/actions

[Previous source](https://github.com/gradle/actions/tree/9c971963bec38e04b3d30dcc455b5382be2fdbfb/) · [Current source](https://github.com/gradle/actions/tree/3f5f9adaf7d9fecd50b5935e54106014257a94e6/) · [Upstream code diff](https://github.com/gradle/actions/compare/9c971963bec38e04b3d30dcc455b5382be2fdbfb...3f5f9adaf7d9fecd50b5935e54106014257a94e6)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9c971963bec38e04b3d30dcc455b5382be2fdbfb | 3f5f9adaf7d9fecd50b5935e54106014257a94e6 |
| Selected tag | v6.3.0 | v6.4.0 |

## HaaLeo/publish-vscode-extension

[Previous source](https://github.com/HaaLeo/publish-vscode-extension/tree/ca5561daa085dee804bf9f37fe0165785a9b14db/) · [Current source](https://github.com/HaaLeo/publish-vscode-extension/tree/1b8df468b849f76a143b8c18bf0ffa2075398d12/) · [Upstream code diff](https://github.com/HaaLeo/publish-vscode-extension/compare/ca5561daa085dee804bf9f37fe0165785a9b14db...1b8df468b849f76a143b8c18bf0ffa2075398d12)

| Changed | Before | After |
| --- | --- | --- |
| Runtime | node20 | node24 |
| Selected SHA | ca5561daa085dee804bf9f37fe0165785a9b14db | 1b8df468b849f76a143b8c18bf0ffa2075398d12 |
| Selected tag | v2.0.0 | v2.1.0 |

## hermes-labs-ai/lintlang

[Previous source](https://github.com/hermes-labs-ai/lintlang/tree/c0cab00048220286858f227aaf4b13cc043f718b/) · [Current source](https://github.com/hermes-labs-ai/lintlang/tree/c5786a7e8c9992675a67ce49b97b55a9c8410b44/) · [Upstream code diff](https://github.com/hermes-labs-ai/lintlang/compare/c0cab00048220286858f227aaf4b13cc043f718b...c5786a7e8c9992675a67ce49b97b55a9c8410b44)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | c0cab00048220286858f227aaf4b13cc043f718b | c5786a7e8c9992675a67ce49b97b55a9c8410b44 |
| Selected tag | v0.8.0 | v0.8.1 |

## jdx/mise-action

[Previous source](https://github.com/jdx/mise-action/tree/c2a87611a18de5b3828c5652fe268e992400cb5c/) · [Current source](https://github.com/jdx/mise-action/tree/9149ea85001c7435d5a66bb127d6a1b6227cb0a5/) · [Upstream code diff](https://github.com/jdx/mise-action/compare/c2a87611a18de5b3828c5652fe268e992400cb5c...9149ea85001c7435d5a66bb127d6a1b6227cb0a5)

| Changed | Before | After |
| --- | --- | --- |
| Input: minimum\_release\_age | {&quot;description&quot;: &quot;When version is not specified, only install stable mise releases older than this threshold.\\nAccepts relative durations such as 24h, 7d, 6mo, or 1y, and absolute ISO dates or timestamps.\\n&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;24h&quot;, &quot;description&quot;: &quot;When version is not specified, only install stable mise releases older than this threshold. Defaults to 24h; set 0s to disable the delay.\\nAccepts relative durations such as 24h, 7d, 6mo, or 1y, and absolute ISO dates or timestamps.\\n&quot;, &quot;required&quot;: false} |
| Input: version | {&quot;description&quot;: &quot;The version of mise to use. If not specified, will use the latest release.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The version of mise to use. If not specified, uses the newest release satisfying minimum\_release\_age.&quot;, &quot;required&quot;: false} |
| Selected SHA | c2a87611a18de5b3828c5652fe268e992400cb5c | 9149ea85001c7435d5a66bb127d6a1b6227cb0a5 |
| Selected tag | v4.3.0 | v5.0.0 |

## mikefarah/yq

[Previous source](https://github.com/mikefarah/yq/tree/c14f446382944492701b16c1ddb48bb9dbe683e3/) · [Current source](https://github.com/mikefarah/yq/tree/504fc38780cc46be8444ea1b72fb55919fc0bfb0/) · [Upstream code diff](https://github.com/mikefarah/yq/compare/c14f446382944492701b16c1ddb48bb9dbe683e3...504fc38780cc46be8444ea1b72fb55919fc0bfb0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | c14f446382944492701b16c1ddb48bb9dbe683e3 | 504fc38780cc46be8444ea1b72fb55919fc0bfb0 |
| Selected tag | v4.53.6 | v4.54.1 |

## owenthereal/action-upterm

[Previous source](https://github.com/owenthereal/action-upterm/tree/41ec120391a17f0dbc38ba074d19245e925855bf/) · [Current source](https://github.com/owenthereal/action-upterm/tree/7df5fa550d6dc458335f4b2685452a0e42d0ba7e/) · [Upstream code diff](https://github.com/owenthereal/action-upterm/compare/41ec120391a17f0dbc38ba074d19245e925855bf...7df5fa550d6dc458335f4b2685452a0e42d0ba7e)

| Changed | Before | After |
| --- | --- | --- |
| Input: limit-access-to-actor | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If only the public SSH keys of the user triggering the workflow should be authorized&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If only the public SSH keys of the user triggering the workflow (and, on a re-run, of whoever re-ran it) should be authorized. Bot accounts such as dependabot\[bot\] have no SSH keys and are skipped; if that leaves no one to authorize, no session is started&quot;, &quot;required&quot;: false} |
| Selected SHA | 41ec120391a17f0dbc38ba074d19245e925855bf | 7df5fa550d6dc458335f4b2685452a0e42d0ba7e |
| Selected tag | v2.3.0 | v2.4.0 |

## Songmu/tagpr

[Previous source](https://github.com/Songmu/tagpr/tree/2afc990a4a5a9a340665cc1a484c2102f7de332f/) · [Current source](https://github.com/Songmu/tagpr/tree/967f2ab22be958948fb5bd439bfa3d404dd9dee8/) · [Upstream code diff](https://github.com/Songmu/tagpr/compare/2afc990a4a5a9a340665cc1a484c2102f7de332f...967f2ab22be958948fb5bd439bfa3d404dd9dee8)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;v1.21.0&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v1.21.1&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} |
| Selected SHA | 2afc990a4a5a9a340665cc1a484c2102f7de332f | 967f2ab22be958948fb5bd439bfa3d404dd9dee8 |
| Selected tag | v1.21.0 | v1.21.1 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/a6a7a76736de1c72abfa96c41ff8af556ffdc55f/) · [Current source](https://github.com/tmatens/compose-lint/tree/2d42617e4c6416f797bbfc6a057950131fa02df3/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/a6a7a76736de1c72abfa96c41ff8af556ffdc55f...2d42617e4c6416f797bbfc6a057950131fa02df3)

| Changed | Before | After |
| --- | --- | --- |
| Input: allow-partial-coverage | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Pass \`--allow-partial-coverage\`: downgrade a coverage gap (an \`include:\` or cross-file \`extends:\` that could not be followed) from exit 2 to a warning.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Pass \`--allow-partial-coverage\`: downgrade a coverage gap (an \`include:\` or cross-file \`extends:\` that could not be followed, or a \`.env\` that could not be read) from exit 2 to a warning.&quot;, &quot;required&quot;: false} |
| Selected SHA | a6a7a76736de1c72abfa96c41ff8af556ffdc55f | 2d42617e4c6416f797bbfc6a057950131fa02df3 |
| Selected tag | v0.31.0 | v0.32.0 |
