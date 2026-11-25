# Latest catalog changes

18 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## actions/dependency-review-action

[Previous source](https://github.com/actions/dependency-review-action/tree/a1d282b36b6f3519aa1f3fc636f609c47dddb294/) · [Current source](https://github.com/actions/dependency-review-action/tree/bbc44d14a204704ccc493733616cd1e93a0321ec/) · [Upstream code diff](https://github.com/actions/dependency-review-action/compare/a1d282b36b6f3519aa1f3fc636f609c47dddb294...bbc44d14a204704ccc493733616cd1e93a0321ec)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a1d282b36b6f3519aa1f3fc636f609c47dddb294 | bbc44d14a204704ccc493733616cd1e93a0321ec |
| Selected tag | v5.0.0 | v5.0.1 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/cc98b3ae241b0fcfb6a42a2690751afffecb4452/) · [Current source](https://github.com/anthropics/claude-code-action/tree/e5812cd75691ca7bbfc57c0ecf4441db3a1ab7dd/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/cc98b3ae241b0fcfb6a42a2690751afffecb4452...e5812cd75691ca7bbfc57c0ecf4441db3a1ab7dd)

| Changed | Before | After |
| --- | --- | --- |
| Input: allow\_fork\_prs | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether to run on pull requests from forks, and on workflow\_run events for a fork&#x27;s run. With any value other than &#x27;true&#x27;, the action skips them, whoever opened them, before it checks anything out. See docs/security.md.&quot;, &quot;required&quot;: false} |
| Input: base\_branch | {&quot;description&quot;: &quot;The branch to use as the base/source when creating new branches (defaults to repository default branch)&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The branch to use as the base/source when creating new branches (defaults to repository default branch). On pull requests from authors without write access that don&#x27;t target the default branch, Claude&#x27;s config also comes from it, so don&#x27;t set it to a value from the pull request&quot;, &quot;required&quot;: false} |
| Selected SHA | cc98b3ae241b0fcfb6a42a2690751afffecb4452 | e5812cd75691ca7bbfc57c0ecf4441db3a1ab7dd |
| Selected tag | v1.0.278 | v1.0.281 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/3ee0df67c0be7bcdec404e9fd9323d638bc586a4/) · [Current source](https://github.com/asklokesh/loki-mode/tree/15e73cbfa4fd97ddb01c17f7a775474d81ecbe22/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/3ee0df67c0be7bcdec404e9fd9323d638bc586a4...15e73cbfa4fd97ddb01c17f7a775474d81ecbe22)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3ee0df67c0be7bcdec404e9fd9323d638bc586a4 | 15e73cbfa4fd97ddb01c17f7a775474d81ecbe22 |
| Selected tag | v11.152.0 | v11.156.0 |

## auscaster/silvertongue

[Previous source](https://github.com/auscaster/silvertongue/tree/06fe432eac6f8420e30102cf7b7cdb13b03f282d/) · [Current source](https://github.com/auscaster/silvertongue/tree/d0ec739c6867dd5b8113c3f8667eae60b28328a5/) · [Upstream code diff](https://github.com/auscaster/silvertongue/compare/06fe432eac6f8420e30102cf7b7cdb13b03f282d...d0ec739c6867dd5b8113c3f8667eae60b28328a5)

| Changed | Before | After |
| --- | --- | --- |
| Description | Funny AI code review. Let Gordon Ramsay school your sloppy PRs, or Ricky Gervais roast them. 65+ celebrity voices and styles. | AI code review in 65+ famous voices. From comedians, to Shakespeare, to Brainrot. Slop doesn&#x27;t have to be boring. |
| Selected SHA | 06fe432eac6f8420e30102cf7b7cdb13b03f282d | d0ec739c6867dd5b8113c3f8667eae60b28328a5 |
| Selected tag | v1.1.1 | v1.2.0 |

## aws-actions/amazon-ecr-login

[Previous source](https://github.com/aws-actions/amazon-ecr-login/tree/03f1aad4c6c7ffd436567f42f9384779290529bd/) · [Current source](https://github.com/aws-actions/amazon-ecr-login/tree/7290e214a610b32bc0eef81748948b6d466a8783/) · [Upstream code diff](https://github.com/aws-actions/amazon-ecr-login/compare/03f1aad4c6c7ffd436567f42f9384779290529bd...7290e214a610b32bc0eef81748948b6d466a8783)

| Changed | Before | After |
| --- | --- | --- |
| Input: ecr-private-token-type | null | {&quot;default&quot;: &quot;regional-token&quot;, &quot;description&quot;: &quot;Choose the token type for ECR Private registries. Options: \[regional-token, global-token\]&quot;, &quot;required&quot;: false} |
| Selected SHA | 03f1aad4c6c7ffd436567f42f9384779290529bd | 7290e214a610b32bc0eef81748948b6d466a8783 |
| Selected tag | v2.1.7 | v2.2.0 |

## aws-actions/aws-secretsmanager-get-secrets

[Previous source](https://github.com/aws-actions/aws-secretsmanager-get-secrets/tree/2297f9a879480a9e3af9b293ed15c70caf8e1c88/) · [Current source](https://github.com/aws-actions/aws-secretsmanager-get-secrets/tree/e952bd7125c27e5be0060e50955b90a7e5addd99/) · [Upstream code diff](https://github.com/aws-actions/aws-secretsmanager-get-secrets/compare/2297f9a879480a9e3af9b293ed15c70caf8e1c88...e952bd7125c27e5be0060e50955b90a7e5addd99)

| Changed | Before | After |
| --- | --- | --- |
| Input: http-proxy | null | {&quot;description&quot;: &quot;(Optional) HTTP or HTTPS proxy URL to route Secrets Manager API calls through, e.g. http://proxy.example.com:3128. Defaults to the https\_proxy/HTTPS\_PROXY environment variable. Set no-proxy to \\&quot;\*\\&quot; to ignore a proxy from the environment.&quot;, &quot;required&quot;: false} |
| Input: no-proxy | null | {&quot;description&quot;: &quot;(Optional) Comma-separated hosts that bypass the proxy, e.g. .amazonaws.com, or \\&quot;\*\\&quot; for all hosts. Defaults to the no\_proxy/NO\_PROXY environment variable, also when http-proxy is set. Only used when a proxy is configured.&quot;, &quot;required&quot;: false} |
| Selected SHA | 2297f9a879480a9e3af9b293ed15c70caf8e1c88 | e952bd7125c27e5be0060e50955b90a7e5addd99 |
| Selected tag | v3.0.2 | v4.0.0 |

## chromaui/action

[Previous source](https://github.com/chromaui/action/tree/6efa19d4a40404313897de5a6d516e0333a2a787/) · [Current source](https://github.com/chromaui/action/tree/86505fc3fa3b2ed5f39eda89f34f4051ea8ff0c8/) · [Upstream code diff](https://github.com/chromaui/action/compare/6efa19d4a40404313897de5a6d516e0333a2a787...86505fc3fa3b2ed5f39eda89f34f4051ea8ff0c8)

| Changed | Before | After |
| --- | --- | --- |
| Input: onlyChanged | {&quot;description&quot;: &quot;Enables TurboSnap: Only run stories affected by files changed since the baseline build&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Enables TurboSnap: Only run stories potentially affected by files changed since the baseline build&quot;, &quot;required&quot;: false} |
| Input: traceChanged | {&quot;description&quot;: &quot;Print dependency trace for changed files to affected story files; set to \\&quot;expanded\\&quot; to list individual modules&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Print dependency trace for changed files to potentially affected story files; set to \\&quot;expanded\\&quot; to list individual modules&quot;, &quot;required&quot;: false} |
| Selected SHA | 6efa19d4a40404313897de5a6d516e0333a2a787 | 86505fc3fa3b2ed5f39eda89f34f4051ea8ff0c8 |
| Selected tag | v18.14.5 | v18.14.6 |

## dawidd6/action-homebrew-bump-formula

[Previous source](https://github.com/dawidd6/action-homebrew-bump-formula/tree/b12d2bc99c46444125e606142f28200ec71a1214/) · [Current source](https://github.com/dawidd6/action-homebrew-bump-formula/tree/346ef10bbd55df1c9c70fbaa6b016d26876eefb1/) · [Upstream code diff](https://github.com/dawidd6/action-homebrew-bump-formula/compare/b12d2bc99c46444125e606142f28200ec71a1214...346ef10bbd55df1c9c70fbaa6b016d26876eefb1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b12d2bc99c46444125e606142f28200ec71a1214 | 346ef10bbd55df1c9c70fbaa6b016d26876eefb1 |
| Selected tag | v10 | v11 |

## Added: gauravsharmaGG/mergejudge-runner

[Source](https://github.com/gauravsharmaGG/mergejudge-runner) — Open-source AI pull request reviewer: sorts every PR into auto, review or block. Rules first, your own AI key.

New entries still require observed stability and fresh scan evidence before usage.

## graalvm/setup-graalvm

[Previous source](https://github.com/graalvm/setup-graalvm/tree/d6eca2595046623d69d636041513c80abf745406/) · [Current source](https://github.com/graalvm/setup-graalvm/tree/60e76998d25690099182b796e99b8804da582d90/) · [Upstream code diff](https://github.com/graalvm/setup-graalvm/compare/d6eca2595046623d69d636041513c80abf745406...60e76998d25690099182b796e99b8804da582d90)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | d6eca2595046623d69d636041513c80abf745406 | 60e76998d25690099182b796e99b8804da582d90 |
| Selected tag | v1.6.9 | v1.6.10 |

## JetBrains/qodana-action

[Previous source](https://github.com/JetBrains/qodana-action) · [Current source](https://github.com/JetBrains/qodana-action/tree/13e3acbbaeb2cbfc37893b98e74594985edf42eb/)

| Changed | Before | After |
| --- | --- | --- |
| Input: additional-cache-key | null | {&quot;default&quot;: &quot;qodana-2026.2-${{ github.ref }}&quot;, &quot;description&quot;: &quot;Set the additional cache key&quot;, &quot;required&quot;: false} |
| Input: args | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Additional Qodana CLI arguments, e.g. \\&quot;--log-level debug --property key=value\\&quot;. Quote arguments containing spaces. Comma-separated format is deprecated.&quot;, &quot;required&quot;: false} |
| Input: artifact-name | null | {&quot;default&quot;: &quot;qodana-report&quot;, &quot;description&quot;: &quot;Specify Qodana results artifact name, used for results uploading&quot;, &quot;required&quot;: false} |
| Input: cache-default-branch-only | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Upload cache for the default branch only&quot;, &quot;required&quot;: false} |
| Input: cache-dir | null | {&quot;default&quot;: &quot;${{ runner.temp }}/qodana/caches&quot;, &quot;description&quot;: &quot;Directory to store Qodana caches&quot;, &quot;required&quot;: false} |
| Input: commit-message | null | {&quot;default&quot;: &quot;🤖 Apply quick-fixes by Qodana&quot;, &quot;description&quot;: &quot;Commit message for the commit with quick-fixes. Not used if \`push-fixes\` is set to \`none\`&quot;, &quot;required&quot;: false} |
| Input: env-vars-to-linter | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Comma-separated names of environment variables whose values should be passed to the Qodana linter container. Docker mode only; ignored in native mode because the linter already inherits the process environment.&quot;, &quot;required&quot;: false} |
| Input: github-token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;GitHub token to access the repository: post annotations, comments&quot;, &quot;required&quot;: false} |
| Input: nightly-version | null | {&quot;default&quot;: &quot;&quot;, &quot;deprecationMessage&quot;: &quot;This option is for development purposes only. Do not use it in production.&quot;, &quot;description&quot;: &quot;Qodana CLI nightly version to use (e.g. 2026.2 or latest). Downloads CLI from tag v{version}-nightly.&quot;, &quot;required&quot;: false} |
| Input: post-pr-comment | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Post a comment with the Qodana results summary to the pull request&quot;, &quot;required&quot;: false} |
| Input: pr-mode | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Analyze ONLY changed files in a pull request&quot;, &quot;required&quot;: false} |
| Input: primary-cache-key | null | {&quot;default&quot;: &quot;qodana-2026.2-${{ github.ref }}-${{ github.sha }}&quot;, &quot;description&quot;: &quot;Set the primary cache key&quot;, &quot;required&quot;: false} |
| Input: push-fixes | null | {&quot;default&quot;: &quot;none&quot;, &quot;description&quot;: &quot;Push Qodana fixes to the repository, can be none, branch to the current branch, or a pull request&quot;, &quot;required&quot;: false} |
| Input: results-dir | null | {&quot;default&quot;: &quot;${{ runner.temp }}/qodana/results&quot;, &quot;description&quot;: &quot;Directory to store the analysis results&quot;, &quot;required&quot;: false} |
| Input: upload-result | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Upload Qodana results (SARIF, other artifacts, logs) as an artifact to the job&quot;, &quot;required&quot;: false} |
| Input: use-annotations | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Use annotations to mark the results in the GitHub user interface&quot;, &quot;required&quot;: false} |
| Input: use-caches | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Automatically restore and save Qodana caches using GitHub caches&quot;, &quot;required&quot;: false} |
| Input: use-installed-cli | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Use a Qodana CLI already available on PATH instead of downloading one.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 13e3acbbaeb2cbfc37893b98e74594985edf42eb |
| Selected tag | null | v2026.2.4 |

## node9-ai/node9-proxy

[Previous source](https://github.com/node9-ai/node9-proxy/tree/e766c8953278ec5379754a864ec63907aaf8593a/) · [Current source](https://github.com/node9-ai/node9-proxy/tree/094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59/) · [Upstream code diff](https://github.com/node9-ai/node9-proxy/compare/e766c8953278ec5379754a864ec63907aaf8593a...094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e766c8953278ec5379754a864ec63907aaf8593a | 094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59 |
| Selected tag | v2.65.0 | v2.65.6 |

## openqodex/openqodex

[Previous source](https://github.com/openqodex/openqodex/tree/833bfb4f11d058b35da61014f1f406dac7516e16/) · [Current source](https://github.com/openqodex/openqodex/tree/0a67e51fdf9e67aebf082d4dcf700a54c200e1af/) · [Upstream code diff](https://github.com/openqodex/openqodex/compare/833bfb4f11d058b35da61014f1f406dac7516e16...0a67e51fdf9e67aebf082d4dcf700a54c200e1af)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.18.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.19.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} |
| Selected SHA | 833bfb4f11d058b35da61014f1f406dac7516e16 | 0a67e51fdf9e67aebf082d4dcf700a54c200e1af |
| Selected tag | v0.18.0 | v0.19.0 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/75f7ee99ad40922d195eff131f025f4ba79035ff/) · [Current source](https://github.com/pullfrog/pullfrog/tree/9eb4e93d38160a21b0e85b759ab8ea9fecaf5e58/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/75f7ee99ad40922d195eff131f025f4ba79035ff...9eb4e93d38160a21b0e85b759ab8ea9fecaf5e58)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 75f7ee99ad40922d195eff131f025f4ba79035ff | 9eb4e93d38160a21b0e85b759ab8ea9fecaf5e58 |
| Selected tag | v0.1.131 | v0.1.138 |

## sbt/setup-sbt

[Previous source](https://github.com/sbt/setup-sbt/tree/67d461eba2c4753196c230e02da850757ba4775e/) · [Current source](https://github.com/sbt/setup-sbt/tree/7e114eae4f32ec3f93c851c2793376a77f384409/) · [Upstream code diff](https://github.com/sbt/setup-sbt/compare/67d461eba2c4753196c230e02da850757ba4775e...7e114eae4f32ec3f93c851c2793376a77f384409)

| Changed | Before | After |
| --- | --- | --- |
| Input: sbt-runner-version | {&quot;default&quot;: &quot;2.0.12&quot;, &quot;description&quot;: &quot;The runner version (The actual version is controlled via project/build.properties)&quot;, &quot;required&quot;: true} | {&quot;default&quot;: &quot;2.1.0&quot;, &quot;description&quot;: &quot;The runner version (The actual version is controlled via project/build.properties)&quot;, &quot;required&quot;: true} |
| Selected SHA | 67d461eba2c4753196c230e02da850757ba4775e | 7e114eae4f32ec3f93c851c2793376a77f384409 |
| Selected tag | v1.5.14 | v1.5.15 |

## step-security/harden-runner

[Previous source](https://github.com/step-security/harden-runner/tree/1d88384fd173af6ecb012dfd0264a306b711241a/) · [Current source](https://github.com/step-security/harden-runner/tree/aebdcf6156ab6691adf63218240e476564a1ed4c/) · [Upstream code diff](https://github.com/step-security/harden-runner/compare/1d88384fd173af6ecb012dfd0264a306b711241a...aebdcf6156ab6691adf63218240e476564a1ed4c)

| Changed | Before | After |
| --- | --- | --- |
| Input: check-run-id | null | {&quot;default&quot;: &quot;${{ job.check\_run\_id }}&quot;, &quot;description&quot;: &quot;Internal, do not set. The job&#x27;s check run ID, used by secure-registry to identify the job when no OIDC token is available.&quot;, &quot;required&quot;: false} |
| Input: secure-registry | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Route npm installs in this job through StepSecurity secure-registry. Set to true for the default settings, or to a YAML block: \`ecosystems\` (all, the default, or a list such as \[npm\]) picks which ecosystems are routed, \`ecosystem-defaults\` holds settings shared by every ecosystem, and a block per ecosystem (for example \`npm:\`) overrides them. id-token: write permission is recommended so GitHub verifies the job&#x27;s identity. Leave empty or set to false to disable.&quot;, &quot;required&quot;: false} |
| Selected SHA | 1d88384fd173af6ecb012dfd0264a306b711241a | aebdcf6156ab6691adf63218240e476564a1ed4c |
| Selected tag | v2.22.4 | v2.23.0 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/ab49d3c64680143e184118bed66a46419fc15519/) · [Current source](https://github.com/taiki-e/install-action/tree/75a7c0f87bd666af3cdb75c5b9e9d03ab6044e6f/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/ab49d3c64680143e184118bed66a46419fc15519...75a7c0f87bd666af3cdb75c5b9e9d03ab6044e6f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ab49d3c64680143e184118bed66a46419fc15519 | 75a7c0f87bd666af3cdb75c5b9e9d03ab6044e6f |
| Selected tag | v2.90.5 | v2.90.6 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/ad1d18f46b594e89658acc08fbc73e04011829d9/) · [Current source](https://github.com/tmatens/compose-lint/tree/a6689c40dc419086077e6ca7d001302c818f0b33/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/ad1d18f46b594e89658acc08fbc73e04011829d9...a6689c40dc419086077e6ca7d001302c818f0b33)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ad1d18f46b594e89658acc08fbc73e04011829d9 | a6689c40dc419086077e6ca7d001302c818f0b33 |
| Selected tag | v1.6.0 | v1.6.1 |
