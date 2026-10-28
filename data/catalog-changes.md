# Latest catalog changes

16 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/db77d4d3c98f3f6380e7cd45ffba2342a3dbde3c/) · [Current source](https://github.com/anthropics/claude-code-action/tree/a5a423f75c251dcbff8a74e99f83b2cb03c72bfa/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/db77d4d3c98f3f6380e7cd45ffba2342a3dbde3c...a5a423f75c251dcbff8a74e99f83b2cb03c72bfa)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | db77d4d3c98f3f6380e7cd45ffba2342a3dbde3c | a5a423f75c251dcbff8a74e99f83b2cb03c72bfa |
| Selected tag | v1.0.254 | v1.0.256 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/986204b217bdd3e10dcf3a2255fe5a01783ef273/) · [Current source](https://github.com/asklokesh/loki-mode/tree/96bf456ce704b32f454588206efa07da8f46ebf8/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/986204b217bdd3e10dcf3a2255fe5a01783ef273...96bf456ce704b32f454588206efa07da8f46ebf8)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 986204b217bdd3e10dcf3a2255fe5a01783ef273 | 96bf456ce704b32f454588206efa07da8f46ebf8 |
| Selected tag | v11.17.103 | v11.18.0 |

## bridgecrewio/checkov-action

[Previous source](https://github.com/bridgecrewio/checkov-action/tree/6f26dc90000b74feb589a906cdfae540f5119895/) · [Current source](https://github.com/bridgecrewio/checkov-action/tree/c3e106d5f8f4253a6de5110efb41a080f83db294/) · [Upstream code diff](https://github.com/bridgecrewio/checkov-action/compare/6f26dc90000b74feb589a906cdfae540f5119895...c3e106d5f8f4253a6de5110efb41a080f83db294)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6f26dc90000b74feb589a906cdfae540f5119895 | c3e106d5f8f4253a6de5110efb41a080f83db294 |
| Selected tag | v12.3134.0 | v12.3135.0 |

## chromaui/action

[Previous source](https://github.com/chromaui/action) · [Current source](https://github.com/chromaui/action/tree/e24559fbc78e0cda863f3889f0e40ac249b07e20/)

| Changed | Before | After |
| --- | --- | --- |
| Input: autoAcceptChanges | null | {&quot;description&quot;: &quot;Automatically accept all changes in chromatic: boolean or branchname&quot;, &quot;required&quot;: false} |
| Input: branchName | null | {&quot;description&quot;: &quot;Override the branch name&quot;, &quot;required&quot;: false} |
| Input: buildCommand | null | {&quot;description&quot;: &quot;The command that builds your Storybook (when your build command does not exist in \\&quot;scripts\\&quot; of your package.json)&quot;, &quot;required&quot;: false} |
| Input: buildScriptName | null | {&quot;description&quot;: &quot;The npm script that builds your Storybook \[build-storybook\]&quot;, &quot;required&quot;: false} |
| Input: chromaticSha | null | {&quot;description&quot;: &quot;The git SHA of the commit that should be tested in Chromatic. Defaults to the SHA of the current branch tip on which the action is running. Use with caution, as it may yield unexpected results.&quot;, &quot;required&quot;: false} |
| Input: configFile | null | {&quot;description&quot;: &quot;Path from where to load the Chromatic config JSON file.&quot;} |
| Input: cypress | null | {&quot;description&quot;: &quot;Run build against \`@chromatic-com/cypress\` test archives&quot;, &quot;required&quot;: false} |
| Input: debug | null | {&quot;description&quot;: &quot;Output verbose debugging information&quot;, &quot;required&quot;: false} |
| Input: diagnosticsFile | null | {&quot;description&quot;: &quot;Write process context information to a JSON file&quot;, &quot;required&quot;: false} |
| Input: dryRun | null | {&quot;description&quot;: &quot;Run without actually publishing to Chromatic&quot;, &quot;required&quot;: false} |
| Input: exitOnceUploaded | null | {&quot;description&quot;: &quot;Exit with 0 once the built version has been sent to chromatic: boolean or branchname&quot;, &quot;required&quot;: false} |
| Input: exitZeroOnChanges | null | {&quot;description&quot;: &quot;Positive exit of action even when there are changes: boolean or branchname&quot;, &quot;required&quot;: false} |
| Input: externals | null | {&quot;description&quot;: &quot;Disable TurboSnap when any of these files have changed since the baseline build&quot;, &quot;required&quot;: false} |
| Input: fileHashing | null | {&quot;description&quot;: &quot;Whether to apply file hashing to skip uploading unchanged files (default: true)&quot;, &quot;required&quot;: false} |
| Input: forceRebuild | null | {&quot;description&quot;: &quot;Do not skip build when a rebuild is detected&quot;, &quot;required&quot;: false} |
| Input: ignoreLastBuildOnBranch | null | {&quot;description&quot;: &quot;Do not use the last build on this branch as a baseline if it is no longer in history (i.e. branch was rebased)&quot;, &quot;required&quot;: false} |
| Input: junitReport | null | {&quot;description&quot;: &quot;Write build results to a JUnit XML file&quot;, &quot;required&quot;: false} |
| Input: logFile | null | {&quot;description&quot;: &quot;Write CLI logs to a file&quot;, &quot;required&quot;: false} |
| Input: logLevel | null | {&quot;description&quot;: &quot;One of: silent, error, warn, info, debug (default: info)&quot;, &quot;required&quot;: false} |
| Input: logPrefix | null | {&quot;description&quot;: &quot;Custom prefix for log messages (default: current timestamp)&quot;, &quot;required&quot;: false} |
| Input: onlyChanged | null | {&quot;description&quot;: &quot;Enables TurboSnap: Only run stories affected by files changed since the baseline build&quot;, &quot;required&quot;: false} |
| Input: onlyStoryFiles | null | {&quot;description&quot;: &quot;Only run a single story or a subset of stories by their filename(s)&quot;, &quot;required&quot;: false} |
| Input: onlyStoryNames | null | {&quot;description&quot;: &quot;Only run a single story or a subset of stories by their name&quot;, &quot;required&quot;: false} |
| Input: outputDir | null | {&quot;description&quot;: &quot;Relative path to target directory containing your Storybook (a temporary directory is used if this is not set)&quot;, &quot;required&quot;: false} |
| Input: playwright | null | {&quot;description&quot;: &quot;Run build against \`@chromatic-com/playwright\` test archives&quot;, &quot;required&quot;: false} |
| Input: preserveMissing | null | {&quot;description&quot;: &quot;Deprecated, use onlyChanged, onlyStoryNames or onlyStoryFiles instead&quot;, &quot;required&quot;: false} |
| Input: projectToken | null | {&quot;description&quot;: &quot;Your chromatic project token (best provided via env.CHROMATIC\_PROJECT\_TOKEN)&quot;, &quot;required&quot;: false} |
| Input: repositorySlug | null | {&quot;description&quot;: &quot;Override the repository slug (e.g. ownerName/repositoryName)&quot;, &quot;required&quot;: false} |
| Input: skip | null | {&quot;description&quot;: &quot;Skip Chromatic tests, but mark the commit as passing&quot;, &quot;required&quot;: false} |
| Input: skipUpdateCheck | null | {&quot;description&quot;: &quot;Skips Chromatic CLI update check&quot;, &quot;required&quot;: false} |
| Input: storybookBaseDir | null | {&quot;description&quot;: &quot;Relative path from repository root to Storybook project root&quot;, &quot;required&quot;: false} |
| Input: storybookBuildDir | null | {&quot;description&quot;: &quot;Provide a directory with your built storybook; use if you have already built your storybook&quot;, &quot;required&quot;: false} |
| Input: storybookConfigDir | null | {&quot;description&quot;: &quot;Relative path from where you run Chromatic to your Storybook config directory&quot;, &quot;required&quot;: false} |
| Input: storybookLogFile | null | {&quot;description&quot;: &quot;Write Storybook build logs to a file&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;description&quot;: &quot;Your github token&quot;, &quot;required&quot;: false} |
| Input: traceChanged | null | {&quot;description&quot;: &quot;Print dependency trace for changed files to affected story files; set to \\&quot;expanded\\&quot; to list individual modules&quot;, &quot;required&quot;: false} |
| Input: untraced | null | {&quot;description&quot;: &quot;Disregard these files and their dependencies when tracing dependent stories for TurboSnap&quot;, &quot;required&quot;: false} |
| Input: uploadMetadata | null | {&quot;description&quot;: &quot;Upload Chromatic metadata files as part of the published Storybook. Defaults to enabled when TurboSnap is requested.&quot;, &quot;required&quot;: false} |
| Input: vitest | null | {&quot;description&quot;: &quot;Run build against \`@chromatic-com/vitest\` test archives&quot;, &quot;required&quot;: false} |
| Input: workingDir | null | {&quot;description&quot;: &quot;Working directory for the package.json file&quot;, &quot;required&quot;: false} |
| Input: zip | null | {&quot;description&quot;: &quot;Publish your Storybook to Chromatic as a single zip file instead of individual content files&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;actualCaptureCount&quot;, &quot;buildUrl&quot;, &quot;changeCount&quot;, &quot;code&quot;, &quot;componentCount&quot;, &quot;errorCount&quot;, &quot;ignoredCount&quot;, &quot;inheritedCaptureCount&quot;, &quot;interactionTestFailuresCount&quot;, &quot;pendingCount&quot;, &quot;specCount&quot;, &quot;storybookUrl&quot;, &quot;testCount&quot;, &quot;url&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | e24559fbc78e0cda863f3889f0e40ac249b07e20 |
| Selected tag | null | v18.13.1 |

## crowdin/github-action

[Previous source](https://github.com/crowdin/github-action/tree/72955432d4aa4f6dd64cf17eeb88dd34d6ba064c/) · [Current source](https://github.com/crowdin/github-action/tree/959dc74ac104447731cba99a016f85d0ae719788/) · [Upstream code diff](https://github.com/crowdin/github-action/compare/72955432d4aa4f6dd64cf17eeb88dd34d6ba064c...959dc74ac104447731cba99a016f85d0ae719788)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 72955432d4aa4f6dd64cf17eeb88dd34d6ba064c | 959dc74ac104447731cba99a016f85d0ae719788 |
| Selected tag | v3.4.0 | v3.5.0 |

## expo/expo-github-action

[Previous source](https://github.com/expo/expo-github-action/tree/eab7a230208c952974db8c3245cfd78402c7b385/) · [Current source](https://github.com/expo/expo-github-action/tree/9da89d3617bb88139671bad31b09c65714c2ee06/) · [Upstream code diff](https://github.com/expo/expo-github-action/compare/eab7a230208c952974db8c3245cfd78402c7b385...9da89d3617bb88139671bad31b09c65714c2ee06)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | eab7a230208c952974db8c3245cfd78402c7b385 | 9da89d3617bb88139671bad31b09c65714c2ee06 |
| Selected tag | 9.0.0 | 9.0.1 |

## hermes-labs-ai/lintlang

[Previous source](https://github.com/hermes-labs-ai/lintlang/tree/6115fb5b86611b81e18144a9d9ec7111b68978f5/) · [Current source](https://github.com/hermes-labs-ai/lintlang/tree/645f57879ff5dbe3bbff37e9696834fb00371194/) · [Upstream code diff](https://github.com/hermes-labs-ai/lintlang/compare/6115fb5b86611b81e18144a9d9ec7111b68978f5...645f57879ff5dbe3bbff37e9696834fb00371194)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6115fb5b86611b81e18144a9d9ec7111b68978f5 | 645f57879ff5dbe3bbff37e9696834fb00371194 |
| Selected tag | v0.8.2 | v0.8.3 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/9a8e9d4106a7f11cabeb114978a053add388225e/) · [Current source](https://github.com/pullfrog/pullfrog/tree/ae4145b3d72b3f4aa045e2352dc6b2c7538daeeb/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/9a8e9d4106a7f11cabeb114978a053add388225e...ae4145b3d72b3f4aa045e2352dc6b2c7538daeeb)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9a8e9d4106a7f11cabeb114978a053add388225e | ae4145b3d72b3f4aa045e2352dc6b2c7538daeeb |
| Selected tag | v0.1.100 | v0.1.101 |

## pypa/cibuildwheel

[Previous source](https://github.com/pypa/cibuildwheel/tree/b3395e271a35f73dad77f21802abe9b986dfe299/) · [Current source](https://github.com/pypa/cibuildwheel/tree/8c2dcd2e96041a619f5ff03c9638d7941e2553a4/) · [Upstream code diff](https://github.com/pypa/cibuildwheel/compare/b3395e271a35f73dad77f21802abe9b986dfe299...8c2dcd2e96041a619f5ff03c9638d7941e2553a4)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b3395e271a35f73dad77f21802abe9b986dfe299 | 8c2dcd2e96041a619f5ff03c9638d7941e2553a4 |
| Selected tag | v4.3.1 | v4.3.3 |

## pypa/gh-action-pypi-publish

[Previous source](https://github.com/pypa/gh-action-pypi-publish/tree/dc37677b2e1c63e2034f94d8a5b11f265b73ba33/) · [Current source](https://github.com/pypa/gh-action-pypi-publish/tree/7245906fb61fa33a13554f9d5fb856fe61758086/) · [Upstream code diff](https://github.com/pypa/gh-action-pypi-publish/compare/dc37677b2e1c63e2034f94d8a5b11f265b73ba33...7245906fb61fa33a13554f9d5fb856fe61758086)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | dc37677b2e1c63e2034f94d8a5b11f265b73ba33 | 7245906fb61fa33a13554f9d5fb856fe61758086 |
| Selected tag | v1.14.2 | v1.14.3 |

## shaftoe/pi-coding-agent-action

[Previous source](https://github.com/shaftoe/pi-coding-agent-action/tree/f7496a9aea9798c5d52d39096d98d5c5b16559b3/) · [Current source](https://github.com/shaftoe/pi-coding-agent-action/tree/381f578da466b8d2ef48f0fdb8a940f276fe4c3c/) · [Upstream code diff](https://github.com/shaftoe/pi-coding-agent-action/compare/f7496a9aea9798c5d52d39096d98d5c5b16559b3...381f578da466b8d2ef48f0fdb8a940f276fe4c3c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f7496a9aea9798c5d52d39096d98d5c5b16559b3 | 381f578da466b8d2ef48f0fdb8a940f276fe4c3c |
| Selected tag | v2.30.0 | v2.30.1 |

## shogo82148/actions-setup-mysql

[Previous source](https://github.com/shogo82148/actions-setup-mysql/tree/1d4ebc60ba1227dd13fc7e6ba845bd3997928d75/) · [Current source](https://github.com/shogo82148/actions-setup-mysql/tree/64d04a653a0c02af310009d36ce74bec5f4dce4f/) · [Upstream code diff](https://github.com/shogo82148/actions-setup-mysql/compare/1d4ebc60ba1227dd13fc7e6ba845bd3997928d75...64d04a653a0c02af310009d36ce74bec5f4dce4f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 1d4ebc60ba1227dd13fc7e6ba845bd3997928d75 | 64d04a653a0c02af310009d36ce74bec5f4dce4f |
| Selected tag | v1.54.2 | v1.55.0 |

## Swatinem/rust-cache

[Previous source](https://github.com/Swatinem/rust-cache/tree/6323deb102c322ba6fcbdcafc7e3dddab59af2b6/) · [Current source](https://github.com/Swatinem/rust-cache/tree/d1527c8f67ef9af357290475d4af4b0fab8f12e0/) · [Upstream code diff](https://github.com/Swatinem/rust-cache/compare/6323deb102c322ba6fcbdcafc7e3dddab59af2b6...d1527c8f67ef9af357290475d4af4b0fab8f12e0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6323deb102c322ba6fcbdcafc7e3dddab59af2b6 | d1527c8f67ef9af357290475d4af4b0fab8f12e0 |
| Selected tag | v2.9.2 | v2.9.3 |

## upptime/uptime-monitor

[Previous source](https://github.com/upptime/uptime-monitor/tree/9aa4499dce16aa3b144134cd767cb5a6aeb9660d/) · [Current source](https://github.com/upptime/uptime-monitor/tree/6d218cca63a6249035b9f3b52765ee501cf88b20/) · [Upstream code diff](https://github.com/upptime/uptime-monitor/compare/9aa4499dce16aa3b144134cd767cb5a6aeb9660d...6d218cca63a6249035b9f3b52765ee501cf88b20)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9aa4499dce16aa3b144134cd767cb5a6aeb9660d | 6d218cca63a6249035b9f3b52765ee501cf88b20 |
| Selected tag | v1.46.2 | v1.46.3 |

## vmactions/openbsd-vm

[Previous source](https://github.com/vmactions/openbsd-vm/tree/5f7b2c933b8846a138361d6843c52af4bef5d945/) · [Current source](https://github.com/vmactions/openbsd-vm/tree/f1ca8bc8ecc5b6ef7218e5b914836e067e1546d3/) · [Upstream code diff](https://github.com/vmactions/openbsd-vm/compare/5f7b2c933b8846a138361d6843c52af4bef5d945...f1ca8bc8ecc5b6ef7218e5b914836e067e1546d3)

| Changed | Before | After |
| --- | --- | --- |
| Input: cache-after-prepare-key-suffix | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional. Extra value appended to the cache-after-prepare cache key. Change it to discard the prepared VM image cache and run prepare again. Default is empty.&quot;, &quot;required&quot;: false} |
| Selected SHA | 5f7b2c933b8846a138361d6843c52af4bef5d945 | f1ca8bc8ecc5b6ef7218e5b914836e067e1546d3 |
| Selected tag | v1.4.8 | v1.4.9 |

## yokawasa/action-setup-kube-tools

[Previous source](https://github.com/yokawasa/action-setup-kube-tools/tree/b16d49b2c459d33cf9d4c300a220ef0bcdbc730a/) · [Current source](https://github.com/yokawasa/action-setup-kube-tools/tree/f8b2f6cdd1eb8575530049beacfe5d04c0ea8944/) · [Upstream code diff](https://github.com/yokawasa/action-setup-kube-tools/compare/b16d49b2c459d33cf9d4c300a220ef0bcdbc730a...f8b2f6cdd1eb8575530049beacfe5d04c0ea8944)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b16d49b2c459d33cf9d4c300a220ef0bcdbc730a | f8b2f6cdd1eb8575530049beacfe5d04c0ea8944 |
| Selected tag | v0.14.0 | v0.14.1 |
