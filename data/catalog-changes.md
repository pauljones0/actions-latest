# Latest catalog changes

13 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/f431adaf77e0fecf918431e75a2b5b45b85af002/) · [Current source](https://github.com/anthropics/claude-code-action/tree/c84e279f859e2591391e95bd309286eb111c345f/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/f431adaf77e0fecf918431e75a2b5b45b85af002...c84e279f859e2591391e95bd309286eb111c345f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f431adaf77e0fecf918431e75a2b5b45b85af002 | c84e279f859e2591391e95bd309286eb111c345f |
| Selected tag | v1.0.283 | v1.0.284 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/3b8cdc5a65cbdf4a53b441f1c9d0255c20aa92f6/) · [Current source](https://github.com/asklokesh/loki-mode/tree/e614a9c0ca51c93943395dd905bc05677f3b517b/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/3b8cdc5a65cbdf4a53b441f1c9d0255c20aa92f6...e614a9c0ca51c93943395dd905bc05677f3b517b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 3b8cdc5a65cbdf4a53b441f1c9d0255c20aa92f6 | e614a9c0ca51c93943395dd905bc05677f3b517b |
| Selected tag | v11.161.0 | v11.170.0 |

## aws-actions/sustainability-scanner

[Previous source](https://github.com/aws-actions/sustainability-scanner/tree/e9cc38a79df82ee4130722108aad2f87a2083fa2/) · [Current source](https://github.com/aws-actions/sustainability-scanner/tree/f29275aa264da97e6e1f1cda9502554739e91ad9/) · [Upstream code diff](https://github.com/aws-actions/sustainability-scanner/compare/e9cc38a79df82ee4130722108aad2f87a2083fa2...f29275aa264da97e6e1f1cda9502554739e91ad9)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e9cc38a79df82ee4130722108aad2f87a2083fa2 | f29275aa264da97e6e1f1cda9502554739e91ad9 |
| Selected tag | v1.4.1 | v1.5.0 |

## chromaui/action

[Previous source](https://github.com/chromaui/action/tree/b46fae7df99a74cc2201b00cb59ec498c3346530/) · [Current source](https://github.com/chromaui/action/tree/9cb4d65a86fe1c4c67a76a8d90f35a51a118e55f/) · [Upstream code diff](https://github.com/chromaui/action/compare/b46fae7df99a74cc2201b00cb59ec498c3346530...9cb4d65a86fe1c4c67a76a8d90f35a51a118e55f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b46fae7df99a74cc2201b00cb59ec498c3346530 | 9cb4d65a86fe1c4c67a76a8d90f35a51a118e55f |
| Selected tag | v18.15.0 | v18.15.1 |

## coursier/setup-action

[Previous source](https://github.com/coursier/setup-action/tree/d5a17f9aaeb260f9ba336a5b582fb49f79c64ac4/) · [Current source](https://github.com/coursier/setup-action/tree/6eefb29fad2c9de9f52a5f2cef1154195c9d4609/) · [Upstream code diff](https://github.com/coursier/setup-action/compare/d5a17f9aaeb260f9ba336a5b582fb49f79c64ac4...6eefb29fad2c9de9f52a5f2cef1154195c9d4609)

| Changed | Before | After |
| --- | --- | --- |
| Input: apps | {&quot;default&quot;: &quot;sbtn&quot;, &quot;description&quot;: &quot;Whitespace- or newline-separated list of apps to install from the Coursier main and contrib channels (set to an empty string to install none)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;sbtn&quot;, &quot;description&quot;: &quot;Whitespace- or newline-separated list of apps to install from the Coursier main and contrib channels, optionally pinned to a version with app:version, like sbt:1.10.7 or scalafmt:3.8.3 (set to an empty string to install none)&quot;, &quot;required&quot;: false} |
| Input: customRepositories | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Pipe-separated (\|) list of extra repositories passed to every cs command. See https://get-coursier.io/docs/other-repositories&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;List of extra repositories passed to every cs command, separated by pipes (\|) or newlines. Empty entries are ignored. See https://get-coursier.io/docs/other-repositories&quot;, &quot;required&quot;: false} |
| Input: extraJvmArgs | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Space-separated list of -D JVM property args passed to every cs invocation. The -J prefix is added automatically if missing (e.g. -Dhttps.proxyHost=proxy.example.com -Dhttps.proxyPort=8080)&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;JVM arguments passed to every cs invocation: -D&lt;key&gt;\[=&lt;value&gt;\] properties, -Xmx / -Xms / -Xss memory settings and -XX: options, optionally prefixed with -J (e.g. -Xmx2g -Dhttps.proxyHost=proxy.example.com). Space-separated, or one argument per line, allowing spaces in values, when the input spans several lines. Native launchers only get -D properties.&quot;, &quot;required&quot;: false} |
| Input: jvm | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;JVM to install, such as \\&quot;21\\&quot; or \\&quot;temurin:21\\&quot; (see cs java --available). When empty, an existing JAVA\_HOME is kept, or Coursier&#x27;s default JVM is installed.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;JVM to install, such as \\&quot;21\\&quot; or \\&quot;temurin:21\\&quot; (see cs java --available). When empty, an existing JAVA\_HOME is kept if it contains bin/java (bin/java.exe on Windows), else Coursier&#x27;s default JVM is installed (with a warning if JAVA\_HOME was set but invalid).&quot;, &quot;required&quot;: false} |
| Selected SHA | d5a17f9aaeb260f9ba336a5b582fb49f79c64ac4 | 6eefb29fad2c9de9f52a5f2cef1154195c9d4609 |
| Selected tag | v3.1.0 | v3.1.1 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/436a838c4e177cdfec37bfdb080957b8f1d576aa/) · [Current source](https://github.com/duriantaco/skylos/tree/87978e69adf91b3811e97b00c40aa39d7937cd94/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/436a838c4e177cdfec37bfdb080957b8f1d576aa...87978e69adf91b3811e97b00c40aa39d7937cd94)

| Changed | Before | After |
| --- | --- | --- |
| Input: diff | null | {&quot;default&quot;: &quot;auto&quot;, &quot;description&quot;: &quot;On pull requests, scan and gate only the lines the PR changes (&#x27;auto&#x27;, the default), so findings already in the repository don&#x27;t fail it. &#x27;false&#x27; scans the whole repository. With a shallow checkout the action fetches the history it needs; set fetch-depth: 0 on actions/checkout to skip that.&quot;, &quot;required&quot;: false} |
| Selected SHA | 436a838c4e177cdfec37bfdb080957b8f1d576aa | 87978e69adf91b3811e97b00c40aa39d7937cd94 |
| Selected tag | v5.6.0 | v5.7.0 |

## EmbarkStudios/cargo-deny-action

[Previous source](https://github.com/EmbarkStudios/cargo-deny-action/tree/70f81531115945ba6eb6b941ec9d39d063438eb9/) · [Current source](https://github.com/EmbarkStudios/cargo-deny-action/tree/17aeb3c839e42274e2b8adf721c8c65edfdc74dd/) · [Upstream code diff](https://github.com/EmbarkStudios/cargo-deny-action/compare/70f81531115945ba6eb6b941ec9d39d063438eb9...17aeb3c839e42274e2b8adf721c8c65edfdc74dd)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 70f81531115945ba6eb6b941ec9d39d063438eb9 | 17aeb3c839e42274e2b8adf721c8c65edfdc74dd |
| Selected tag | v2.1.2 | v2.1.3 |

## github/codeql-action

[Previous source](https://github.com/github/codeql-action/tree/33d7b85da1a04171e211befe2c739303b9a4c066/) · [Current source](https://github.com/github/codeql-action/tree/1bd86f2fdb4b86187fa4059f16f31a3202acc9ea/) · [Upstream code diff](https://github.com/github/codeql-action/compare/33d7b85da1a04171e211befe2c739303b9a4c066...1bd86f2fdb4b86187fa4059f16f31a3202acc9ea)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 33d7b85da1a04171e211befe2c739303b9a4c066 | 1bd86f2fdb4b86187fa4059f16f31a3202acc9ea |
| Selected tag | v4.39.3 | v4.39.4 |

## JetBrains/qodana-action

[Previous source](https://github.com/JetBrains/qodana-action/tree/13e3acbbaeb2cbfc37893b98e74594985edf42eb/) · [Current source](https://github.com/JetBrains/qodana-action/tree/aa698739cd4b8204ad53291bea7e16cd75da3c9f/) · [Upstream code diff](https://github.com/JetBrains/qodana-action/compare/13e3acbbaeb2cbfc37893b98e74594985edf42eb...aa698739cd4b8204ad53291bea7e16cd75da3c9f)

| Changed | Before | After |
| --- | --- | --- |
| Input: additional-cache-key | {&quot;default&quot;: &quot;qodana-2026.2-${{ github.ref }}&quot;, &quot;description&quot;: &quot;Set the additional cache key&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;qodana-2026.3-${{ github.ref }}&quot;, &quot;description&quot;: &quot;Set the additional cache key&quot;, &quot;required&quot;: false} |
| Input: nightly-version | {&quot;default&quot;: &quot;&quot;, &quot;deprecationMessage&quot;: &quot;This option is for development purposes only. Do not use it in production.&quot;, &quot;description&quot;: &quot;Qodana CLI nightly version to use (e.g. 2026.2 or latest). Downloads CLI from tag v{version}-nightly.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;deprecationMessage&quot;: &quot;This option is for development purposes only. Do not use it in production.&quot;, &quot;description&quot;: &quot;Qodana CLI nightly version to use (e.g. 2026.3 or latest). Downloads CLI from tag v{version}-nightly.&quot;, &quot;required&quot;: false} |
| Input: primary-cache-key | {&quot;default&quot;: &quot;qodana-2026.2-${{ github.ref }}-${{ github.sha }}&quot;, &quot;description&quot;: &quot;Set the primary cache key&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;qodana-2026.3-${{ github.ref }}-${{ github.sha }}&quot;, &quot;description&quot;: &quot;Set the primary cache key&quot;, &quot;required&quot;: false} |
| Selected SHA | 13e3acbbaeb2cbfc37893b98e74594985edf42eb | aa698739cd4b8204ad53291bea7e16cd75da3c9f |
| Selected tag | v2026.2.4 | v2026.3.1 |

## node9-ai/node9-proxy

[Previous source](https://github.com/node9-ai/node9-proxy/tree/094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59/) · [Current source](https://github.com/node9-ai/node9-proxy/tree/d12ef7dc57652589f3358a75571a612c8dfd66c9/) · [Upstream code diff](https://github.com/node9-ai/node9-proxy/compare/094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59...d12ef7dc57652589f3358a75571a612c8dfd66c9)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 094b4fb1d72ea3b0ee5bb47755aad1d0433c1e59 | d12ef7dc57652589f3358a75571a612c8dfd66c9 |
| Selected tag | v2.65.6 | v2.65.8 |

## openqodex/openqodex

[Previous source](https://github.com/openqodex/openqodex/tree/e92228a3b0611d4641acf69abbd2c7c3c089599b/) · [Current source](https://github.com/openqodex/openqodex/tree/9d057d09347c5ce3ada31d214156760a5be55a12/) · [Upstream code diff](https://github.com/openqodex/openqodex/compare/e92228a3b0611d4641acf69abbd2c7c3c089599b...9d057d09347c5ce3ada31d214156760a5be55a12)

| Changed | Before | After |
| --- | --- | --- |
| Input: version | {&quot;default&quot;: &quot;0.20.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;0.22.0&quot;, &quot;description&quot;: &quot;The openqodex version to run, an exact release version such as 0.6.1. The release workflow sets the default to the version it publishes.&quot;, &quot;required&quot;: false} |
| Selected SHA | e92228a3b0611d4641acf69abbd2c7c3c089599b | 9d057d09347c5ce3ada31d214156760a5be55a12 |
| Selected tag | v0.20.0 | v0.22.0 |

## Added: reagento/relator

[Source](https://github.com/reagento/relator) — Send Telegram and Discord notifications for new GitHub issues or PRs

New entries still require observed stability and fresh scan evidence before usage.

## stefanzweifel/changelog-updater-action

[Previous source](https://github.com/stefanzweifel/changelog-updater-action/tree/1171d74932456fd2049c486b8757956a6adcc11b/) · [Current source](https://github.com/stefanzweifel/changelog-updater-action/tree/f7c43fed0c8760b25199be6eae5c28fc22830ec6/) · [Upstream code diff](https://github.com/stefanzweifel/changelog-updater-action/compare/1171d74932456fd2049c486b8757956a6adcc11b...f7c43fed0c8760b25199be6eae5c28fc22830ec6)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 1171d74932456fd2049c486b8757956a6adcc11b | f7c43fed0c8760b25199be6eae5c28fc22830ec6 |
| Selected tag | v1.13.0 | v1.13.3 |
