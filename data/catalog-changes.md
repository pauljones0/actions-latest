# Latest catalog changes

3 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## jurplel/install-qt-action

[Previous source](https://github.com/jurplel/install-qt-action) · [Current source](https://github.com/jurplel/install-qt-action/tree/a9c63c7c123f3069cff414e7e482d95dfa9d8125/)

| Changed | Before | After |
| --- | --- | --- |
| Input: add-tools-to-path | null | {&quot;default&quot;: true, &quot;description&quot;: &quot;When true, prepends directories of tools to PATH environment variable.&quot;} |
| Input: aqtsource | null | {&quot;description&quot;: &quot;Location to source aqtinstall from in case of issues&quot;} |
| Input: aqtversion | null | {&quot;default&quot;: &quot;==3.3.\*&quot;, &quot;description&quot;: &quot;Version of aqtinstall to use in case of issues&quot;} |
| Input: arch | null | {&quot;description&quot;: &quot;Architecture for Windows/Android&quot;} |
| Input: archives | null | {&quot;description&quot;: &quot;Specify which Qt archive to install&quot;} |
| Input: cache | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Whether or not to cache Qt automatically&quot;} |
| Input: cache-key-prefix | null | {&quot;default&quot;: &quot;install-qt-action&quot;, &quot;description&quot;: &quot;Cache key prefix for automatic cache&quot;} |
| Input: dir | null | {&quot;description&quot;: &quot;Directory to install Qt&quot;} |
| Input: doc-archives | null | {&quot;description&quot;: &quot;Space-separated list of .7z docs archives to install. Used to reduce download/image sizes.&quot;} |
| Input: doc-modules | null | {&quot;description&quot;: &quot;Space-separated list of additional documentation modules to install.&quot;} |
| Input: documentation | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Whether or not to install Qt documentation.&quot;} |
| Input: email | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Your Qt email&quot;} |
| Input: example-archives | null | {&quot;description&quot;: &quot;Space-separated list of .7z example archives to install. Used to reduce download/image sizes.&quot;} |
| Input: example-modules | null | {&quot;description&quot;: &quot;Space-separated list of additional example modules to install.&quot;} |
| Input: examples | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Whether or not to install Qt example code.&quot;} |
| Input: extra | null | {&quot;description&quot;: &quot;Any extra arguments to append to the back&quot;} |
| Input: host | null | {&quot;description&quot;: &quot;Host platform&quot;} |
| Input: install-deps | null | {&quot;default&quot;: true, &quot;description&quot;: &quot;Whether or not to install Qt dependencies on Linux&quot;} |
| Input: modules | null | {&quot;description&quot;: &quot;Additional Qt modules to install&quot;} |
| Input: no-qt-binaries | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Turns off installation of Qt. Useful for installing tools, source, documentation, or examples.&quot;} |
| Input: pw | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Your Qt password&quot;} |
| Input: py7zrversion | null | {&quot;default&quot;: &quot;==1.1.0&quot;, &quot;description&quot;: &quot;Version of py7zr to use in case of issues&quot;} |
| Input: set-env | null | {&quot;default&quot;: true, &quot;description&quot;: &quot;Whether or not to set environment variables after running aqtinstall&quot;} |
| Input: setup-python | null | {&quot;default&quot;: true, &quot;description&quot;: &quot;Whether or not to automatically run setup-python to find a valid python version.&quot;} |
| Input: source | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Whether or not to install Qt source code.&quot;} |
| Input: src-archives | null | {&quot;description&quot;: &quot;Space-separated list of .7z source archives to install. Used to reduce download/image sizes.&quot;} |
| Input: target | null | {&quot;default&quot;: &quot;desktop&quot;, &quot;description&quot;: &quot;Target platform for build&quot;} |
| Input: tools | null | {&quot;description&quot;: &quot;Qt tools to download -- specify comma-separated argument lists which are themselves separated by spaces: &lt;tool\_name&gt;,&lt;tool\_version&gt;,&lt;tool\_arch&gt;\\n&quot;} |
| Input: tools-only | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Synonym for \`no-qt-binaries\`, used for backwards compatibility.&quot;} |
| Input: use-official | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Whether to use aqtinstall to install Qt using the official installer, requires email &amp; pw&quot;} |
| Input: version | null | {&quot;default&quot;: &quot;6.8.3&quot;, &quot;description&quot;: &quot;Version of Qt to install&quot;} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | composite |
| Security | unknown | clean |
| Selected SHA | null | a9c63c7c123f3069cff414e7e482d95dfa9d8125 |
| Selected tag | null | v4.4.1 |

## renovatebot/github-action

[Previous source](https://github.com/renovatebot/github-action/tree/e26264186543fd355dc60776e21f7fbb67ce6f85/) · [Current source](https://github.com/renovatebot/github-action/tree/9fea9f0fbf80401026d11d03911d62b1f70fef1f/) · [Upstream code diff](https://github.com/renovatebot/github-action/compare/e26264186543fd355dc60776e21f7fbb67ce6f85...9fea9f0fbf80401026d11d03911d62b1f70fef1f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e26264186543fd355dc60776e21f7fbb67ce6f85 | 9fea9f0fbf80401026d11d03911d62b1f70fef1f |
| Selected tag | v46.3.2 | v46.3.3 |

## upptime/uptime-monitor

[Previous source](https://github.com/upptime/uptime-monitor/tree/2e53e7570ad597ccf3f251d43502846a042165d2/) · [Current source](https://github.com/upptime/uptime-monitor/tree/8be193bbcb957a3a917d2bb16a0c96959778a889/) · [Upstream code diff](https://github.com/upptime/uptime-monitor/compare/2e53e7570ad597ccf3f251d43502846a042165d2...8be193bbcb957a3a917d2bb16a0c96959778a889)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2e53e7570ad597ccf3f251d43502846a042165d2 | 8be193bbcb957a3a917d2bb16a0c96959778a889 |
| Selected tag | v1.44.0 | v1.44.1 |
