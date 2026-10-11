# Latest catalog changes

11 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/ed670b4cf9de2a5a570d130d2f6197b9e543cd64/) · [Current source](https://github.com/anthropics/claude-code-action/tree/cab360f6565aa35a51d6ce9e43f1f4287c0a32ea/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/ed670b4cf9de2a5a570d130d2f6197b9e543cd64...cab360f6565aa35a51d6ce9e43f1f4287c0a32ea)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ed670b4cf9de2a5a570d130d2f6197b9e543cd64 | cab360f6565aa35a51d6ce9e43f1f4287c0a32ea |
| Selected tag | v1.0.240 | v1.0.241 |

## arduino/setup-task

[Previous source](https://github.com/arduino/setup-task) · [Current source](https://github.com/arduino/setup-task/tree/c0bc642852239c2689f73f4ea6459c29405f3c52/)

| Changed | Before | After |
| --- | --- | --- |
| Input: repo-token | null | {&quot;description&quot;: &quot;Token with permissions to do repo things&quot;, &quot;required&quot;: false} |
| Input: version | null | {&quot;default&quot;: &quot;3.x&quot;, &quot;description&quot;: &quot;Version to use. Example: 3.4.2&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | c0bc642852239c2689f73f4ea6459c29405f3c52 |
| Selected tag | null | v3.0.0 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43/) · [Current source](https://github.com/asklokesh/loki-mode/tree/1dda5ccec5b833b5b445478790dbc899cf7c5383/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43...1dda5ccec5b833b5b445478790dbc899cf7c5383)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43 | 1dda5ccec5b833b5b445478790dbc899cf7c5383 |
| Selected tag | v10.6.11 | v11.0.1 |

## dorny/test-reporter

[Previous source](https://github.com/dorny/test-reporter/tree/a43b3a5f7366b97d083190328d2c652e1a8b6aa2/) · [Current source](https://github.com/dorny/test-reporter/tree/d1b5dff021aa968b288b02285a8bf47471c5928a/) · [Upstream code diff](https://github.com/dorny/test-reporter/compare/a43b3a5f7366b97d083190328d2c652e1a8b6aa2...d1b5dff021aa968b288b02285a8bf47471c5928a)

| Changed | Before | After |
| --- | --- | --- |
| Input: list-files | null | {&quot;default&quot;: &quot;all&quot;, &quot;description&quot;: &quot;Limits which test result files are listed. Supported options:\\n  - all\\n  - failed\\n  - none\\n&quot;, &quot;required&quot;: false} |
| Input: reporter | {&quot;description&quot;: &quot;Format of test results. Supported options:\\n  - dart-json\\n  - dotnet-nunit\\n  - dotnet-trx\\n  - flutter-json\\n  - golang-json\\n  - java-junit\\n  - jest-junit\\n  - mocha-json\\n  - tester-junit\\n  - phpunit-junit\\n  - python-xunit\\n  - rspec-json\\n  - swift-xunit\\n&quot;, &quot;required&quot;: true} | {&quot;description&quot;: &quot;Format of test results. Supported options:\\n  - dart-json\\n  - dotnet-nunit\\n  - dotnet-trx\\n  - flutter-json\\n  - golang-json\\n  - java-junit\\n  - jest-junit\\n  - mocha-json\\n  - tester-junit\\n  - phpunit-junit\\n  - python-xunit\\n  - rspec-json\\n  - swift-xunit\\n  - unreal-json\\n&quot;, &quot;required&quot;: true} |
| Outputs | \[&quot;conclusion&quot;, &quot;failed&quot;, &quot;passed&quot;, &quot;skipped&quot;, &quot;slug\_prefix&quot;, &quot;time&quot;, &quot;url&quot;, &quot;url\_html&quot;\] | \[&quot;conclusion&quot;, &quot;failed&quot;, &quot;passed&quot;, &quot;skipped&quot;, &quot;slug\_prefix&quot;, &quot;summary\_file&quot;, &quot;time&quot;, &quot;url&quot;, &quot;url\_html&quot;\] |
| Selected SHA | a43b3a5f7366b97d083190328d2c652e1a8b6aa2 | d1b5dff021aa968b288b02285a8bf47471c5928a |
| Selected tag | v3.0.0 | v3.2.0 |

## futureware-tech/simulator-action

[Previous source](https://github.com/futureware-tech/simulator-action/tree/e89aa8f93d3aec35083ff49d2854d07f7186f7f5/) · [Current source](https://github.com/futureware-tech/simulator-action/tree/c768f52966d5f70335ec77881f9806b24a52f80e/) · [Upstream code diff](https://github.com/futureware-tech/simulator-action/compare/e89aa8f93d3aec35083ff49d2854d07f7186f7f5...c768f52966d5f70335ec77881f9806b24a52f80e)

| Changed | Before | After |
| --- | --- | --- |
| Input: model | {&quot;description&quot;: &quot;Simulator device model name (e.g. &#x27;iPhone 8&#x27; )&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Simulator device model name (e.g. &#x27;iPhone 16&#x27;)&quot;, &quot;required&quot;: false} |
| Input: os\_version | {&quot;description&quot;: &quot;OS version requirement in semver format (e.g. &#x27;^14.4&#x27;)&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;OS version requirement in semver format (e.g. &#x27;^18.0&#x27;)&quot;, &quot;required&quot;: false} |
| Input: settle\_check\_interval\_seconds | null | {&quot;default&quot;: &quot;2&quot;, &quot;description&quot;: &quot;Number of seconds between checks of the Simulator&#x27;s background CPU usage. Only relevant when settle\_timeout\_seconds is set to a positive value.\\n&quot;, &quot;required&quot;: false} |
| Input: settle\_consecutive\_samples | null | {&quot;default&quot;: &quot;3&quot;, &quot;description&quot;: &quot;Number of consecutive checks below settle\_cpu\_threshold\_percent required before the Simulator is considered settled. Only relevant when settle\_timeout\_seconds is set to a positive value.\\n&quot;, &quot;required&quot;: false} |
| Input: settle\_cpu\_threshold\_percent | null | {&quot;default&quot;: &quot;20&quot;, &quot;description&quot;: &quot;Aggregate %CPU (summed across all direct children of launchd\_sim) below which the Simulator is considered settled. Only relevant when settle\_timeout\_seconds is set to a positive value.\\n&quot;, &quot;required&quot;: false} |
| Input: settle\_timeout\_seconds | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Maximum number of seconds to wait, after boot, for the Simulator&#x27;s background CPU usage (daemons spawned by launchd\_sim) to settle down before continuing. Leave unset (default) to skip this check entirely, preserving prior behavior. Set to 0 to skip it explicitly. If the Simulator hasn&#x27;t settled within this time, a warning is logged and the action continues without failing the job.\\n&quot;, &quot;required&quot;: false} |
| Runtime | node20 | node24 |
| Selected SHA | e89aa8f93d3aec35083ff49d2854d07f7186f7f5 | c768f52966d5f70335ec77881f9806b24a52f80e |
| Selected tag | v5 | v6 |

## int128/datadog-actions-metrics

[Previous source](https://github.com/int128/datadog-actions-metrics/tree/de8c8077e77fb52a7eb2e535c42a22b623034724/) · [Current source](https://github.com/int128/datadog-actions-metrics/tree/453ea18176f0469f6c9ee6e65a3818a866b82bf1/) · [Upstream code diff](https://github.com/int128/datadog-actions-metrics/compare/de8c8077e77fb52a7eb2e535c42a22b623034724...453ea18176f0469f6c9ee6e65a3818a866b82bf1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | de8c8077e77fb52a7eb2e535c42a22b623034724 | 453ea18176f0469f6c9ee6e65a3818a866b82bf1 |
| Selected tag | v1.184.0 | v1.186.0 |

## int128/docker-manifest-create-action

[Previous source](https://github.com/int128/docker-manifest-create-action/tree/6edb43463bd4878b8cee224ca274378a3635d78f/) · [Current source](https://github.com/int128/docker-manifest-create-action/tree/a118e9fe12455375d4810aa318c20e6dba77288e/) · [Upstream code diff](https://github.com/int128/docker-manifest-create-action/compare/6edb43463bd4878b8cee224ca274378a3635d78f...a118e9fe12455375d4810aa318c20e6dba77288e)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6edb43463bd4878b8cee224ca274378a3635d78f | a118e9fe12455375d4810aa318c20e6dba77288e |
| Selected tag | v2.28.0 | v2.29.0 |

## jdx/mise-action

[Previous source](https://github.com/jdx/mise-action/tree/7a4e45a543138629540c9a1616d08632b893e492/) · [Current source](https://github.com/jdx/mise-action/tree/94c60b39bc2d90ab2f9bab27f38d3cc4812c1834/) · [Upstream code diff](https://github.com/jdx/mise-action/compare/7a4e45a543138629540c9a1616d08632b893e492...94c60b39bc2d90ab2f9bab27f38d3cc4812c1834)

| Changed | Before | After |
| --- | --- | --- |
| Input: auto\_update | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;When \`version\` is unset, reinstall a cached mise if a newer release is available. By default a cached mise is kept until the cache key changes.&quot;, &quot;required&quot;: false} |
| Input: cache\_save\_post | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;if true, save the cache in the post step instead of right after install, so tools installed by later steps (e.g. monorepo sub-projects or task tools) are included. Only applies on a cache miss. The post step runs even if a later step fails, as the immediate save would have.&quot;, &quot;required&quot;: false} |
| Input: plugins | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Plugins to install before tools, one per line as \`name\` or \`name url\`, e.g. \`yarn\` or \`php https://github.com/verzly/mise-php#latest\`. Useful for idiomatic version files (such as .yvmrc) that need a plugin.&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;cache-hit&quot;\] | \[&quot;cache-hit&quot;, &quot;versions&quot;\] |
| Selected SHA | 7a4e45a543138629540c9a1616d08632b893e492 | 94c60b39bc2d90ab2f9bab27f38d3cc4812c1834 |
| Selected tag | v5.0.1 | v5.1.0 |

## kerlenton/mcpsnoop

[Previous source](https://github.com/kerlenton/mcpsnoop/tree/5518964384cd855d3f43a58eace033e75dc222ff/) · [Current source](https://github.com/kerlenton/mcpsnoop/tree/ab20b0ebbad9f76de884dfd980e8f5ae6c142433/) · [Upstream code diff](https://github.com/kerlenton/mcpsnoop/compare/5518964384cd855d3f43a58eace033e75dc222ff...ab20b0ebbad9f76de884dfd980e8f5ae6c142433)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Which mcpsnoop to install, for example v0.21.0. Defaults to the release you\\npinned the action to, so normally there is nothing to set. Needed only when\\npinning a branch or a commit, which names no release.\\n&quot;} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Which mcpsnoop to install, for example v0.24.0. Defaults to the release you\\npinned the action to, so normally there is nothing to set. Needed only when\\npinning a branch or a commit, which names no release.\\n&quot;} |
| Selected SHA | 5518964384cd855d3f43a58eace033e75dc222ff | ab20b0ebbad9f76de884dfd980e8f5ae6c142433 |
| Selected tag | v0.23.0 | v0.24.0 |

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/13465d022aa41c282f730be17574b5ce692d0186/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/1758727be30241166609dad4c97588b6ad411f32/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/13465d022aa41c282f730be17574b5ce692d0186...1758727be30241166609dad4c97588b6ad411f32)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 13465d022aa41c282f730be17574b5ce692d0186 | 1758727be30241166609dad4c97588b6ad411f32 |
| Selected tag | v1.78.1 | v1.79.1 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/83ac0ad63c0167e6f06796fab0fce28db1bf3db0/) · [Current source](https://github.com/taiki-e/install-action/tree/e407f7bafb71fd004bc5c2da3032e5470cbb6ef0/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/83ac0ad63c0167e6f06796fab0fce28db1bf3db0...e407f7bafb71fd004bc5c2da3032e5470cbb6ef0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 83ac0ad63c0167e6f06796fab0fce28db1bf3db0 | e407f7bafb71fd004bc5c2da3032e5470cbb6ef0 |
| Selected tag | v2.87.22 | v2.87.24 |
