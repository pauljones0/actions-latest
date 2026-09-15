# Latest catalog changes

14 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## actions-rust-lang/setup-rust-toolchain

[Previous source](https://github.com/actions-rust-lang/setup-rust-toolchain/tree/166cdcfd11aee3cb47222f9ddb555ce30ddb9659/) · [Current source](https://github.com/actions-rust-lang/setup-rust-toolchain/tree/ecabd13d1c56bd1345c230e542e9144811ad706f/) · [Upstream code diff](https://github.com/actions-rust-lang/setup-rust-toolchain/compare/166cdcfd11aee3cb47222f9ddb555ce30ddb9659...ecabd13d1c56bd1345c230e542e9144811ad706f)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\]\] | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\]\] |
| Input: build-warnings | null | {&quot;default&quot;: &quot;deny&quot;, &quot;description&quot;: &quot;Sets the build.warnings config via the CARGO\_BUILD\_WARNINGS variable.&quot;, &quot;required&quot;: false} |
| Input: rustflags | {&quot;default&quot;: &quot;-D warnings&quot;, &quot;description&quot;: &quot;set RUSTFLAGS environment variable, set to empty string to avoid overwriting build.rustflags&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;set RUSTFLAGS environment variable, set to empty string to avoid overwriting build.rustflags&quot;, &quot;required&quot;: false} |
| Selected SHA | 166cdcfd11aee3cb47222f9ddb555ce30ddb9659 | ecabd13d1c56bd1345c230e542e9144811ad706f |
| Selected tag | v1.17.0 | v2.0.0 |

## aminya/setup-cpp

[Previous source](https://github.com/aminya/setup-cpp) · [Current source](https://github.com/aminya/setup-cpp/tree/59179aabb1f9453d12daf81c00d789af3b67b1a6/)

| Changed | Before | After |
| --- | --- | --- |
| Input: apple-clang | null | {&quot;description&quot;: &quot;Wether to install apple-clang (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: apple-llvm | null | {&quot;description&quot;: &quot;Wether to install apple-llvm (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: appleclang | null | {&quot;description&quot;: &quot;Wether to install apple-clang (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: applellvm | null | {&quot;description&quot;: &quot;Wether to install apple-llvm (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: architecture | null | {&quot;description&quot;: &quot;The CPU architecture&quot;, &quot;required&quot;: false} |
| Input: autoreconf | null | {&quot;description&quot;: &quot;Wether to install autoreconf (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: brew | null | {&quot;description&quot;: &quot;Wether to install brew (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cache-tools | null | {&quot;description&quot;: &quot;If should cache the installed tools? (Default: false)&quot;, &quot;required&quot;: false} |
| Input: ccache | null | {&quot;description&quot;: &quot;Wether to install ccache (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: choco | null | {&quot;description&quot;: &quot;Wether to install chocolatey (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cl | null | {&quot;description&quot;: &quot;Wether to install cl (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: clang | null | {&quot;description&quot;: &quot;Wether to install clang (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: clang-format | null | {&quot;description&quot;: &quot;The clangWether to install format (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: clang-tidy | null | {&quot;description&quot;: &quot;Wether to install clang-tidy (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: clangformat | null | {&quot;description&quot;: &quot;The clangWether to install format (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: clangtidy | null | {&quot;description&quot;: &quot;The clangWether to install tidy (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmake | null | {&quot;description&quot;: &quot;Wether to install cmake (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmake-format | null | {&quot;description&quot;: &quot;Wether to install cmake-format (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmake-lint | null | {&quot;description&quot;: &quot;Wether to install cmake-lint (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmakeformat | null | {&quot;description&quot;: &quot;Wether to install cmake-format (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmakelang | null | {&quot;description&quot;: &quot;Wether to install cmakelang (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cmakelint | null | {&quot;description&quot;: &quot;Wether to install cmake-lint (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: compiler | null | {&quot;description&quot;: &quot;The compiler to use and its optional version separated by - e.g. llvm-13.0.0&quot;, &quot;required&quot;: false} |
| Input: conan | null | {&quot;description&quot;: &quot;Wether to install conan (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cppcheck | null | {&quot;description&quot;: &quot;Wether to install cppcheck (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: cpplint | null | {&quot;description&quot;: &quot;Wether to install cpplint (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: doxygen | null | {&quot;description&quot;: &quot;Wether to install doxygen (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: flawfinder | null | {&quot;description&quot;: &quot;Wether to install flawfinder (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: gcc | null | {&quot;description&quot;: &quot;Wether to install gcc (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: gcovr | null | {&quot;description&quot;: &quot;Wether to install gcovr (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: git | null | {&quot;description&quot;: &quot;Wether to install git (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: graphviz | null | {&quot;description&quot;: &quot;Wether to install graphviz (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: infer | null | {&quot;description&quot;: &quot;Wether to install facebook/infer (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: kcov | null | {&quot;description&quot;: &quot;Wether to install kcov (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: lizard | null | {&quot;description&quot;: &quot;Wether to install lizard (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: llvm | null | {&quot;description&quot;: &quot;Wether to install llvm (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: make | null | {&quot;description&quot;: &quot;Wether to install make (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: meson | null | {&quot;description&quot;: &quot;Wether to install meson (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: msbuild | null | {&quot;description&quot;: &quot;Wether to install msbuild (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: msvc | null | {&quot;description&quot;: &quot;Wether to install msvc (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Input: nala | null | {&quot;description&quot;: &quot;Wether to install nala (true/false) or the specific version to install (\\&quot;\\&quot; or \\&quot;legacy\\&quot;).&quot;, &quot;required&quot;: false} |
| Input: ninja | null | {&quot;description&quot;: &quot;Wether to install ninja (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: node-package-manager | null | {&quot;description&quot;: &quot;The node package manager to use (npm/yarn/pnpm) when installing setup-cpp globally&quot;, &quot;required&quot;: false} |
| Input: opencppcoverage | null | {&quot;description&quot;: &quot;Wether to install opencppcoverage (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: powershell | null | {&quot;description&quot;: &quot;Wether to install powershell (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: pwsh | null | {&quot;description&quot;: &quot;Wether to install pwsh (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: python | null | {&quot;description&quot;: &quot;Wether to install python (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: sccache | null | {&quot;description&quot;: &quot;Wether to install sccache (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: setup-cpp | null | {&quot;description&quot;: &quot;Wether to install setup-cpp (true/false) or the specific version to install. (Default to the current version called by the action)&quot;, &quot;required&quot;: false} |
| Input: sevenzip | null | {&quot;description&quot;: &quot;Wether to install 7z (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: tar | null | {&quot;description&quot;: &quot;Wether to install tar (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: task | null | {&quot;description&quot;: &quot;Wether to install task (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: timeout | null | {&quot;default&quot;: &quot;20&quot;, &quot;description&quot;: &quot;The timeout for installation of one tool (in minutes).&quot;, &quot;required&quot;: false} |
| Input: vcpkg | null | {&quot;description&quot;: &quot;Wether to install vcpkg (true/false) or the specific version to install.&quot;, &quot;required&quot;: false} |
| Input: vcvarsall | null | {&quot;description&quot;: &quot;If should run vcvarsall?&quot;, &quot;required&quot;: false} |
| Input: visualstudio | null | {&quot;description&quot;: &quot;Wether to install visualstudio (true/false) or the specific version to install&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 59179aabb1f9453d12daf81c00d789af3b67b1a6 |
| Selected tag | null | v1.10.0 |

## Added: amirisback/automated-build-android-app-with-github-action

[Source](https://github.com/amirisback/automated-build-android-app-with-github-action) — Automated build android app bundle and apk with github action

New entries still require observed stability and fresh scan evidence before usage.

## Added: benchmark-action/github-action-benchmark

[Source](https://github.com/benchmark-action/github-action-benchmark) — Continuous Benchmark using GitHub pages as dash board for keeping performance

New entries still require observed stability and fresh scan evidence before usage.

## cncf/prow-github-actions

[Previous source](https://github.com/cncf/prow-github-actions) · [Current source](https://github.com/cncf/prow-github-actions/tree/c44ac3a57d67639e39e4a4988b52049ef45b80dd/)

| Changed | Before | After |
| --- | --- | --- |
| Input: github-token | null | {&quot;description&quot;: &quot;Token used by prow actions to accomplish jobs and tasks. May be a bot user access token or the limited scope Github token&quot;, &quot;required&quot;: true} |
| Input: jobs | null | {&quot;description&quot;: &quot;The jobs to automatically run on event. Space delimited. Expect commands on own line.&quot;, &quot;required&quot;: false} |
| Input: merge-method | null | {&quot;description&quot;: &quot;Strategy for Prow-github-actions to take when merging a pull request using the lgtm cron-job. Can be &#x27;squash&#x27;, &#x27;rebase&#x27;, or &#x27;merge&#x27;. Defaults to &#x27;merge&#x27;&quot;, &quot;required&quot;: false} |
| Input: prow-commands | null | {&quot;description&quot;: &quot;Comment keywords/commands to look for. Space delimited. Expect commands on own line.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node20 |
| Security | unknown | clean |
| Selected SHA | null | c44ac3a57d67639e39e4a4988b52049ef45b80dd |
| Selected tag | null | v2.0.0 |

## coursier/setup-action

[Previous source](https://github.com/coursier/setup-action) · [Current source](https://github.com/coursier/setup-action/tree/9b7939bf01fd1185ce2babe16135168361bf2c62/)

| Changed | Before | After |
| --- | --- | --- |
| Input: apps | null | {&quot;default&quot;: &quot;sbtn&quot;, &quot;description&quot;: &quot;Applications to install&quot;, &quot;required&quot;: false} |
| Input: customRepositories | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;The pipe (\|) seperated locations of non-standard repositories. See https://get-coursier.io/docs/other-repositories&quot;, &quot;required&quot;: false} |
| Input: disableDefaultRepos | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to pass the --no-default flag to coursier&quot;, &quot;required&quot;: false} |
| Input: extraJvmArgs | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Space-separated list of -D JVM property args passed to every cs invocation. The -J prefix is added automatically if missing (e.g. -Dhttps.proxyHost=proxy.example.com -Dhttps.proxyPort=8080)&quot;, &quot;required&quot;: false} |
| Input: jvm | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;JVM to install (leave empty to use default)&quot;, &quot;required&quot;: false} |
| Input: jvm-index | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Arbitrary URL containing the JVM index source (leave empty to use default)&quot;, &quot;required&quot;: false} |
| Input: launcher | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Coursier launcher to use. Leave empty (default) to install the default native binary launcher when available (on Windows ARM64, the jpackage JVM distribution cs-aarch64-pc-win32-jvm.zip). Accepts JVM launchers \\&quot;thin\\&quot;, \\&quot;jvm\\&quot;, and \\&quot;assembly\\&quot;, or native launcher flavors such as \\&quot;container\\&quot;, \\&quot;compat\\&quot;, and \\&quot;static\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: mirrors | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Newline-separated list of \\&quot;from=to\\&quot; mirror entries written to ~/.config/coursier/mirror.properties before any cs invocation. The \\&quot;from\\&quot; side may be a comma-separated list of source URLs. Unlike customRepositories / disableDefaultRepos, mirrors are applied at the resolver level to every repository coursier sees — including ones declared inside app descriptors that customRepositories cannot override. See https://get-coursier.io/docs/other-mirrors&quot;, &quot;required&quot;: false} |
| Input: preferredLauncher | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Preferred native Coursier launcher flavor (for example, \\&quot;container\\&quot;, \\&quot;compat\\&quot;, or \\&quot;static\\&quot;). Falls back to the default launcher when the flavored launcher returns a 4xx HTTP response. JVM launcher values are not accepted.&quot;, &quot;required&quot;: false} |
| Input: useContainerImage | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Deprecated alias for launcher: container.&quot;, &quot;required&quot;: false} |
| Input: version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Coursier version to install (use \\&quot;nightly\\&quot; for the latest nightly build from https://github.com/coursier/coursier/releases/tag/nightly)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;cs-version&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 9b7939bf01fd1185ce2babe16135168361bf2c62 |
| Selected tag | null | v3.0.2 |

## devops-infra/action-pull-request

[Previous source](https://github.com/devops-infra/action-pull-request) · [Current source](https://github.com/devops-infra/action-pull-request/tree/1d8aa3c4a6060a1410641f700f91353af65cc94b/)

| Changed | Before | After |
| --- | --- | --- |
| Input: allow\_no\_diff | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Allows to continue on merge commits with no diffs&quot;, &quot;required&quot;: false} |
| Input: assignee | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Assignee&#x27;s usernames&quot;, &quot;required&quot;: false} |
| Input: body | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Pull request body&quot;, &quot;required&quot;: false} |
| Input: create\_missing\_labels | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to create labels that do not already exist before creating the PR&quot;, &quot;required&quot;: false} |
| Input: draft | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to mark it as a draft&quot;, &quot;required&quot;: false} |
| Input: get\_diff | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to inject difference into template&quot;, &quot;required&quot;: false} |
| Input: github\_token | null | {&quot;description&quot;: &quot;GitHub token&quot;, &quot;required&quot;: true} |
| Input: ignore\_users | null | {&quot;default&quot;: &quot;dependabot&quot;, &quot;description&quot;: &quot;List of users to ignore, coma separated&quot;, &quot;required&quot;: false} |
| Input: label | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Labels to apply, coma separated&quot;, &quot;required&quot;: false} |
| Input: max\_body\_bytes | null | {&quot;default&quot;: &quot;65000&quot;, &quot;description&quot;: &quot;Maximum PR body size in bytes before overflow is moved into managed comments&quot;, &quot;required&quot;: false} |
| Input: max\_diff\_lines | null | {&quot;default&quot;: &quot;0&quot;, &quot;description&quot;: &quot;Maximum lines per generated diff section (0 means unlimited)&quot;, &quot;required&quot;: false} |
| Input: milestone | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Milestone&quot;, &quot;required&quot;: false} |
| Input: new\_string | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;New string for the replacement in the template&quot;, &quot;required&quot;: false} |
| Input: old\_string | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Old string for the replacement in template&quot;, &quot;required&quot;: false} |
| Input: project | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;GitHub Project title to add the pull request to&quot;, &quot;required&quot;: false} |
| Input: repository | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Repository in owner/name format used for API calls and git remote auth (defaults to current repository)&quot;, &quot;required&quot;: false} |
| Input: repository\_path | null | {&quot;default&quot;: &quot;.&quot;, &quot;description&quot;: &quot;Relative path under GITHUB\_WORKSPACE to the checked-out repository (use when actions/checkout path is set)&quot;, &quot;required&quot;: false} |
| Input: reviewer | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Reviewer&#x27;s username&quot;, &quot;required&quot;: false} |
| Input: source\_branch | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Name of the source branch&quot;, &quot;required&quot;: false} |
| Input: target\_branch | null | {&quot;default&quot;: &quot;master&quot;, &quot;description&quot;: &quot;Name of the target branch&quot;, &quot;required&quot;: false} |
| Input: template | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Template file location&quot;, &quot;required&quot;: false} |
| Input: title | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Pull request title&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;pr\_number&quot;, &quot;url&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 1d8aa3c4a6060a1410641f700f91353af65cc94b |
| Selected tag | null | v1.4.0 |

## dprint/check

[Previous source](https://github.com/dprint/check/tree/06e1a587a762d4e06663c3e3d46afedc93d9f185/) · [Current source](https://github.com/dprint/check/tree/7dc032d8874778fc024f6f9b4a7e6d896782c330/) · [Upstream code diff](https://github.com/dprint/check/compare/06e1a587a762d4e06663c3e3d46afedc93d9f185...7dc032d8874778fc024f6f9b4a7e6d896782c330)

| Changed | Before | After |
| --- | --- | --- |
| Input: working-directory | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Directory to run dprint check in, relative to the workspace (ex. packages/app)&quot;, &quot;required&quot;: false} |
| Outputs | \[&quot;cache-changed&quot;, &quot;cache-matched-key&quot;, &quot;dprint-version&quot;\] | \[&quot;cache-changed&quot;, &quot;cache-matched-key&quot;, &quot;dprint-version&quot;, &quot;unformatted-count&quot;, &quot;unformatted-files&quot;\] |
| Selected SHA | 06e1a587a762d4e06663c3e3d46afedc93d9f185 | 7dc032d8874778fc024f6f9b4a7e6d896782c330 |
| Selected tag | v2.4 | v2.5 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/89d33c0e856f3451eb88c7f60410051ded8d3109/) · [Current source](https://github.com/duriantaco/skylos/tree/2c963dcec8097bb6e931819804e817f32f49a5b0/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/89d33c0e856f3451eb88c7f60410051ded8d3109...2c963dcec8097bb6e931819804e817f32f49a5b0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 89d33c0e856f3451eb88c7f60410051ded8d3109 | 2c963dcec8097bb6e931819804e817f32f49a5b0 |
| Selected tag | v4.35.0 | v4.36.0 |

## Added: jbrooksuk/laravel-forge-action

[Source](https://github.com/jbrooksuk/laravel-forge-action) — Trigger Laravel Forge Deployments with Github Actions

New entries still require observed stability and fresh scan evidence before usage.

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/0212dedb0f92b8ba4020c17dc30d3eced32415d7/) · [Current source](https://github.com/pullfrog/pullfrog/tree/22442cbbe9039fe186e20f1fdf9206bb4a07e7cd/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/0212dedb0f92b8ba4020c17dc30d3eced32415d7...22442cbbe9039fe186e20f1fdf9206bb4a07e7cd)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 0212dedb0f92b8ba4020c17dc30d3eced32415d7 | 22442cbbe9039fe186e20f1fdf9206bb4a07e7cd |
| Selected tag | v0.1.68 | v0.1.69 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/84f5ac3124727fb3d284d4d22ee9ab3654fd09a6/) · [Current source](https://github.com/taiki-e/install-action/tree/d438492cf8a250514fa2d34b30bc3c0dc37c65ff/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/84f5ac3124727fb3d284d4d22ee9ab3654fd09a6...d438492cf8a250514fa2d34b30bc3c0dc37c65ff)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 84f5ac3124727fb3d284d4d22ee9ab3654fd09a6 | d438492cf8a250514fa2d34b30bc3c0dc37c65ff |
| Selected tag | v2.87.7 | v2.87.8 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/6989a93e81a4b1d5d11a91b1b84496db66c37c45/) · [Current source](https://github.com/tmatens/compose-lint/tree/d0434054779e9026c6082bc47ecc818ec2aa981d/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/6989a93e81a4b1d5d11a91b1b84496db66c37c45...d0434054779e9026c6082bc47ecc818ec2aa981d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6989a93e81a4b1d5d11a91b1b84496db66c37c45 | d0434054779e9026c6082bc47ecc818ec2aa981d |
| Selected tag | v0.27.0 | v0.28.0 |

## vmactions/solaris-vm

[Previous source](https://github.com/vmactions/solaris-vm/tree/96d8d976f9e67d82ec6c7e8ce9c1060731f9e21c/) · [Current source](https://github.com/vmactions/solaris-vm/tree/a11f407d3720a3717673d4194f19ee63b284977e/) · [Upstream code diff](https://github.com/vmactions/solaris-vm/compare/96d8d976f9e67d82ec6c7e8ce9c1060731f9e21c...a11f407d3720a3717673d4194f19ee63b284977e)

| Changed | Before | After |
| --- | --- | --- |
| Input: osname | {&quot;default&quot;: &quot;Solaris&quot;, &quot;description&quot;: &quot;The OS name&quot;, &quot;required&quot;: true} | {&quot;default&quot;: &quot;solaris&quot;, &quot;description&quot;: &quot;The OS name&quot;, &quot;required&quot;: true} |
| Selected SHA | 96d8d976f9e67d82ec6c7e8ce9c1060731f9e21c | a11f407d3720a3717673d4194f19ee63b284977e |
| Selected tag | v1.3.9 | v1.4.0 |
