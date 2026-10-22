# Latest catalog changes

24 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## actions/setup-java

[Previous source](https://github.com/actions/setup-java/tree/de7274f081f381c8f8158605e0321c36c376e2e6/) · [Current source](https://github.com/actions/setup-java/tree/b843ebf9b913146b38da2eaa7aeddf76074ae1ad/) · [Upstream code diff](https://github.com/actions/setup-java/compare/de7274f081f381c8f8158605e0321c36c376e2e6...b843ebf9b913146b38da2eaa7aeddf76074ae1ad)

| Changed | Before | After |
| --- | --- | --- |
| Input: architecture | {&quot;description&quot;: &quot;The architecture of the package (\`x86\`, \`x64\`, \`armv7\`, \`aarch64\`, \`ppc64le\`, \`ppc64\`, or \`s390x\`). Aliases \`ia32\`, \`amd64\`, \`arm\`, and \`arm64\` are normalized to \`x86\`, \`x64\`, \`armv7\`, and \`aarch64\`. Supported values vary by distribution and operating system. Defaults to the action runner&#x27;s architecture.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The architecture of the package (\`x86\`, \`x64\`, \`armv7\`, \`aarch64\`, \`ppc64le\`, \`ppc64\`, \`riscv64\`, or \`s390x\`). Aliases \`ia32\`, \`amd64\`, \`arm\`, and \`arm64\` are normalized to \`x86\`, \`x64\`, \`armv7\`, and \`aarch64\`. Supported values vary by distribution and operating system. Defaults to the action runner&#x27;s architecture.&quot;, &quot;required&quot;: false} |
| Input: mvn-plugin-repositories | null | {&quot;description&quot;: &quot;Multiline list of Maven plugin repositories in the format \`repository-id:repository-url:snapshots-enabled\`.&quot;, &quot;required&quot;: false} |
| Input: mvn-repositories-include-central | {&quot;default&quot;: true, &quot;description&quot;: &quot;Include Maven Central in the generated dependency repositories profile. When false, Central is disabled unless an explicit repository with ID \`central\` is declared.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: true, &quot;description&quot;: &quot;Include Maven Central for dependency and plugin repositories in the generated profile. When false, Central is disabled for both types unless that type explicitly declares ID \`central\`. Has no effect when neither repository list is configured.&quot;, &quot;required&quot;: false} |
| Input: mvn-repositories-prioritize-central | {&quot;default&quot;: true, &quot;description&quot;: &quot;Place Maven Central before custom dependency repositories. Has no effect when Maven Central is excluded.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: true, &quot;description&quot;: &quot;Place Maven Central before custom dependency and plugin repositories. Has no effect when Maven Central is excluded or neither repository list is configured.&quot;, &quot;required&quot;: false} |
| Input: mvn-server-repository-origins | null | {&quot;description&quot;: &quot;Multiline list of Maven credential origins in the format \`server-id:repository-origin\`. Each origin must belong to a configured server ID. Requires Maven 3.10+.&quot;, &quot;required&quot;: false} |
| Selected SHA | de7274f081f381c8f8158605e0321c36c376e2e6 | b843ebf9b913146b38da2eaa7aeddf76074ae1ad |
| Selected tag | v6.0.1 | v6.1.0 |

## Aletheore/Aletheore

[Previous source](https://github.com/Aletheore/Aletheore/tree/50a3a3952892a6139b8eb799bca43b96d52097cc/) · [Current source](https://github.com/Aletheore/Aletheore/tree/c6a30932649c6d543123f67bd74b22803290156c/) · [Upstream code diff](https://github.com/Aletheore/Aletheore/compare/50a3a3952892a6139b8eb799bca43b96d52097cc...c6a30932649c6d543123f67bd74b22803290156c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 50a3a3952892a6139b8eb799bca43b96d52097cc | c6a30932649c6d543123f67bd74b22803290156c |
| Selected tag | v0.9.26 | v0.9.27 |

## ansible/ansible-lint

[Previous source](https://github.com/ansible/ansible-lint/tree/fac2489f3e4ccffa83a40b839770abbf4ab52327/) · [Current source](https://github.com/ansible/ansible-lint/tree/9bce2bfb8f4a984e6b13767bc0d6bf0a49492164/) · [Upstream code diff](https://github.com/ansible/ansible-lint/compare/fac2489f3e4ccffa83a40b839770abbf4ab52327...9bce2bfb8f4a984e6b13767bc0d6bf0a49492164)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | fac2489f3e4ccffa83a40b839770abbf4ab52327 | 9bce2bfb8f4a984e6b13767bc0d6bf0a49492164 |
| Selected tag | v26.10.0 | v26.10.1 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/1d6de8cb0c237e7c15e9e1bdf973826ebae490cc/) · [Current source](https://github.com/anthropics/claude-code-action/tree/a26b07d8c778b0c43f64618e5fd29fd0f8af72e8/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/1d6de8cb0c237e7c15e9e1bdf973826ebae490cc...a26b07d8c778b0c43f64618e5fd29fd0f8af72e8)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 1d6de8cb0c237e7c15e9e1bdf973826ebae490cc | a26b07d8c778b0c43f64618e5fd29fd0f8af72e8 |
| Selected tag | v1.0.248 | v1.0.250 |

## Burnett01/rsync-deployments

[Previous source](https://github.com/Burnett01/rsync-deployments/tree/155b6d6c1219ab2224c20c58d423a3f1b850395f/) · [Current source](https://github.com/Burnett01/rsync-deployments/tree/2cbb5ed94b73d111d07a40b071b1c7d3c0272435/) · [Upstream code diff](https://github.com/Burnett01/rsync-deployments/compare/155b6d6c1219ab2224c20c58d423a3f1b850395f...2cbb5ed94b73d111d07a40b071b1c7d3c0272435)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 155b6d6c1219ab2224c20c58d423a3f1b850395f | 2cbb5ed94b73d111d07a40b071b1c7d3c0272435 |
| Selected tag | 9.0.1 | 9.0.2 |

## cycjimmy/semantic-release-action

[Previous source](https://github.com/cycjimmy/semantic-release-action/tree/bda3da8d0cac44ed30fdc42bf9ad6a0362ce0583/) · [Current source](https://github.com/cycjimmy/semantic-release-action/tree/9e1f8a3ef91f1097285028e799a5fb8bb90e8899/) · [Upstream code diff](https://github.com/cycjimmy/semantic-release-action/compare/bda3da8d0cac44ed30fdc42bf9ad6a0362ce0583...9e1f8a3ef91f1097285028e799a5fb8bb90e8899)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | bda3da8d0cac44ed30fdc42bf9ad6a0362ce0583 | 9e1f8a3ef91f1097285028e799a5fb8bb90e8899 |
| Selected tag | v8.0.1 | v8.1.0 |

## davelosert/vitest-coverage-report-action

[Previous source](https://github.com/davelosert/vitest-coverage-report-action/tree/c4bbc33a89b7ace0e63d35f1f7d4bcee31155a73/) · [Current source](https://github.com/davelosert/vitest-coverage-report-action/tree/8f86cfb56ed6d5613ea8cdc5259f207fbfd51ece/) · [Upstream code diff](https://github.com/davelosert/vitest-coverage-report-action/compare/c4bbc33a89b7ace0e63d35f1f7d4bcee31155a73...8f86cfb56ed6d5613ea8cdc5259f207fbfd51ece)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | c4bbc33a89b7ace0e63d35f1f7d4bcee31155a73 | 8f86cfb56ed6d5613ea8cdc5259f207fbfd51ece |
| Selected tag | v2.13.0 | v2.13.1 |

## DeterminateSystems/determinate-nix-action

[Previous source](https://github.com/DeterminateSystems/determinate-nix-action/tree/d0c908e6cbe9f89f36ed8205a3ab6f092636916a/) · [Current source](https://github.com/DeterminateSystems/determinate-nix-action/tree/e847f25223456b3058e12f7fc9d777b6a6f25060/) · [Upstream code diff](https://github.com/DeterminateSystems/determinate-nix-action/compare/d0c908e6cbe9f89f36ed8205a3ab6f092636916a...e847f25223456b3058e12f7fc9d777b6a6f25060)

| Changed | Before | After |
| --- | --- | --- |
| Input: source-tag | {&quot;default&quot;: &quot;v3.23.1&quot;, &quot;description&quot;: &quot;The tag of \`nix-installer\` to use (conflicts with \`source-revision\`, \`source-branch\`, \`source-pr\`)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v3.23.2&quot;, &quot;description&quot;: &quot;The tag of \`nix-installer\` to use (conflicts with \`source-revision\`, \`source-branch\`, \`source-pr\`)&quot;, &quot;required&quot;: false} |
| Selected SHA | d0c908e6cbe9f89f36ed8205a3ab6f092636916a | e847f25223456b3058e12f7fc9d777b6a6f25060 |
| Selected tag | v3.23.1 | v3.23.2 |

## docker/bake-action

[Previous source](https://github.com/docker/bake-action/tree/018cb6412ab401ebaa809aa5f85966b74628600f/) · [Current source](https://github.com/docker/bake-action/tree/59cb1203cd42bcefd40a1b6d73b589e48c86040e/) · [Upstream code diff](https://github.com/docker/bake-action/compare/018cb6412ab401ebaa809aa5f85966b74628600f...59cb1203cd42bcefd40a1b6d73b589e48c86040e)

| Changed | Before | After |
| --- | --- | --- |
| Input: vars | {&quot;description&quot;: &quot;Variables to set in the Bake definition as list of key-value pair&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Variables to set in the Bake definition as a list of key-value pairs or a JSON array of strings&quot;, &quot;required&quot;: false} |
| Selected SHA | 018cb6412ab401ebaa809aa5f85966b74628600f | 59cb1203cd42bcefd40a1b6d73b589e48c86040e |
| Selected tag | v7.4.0 | v7.5.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/71777cd1994fa1bfd5f0ab90a57d36ac45f1e611/) · [Current source](https://github.com/duriantaco/skylos/tree/88078907963f76fe8971cbd69e4a4f6975d8a900/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/71777cd1994fa1bfd5f0ab90a57d36ac45f1e611...88078907963f76fe8971cbd69e4a4f6975d8a900)

| Changed | Before | After |
| --- | --- | --- |
| Input: max-comments | {&quot;default&quot;: &quot;15&quot;, &quot;description&quot;: &quot;Maximum inline PR review comments (default: 15)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;15&quot;, &quot;description&quot;: &quot;Maximum inline PR review comments per pull request (default: 15). Later pushes comment only on new findings and edit the one summary comment&quot;, &quot;required&quot;: false} |
| Selected SHA | 71777cd1994fa1bfd5f0ab90a57d36ac45f1e611 | 88078907963f76fe8971cbd69e4a4f6975d8a900 |
| Selected tag | v4.48.0 | v4.50.0 |

## jfrog/setup-jfrog-cli

[Previous source](https://github.com/jfrog/setup-jfrog-cli/tree/68c0efdc951dd2359bbbfa15c48bc67b3ae8e4d6/) · [Current source](https://github.com/jfrog/setup-jfrog-cli/tree/1e584506871998c267b7c100c02628a5b9c81db6/) · [Upstream code diff](https://github.com/jfrog/setup-jfrog-cli/compare/68c0efdc951dd2359bbbfa15c48bc67b3ae8e4d6...1e584506871998c267b7c100c02628a5b9c81db6)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;2.124.0&quot;, &quot;description&quot;: &quot;JFrog CLI Version. A concrete X.Y.Z is recommended when download-repository points to a remote repository that stores artifacts locally, since latest is requested as the v2/\[RELEASE\] path and can be served from cache.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;2.127.0&quot;, &quot;description&quot;: &quot;JFrog CLI Version. A concrete X.Y.Z is recommended when download-repository points to a remote repository that stores artifacts locally, since latest is requested as the v2/\[RELEASE\] path and can be served from cache.&quot;, &quot;required&quot;: false} |
| Selected SHA | 68c0efdc951dd2359bbbfa15c48bc67b3ae8e4d6 | 1e584506871998c267b7c100c02628a5b9c81db6 |
| Selected tag | v5.2.0 | v5.3.0 |

## jianruntech/geo-score

[Previous source](https://github.com/jianruntech/geo-score/tree/8059236e60deb9027b97b7ee630a469b43f958db/) · [Current source](https://github.com/jianruntech/geo-score/tree/65bf9ee68de92057393b434bd89df8a27e363148/) · [Upstream code diff](https://github.com/jianruntech/geo-score/compare/8059236e60deb9027b97b7ee630a469b43f958db...65bf9ee68de92057393b434bd89df8a27e363148)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 8059236e60deb9027b97b7ee630a469b43f958db | 65bf9ee68de92057393b434bd89df8a27e363148 |
| Selected tag | v1.8.2 | v1.8.3 |

## luckyPipewrench/pipelock

[Previous source](https://github.com/luckyPipewrench/pipelock/tree/3e868ac5d5b62d3a2790958542171143af8a0e38/) · [Current source](https://github.com/luckyPipewrench/pipelock/tree/47c14c59b14f835f53971d22941b556f44f2baa0/) · [Upstream code diff](https://github.com/luckyPipewrench/pipelock/compare/3e868ac5d5b62d3a2790958542171143af8a0e38...47c14c59b14f835f53971d22941b556f44f2baa0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3e868ac5d5b62d3a2790958542171143af8a0e38 | 47c14c59b14f835f53971d22941b556f44f2baa0 |
| Selected tag | v3.6.0 | v3.7.0 |

## nrwl/nx-set-shas

[Previous source](https://github.com/nrwl/nx-set-shas/tree/afb73a62d26e41464e9254689e1fd6122ee683c1/) · [Current source](https://github.com/nrwl/nx-set-shas/tree/e602fada7ad5987b0f7b1905e7a99ea1c661514c/) · [Upstream code diff](https://github.com/nrwl/nx-set-shas/compare/afb73a62d26e41464e9254689e1fd6122ee683c1...e602fada7ad5987b0f7b1905e7a99ea1c661514c)

| Changed | Before | After |
| --- | --- | --- |
| Input: lookup-strategy | null | {&quot;default&quot;: &quot;list&quot;, &quot;description&quot;: &quot;How to find the last successful workflow run. &#x27;list&#x27; lists the latest successful runs of the workflow and checks that their commit is among the latest 100 commits of the main branch. &#x27;per-commit&#x27; walks the first-parent git history before HEAD and queries the runs of each commit (by head SHA), using the first commit with a successful run&quot;} |
| Input: max-commits | null | {&quot;default&quot;: &quot;100&quot;, &quot;description&quot;: &quot;The maximum number of commits to check when &#x27;lookup-strategy&#x27; is &#x27;per-commit&#x27;&quot;} |
| Selected SHA | afb73a62d26e41464e9254689e1fd6122ee683c1 | e602fada7ad5987b0f7b1905e7a99ea1c661514c |
| Selected tag | v5.0.1 | v5.1.0 |

## prefix-dev/setup-pixi

[Previous source](https://github.com/prefix-dev/setup-pixi/tree/9dabb60412d3d2d967a8d682f7ce01317af40514/) · [Current source](https://github.com/prefix-dev/setup-pixi/tree/ad1da6449d9e506fd127fd67ab2d054a769f6a94/) · [Upstream code diff](https://github.com/prefix-dev/setup-pixi/compare/9dabb60412d3d2d967a8d682f7ce01317af40514...ad1da6449d9e506fd127fd67ab2d054a769f6a94)

| Changed | Before | After |
| --- | --- | --- |
| Input: auth-host | {&quot;description&quot;: &quot;Host to use for authentication. If not set, pixi is not authenticating.\\nRequires \`auth-token\` or \`auth-conda-token\` or \`auth-username\` and \`auth-password\` to be set.\\nSee https://pixi.prefix.dev/latest/deployment/authentication/\\n&quot;} | {&quot;description&quot;: &quot;Host to use for authentication. If not set, pixi is not authenticating.\\nRequires \`auth-token\`, \`auth-conda-token\`, \`auth-workload-identity\`, \`auth-s3-access-key-id\` and \`auth-s3-secret-access-key\`,\\nor \`auth-username\` and \`auth-password\` to be set.\\nSee https://pixi.prefix.dev/latest/deployment/authentication/\\n&quot;} |
| Input: auth-workload-identity | null | {&quot;description&quot;: &quot;Whether to log in non-interactively by exchanging the GitHub Actions OIDC ID token for an access token\\n(\`pixi auth login --workload-identity\`). Defaults to \`false\`. Requires \`auth-host\` and \`permissions: id-token: write\`.\\n&quot;} |
| Input: auth-workload-identity-audience | null | {&quot;description&quot;: &quot;Audience requested in the OIDC ID token. Defaults to the host, or \`prefix.dev\` for prefix.dev hosts.\\nRequires \`auth-workload-identity\`.\\n&quot;} |
| Input: auth-workload-identity-exchange | null | {&quot;description&quot;: &quot;How the server exchanges the ID token.\\nRequires \`auth-workload-identity\`.\\noptions: token-exchange, prefix\\n- \`token-exchange\`: OAuth 2.0 Token Exchange (RFC 8693) at \`auth-workload-identity-token-endpoint\`.\\n- \`prefix\`: prefix.dev&#x27;s mint endpoint.\\n&quot;} |
| Input: auth-workload-identity-token-endpoint | null | {&quot;description&quot;: &quot;Token endpoint for \`auth-workload-identity-exchange: token-exchange\`: a URL or a path on the host.\\nDefaults to the \`token\_endpoint\` from the host&#x27;s RFC 8414 metadata.\\nRequires \`auth-workload-identity\`.\\n&quot;} |
| Input: working-directory | {&quot;description&quot;: &quot;Working directory to use for pixi commands. If specified, pixi will look for manifest files (pixi.toml or pyproject.toml) \\nin this directory instead of the repository root. Useful for monorepos where pixi projects are in subdirectories.\\n&quot;} | {&quot;description&quot;: &quot;Working directory to use for pixi commands. If specified, pixi will look for manifest files (pixi.toml or pyproject.toml)\\nin this directory instead of the repository root. Useful for monorepos where pixi projects are in subdirectories.\\n&quot;} |
| Selected SHA | 9dabb60412d3d2d967a8d682f7ce01317af40514 | ad1da6449d9e506fd127fd67ab2d054a769f6a94 |
| Selected tag | v0.11.0 | v0.11.2 |

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/a8ac3eea598697a830f7d8e701fc9fcbfde88974/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/3cbf14efd750961dba35fccbf00f9e14028cb1f5/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/a8ac3eea598697a830f7d8e701fc9fcbfde88974...3cbf14efd750961dba35fccbf00f9e14028cb1f5)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a8ac3eea598697a830f7d8e701fc9fcbfde88974 | 3cbf14efd750961dba35fccbf00f9e14028cb1f5 |
| Selected tag | v1.80.0 | v1.80.2 |

## reviewdog/action-cpplint

[Previous source](https://github.com/reviewdog/action-cpplint/tree/5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d/) · [Current source](https://github.com/reviewdog/action-cpplint/tree/85949cd74d65e9f24a0410483991e50b7aefeb61/) · [Upstream code diff](https://github.com/reviewdog/action-cpplint/compare/5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d...85949cd74d65e9f24a0410483991e50b7aefeb61)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d | 85949cd74d65e9f24a0410483991e50b7aefeb61 |
| Selected tag | v1.12.0 | v1.13.0 |

## reviewdog/action-detect-secrets

[Previous source](https://github.com/reviewdog/action-detect-secrets/tree/53195a798553d71f8d0884ab7335aa5ac42e73e9/) · [Current source](https://github.com/reviewdog/action-detect-secrets/tree/8eeb4956ce5c9f4bebff8e21fd31066a9a011c4c/) · [Upstream code diff](https://github.com/reviewdog/action-detect-secrets/compare/53195a798553d71f8d0884ab7335aa5ac42e73e9...8eeb4956ce5c9f4bebff8e21fd31066a9a011c4c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 53195a798553d71f8d0884ab7335aa5ac42e73e9 | 8eeb4956ce5c9f4bebff8e21fd31066a9a011c4c |
| Selected tag | v0.31.1 | v0.31.2 |

## reviewdog/action-yamllint

[Previous source](https://github.com/reviewdog/action-yamllint/tree/5dd4640db975e4cac6f4e775a401695bafc28068/) · [Current source](https://github.com/reviewdog/action-yamllint/tree/3224b47de22a2fd9c8c0fbc120e6d0049d1f5060/) · [Upstream code diff](https://github.com/reviewdog/action-yamllint/compare/5dd4640db975e4cac6f4e775a401695bafc28068...3224b47de22a2fd9c8c0fbc120e6d0049d1f5060)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5dd4640db975e4cac6f4e775a401695bafc28068 | 3224b47de22a2fd9c8c0fbc120e6d0049d1f5060 |
| Selected tag | v1.25.1 | v1.25.2 |

## scalacenter/sbt-dependency-submission

[Previous source](https://github.com/scalacenter/sbt-dependency-submission) · [Current source](https://github.com/scalacenter/sbt-dependency-submission/tree/d84eef4c09e633bcf5f113bcad7fd5e9af1baee9/)

| Changed | Before | After |
| --- | --- | --- |
| Input: configs-ignore | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A list of space-separated names of configurations to ignore. The action will not submit the dependencies of these configurations.\\nExample: \`test scala-doc-tool\`\\n&quot;, &quot;required&quot;: false} |
| Input: correlator | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;An optional identifier to distinguish between multiple dependency snapshots of the same type.\\nDefaults to the concatenation of the workflow name, the job id and the action id.\\n&quot;, &quot;required&quot;: false} |
| Input: modules-ignore | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A list of space-separated names of modules to ignore. The action will not resolve nor submit the dependencies of these modules.\\nThe name of a module contains the name of the project and its binary version.\\nExample: \`foo\_2.13 bar\_2.13\`\\n&quot;, &quot;required&quot;: false} |
| Input: on-resolve-failure | null | {&quot;default&quot;: &quot;error&quot;, &quot;description&quot;: &quot;Either &#x27;error&#x27; or &#x27;warning&#x27;.\\nWhen a dependency resolution failure happens, if &#x27;error&#x27; the job will fail and will not submit the snapshot.\\nIf &#x27;warning&#x27;, the job will ignore the failing modules and submit the snapshot.\\n&quot;, &quot;required&quot;: false} |
| Input: sbt-plugin-version | null | {&quot;default&quot;: &quot;3.2.2&quot;, &quot;description&quot;: &quot;Version of the sbt plugin to use.&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;GitHub Personal Access Token (PAT). Defaults to PAT provided by Action runner.&quot;, &quot;required&quot;: false} |
| Input: working-directory | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;The relative path of the working directory of the sbt build.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;snapshot-json-path&quot;, &quot;submission-api-url&quot;, &quot;submission-id&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | d84eef4c09e633bcf5f113bcad7fd5e9af1baee9 |
| Selected tag | null | v3.2.3 |

## streetsidesoftware/cspell-action

[Previous source](https://github.com/streetsidesoftware/cspell-action/tree/6f3c77c1406bc930f944ba97e9801a22e42caf58/) · [Current source](https://github.com/streetsidesoftware/cspell-action/tree/ce1816e4ce36532956ac6e983737392774b6e169/) · [Upstream code diff](https://github.com/streetsidesoftware/cspell-action/compare/6f3c77c1406bc930f944ba97e9801a22e42caf58...ce1816e4ce36532956ac6e983737392774b6e169)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6f3c77c1406bc930f944ba97e9801a22e42caf58 | ce1816e4ce36532956ac6e983737392774b6e169 |
| Selected tag | v9.1.0 | v9.2.0 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/460732eb877ccc9ea5bd778d876667774ce51ff8/) · [Current source](https://github.com/tmatens/compose-lint/tree/3612161d5d32822b54067595ae4fe4b4e408837b/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/460732eb877ccc9ea5bd778d876667774ce51ff8...3612161d5d32822b54067595ae4fe4b4e408837b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 460732eb877ccc9ea5bd778d876667774ce51ff8 | 3612161d5d32822b54067595ae4fe4b4e408837b |
| Selected tag | v0.34.1 | v0.35.0 |

## UiPath/coder\_eval

[Previous source](https://github.com/UiPath/coder_eval/tree/1770360190187638f3b5b4a06503f0e2a28adf4b/) · [Current source](https://github.com/UiPath/coder_eval/tree/3ffb2efdb712f1d8548bbf990e51d0555ce6a8b1/) · [Upstream code diff](https://github.com/UiPath/coder_eval/compare/1770360190187638f3b5b4a06503f0e2a28adf4b...3ffb2efdb712f1d8548bbf990e51d0555ce6a8b1)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.12.12&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.12.13&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} |
| Selected SHA | 1770360190187638f3b5b4a06503f0e2a28adf4b | 3ffb2efdb712f1d8548bbf990e51d0555ce6a8b1 |
| Selected tag | v0.12.12 | v0.12.13 |

## warpdotdev/oz-agent-action

[Previous source](https://github.com/warpdotdev/oz-agent-action/tree/ccb5247d8faee3d0a4b70b8a776727c8f52e2355/) · [Current source](https://github.com/warpdotdev/oz-agent-action/tree/8025b8045e60b8733022456300c304a2ed8a3764/) · [Upstream code diff](https://github.com/warpdotdev/oz-agent-action/compare/ccb5247d8faee3d0a4b70b8a776727c8f52e2355...8025b8045e60b8733022456300c304a2ed8a3764)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ccb5247d8faee3d0a4b70b8a776727c8f52e2355 | 8025b8045e60b8733022456300c304a2ed8a3764 |
| Selected tag | v1.0.36 | v1.0.37 |
