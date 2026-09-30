# Latest catalog changes

16 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## Aletheore/Aletheore

[Previous source](https://github.com/Aletheore/Aletheore/tree/e1eb71895c7ce2a01df7be98a1ac41ef70656884/) · [Current source](https://github.com/Aletheore/Aletheore/tree/58525fda08ab3f6a8c385022293c90070bd6dd42/) · [Upstream code diff](https://github.com/Aletheore/Aletheore/compare/e1eb71895c7ce2a01df7be98a1ac41ef70656884...58525fda08ab3f6a8c385022293c90070bd6dd42)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e1eb71895c7ce2a01df7be98a1ac41ef70656884 | 58525fda08ab3f6a8c385022293c90070bd6dd42 |
| Selected tag | v0.9.18 | v0.9.19 |

## ansible/ansible-lint

[Previous source](https://github.com/ansible/ansible-lint/tree/665d9e07a1943254d2910faffc106adaf7ea7294/) · [Current source](https://github.com/ansible/ansible-lint/tree/e7f397ad6dfa20d274afa17cd7bbedd84ed136f5/) · [Upstream code diff](https://github.com/ansible/ansible-lint/compare/665d9e07a1943254d2910faffc106adaf7ea7294...e7f397ad6dfa20d274afa17cd7bbedd84ed136f5)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 665d9e07a1943254d2910faffc106adaf7ea7294 | e7f397ad6dfa20d274afa17cd7bbedd84ed136f5 |
| Selected tag | v26.8.0 | v26.9.0 |

## bufbuild/buf-action

[Previous source](https://github.com/bufbuild/buf-action/tree/8c6a16e16f12ba20b6470afa9c2ba9b5ba8c97c3/) · [Current source](https://github.com/bufbuild/buf-action/tree/85aebf73123b5c15fd5528aaecbf9129cddf7fa7/) · [Upstream code diff](https://github.com/bufbuild/buf-action/compare/8c6a16e16f12ba20b6470afa9c2ba9b5ba8c97c3...85aebf73123b5c15fd5528aaecbf9129cddf7fa7)

| Changed | Before | After |
| --- | --- | --- |
| Input: archive | {&quot;default&quot;: &quot;${{ github.event\_name == &#x27;delete&#x27; }}&quot;, &quot;description&quot;: &quot;Whether to run the archive step. Runs by default on deletes, for non forked repositories.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;${{ github.event\_name == &#x27;delete&#x27; &amp;&amp; !github.event.repository.fork }}&quot;, &quot;description&quot;: &quot;Whether to run the archive step. Runs by default on deletes, for non forked repositories.&quot;, &quot;required&quot;: false} |
| Input: bot\_username | null | {&quot;description&quot;: &quot;Username of the bot user to authenticate as with workload identity\\nfederation, instead of a static API token.\\nRequires \\&quot;permissions: id-token: write\\&quot; on the job, and a trust\\ncredential configured on the bot user.\\nSee: https://buf.build/docs/bsr/authentication&quot;, &quot;required&quot;: false} |
| Input: push | {&quot;default&quot;: &quot;${{ github.event\_name == &#x27;push&#x27; }}&quot;, &quot;description&quot;: &quot;Whether to run the push step. Runs by default on pushes, for non forked repositories.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;${{ github.event\_name == &#x27;push&#x27; &amp;&amp; !github.event.repository.fork }}&quot;, &quot;description&quot;: &quot;Whether to run the push step. Runs by default on pushes, for non forked repositories.&quot;, &quot;required&quot;: false} |
| Input: token | {&quot;description&quot;: &quot;API token for logging into the BSR.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;API token for logging into the BSR.\\nIf not set, \\&quot;bot\_username\\&quot; is used to mint a short-lived token with\\nworkload identity federation.\\nSee: https://buf.build/docs/bsr/authentication&quot;, &quot;required&quot;: false} |
| Input: version | {&quot;description&quot;: &quot;Version of the Buf CLI to use.\\nExample:\\n  with:\\n    version: 1.50.1&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Version of the Buf CLI to use.\\nExample:\\n  with:\\n    version: 1.73.0&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;buf\_path&quot;, &quot;buf\_version&quot;\] | \[&quot;buf\_path&quot;, &quot;buf\_version&quot;, &quot;token&quot;\] |
| Selected SHA | 8c6a16e16f12ba20b6470afa9c2ba9b5ba8c97c3 | 85aebf73123b5c15fd5528aaecbf9129cddf7fa7 |
| Selected tag | v1.5.0 | v1.6.0 |

## cloudflare/wrangler-action

[Previous source](https://github.com/cloudflare/wrangler-action/tree/ebbaa1584979971c8614a24965b4405ff95890e0/) · [Current source](https://github.com/cloudflare/wrangler-action/tree/4e88846969242f7752bcfdaf5511bfbb3985ca47/) · [Upstream code diff](https://github.com/cloudflare/wrangler-action/compare/ebbaa1584979971c8614a24965b4405ff95890e0...4e88846969242f7752bcfdaf5511bfbb3985ca47)

| Changed | Before | After |
| --- | --- | --- |
| Input: command | {&quot;description&quot;: &quot;The Wrangler command (along with any arguments) you wish to run. Multiple Wrangler commands can be run by separating each command with a newline. Defaults to \`\\&quot;deploy\\&quot;\`.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The Wrangler command (along with any arguments) you wish to run. Multiple Wrangler commands can be run by separating each command with a newline. Defaults to \`\\&quot;deploy\\&quot;\`. The \`preview\` command requires Wrangler &gt;= 4.136.0.&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;command-output&quot;, &quot;command-stderr&quot;, &quot;deployment-url&quot;, &quot;pages-deployment-alias-url&quot;, &quot;pages-deployment-id&quot;, &quot;pages-environment&quot;\] | \[&quot;command-output&quot;, &quot;command-stderr&quot;, &quot;deployment-url&quot;, &quot;pages-deployment-alias-url&quot;, &quot;pages-deployment-id&quot;, &quot;pages-environment&quot;, &quot;preview-deployment-id&quot;, &quot;preview-deployment-url&quot;, &quot;preview-id&quot;, &quot;preview-name&quot;, &quot;preview-url&quot;\] |
| Selected SHA | ebbaa1584979971c8614a24965b4405ff95890e0 | 4e88846969242f7752bcfdaf5511bfbb3985ca47 |
| Selected tag | v4.0.0 | v4.1.1 |

## cncf/prow-github-actions

[Previous source](https://github.com/cncf/prow-github-actions/tree/c44ac3a57d67639e39e4a4988b52049ef45b80dd/) · [Current source](https://github.com/cncf/prow-github-actions/tree/582d83b8c37fd9a48f67d65d24fb1f37ce2030eb/) · [Upstream code diff](https://github.com/cncf/prow-github-actions/compare/c44ac3a57d67639e39e4a4988b52049ef45b80dd...582d83b8c37fd9a48f67d65d24fb1f37ce2030eb)

| Changed | Before | After |
| --- | --- | --- |
| Input: cat-api-key | null | {&quot;description&quot;: &quot;Optional API key for the /meow image provider (https://thecatapi.com), sent as the x-api-key header. Provide it from a repository secret. The action registers it for runner masking before use and never intentionally includes it in request URLs or GitHub comments.&quot;, &quot;required&quot;: false} |
| Input: config | null | {&quot;description&quot;: &quot;Optional explicit source of the shared prow configuration, replacing the organization&#x27;s .project/.github lookup: &#x27;owner/repo:path\[@ref\]&#x27; (read with github-token) or an &#x27;https://&#x27; url (fetched anonymously). The repository&#x27;s own prow.yaml or .prowlabels.yaml is still layered on top.&quot;, &quot;required&quot;: false} |
| Input: dry-run | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;When &#x27;true&#x27;, the label-sync job logs the labels it would create or update and writes nothing. Defaults to &#x27;false&#x27;.&quot;, &quot;required&quot;: false} |
| Input: jobs | {&quot;description&quot;: &quot;The jobs to automatically run on event. Space delimited. Expect commands on own line.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;The jobs to run for schedule, workflow\_dispatch, push and pull\_request events. Space or newline delimited: &#x27;lgtm&#x27; (merge lgtm PRs on a schedule, remove lgtm on pull\_request), &#x27;sweep&#x27; (evaluate the pull requests updated within sweep.lookback on a schedule, for fork pull requests under pull\_request), &#x27;label-sync&#x27; (create and update the repository labels from the prow configuration; never deletes).&quot;, &quot;required&quot;: false} |
| Input: merge-method | {&quot;description&quot;: &quot;Strategy for Prow-github-actions to take when merging a pull request using the lgtm cron-job. Can be &#x27;squash&#x27;, &#x27;rebase&#x27;, or &#x27;merge&#x27;. Defaults to &#x27;merge&#x27;&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Strategy for Prow-github-actions to take when merging a pull request, on events and in the lgtm cron-job. Can be &#x27;squash&#x27;, &#x27;rebase&#x27;, or &#x27;merge&#x27;. Defaults to &#x27;merge&#x27;. A tide.merge\_method in the prow configuration wins over this input.&quot;, &quot;required&quot;: false} |
| Input: prow-commands | {&quot;description&quot;: &quot;Comment keywords/commands to look for. Space delimited. Expect commands on own line.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Comment keywords/commands to look for. Space delimited. Expect commands on own line. Prow-style aliases (e.g. /unhold, /remove-lgtm) are enabled with their base command, and listing an alias enables the whole command family (e.g. /remove-kind also enables /kind).&quot;, &quot;required&quot;: false} |
| Runtime | node20 | node24 |
| Selected SHA | c44ac3a57d67639e39e4a4988b52049ef45b80dd | 582d83b8c37fd9a48f67d65d24fb1f37ce2030eb |
| Selected tag | v2.0.0 | v3.0.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/d8288c5837793e2c51be869714573ebb7f2a044d/) · [Current source](https://github.com/duriantaco/skylos/tree/ba4c85f963e56053684f1a7eb3d8fc7aa09e8458/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/d8288c5837793e2c51be869714573ebb7f2a044d...ba4c85f963e56053684f1a7eb3d8fc7aa09e8458)

| Changed | Before | After |
| --- | --- | --- |
| Description | SAST, dead code detection, secrets scanning, and PR gating for Python, TypeScript, Java, and Go. | SAST, dead code, secrets, PR gates, and digest-pinned container image vulnerability scans. |
| Input: image | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional repository@sha256:digest to scan instead of source code; requires an installed Trivy&quot;, &quot;required&quot;: false} |
| Input: image-fail-on | null | {&quot;default&quot;: &quot;high&quot;, &quot;description&quot;: &quot;Image severity threshold for mode gate: low, medium, high, or critical&quot;, &quot;required&quot;: false} |
| Input: image-platform | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Required with image: deployment os/architecture\[/variant\], for example linux/amd64&quot;, &quot;required&quot;: false} |
| Input: mode | {&quot;default&quot;: &quot;gate&quot;, &quot;description&quot;: &quot;Scan mode: &#x27;scan&#x27; (report only), &#x27;gate&#x27; (fail on issues), &#x27;review&#x27; (PR comments + gate)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;gate&quot;, &quot;description&quot;: &quot;Scan mode: &#x27;scan&#x27; (report only), &#x27;gate&#x27; (fail on issues), or source-only &#x27;review&#x27; (PR comments + gate)&quot;, &quot;required&quot;: false} |
| Selected SHA | d8288c5837793e2c51be869714573ebb7f2a044d | ba4c85f963e56053684f1a7eb3d8fc7aa09e8458 |
| Selected tag | v4.38.0 | v4.39.0 |

## grafana/run-k6-action

[Previous source](https://github.com/grafana/run-k6-action/tree/de51a7390bdf0ac85a3bef493691bd71d4c7c158/) · [Current source](https://github.com/grafana/run-k6-action/tree/4082a08c7e40cf6d65863911077dfb60ae0a4f04/) · [Upstream code diff](https://github.com/grafana/run-k6-action/compare/de51a7390bdf0ac85a3bef493691bd71d4c7c158...4082a08c7e40cf6d65863911077dfb60ae0a4f04)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | de51a7390bdf0ac85a3bef493691bd71d4c7c158 | 4082a08c7e40cf6d65863911077dfb60ae0a4f04 |
| Selected tag | v1.4.0 | v1.5.0 |

## grafana/setup-k6-action

[Previous source](https://github.com/grafana/setup-k6-action/tree/db07bd9765aac508ef18982e52ab937fe633a065/) · [Current source](https://github.com/grafana/setup-k6-action/tree/43b9fc21641a76002687994433dd586f56e791b1/) · [Upstream code diff](https://github.com/grafana/setup-k6-action/compare/db07bd9765aac508ef18982e52ab937fe633a065...43b9fc21641a76002687994433dd586f56e791b1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | db07bd9765aac508ef18982e52ab937fe633a065 | 43b9fc21641a76002687994433dd586f56e791b1 |
| Selected tag | v1.2.1 | v1.2.2 |

## owenthereal/action-upterm

[Previous source](https://github.com/owenthereal/action-upterm) · [Current source](https://github.com/owenthereal/action-upterm/tree/42902ffb5244d6d63501c1daf4f4ec82884025f6/)

| Changed | Before | After |
| --- | --- | --- |
| Input: detached | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;In detached mode, the workflow job will continue while the upterm session is active&quot;, &quot;required&quot;: false} |
| Input: limit-access-to-actor | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If only the public SSH keys of the user triggering the workflow should be authorized&quot;, &quot;required&quot;: false} |
| Input: limit-access-to-users | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If only the public SSH keys of the listed GitHub users should be authorized&quot;, &quot;required&quot;: false} |
| Input: upterm-server | null | {&quot;default&quot;: &quot;ssh://uptermd.upterm.dev:22&quot;, &quot;description&quot;: &quot;upterm server address (required), supported protocols are ssh, ws, or wss.&quot;, &quot;required&quot;: true} |
| Input: upterm-version | null | {&quot;description&quot;: &quot;Upterm version/tag to install (e.g., v0.30.0). Requires v0.30.0 or newer. Defaults to latest when unset.&quot;, &quot;required&quot;: false} |
| Input: wait-timeout-minutes | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Integer number of minutes to wait for user to connect before shutting down server. In detached mode, the countdown starts after all regular steps finish. Once a user connects, the server will stay up.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;ssh-command&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 42902ffb5244d6d63501c1daf4f4ec82884025f6 |
| Selected tag | null | v1.16.0 |

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/5be522b94290e249dba9f5daded2f7157733e3d2/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/2085657ab2c7f48c58edcc767fba576f63bea76b/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/5be522b94290e249dba9f5daded2f7157733e3d2...2085657ab2c7f48c58edcc767fba576f63bea76b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5be522b94290e249dba9f5daded2f7157733e3d2 | 2085657ab2c7f48c58edcc767fba576f63bea76b |
| Selected tag | v1.76.1 | v1.77.0 |

## sbt/setup-sbt

[Previous source](https://github.com/sbt/setup-sbt/tree/82da71df4e122282484a99a8d70096bc2369dbd8/) · [Current source](https://github.com/sbt/setup-sbt/tree/ce95da69b39609ea153bad087708da5f37366897/) · [Upstream code diff](https://github.com/sbt/setup-sbt/compare/82da71df4e122282484a99a8d70096bc2369dbd8...ce95da69b39609ea153bad087708da5f37366897)

| Changed | Before | After |
| --- | --- | --- |
| Input: sbt-runner-version | {&quot;default&quot;: &quot;2.0.8&quot;, &quot;description&quot;: &quot;The runner version (The actual version is controlled via project/build.properties)&quot;, &quot;required&quot;: true} | {&quot;default&quot;: &quot;2.0.9&quot;, &quot;description&quot;: &quot;The runner version (The actual version is controlled via project/build.properties)&quot;, &quot;required&quot;: true} |
| Selected SHA | 82da71df4e122282484a99a8d70096bc2369dbd8 | ce95da69b39609ea153bad087708da5f37366897 |
| Selected tag | v1.5.9 | v1.5.10 |

## Songmu/tagpr

[Previous source](https://github.com/Songmu/tagpr/tree/7ebae2dcc300132baa7cc9dd108c8923b07fc366/) · [Current source](https://github.com/Songmu/tagpr/tree/2afc990a4a5a9a340665cc1a484c2102f7de332f/) · [Upstream code diff](https://github.com/Songmu/tagpr/compare/7ebae2dcc300132baa7cc9dd108c8923b07fc366...2afc990a4a5a9a340665cc1a484c2102f7de332f)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;v1.20.3&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v1.21.0&quot;, &quot;description&quot;: &quot;A version to install tagpr&quot;, &quot;required&quot;: false} |
| Selected SHA | 7ebae2dcc300132baa7cc9dd108c8923b07fc366 | 2afc990a4a5a9a340665cc1a484c2102f7de332f |
| Selected tag | v1.20.3 | v1.21.0 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/94c31af3204a9f15ab40b35ad084410b905bbc73/) · [Current source](https://github.com/taiki-e/install-action/tree/7623a79cdfecb99d681017af368ca353d9f49bb5/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/94c31af3204a9f15ab40b35ad084410b905bbc73...7623a79cdfecb99d681017af368ca353d9f49bb5)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 94c31af3204a9f15ab40b35ad084410b905bbc73 | 7623a79cdfecb99d681017af368ca353d9f49bb5 |
| Selected tag | v2.87.17 | v2.87.19 |

## tailscale/github-action

[Previous source](https://github.com/tailscale/github-action/tree/780049a30b6ff5c378a9e7b389d15ece7a204888/) · [Current source](https://github.com/tailscale/github-action/tree/d1b6cd204f8dceda5b3eaad7f1f767be390056cd/) · [Upstream code diff](https://github.com/tailscale/github-action/compare/780049a30b6ff5c378a9e7b389d15ece7a204888...d1b6cd204f8dceda5b3eaad7f1f767be390056cd)

| Changed | Before | After |
| --- | --- | --- |
| Input: log-mode | null | {&quot;default&quot;: &quot;grouped&quot;, &quot;description&quot;: &quot;Controls action log output mode. Use \`grouped\` to fold major setup and cleanup phases, \`normal\` for ungrouped logs, or \`quiet\` to suppress routine informational output.&quot;, &quot;required&quot;: false} |
| Selected SHA | 780049a30b6ff5c378a9e7b389d15ece7a204888 | d1b6cd204f8dceda5b3eaad7f1f767be390056cd |
| Selected tag | v4.1.3 | v4.2.0 |

## ThreeMoonsLab/agents-shipgate

[Previous source](https://github.com/ThreeMoonsLab/agents-shipgate/tree/bace7c1871834e0b3eb98e6f60c0627725c53a59/) · [Current source](https://github.com/ThreeMoonsLab/agents-shipgate/tree/e3c6cb0c7657d9c53d4e29b2061d04dcf99a4e9b/) · [Upstream code diff](https://github.com/ThreeMoonsLab/agents-shipgate/compare/bace7c1871834e0b3eb98e6f60c0627725c53a59...e3c6cb0c7657d9c53d4e29b2061d04dcf99a4e9b)

| Changed | Before | After |
| --- | --- | --- |
| Input: output\_dir | {&quot;default&quot;: &quot;agents-shipgate-reports&quot;, &quot;description&quot;: &quot;Output directory for reports.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;agents-shipgate-reports&quot;, &quot;description&quot;: &quot;Output directory for reports. verify refuses (exit 2) a directory inside the repository that holds committed files or unignored files other than Shipgate artifacts, or that lies in a trust root Git does not ignore.&quot;, &quot;required&quot;: false} |
| Selected SHA | bace7c1871834e0b3eb98e6f60c0627725c53a59 | e3c6cb0c7657d9c53d4e29b2061d04dcf99a4e9b |
| Selected tag | v1.0.0 | v1.1.0 |

## UiPath/coder\_eval

[Previous source](https://github.com/UiPath/coder_eval/tree/d960de1c433a1b050d2509f04d94a60e3cabaaf0/) · [Current source](https://github.com/UiPath/coder_eval/tree/fdb3bc1e33edc1f5c044c9202548f38e4b9ae4f4/) · [Upstream code diff](https://github.com/UiPath/coder_eval/compare/d960de1c433a1b050d2509f04d94a60e3cabaaf0...fdb3bc1e33edc1f5c044c9202548f38e4b9ae4f4)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.12.4&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.12.5&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} |
| Selected SHA | d960de1c433a1b050d2509f04d94a60e3cabaaf0 | fdb3bc1e33edc1f5c044c9202548f38e4b9ae4f4 |
| Selected tag | v0.12.4 | v0.12.5 |
