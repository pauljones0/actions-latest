# Latest catalog changes

10 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## Aletheore/Aletheore

[Previous source](https://github.com/Aletheore/Aletheore/tree/ec86d25726288b5200009dc49870c047a76c6118/) · [Current source](https://github.com/Aletheore/Aletheore/tree/50a3a3952892a6139b8eb799bca43b96d52097cc/) · [Upstream code diff](https://github.com/Aletheore/Aletheore/compare/ec86d25726288b5200009dc49870c047a76c6118...50a3a3952892a6139b8eb799bca43b96d52097cc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ec86d25726288b5200009dc49870c047a76c6118 | 50a3a3952892a6139b8eb799bca43b96d52097cc |
| Selected tag | v0.9.24 | v0.9.26 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/2dca132ff0e0c4094ce6048b422c6915a071210b/) · [Current source](https://github.com/anthropics/claude-code-action/tree/1d6de8cb0c237e7c15e9e1bdf973826ebae490cc/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/2dca132ff0e0c4094ce6048b422c6915a071210b...1d6de8cb0c237e7c15e9e1bdf973826ebae490cc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2dca132ff0e0c4094ce6048b422c6915a071210b | 1d6de8cb0c237e7c15e9e1bdf973826ebae490cc |
| Selected tag | v1.0.247 | v1.0.248 |

## astral-sh/setup-uv

[Previous source](https://github.com/astral-sh/setup-uv/tree/c18668ad3cf93ea998bef934396af7bb5c839dc7/) · [Current source](https://github.com/astral-sh/setup-uv/tree/1c37ad07a6a961277cf70c0d37d6f313000f5884/) · [Upstream code diff](https://github.com/astral-sh/setup-uv/compare/c18668ad3cf93ea998bef934396af7bb5c839dc7...1c37ad07a6a961277cf70c0d37d6f313000f5884)

| Changed | Before | After |
| --- | --- | --- |
| Input: python-arch | null | {&quot;description&quot;: &quot;The Python architecture to set UV\_PYTHON\_ARCH to, e.g., x86\_64 or aarch64. Overrides UV\_PYTHON\_ARCH.&quot;, &quot;required&quot;: false} |
| Selected SHA | c18668ad3cf93ea998bef934396af7bb5c839dc7 | 1c37ad07a6a961277cf70c0d37d6f313000f5884 |
| Selected tag | v10.2.0 | v10.3.0 |

## aws-actions/amazon-ecs-deploy-task-definition

[Previous source](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/tree/c465972ecbd160473f22e683363b422a5412a3de/) · [Current source](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/tree/a00d4d57ac0de1a99b39fe469f3d898d38717c2b/) · [Upstream code diff](https://github.com/aws-actions/amazon-ecs-deploy-task-definition/compare/c465972ecbd160473f22e683363b422a5412a3de...a00d4d57ac0de1a99b39fe469f3d898d38717c2b)

| Changed | Before | After |
| --- | --- | --- |
| Input: wait-max-delay-seconds | {&quot;description&quot;: &quot;Maximum delay in seconds between polling attempts when waiting for service stability or task completion. If not set, AWS SDK uses exponential backoff up to 120 seconds. Set to 15 for consistent 15-second polling intervals.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Maximum delay in seconds between polling attempts when waiting for service stability or task completion. If not set, the AWS SDK applies exponential backoff up to the waiter default maximum delay, which is 600 seconds (10 minutes) for the ECS waiters and 120 seconds for CodeDeploy deployments. Set to 15 for consistent 15-second polling intervals.&quot;, &quot;required&quot;: false} |
| Selected SHA | c465972ecbd160473f22e683363b422a5412a3de | a00d4d57ac0de1a99b39fe469f3d898d38717c2b |
| Selected tag | v2.6.3 | v2.6.4 |

## cycjimmy/semantic-release-action

[Previous source](https://github.com/cycjimmy/semantic-release-action/tree/7261f53f41d97434955b6ca5e26a2b0805f0cba2/) · [Current source](https://github.com/cycjimmy/semantic-release-action/tree/1989a0fefc4aea321e07f717680ed8e345925dc1/) · [Upstream code diff](https://github.com/cycjimmy/semantic-release-action/compare/7261f53f41d97434955b6ca5e26a2b0805f0cba2...1989a0fefc4aea321e07f717680ed8e345925dc1)

| Changed | Before | After |
| --- | --- | --- |
| Input: skip\_npm\_plugin | null | {&quot;description&quot;: &quot;Whether to skip the @semantic-release/npm default plugin. Useful for non-Node.js projects without a package.json file. When true, the default plugins are replaced with @semantic-release/commit-analyzer, @semantic-release/release-notes-generator and @semantic-release/github. It will override the plugins attribute in your configuration file.&quot;, &quot;required&quot;: false} |
| Selected SHA | 7261f53f41d97434955b6ca5e26a2b0805f0cba2 | 1989a0fefc4aea321e07f717680ed8e345925dc1 |
| Selected tag | v7.0.0 | v7.1.2 |

## helm/chart-testing-action

[Previous source](https://github.com/helm/chart-testing-action/tree/6ec842c01de15ebb84c8627d2744a0c2f2755c9f/) · [Current source](https://github.com/helm/chart-testing-action/tree/720270857a28afd41e2426521a7801db09e9b510/) · [Upstream code diff](https://github.com/helm/chart-testing-action/compare/6ec842c01de15ebb84c8627d2744a0c2f2755c9f...720270857a28afd41e2426521a7801db09e9b510)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;error&quot;, &quot;code injection via template expansion&quot;\]\] | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\]\] |
| Input: github\_token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;GitHub token for authenticating with the GitHub API (default: github.token)&quot;, &quot;required&quot;: false} |
| Input: lint\_config | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to a custom yamllint config file. If set, ct lint uses it instead of the default lintconf.yaml.&quot;, &quot;required&quot;: false} |
| Input: uv\_version | null | {&quot;default&quot;: &quot;latest&quot;, &quot;description&quot;: &quot;The uv version to install (default: latest)&quot;, &quot;required&quot;: false} |
| Input: verify\_blob | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;determines whether the download blob should be verified (default: true)&quot;, &quot;required&quot;: false} |
| Input: version | {&quot;default&quot;: &quot;3.14.0&quot;, &quot;description&quot;: &quot;The chart-testing version to install (default: 3.12.0)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;3.15.0&quot;, &quot;description&quot;: &quot;The chart-testing version to install&quot;, &quot;required&quot;: false} |
| Input: yamale\_version | {&quot;default&quot;: &quot;6.0.0&quot;, &quot;description&quot;: &quot;The yamale version to install (default: 6.0.0)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;6.0.0&quot;, &quot;description&quot;: &quot;The yamale version to install&quot;, &quot;required&quot;: false} |
| Input: yamllint\_version | {&quot;default&quot;: &quot;1.33.0&quot;, &quot;description&quot;: &quot;The yamllint version to install (default: 1.27.1)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;1.33.0&quot;, &quot;description&quot;: &quot;The yamllint version to install&quot;, &quot;required&quot;: false} |
| Selected SHA | 6ec842c01de15ebb84c8627d2744a0c2f2755c9f | 720270857a28afd41e2426521a7801db09e9b510 |
| Selected tag | v2.8.0 | v2.9.0 |

## irgaly/xcode-cache

[Previous source](https://github.com/irgaly/xcode-cache) · [Current source](https://github.com/irgaly/xcode-cache/tree/4141f139f00e335c6e1031fb93e667181f86146f/)

| Changed | Before | After |
| --- | --- | --- |
| Input: cache-read-only | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;When true, existing entries will be read from the cache but no entries will be written.&quot;, &quot;required&quot;: false} |
| Input: delete-used-deriveddata-cache | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;delete the DerivedData cache used for this job, when job has succeeded.&quot;, &quot;required&quot;: false} |
| Input: deriveddata-directory | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;a directory of project&#x27;s DerivedData. default: ~/Library/Developer/Xcode/DerivedData&quot;, &quot;required&quot;: false} |
| Input: key | null | {&quot;description&quot;: &quot;cache key for DerivedData&quot;, &quot;required&quot;: true} |
| Input: restore-keys | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;cache restore keys for DerivedData.&quot;, &quot;required&quot;: false} |
| Input: restore-mtime-targets | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;the targets glob pattern of restoring mtime. exclude pattern &#x27;!{pattern}&#x27; can be used. This glob pattern is applied with GitHub action toolkit glob option implicitDescendants = false&quot;, &quot;required&quot;: false} |
| Input: sourcepackages-directory | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;a directory of SourcePackages. default: {deriveddata-directory}/SourcePackages&quot;, &quot;required&quot;: false} |
| Input: swiftpm-cache-key | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;cache key for SourcePackages. default: irgaly/xcode-cache-sourcepackages-{hashFiles({resolvedFiles})}&quot;, &quot;required&quot;: false} |
| Input: swiftpm-cache-restore-keys | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;cache restore keys for SourcePackages&quot;, &quot;required&quot;: false} |
| Input: swiftpm-package-resolved-file | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Xcode&#x27;s Package.resolved file path glob pattern. default: \*\*/\*.xcodeproj/project.xcworkspace/xcshareddata/swiftpm/Package.resolved , \*\*/\*.xcworkspace/xcshareddata/swiftpm/Package.resolved&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;an GitHub Token for deleting the DerivedData operation. default: github.token&quot;, &quot;required&quot;: false} |
| Input: use-default-mtime-targets | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;process default mtime targets: \*\*/\*.swift , \*\*/\*.xib , \*\*/\*.storyboard , \*\*/\*.strings , \*\*/\*.xcstrings, \*\*/\*.plist , \*\*/\*.xcassets , \*\*/\*.xcassets/\*\*/\* , \*\*/\*.bundle , \*\*/\*.bundle/\*\*/\*, \*\*/\*.xcdatamodel , \*\*/\*.xcdatamodel/\*\*/\* , \*\*/\*.framework , \*\*/\*.framework/\*\*/\* , \*\*/\*.xcframework , \*\*/\*.xcframework/\*\*/\* , \*\*/\*.m , \*\*/\*.mm , \*\*/\*.h , \*\*/\*.c , \*\*/\*.cc , \*\*/\*.cpp , \*\*/\*.hpp , \*\*/\*.hxx&quot;, &quot;required&quot;: false} |
| Input: verbose | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;enable verbose logging&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 4141f139f00e335c6e1031fb93e667181f86146f |
| Selected tag | null | v1.9.2 |

## openqodex/openqodex

[Previous source](https://github.com/openqodex/openqodex/tree/5b50fe786786a0b8083204865072a9eba5d0ab85/) · [Current source](https://github.com/openqodex/openqodex/tree/2f2fa9e48c1f62a6123997eb14111140d8e22a74/) · [Upstream code diff](https://github.com/openqodex/openqodex/compare/5b50fe786786a0b8083204865072a9eba5d0ab85...2f2fa9e48c1f62a6123997eb14111140d8e22a74)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.10.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.11.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} |
| Selected SHA | 5b50fe786786a0b8083204865072a9eba5d0ab85 | 2f2fa9e48c1f62a6123997eb14111140d8e22a74 |
| Selected tag | v0.10.0 | v0.11.0 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/f7e5d7c961414b23f5b25b2da9294395d08513ad/) · [Current source](https://github.com/taiki-e/install-action/tree/ab6895351a88b908e96a4697860d4ffea5e57dbe/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/f7e5d7c961414b23f5b25b2da9294395d08513ad...ab6895351a88b908e96a4697860d4ffea5e57dbe)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f7e5d7c961414b23f5b25b2da9294395d08513ad | ab6895351a88b908e96a4697860d4ffea5e57dbe |
| Selected tag | v2.87.26 | v2.87.27 |

## upptime/uptime-monitor

[Previous source](https://github.com/upptime/uptime-monitor/tree/8be193bbcb957a3a917d2bb16a0c96959778a889/) · [Current source](https://github.com/upptime/uptime-monitor/tree/5811f280953e960b7667f0031a4d326f5f97ba99/) · [Upstream code diff](https://github.com/upptime/uptime-monitor/compare/8be193bbcb957a3a917d2bb16a0c96959778a889...5811f280953e960b7667f0031a4d326f5f97ba99)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 8be193bbcb957a3a917d2bb16a0c96959778a889 | 5811f280953e960b7667f0031a4d326f5f97ba99 |
| Selected tag | v1.44.1 | v1.45.0 |
