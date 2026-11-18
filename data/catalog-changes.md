# Latest catalog changes

15 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## aws-actions/vulnerability-scan-github-action-for-amazon-inspector

[Previous source](https://github.com/aws-actions/vulnerability-scan-github-action-for-amazon-inspector/tree/c87d8a405e237cfdf16e5dd3808d28d088d7cb6f/) · [Current source](https://github.com/aws-actions/vulnerability-scan-github-action-for-amazon-inspector/tree/6b57bbc6000f30afb3cfc2d00b9c442ddc4f1fc9/) · [Upstream code diff](https://github.com/aws-actions/vulnerability-scan-github-action-for-amazon-inspector/compare/c87d8a405e237cfdf16e5dd3808d28d088d7cb6f...6b57bbc6000f30afb3cfc2d00b9c442ddc4f1fc9)

| Changed | Before | After |
| --- | --- | --- |
| Input: fail\_on\_malicious\_packages | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;If set to true, the action fails (nonzero exit) when Amazon Inspector reports one or more malicious packages. Reports and outputs are still written first. Entries in ignore\_findings or .inspector-ignore do not bypass this check. Accepts only &#x27;true&#x27; or &#x27;false&#x27; (any case); any other value fails the step.&quot;, &quot;required&quot;: false} |
| Input: ignore\_findings | {&quot;default&quot;: &quot;&#x27;&#x27;&quot;, &quot;description&quot;: &quot;A comma-separated list of finding IDs to ignore. Ignored findings are excluded from reports and do not count towards vulnerability thresholds. You can also place an &#x27;.inspector-ignore&#x27; plain-text file (one ID per line, # for comments) at the root of your repository (the workflow&#x27;s working directory).&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&#x27;&#x27;&quot;, &quot;description&quot;: &quot;A comma-separated list of finding IDs to ignore. Ignored findings are excluded from reports and do not count towards vulnerability thresholds. You can also place an &#x27;.inspector-ignore&#x27; plain-text file (one ID per line, # for comments; add SNOOZE:YYYY-MM-DD to a comment to ignore only until that date) at the root of your repository (the workflow&#x27;s working directory).&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;artifact\_sbom&quot;, &quot;inspector\_dockerile\_scan\_results\_csv&quot;, &quot;inspector\_dockerile\_scan\_results\_markdown&quot;, &quot;inspector\_license\_results\_csv&quot;, &quot;inspector\_license\_results\_markdown&quot;, &quot;inspector\_malware\_scan\_results\_markdown&quot;, &quot;inspector\_scan\_results&quot;, &quot;inspector\_scan\_results\_csv&quot;, &quot;inspector\_scan\_results\_markdown&quot;, &quot;inspector\_scan\_results\_sarif&quot;, &quot;vulnerability\_threshold\_exceeded&quot;\] | \[&quot;artifact\_sbom&quot;, &quot;inspector\_dockerfile\_scan\_results\_csv&quot;, &quot;inspector\_dockerfile\_scan\_results\_markdown&quot;, &quot;inspector\_dockerile\_scan\_results\_csv&quot;, &quot;inspector\_dockerile\_scan\_results\_markdown&quot;, &quot;inspector\_license\_results\_csv&quot;, &quot;inspector\_license\_results\_markdown&quot;, &quot;inspector\_malware\_scan\_results\_markdown&quot;, &quot;inspector\_scan\_results&quot;, &quot;inspector\_scan\_results\_csv&quot;, &quot;inspector\_scan\_results\_markdown&quot;, &quot;inspector\_scan\_results\_sarif&quot;, &quot;vulnerability\_threshold\_exceeded&quot;\] |
| Selected SHA | c87d8a405e237cfdf16e5dd3808d28d088d7cb6f | 6b57bbc6000f30afb3cfc2d00b9c442ddc4f1fc9 |
| Selected tag | v1.6.1 | v1.7.0 |

## bridgecrewio/checkov-action

[Previous source](https://github.com/bridgecrewio/checkov-action/tree/45edc9d8856b664db2ec251f5f8632361f0a67aa/) · [Current source](https://github.com/bridgecrewio/checkov-action/tree/a32f8b5c5c7c958bc38947c65dfe139debaf0607/) · [Upstream code diff](https://github.com/bridgecrewio/checkov-action/compare/45edc9d8856b664db2ec251f5f8632361f0a67aa...a32f8b5c5c7c958bc38947c65dfe139debaf0607)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 45edc9d8856b664db2ec251f5f8632361f0a67aa | a32f8b5c5c7c958bc38947c65dfe139debaf0607 |
| Selected tag | v12.3139.0 | v12.3140.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/e25c22b235684dcb3a8ee23ee15d4a21c89fcf97/) · [Current source](https://github.com/duriantaco/skylos/tree/436a838c4e177cdfec37bfdb080957b8f1d576aa/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/e25c22b235684dcb3a8ee23ee15d4a21c89fcf97...436a838c4e177cdfec37bfdb080957b8f1d576aa)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e25c22b235684dcb3a8ee23ee15d4a21c89fcf97 | 436a838c4e177cdfec37bfdb080957b8f1d576aa |
| Selected tag | v5.5.0 | v5.6.0 |

## Added: JetBrains/qodana-action

[Source](https://github.com/JetBrains/qodana-action) — Scan your projects with Qodana on GitHub. Docs: https://jb.gg/qodana-github-action

New entries still require observed stability and fresh scan evidence before usage.

## julia-actions/julia-runtest

[Previous source](https://github.com/julia-actions/julia-runtest/tree/6e050c8013b833b1195105ff2fce9cd802f53271/) · [Current source](https://github.com/julia-actions/julia-runtest/tree/e89ac6c957d7c4d7e0cb3162f12d8290a008f9d1/) · [Upstream code diff](https://github.com/julia-actions/julia-runtest/compare/6e050c8013b833b1195105ff2fce9cd802f53271...e89ac6c957d7c4d7e0cb3162f12d8290a008f9d1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6e050c8013b833b1195105ff2fce9cd802f53271 | e89ac6c957d7c4d7e0cb3162f12d8290a008f9d1 |
| Selected tag | v1.12.0 | v1.13.0 |

## korthout/backport-action

[Previous source](https://github.com/korthout/backport-action/tree/0ebd44f9c79a4a0a171200dcdcceec3ed9ca732f/) · [Current source](https://github.com/korthout/backport-action/tree/ad272ff24e4a8593bf18a951a154ae6af93b26b8/) · [Upstream code diff](https://github.com/korthout/backport-action/compare/0ebd44f9c79a4a0a171200dcdcceec3ed9ca732f...ad272ff24e4a8593bf18a951a154ae6af93b26b8)

| Changed | Before | After |
| --- | --- | --- |
| Input: github\_token | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;Token to authenticate requests to GitHub. Used to create and label pull requests and to comment. Either GITHUB\_TOKEN or a repo-scoped Personal Access Token (PAT).\\n&quot;} | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;Token to authenticate requests to GitHub. Used to create and label pull requests and to comment. Either GITHUB\_TOKEN, a GitHub App token, or a Personal Access Token (PAT).\\n&quot;} |
| Input: merge\_commits | {&quot;default&quot;: &quot;fail&quot;, &quot;description&quot;: &quot;Specifies how the action should deal with merge commits on the merged pull request. When set to \`fail\` the backport fails when the action detects one or more merge commits. When set to \`skip\` the action only cherry-picks non-merge commits, i.e. it ignores merge commits.\\n&quot;} | {&quot;default&quot;: &quot;fail&quot;, &quot;description&quot;: &quot;Specifies how the action should deal with merge commits on the merged pull request. When set to \`fail\` the backport fails when the action detects one or more merge commits. When set to \`skip\` the action only cherry-picks non-merge commits, i.e. it excludes merge commits. If no commits remain after excluding merge commits, the action doesn&#x27;t backport to any target branch.\\n&quot;} |
| Selected SHA | 0ebd44f9c79a4a0a171200dcdcceec3ed9ca732f | ad272ff24e4a8593bf18a951a154ae6af93b26b8 |
| Selected tag | v4.7.1 | v5.0.0 |

## node9-ai/node9-proxy

[Previous source](https://github.com/node9-ai/node9-proxy/tree/100325fbd570bf8c39a3332da5c7a08e7b402dff/) · [Current source](https://github.com/node9-ai/node9-proxy/tree/1d1aee7b2574a1155600e6c79f015163582b8438/) · [Upstream code diff](https://github.com/node9-ai/node9-proxy/compare/100325fbd570bf8c39a3332da5c7a08e7b402dff...1d1aee7b2574a1155600e6c79f015163582b8438)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 100325fbd570bf8c39a3332da5c7a08e7b402dff | 1d1aee7b2574a1155600e6c79f015163582b8438 |
| Selected tag | v2.60.0 | v2.61.1 |

## openqodex/openqodex

[Previous source](https://github.com/openqodex/openqodex/tree/6d879d65de94ab201bddd9ccad76e1d1bcff70ca/) · [Current source](https://github.com/openqodex/openqodex/tree/833bfb4f11d058b35da61014f1f406dac7516e16/) · [Upstream code diff](https://github.com/openqodex/openqodex/compare/6d879d65de94ab201bddd9ccad76e1d1bcff70ca...833bfb4f11d058b35da61014f1f406dac7516e16)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.16.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.18.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} |
| Selected SHA | 6d879d65de94ab201bddd9ccad76e1d1bcff70ca | 833bfb4f11d058b35da61014f1f406dac7516e16 |
| Selected tag | v0.16.0 | v0.18.0 |

## peter-evans/create-pull-request

[Previous source](https://github.com/peter-evans/create-pull-request/tree/15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8/) · [Current source](https://github.com/peter-evans/create-pull-request/tree/3ffccacd46053766916f087ce41d627c0b8cf2d1/) · [Upstream code diff](https://github.com/peter-evans/create-pull-request/compare/15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8...3ffccacd46053766916f087ce41d627c0b8cf2d1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 15733dbdfeedb4f7fdb73d13c6f5ac83b710fab8 | 3ffccacd46053766916f087ce41d627c0b8cf2d1 |
| Selected tag | v8.1.2 | v8.1.3 |

## peter-evans/rebase

[Previous source](https://github.com/peter-evans/rebase/tree/e4945786f7ca41fe6e101cead4395f5489593943/) · [Current source](https://github.com/peter-evans/rebase/tree/d6f70ba4beda4faa44e582a974ec3b7b40713951/) · [Upstream code diff](https://github.com/peter-evans/rebase/compare/e4945786f7ca41fe6e101cead4395f5489593943...d6f70ba4beda4faa44e582a974ec3b7b40713951)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e4945786f7ca41fe6e101cead4395f5489593943 | d6f70ba4beda4faa44e582a974ec3b7b40713951 |
| Selected tag | v4.0.0 | v4.1.1 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/6ea756a2610692d1c241dfb985e0240c46bb1925/) · [Current source](https://github.com/pullfrog/pullfrog/tree/88bcc3d4bb26951b99fafe09f65d90d20d5b6d62/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/6ea756a2610692d1c241dfb985e0240c46bb1925...88bcc3d4bb26951b99fafe09f65d90d20d5b6d62)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6ea756a2610692d1c241dfb985e0240c46bb1925 | 88bcc3d4bb26951b99fafe09f65d90d20d5b6d62 |
| Selected tag | v0.1.125 | v0.1.126 |

## py-cov-action/python-coverage-comment-action

[Previous source](https://github.com/py-cov-action/python-coverage-comment-action/tree/e5fb2218463c3377f3504b0c5b5646ed53da7a2f/) · [Current source](https://github.com/py-cov-action/python-coverage-comment-action/tree/07249dd712cd2464873eb8a59a24f97fd281e76f/) · [Upstream code diff](https://github.com/py-cov-action/python-coverage-comment-action/compare/e5fb2218463c3377f3504b0c5b5646ed53da7a2f...07249dd712cd2464873eb8a59a24f97fd281e76f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e5fb2218463c3377f3504b0c5b5646ed53da7a2f | 07249dd712cd2464873eb8a59a24f97fd281e76f |
| Selected tag | v4.5 | v4.6 |

## reviewdog/action-depup

[Previous source](https://github.com/reviewdog/action-depup/tree/99f7aecf3e4d06d5a3faf190dae5dc79ac530b5a/) · [Current source](https://github.com/reviewdog/action-depup/tree/a03fa2103b273193becba8cca43a992b9173f5dc/) · [Upstream code diff](https://github.com/reviewdog/action-depup/compare/99f7aecf3e4d06d5a3faf190dae5dc79ac530b5a...a03fa2103b273193becba8cca43a992b9173f5dc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 99f7aecf3e4d06d5a3faf190dae5dc79ac530b5a | a03fa2103b273193becba8cca43a992b9173f5dc |
| Selected tag | v1.6.5 | v1.6.7 |

## rtCamp/action-deploy-wordpress

[Previous source](https://github.com/rtCamp/action-deploy-wordpress/tree/a586389295b2c24952f1803423129cb9656f203e/) · [Current source](https://github.com/rtCamp/action-deploy-wordpress/tree/5e86d60c4593a2cab0e40459286cd7b24f2386ee/) · [Upstream code diff](https://github.com/rtCamp/action-deploy-wordpress/compare/a586389295b2c24952f1803423129cb9656f203e...5e86d60c4593a2cab0e40459286cd7b24f2386ee)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a586389295b2c24952f1803423129cb9656f203e | 5e86d60c4593a2cab0e40459286cd7b24f2386ee |
| Selected tag | v3.4.2 | v3.4.3 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/07041a0807805b1bb134c4c83efad61fe8abb7b5/) · [Current source](https://github.com/tmatens/compose-lint/tree/c73d88084090f034b1f6c63115ebfebfb8212e1b/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/07041a0807805b1bb134c4c83efad61fe8abb7b5...c73d88084090f034b1f6c63115ebfebfb8212e1b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 07041a0807805b1bb134c4c83efad61fe8abb7b5 | c73d88084090f034b1f6c63115ebfebfb8212e1b |
| Selected tag | v1.2.0 | v1.3.0 |
