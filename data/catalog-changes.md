# Latest catalog changes

22 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anchore/sbom-action

[Previous source](https://github.com/anchore/sbom-action/tree/3ad7283483fc7af8ff2b4ea19663c2d5ca935e26/) · [Current source](https://github.com/anchore/sbom-action/tree/66cbf4bc1f1c0d2edc94016e65bc221b6bb0ad6c/) · [Upstream code diff](https://github.com/anchore/sbom-action/compare/3ad7283483fc7af8ff2b4ea19663c2d5ca935e26...66cbf4bc1f1c0d2edc94016e65bc221b6bb0ad6c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3ad7283483fc7af8ff2b4ea19663c2d5ca935e26 | 66cbf4bc1f1c0d2edc94016e65bc221b6bb0ad6c |
| Selected tag | v0.24.2 | v0.24.3 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/97c53473391bff1901034d4b454b5bac7ab7a029/) · [Current source](https://github.com/anthropics/claude-code-action/tree/ed670b4cf9de2a5a570d130d2f6197b9e543cd64/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/97c53473391bff1901034d4b454b5bac7ab7a029...ed670b4cf9de2a5a570d130d2f6197b9e543cd64)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 97c53473391bff1901034d4b454b5bac7ab7a029 | ed670b4cf9de2a5a570d130d2f6197b9e543cd64 |
| Selected tag | v1.0.239 | v1.0.240 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/456058bae0678ad3b7347c9b6fec9bdf7625bc79/) · [Current source](https://github.com/asklokesh/loki-mode/tree/f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/456058bae0678ad3b7347c9b6fec9bdf7625bc79...f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43)

| Changed | Before | After |
| --- | --- | --- |
| Input: budget\_limit | {&quot;default&quot;: &quot;5.00&quot;, &quot;description&quot;: &quot;Max cost in USD before stopping (maps to --budget CLI flag)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;5.00&quot;, &quot;description&quot;: &quot;Max cost in USD before stopping (maps to the Loki 10 --max-cost flag)&quot;, &quot;required&quot;: false} |
| Input: prd\_file | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to PRD file relative to repo root (optional, used as positional arg to loki start)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to PRD file relative to repo root (optional, folded into the task text passed to loki start)&quot;, &quot;required&quot;: false} |
| Selected SHA | 456058bae0678ad3b7347c9b6fec9bdf7625bc79 | f9dbe5f4c6fe871138ebe46f2a6f9b4e61c60f43 |
| Selected tag | v10.6.6 | v10.6.11 |

## CodelyTV/pr-size-labeler

[Previous source](https://github.com/CodelyTV/pr-size-labeler/tree/4e3aa0f77f348c8066513d453515316ffa01a607/) · [Current source](https://github.com/CodelyTV/pr-size-labeler/tree/19c335e7695ba922de938806dd129f0a9b992644/) · [Upstream code diff](https://github.com/CodelyTV/pr-size-labeler/compare/4e3aa0f77f348c8066513d453515316ffa01a607...19c335e7695ba922de938806dd129f0a9b992644)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 4e3aa0f77f348c8066513d453515316ffa01a607 | 19c335e7695ba922de938806dd129f0a9b992644 |
| Selected tag | v1.11.1 | v1.12.0 |

## danielroe/uppt

[Previous source](https://github.com/danielroe/uppt/tree/65a86313a63b10a6793de6c4ff8614b18e127a71/) · [Current source](https://github.com/danielroe/uppt/tree/6ec27140623aa835e362f866d8ab0018ab057f4d/) · [Upstream code diff](https://github.com/danielroe/uppt/compare/65a86313a63b10a6793de6c4ff8614b18e127a71...6ec27140623aa835e362f866d8ab0018ab057f4d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 65a86313a63b10a6793de6c4ff8614b18e127a71 | 6ec27140623aa835e362f866d8ab0018ab057f4d |
| Selected tag | v0.6.10 | v0.6.11 |

## dawidd6/action-ansible-playbook

[Previous source](https://github.com/dawidd6/action-ansible-playbook) · [Current source](https://github.com/dawidd6/action-ansible-playbook/tree/126642a1c6ce512da255ef2b41e8ee90f0077474/)

| Changed | Before | After |
| --- | --- | --- |
| Input: check\_mode | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Set to \\&quot;true\\&quot; to enable check (dry-run) mode&quot;, &quot;required&quot;: false} |
| Input: configuration | null | {&quot;description&quot;: &quot;Ansible configuration file content (ansible.cfg)&quot;, &quot;required&quot;: false} |
| Input: directory | null | {&quot;description&quot;: &quot;Root directory of Ansible project (defaults to current)&quot;, &quot;required&quot;: false} |
| Input: inventory | null | {&quot;description&quot;: &quot;Custom content to write into hosts&quot;, &quot;required&quot;: false} |
| Input: key | null | {&quot;description&quot;: &quot;SSH private key used to connect to the host&quot;, &quot;required&quot;: false} |
| Input: known\_hosts | null | {&quot;description&quot;: &quot;Contents of SSH known\_hosts file&quot;, &quot;required&quot;: false} |
| Input: no\_color | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Set to \\&quot;true\\&quot; if the Ansible output should not include colors (defaults to \\&quot;false\\&quot;)&quot;, &quot;required&quot;: false} |
| Input: options | null | {&quot;description&quot;: &quot;Extra options that should be passed to ansible-playbook command&quot;, &quot;required&quot;: false} |
| Input: playbook | null | {&quot;description&quot;: &quot;Ansible playbook filepath&quot;, &quot;required&quot;: true} |
| Input: requirements | null | {&quot;description&quot;: &quot;Ansible Galaxy requirements filepath&quot;, &quot;required&quot;: false} |
| Input: sudo | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Set to \\&quot;true\\&quot; if root is required for running your playbook&quot;, &quot;required&quot;: false} |
| Input: vault\_password | null | {&quot;description&quot;: &quot;The password used for decrypting vaulted files&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;output&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 126642a1c6ce512da255ef2b41e8ee90f0077474 |
| Selected tag | null | v9 |

## DeterminateSystems/determinate-nix-action

[Previous source](https://github.com/DeterminateSystems/determinate-nix-action/tree/8d87e8d5e5b8a8309d4281094560f127d9a265f1/) · [Current source](https://github.com/DeterminateSystems/determinate-nix-action/tree/4d65ea9cab522b6d9f29a170aed23ededc1b27af/) · [Upstream code diff](https://github.com/DeterminateSystems/determinate-nix-action/compare/8d87e8d5e5b8a8309d4281094560f127d9a265f1...4d65ea9cab522b6d9f29a170aed23ededc1b27af)

| Changed | Before | After |
| --- | --- | --- |
| Input: source-tag | {&quot;default&quot;: &quot;v3.22.5&quot;, &quot;description&quot;: &quot;The tag of \`nix-installer\` to use (conflicts with \`source-revision\`, \`source-branch\`, \`source-pr\`)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;v3.23.0&quot;, &quot;description&quot;: &quot;The tag of \`nix-installer\` to use (conflicts with \`source-revision\`, \`source-branch\`, \`source-pr\`)&quot;, &quot;required&quot;: false} |
| Selected SHA | 8d87e8d5e5b8a8309d4281094560f127d9a265f1 | 4d65ea9cab522b6d9f29a170aed23ededc1b27af |
| Selected tag | v3.22.5 | v3.23.0 |

## Added: irgaly/xcode-cache

[Source](https://github.com/irgaly/xcode-cache) — Cache Xcode&#x27;s DerivedData for incremental build.

New entries still require observed stability and fresh scan evidence before usage.

## jianruntech/geo-score

[Previous source](https://github.com/jianruntech/geo-score/tree/884c4725841b5b3f67b8a54458030e1a5c76d0d7/) · [Current source](https://github.com/jianruntech/geo-score/tree/10423969cc749018934919ae8081ac8085b176b1/) · [Upstream code diff](https://github.com/jianruntech/geo-score/compare/884c4725841b5b3f67b8a54458030e1a5c76d0d7...10423969cc749018934919ae8081ac8085b176b1)

| Changed | Before | After |
| --- | --- | --- |
| Input: assert | null | {&quot;description&quot;: &quot;Per-check assertions, one per line, each CHECK OP VALUE: a check id or a glob over them, &gt;=, &gt; or =, and a number or max (for example g.robots=max or p1.llms-txt&gt;=4). A failed one fails the job; a check the run could not observe is skipped.&quot;, &quot;required&quot;: false} |
| Input: badge | null | {&quot;description&quot;: &quot;Write the score as a badge to this path: a path ending in .json gets shields.io endpoint JSON (host it and use https://img.shields.io/endpoint?url=&lt;its URL&gt;), any other path an SVG. The action writes the file; committing or publishing it is up to the workflow.&quot;, &quot;required&quot;: false} |
| Input: baseline | null | {&quot;description&quot;: &quot;An earlier JSON report (json-out) to compare with: the action scores the pages it sampled, as urls-from does, prints what changed check by check, adds a &#x27;Changes since baseline&#x27; section to the job summary and sets the delta and dropped-checks outputs. Not with urls-from.&quot;, &quot;required&quot;: false} |
| Input: fail-on-gate | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;true to fail the job when any gate check (g.\*) scores zero. A gate at zero caps the score at 40: a site that would otherwise score 40 or more reads exactly 40 and passes fail-under: 40; fail-on-gate fails any capped site. The same as the assertion g.\*&gt;0.&quot;, &quot;required&quot;: false} |
| Input: sample | {&quot;default&quot;: &quot;8&quot;, &quot;description&quot;: &quot;How many pages to sample (default 8).&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;8&quot;, &quot;description&quot;: &quot;How many pages to sample, 1 or more (default 8).&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;band&quot;, &quot;gate-capped&quot;, &quot;report&quot;, &quot;report-path&quot;, &quot;score&quot;\] | \[&quot;badge-path&quot;, &quot;band&quot;, &quot;delta&quot;, &quot;dropped-checks&quot;, &quot;gate-capped&quot;, &quot;report&quot;, &quot;report-path&quot;, &quot;score&quot;\] |
| Selected SHA | 884c4725841b5b3f67b8a54458030e1a5c76d0d7 | 10423969cc749018934919ae8081ac8085b176b1 |
| Selected tag | v1.4.0 | v1.6.0 |

## jsdhwfmax/EvalForge

[Previous source](https://github.com/jsdhwfmax/EvalForge/tree/2f80674feb1f4c1ff2ec03aeb1933865670d6971/) · [Current source](https://github.com/jsdhwfmax/EvalForge/tree/54c4667a67fefe6d34435cb5bc166c0b81a8deb5/) · [Upstream code diff](https://github.com/jsdhwfmax/EvalForge/compare/2f80674feb1f4c1ff2ec03aeb1933865670d6971...54c4667a67fefe6d34435cb5bc166c0b81a8deb5)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2f80674feb1f4c1ff2ec03aeb1933865670d6971 | 54c4667a67fefe6d34435cb5bc166c0b81a8deb5 |
| Selected tag | v0.5.0 | v0.6.0 |

## KengoTODA/actions-setup-docker-compose

[Previous source](https://github.com/KengoTODA/actions-setup-docker-compose/tree/caf887cb5173b7ea66cce3c7db3b1e04974a53d4/) · [Current source](https://github.com/KengoTODA/actions-setup-docker-compose/tree/4c09ef903b1119511e9071b6b076e904f9240f3d/) · [Upstream code diff](https://github.com/KengoTODA/actions-setup-docker-compose/compare/caf887cb5173b7ea66cce3c7db3b1e04974a53d4...4c09ef903b1119511e9071b6b076e904f9240f3d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | caf887cb5173b7ea66cce3c7db3b1e04974a53d4 | 4c09ef903b1119511e9071b6b076e904f9240f3d |
| Selected tag | v1.2.8 | v1.2.9 |

## kerlenton/mcpsnoop

[Previous source](https://github.com/kerlenton/mcpsnoop) · [Current source](https://github.com/kerlenton/mcpsnoop/tree/5518964384cd855d3f43a58eace033e75dc222ff/)

| Changed | Before | After |
| --- | --- | --- |
| Input: args | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Any other mcpsnoop check flags, quoted as they would be on a command line,\\nfor example: --expect-tool search --max-server-duration 500ms\\n--format is not accepted: the action reads the report this step produces.\\n&quot;} |
| Input: category | null | {&quot;default&quot;: &quot;mcpsnoop&quot;, &quot;description&quot;: &quot;The code scanning category the report is filed under. A category is a\\nnamespace: two analyses sharing one overwrite each other, so give each tool\\nits own, and vary it per leg of a matrix.\\n&quot;} |
| Input: fail-on | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Comma-separated signals to fail on, any of error, invalid, warn, mismatch,\\npending, late-result, drift, deprecated, incomplete, schema. Defaults to\\nwhat the CLI defaults to, which is error,invalid,warn.\\n&quot;} |
| Input: fail-on-findings | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Fail the job when the check finds something. Set to false to file the\\nalerts and let code scanning&#x27;s own required check decide the build. A run\\nthat could not check at all fails either way, since nothing was verified.\\n&quot;} |
| Input: install | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Install the binary. Set to false when mcpsnoop is already on PATH, which is\\nthe way in on a platform no release is built for.\\n&quot;} |
| Input: session | null | {&quot;description&quot;: &quot;Path to the .jsonl capture to check, relative to the repository root.\\nRecord one by wrapping your server with mcpsnoop in an earlier step.\\n&quot;, &quot;required&quot;: true} |
| Input: upload-sarif | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Upload the report to code scanning. Needs security-events: write on the\\njob. Set to false in a repository without code scanning, or to keep the\\nreport to yourself.\\n&quot;} |
| Input: version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Which mcpsnoop to install, for example v0.21.0. Defaults to the release you\\npinned the action to, so normally there is nothing to set. Needed only when\\npinning a branch or a commit, which names no release.\\n&quot;} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;exit-code&quot;, &quot;outcome&quot;, &quot;sarif&quot;\] |
| Runtime | null | composite |
| Security | unknown | clean |
| Selected SHA | null | 5518964384cd855d3f43a58eace033e75dc222ff |
| Selected tag | null | v0.23.0 |

## luckyPipewrench/pipelock

[Previous source](https://github.com/luckyPipewrench/pipelock/tree/ca05ed06f360f5aac5518ab6ea2b11d729b70bee/) · [Current source](https://github.com/luckyPipewrench/pipelock/tree/3e868ac5d5b62d3a2790958542171143af8a0e38/) · [Upstream code diff](https://github.com/luckyPipewrench/pipelock/compare/ca05ed06f360f5aac5518ab6ea2b11d729b70bee...3e868ac5d5b62d3a2790958542171143af8a0e38)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ca05ed06f360f5aac5518ab6ea2b11d729b70bee | 3e868ac5d5b62d3a2790958542171143af8a0e38 |
| Selected tag | v3.5.0 | v3.6.0 |

## plengauer/Thoth

[Previous source](https://github.com/plengauer/Thoth/tree/db7b5a16bf2d905493c86f582aba4bb056d8aada/) · [Current source](https://github.com/plengauer/Thoth/tree/48918a17e96079ba32d8379d536c89679ab39340/) · [Upstream code diff](https://github.com/plengauer/Thoth/compare/db7b5a16bf2d905493c86f582aba4bb056d8aada...48918a17e96079ba32d8379d536c89679ab39340)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | db7b5a16bf2d905493c86f582aba4bb056d8aada | 48918a17e96079ba32d8379d536c89679ab39340 |
| Selected tag | v5.62.1 | v5.63.0 |

## pypa/gh-action-pypi-publish

[Previous source](https://github.com/pypa/gh-action-pypi-publish) · [Current source](https://github.com/pypa/gh-action-pypi-publish/tree/dc37677b2e1c63e2034f94d8a5b11f265b73ba33/)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\] | \[\[&quot;self-repository&quot;, &quot;warning&quot;, &quot;use GitHub&#x27;s dedicated self-repository syntax&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\]\] |
| Input: attestations | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Enable support for PEP 740 attestations. Only works with PyPI and TestPyPI via Trusted Publishing.&quot;, &quot;required&quot;: false} |
| Input: packages-dir | null | {&quot;description&quot;: &quot;The target directory for distribution&quot;, &quot;required&quot;: false} |
| Input: packages\_dir | null | {&quot;default&quot;: &quot;dist&quot;, &quot;deprecationMessage&quot;: &quot;The inputs have been normalized to use kebab-case. Use \`packages-dir\` instead.&quot;, &quot;description&quot;: &quot;\[DEPRECATED\] The target directory for distribution&quot;, &quot;required&quot;: false} |
| Input: password | null | {&quot;description&quot;: &quot;Password for your PyPI user or an access token&quot;, &quot;required&quot;: false} |
| Input: print-hash | null | {&quot;description&quot;: &quot;Show hash values of files to be uploaded&quot;, &quot;required&quot;: false} |
| Input: print\_hash | null | {&quot;default&quot;: &quot;true&quot;, &quot;deprecationMessage&quot;: &quot;The inputs have been normalized to use kebab-case. Use \`print-hash\` instead.&quot;, &quot;description&quot;: &quot;\[DEPRECATED\] Show hash values of files to be uploaded&quot;, &quot;required&quot;: false} |
| Input: repository-url | null | {&quot;description&quot;: &quot;The repository URL to use&quot;, &quot;required&quot;: false} |
| Input: repository\_url | null | {&quot;default&quot;: &quot;https://upload.pypi.org/legacy/&quot;, &quot;deprecationMessage&quot;: &quot;The inputs have been normalized to use kebab-case. Use \`repository-url\` instead.&quot;, &quot;description&quot;: &quot;\[DEPRECATED\] The repository URL to use&quot;, &quot;required&quot;: false} |
| Input: skip-existing | null | {&quot;description&quot;: &quot;Do not fail if a Python package distribution exists in the target package index&quot;, &quot;required&quot;: false} |
| Input: skip\_existing | null | {&quot;default&quot;: &quot;false&quot;, &quot;deprecationMessage&quot;: &quot;The inputs have been normalized to use kebab-case. Use \`skip-existing\` instead.&quot;, &quot;description&quot;: &quot;\[DEPRECATED\] Do not fail if a Python package distribution exists in the target package index&quot;, &quot;required&quot;: false} |
| Input: user | null | {&quot;default&quot;: &quot;\_\_token\_\_&quot;, &quot;description&quot;: &quot;PyPI user&quot;, &quot;required&quot;: false} |
| Input: verbose | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Show verbose output.&quot;, &quot;required&quot;: false} |
| Input: verify-metadata | null | {&quot;description&quot;: &quot;Check metadata before uploading&quot;, &quot;required&quot;: false} |
| Input: verify\_metadata | null | {&quot;default&quot;: &quot;true&quot;, &quot;deprecationMessage&quot;: &quot;The inputs have been normalized to use kebab-case. Use \`verify-metadata\` instead.&quot;, &quot;description&quot;: &quot;\[DEPRECATED\] Check metadata before uploading&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | composite |
| Security | unknown | warning |
| Selected SHA | null | dc37677b2e1c63e2034f94d8a5b11f265b73ba33 |
| Selected tag | null | v1.14.2 |

## suzuki-shunsuke/tfaction

[Previous source](https://github.com/suzuki-shunsuke/tfaction/tree/e71f80efd3d0eeaca305cb93267e7274d9c6f8c9/) · [Current source](https://github.com/suzuki-shunsuke/tfaction/tree/07a983968cbace490e9059103a7019a638c65e10/) · [Upstream code diff](https://github.com/suzuki-shunsuke/tfaction/compare/e71f80efd3d0eeaca305cb93267e7274d9c6f8c9...07a983968cbace490e9059103a7019a638c65e10)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e71f80efd3d0eeaca305cb93267e7274d9c6f8c9 | 07a983968cbace490e9059103a7019a638c65e10 |
| Selected tag | v2.3.2 | v2.3.3 |

## typesafegithub/github-actions-typing

[Previous source](https://github.com/typesafegithub/github-actions-typing) · [Current source](https://github.com/typesafegithub/github-actions-typing/tree/9ddf35b71a482be7d8922b28e8d00df16b77e315/)

| Changed | Before | After |
| --- | --- | --- |
| Input: ignored-action-files | null | {&quot;description&quot;: &quot;Paths to &#x27;action.y(a)ml&#x27; files that shouldn&#x27;t be validated against their typings. The separator character is &#x27;/&#x27;, regardless of the operating system.\\n&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 9ddf35b71a482be7d8922b28e8d00df16b77e315 |
| Selected tag | null | v2.2.2 |

## UiPath/coder\_eval

[Previous source](https://github.com/UiPath/coder_eval/tree/ee8e145440c1eca48f776f9fa5ff6270158229bc/) · [Current source](https://github.com/UiPath/coder_eval/tree/0fa062a25e6db7cf76edc487cab6967ebe5c55bf/) · [Upstream code diff](https://github.com/UiPath/coder_eval/compare/ee8e145440c1eca48f776f9fa5ff6270158229bc...0fa062a25e6db7cf76edc487cab6967ebe5c55bf)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.12.9&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.12.10&quot;, &quot;description&quot;: &quot;coder-eval version to install from PyPI, or \\&quot;local\\&quot; to install from the action checkout&quot;, &quot;required&quot;: false} |
| Selected SHA | ee8e145440c1eca48f776f9fa5ff6270158229bc | 0fa062a25e6db7cf76edc487cab6967ebe5c55bf |
| Selected tag | v0.12.9 | v0.12.10 |

## vladopajic/go-test-coverage

[Previous source](https://github.com/vladopajic/go-test-coverage/tree/f94bcf0d6b9fa5fb8b783830b22648f6c17475e2/) · [Current source](https://github.com/vladopajic/go-test-coverage/tree/f484eec846448c97c777a26f8b58c5a69a327e12/) · [Upstream code diff](https://github.com/vladopajic/go-test-coverage/compare/f94bcf0d6b9fa5fb8b783830b22648f6c17475e2...f484eec846448c97c777a26f8b58c5a69a327e12)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f94bcf0d6b9fa5fb8b783830b22648f6c17475e2 | f484eec846448c97c777a26f8b58c5a69a327e12 |
| Selected tag | v2.19.0 | v2.20.0 |

## vmactions/freebsd-vm

[Previous source](https://github.com/vmactions/freebsd-vm/tree/a2f9a41fa97f6848b8c3b791087dfcdaa5b473ff/) · [Current source](https://github.com/vmactions/freebsd-vm/tree/c46abacb49f09938ca4e1702d15d836285d694cc/) · [Upstream code diff](https://github.com/vmactions/freebsd-vm/compare/a2f9a41fa97f6848b8c3b791087dfcdaa5b473ff...c46abacb49f09938ca4e1702d15d836285d694cc)

| Changed | Before | After |
| --- | --- | --- |
| Input: cache-after-prepare-key-suffix | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional. Extra value appended to the cache-after-prepare cache key. Change it to discard the prepared VM image cache and run prepare again. Default is empty.&quot;, &quot;required&quot;: false} |
| Selected SHA | a2f9a41fa97f6848b8c3b791087dfcdaa5b473ff | c46abacb49f09938ca4e1702d15d836285d694cc |
| Selected tag | v1.5.8 | v1.5.9 |

## zgosalvez/github-actions-ensure-sha-pinned-actions

[Previous source](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/tree/62574f011e0d1967d555a862bd28a7abba8684fe/) · [Current source](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/tree/c4e71056006d29f90204b2d063be337109507d62/) · [Upstream code diff](https://github.com/zgosalvez/github-actions-ensure-sha-pinned-actions/compare/62574f011e0d1967d555a862bd28a7abba8684fe...c4e71056006d29f90204b2d063be337109507d62)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 62574f011e0d1967d555a862bd28a7abba8684fe | c4e71056006d29f90204b2d063be337109507d62 |
| Selected tag | v5.0.9 | v5.0.10 |

## zgosalvez/github-actions-report-lcov

[Previous source](https://github.com/zgosalvez/github-actions-report-lcov/tree/72cb85c549acad28913c9607dbd04af41bec7980/) · [Current source](https://github.com/zgosalvez/github-actions-report-lcov/tree/1f890959536bc7cc4f8ac36e78626797c41f6ac1/) · [Upstream code diff](https://github.com/zgosalvez/github-actions-report-lcov/compare/72cb85c549acad28913c9607dbd04af41bec7980...1f890959536bc7cc4f8ac36e78626797c41f6ac1)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 72cb85c549acad28913c9607dbd04af41bec7980 | 1f890959536bc7cc4f8ac36e78626797c41f6ac1 |
| Selected tag | v7.2.1 | v7.2.2 |
