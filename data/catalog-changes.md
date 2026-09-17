# Latest catalog changes

25 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## actions/setup-java

[Previous source](https://github.com/actions/setup-java/tree/dd06d9cba3e5552c54d9f8ea23572deb30010f7c/) · [Current source](https://github.com/actions/setup-java/tree/de7274f081f381c8f8158605e0321c36c376e2e6/) · [Upstream code diff](https://github.com/actions/setup-java/compare/dd06d9cba3e5552c54d9f8ea23572deb30010f7c...de7274f081f381c8f8158605e0321c36c376e2e6)

| Changed | Before | After |
| --- | --- | --- |
| Input: verify-signature | {&quot;description&quot;: &quot;Verify downloaded Java package signatures when supported by the selected distribution&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Check downloaded Java package signatures when supported by the selected distribution. When omitted, failures produce warnings. Explicitly setting this to true enforces verification and makes failures fatal, including failures caused by an unexpected vendor signing-key rotation.&quot;, &quot;required&quot;: false} |
| Input: verify-signature-public-key | {&quot;description&quot;: &quot;ASCII-armored GPG public key used to verify the downloaded package signature. Overrides the default bundled key for the selected distribution.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;One or more ASCII-armored GPG public keys used to verify downloaded package signatures. Concatenate multiple armored key blocks. Custom keys replace the bundled keys for the selected distribution.&quot;, &quot;required&quot;: false} |
| Selected SHA | dd06d9cba3e5552c54d9f8ea23572deb30010f7c | de7274f081f381c8f8158605e0321c36c376e2e6 |
| Selected tag | v6.0.0 | v6.0.1 |

## aminya/setup-cpp

[Previous source](https://github.com/aminya/setup-cpp/tree/59179aabb1f9453d12daf81c00d789af3b67b1a6/) · [Current source](https://github.com/aminya/setup-cpp/tree/15a6bd8cf39030f88b5da3d203a829ec4eea4955/) · [Upstream code diff](https://github.com/aminya/setup-cpp/compare/59179aabb1f9453d12daf81c00d789af3b67b1a6...15a6bd8cf39030f88b5da3d203a829ec4eea4955)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 59179aabb1f9453d12daf81c00d789af3b67b1a6 | 15a6bd8cf39030f88b5da3d203a829ec4eea4955 |
| Selected tag | v1.10.0 | v1.10.1 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/5ccc3a35a6367cdb8e6fbd0728287467540ecfe2/) · [Current source](https://github.com/anthropics/claude-code-action/tree/19dda84776b3518d98b8798e591daee763049ed3/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/5ccc3a35a6367cdb8e6fbd0728287467540ecfe2...19dda84776b3518d98b8798e591daee763049ed3)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5ccc3a35a6367cdb8e6fbd0728287467540ecfe2 | 19dda84776b3518d98b8798e591daee763049ed3 |
| Selected tag | v1.0.219 | v1.0.220 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/e71827db642cfffc91dd661e668e8953d341dc16/) · [Current source](https://github.com/asklokesh/loki-mode/tree/95a6f54149a82f0d54d9f6d3275461cad18f0fc0/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/e71827db642cfffc91dd661e668e8953d341dc16...95a6f54149a82f0d54d9f6d3275461cad18f0fc0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | e71827db642cfffc91dd661e668e8953d341dc16 | 95a6f54149a82f0d54d9f6d3275461cad18f0fc0 |
| Selected tag | v9.22.13 | v9.26.3 |

## aws-actions/aws-secretsmanager-get-secrets

[Previous source](https://github.com/aws-actions/aws-secretsmanager-get-secrets/tree/2cb1a461cbd4865ac4299648312e4704c646cd53/) · [Current source](https://github.com/aws-actions/aws-secretsmanager-get-secrets/tree/2297f9a879480a9e3af9b293ed15c70caf8e1c88/) · [Upstream code diff](https://github.com/aws-actions/aws-secretsmanager-get-secrets/compare/2cb1a461cbd4865ac4299648312e4704c646cd53...2297f9a879480a9e3af9b293ed15c70caf8e1c88)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2cb1a461cbd4865ac4299648312e4704c646cd53 | 2297f9a879480a9e3af9b293ed15c70caf8e1c88 |
| Selected tag | v3.0.1 | v3.0.2 |

## Azure/login

[Previous source](https://github.com/Azure/login/tree/7ddb5af1ef8758cf1353cf3b42f940aee27ba21c/) · [Current source](https://github.com/Azure/login/tree/a641126d1b8aa4d1fa005f4f92df94a3a4c4c906/) · [Upstream code diff](https://github.com/Azure/login/compare/7ddb5af1ef8758cf1353cf3b42f940aee27ba21c...a641126d1b8aa4d1fa005f4f92df94a3a4c4c906)

| Changed | Before | After |
| --- | --- | --- |
| Input: mask-client-id | null | {&quot;default&quot;: true, &quot;description&quot;: &quot;Set this value to false to stop registering the client-id as a secret, so it is not masked in workflow logs&quot;, &quot;required&quot;: false} |
| Input: max-context-population | null | {&quot;description&quot;: &quot;Only used when enable-AzPSSession is true. Overrides the Azure PowerShell MaxContextPopulation used by Connect-AzAccount (the number of subscription contexts loaded). Set to -1 to load all subscriptions, or a positive integer. When unset, the Azure PowerShell default of 25 applies.&quot;, &quot;required&quot;: false} |
| Selected SHA | 7ddb5af1ef8758cf1353cf3b42f940aee27ba21c | a641126d1b8aa4d1fa005f4f92df94a3a4c4c906 |
| Selected tag | v3.0.2 | v3.1.0 |

## bridgecrewio/checkov-action

[Previous source](https://github.com/bridgecrewio/checkov-action/tree/f967808197a8d784d3e72919f38c3ff0cda7884e/) · [Current source](https://github.com/bridgecrewio/checkov-action/tree/a8664e3a0549367977f0cda990a34311835c87c0/) · [Upstream code diff](https://github.com/bridgecrewio/checkov-action/compare/f967808197a8d784d3e72919f38c3ff0cda7884e...a8664e3a0549367977f0cda990a34311835c87c0)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f967808197a8d784d3e72919f38c3ff0cda7884e | a8664e3a0549367977f0cda990a34311835c87c0 |
| Selected tag | v12.3122.0 | v12.3123.0 |

## DeterminateSystems/flake-checker-action

[Previous source](https://github.com/DeterminateSystems/flake-checker-action/tree/de924abd783455e8429c858962b9e43062d19da1/) · [Current source](https://github.com/DeterminateSystems/flake-checker-action/tree/786422608c7bded2bbc9741ad9f91356842bf520/) · [Upstream code diff](https://github.com/DeterminateSystems/flake-checker-action/compare/de924abd783455e8429c858962b9e43062d19da1...786422608c7bded2bbc9741ad9f91356842bf520)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | de924abd783455e8429c858962b9e43062d19da1 | 786422608c7bded2bbc9741ad9f91356842bf520 |
| Selected tag | v13 | v14 |

## DeterminateSystems/flakehub-push

[Previous source](https://github.com/DeterminateSystems/flakehub-push/tree/71f57208810a5d299fc6545350981de98fdbc860/) · [Current source](https://github.com/DeterminateSystems/flakehub-push/tree/e001ee821cdb763ef120c01f1048bfb2f938bb9c/) · [Upstream code diff](https://github.com/DeterminateSystems/flakehub-push/compare/71f57208810a5d299fc6545350981de98fdbc860...e001ee821cdb763ef120c01f1048bfb2f938bb9c)

| Changed | Before | After |
| --- | --- | --- |
| Input: rev | null | {&quot;default&quot;: null, &quot;description&quot;: &quot;The Git revision SHA to use for non-rolling releases.&quot;, &quot;required&quot;: false} |
| Input: rolling-major | null | {&quot;default&quot;: null, &quot;description&quot;: &quot;Specify the SemVer major version of your rolling releases. All releases will follow the versioning scheme &#x27;\[rolling-major\].\[rolling-minor\].\[commit count\]+rev-\[git sha\]&#x27;&quot;, &quot;required&quot;: false} |
| Input: rolling-minor | {&quot;default&quot;: null, &quot;description&quot;: &quot;Specify the SemVer minor version of your rolling releases. All releases will follow the versioning scheme &#x27;0.\[rolling-minor\].\[commit count\]+rev-\[git sha\]&#x27;&quot;, &quot;required&quot;: false} | {&quot;default&quot;: null, &quot;description&quot;: &quot;Specify the SemVer minor version of your rolling releases. All releases will follow the versioning scheme &#x27;\[rolling-major\].\[rolling-minor\].\[commit count\]+rev-\[git sha\]&#x27;&quot;, &quot;required&quot;: false} |
| Input: sbom-path | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;The path to the SBOM for this flake.&quot;, &quot;required&quot;: false} |
| Runtime | node20 | node24 |
| Selected SHA | 71f57208810a5d299fc6545350981de98fdbc860 | e001ee821cdb763ef120c01f1048bfb2f938bb9c |
| Selected tag | v6 | v7 |

## DeterminateSystems/magic-nix-cache-action

[Previous source](https://github.com/DeterminateSystems/magic-nix-cache-action/tree/908b263ff629f4cc17666315b7fd3ec127c6244d/) · [Current source](https://github.com/DeterminateSystems/magic-nix-cache-action/tree/84c0677f58dcedf3b91f8223ce36a9ea5b3c84b7/) · [Upstream code diff](https://github.com/DeterminateSystems/magic-nix-cache-action/compare/908b263ff629f4cc17666315b7fd3ec127c6244d...84c0677f58dcedf3b91f8223ce36a9ea5b3c84b7)

| Changed | Before | After |
| --- | --- | --- |
| Input: source-checksums-sha256 | null | {&quot;description&quot;: &quot;Pinned SHA-256 (hex) of the file served at \`source-checksums-url\`. Must be set together with\\n\`source-checksums-url\`.\\n&quot;, &quot;required&quot;: false} |
| Input: source-checksums-url | null | {&quot;description&quot;: &quot;URL of a \`shasum\`-format checksums file listing the SHA-256 of each artifact. Used together\\nwith \`source-checksums-sha256\` to verify the downloaded installer.\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | 908b263ff629f4cc17666315b7fd3ec127c6244d | 84c0677f58dcedf3b91f8223ce36a9ea5b3c84b7 |
| Selected tag | v14 | v15 |

## DeterminateSystems/nix-installer-action

[Previous source](https://github.com/DeterminateSystems/nix-installer-action/tree/ef8a148080ab6020fd15196c2084a2eea5ff2d25/) · [Current source](https://github.com/DeterminateSystems/nix-installer-action/tree/3138316df39ed29be04236d7ffc686fa525866aa/) · [Upstream code diff](https://github.com/DeterminateSystems/nix-installer-action/compare/ef8a148080ab6020fd15196c2084a2eea5ff2d25...3138316df39ed29be04236d7ffc686fa525866aa)

| Changed | Before | After |
| --- | --- | --- |
| Input: source-checksums-sha256 | null | {&quot;description&quot;: &quot;Pinned SHA-256 (hex) of the file served at \`source-checksums-url\`. Must\\nbe set together with \`source-checksums-url\`.\\n&quot;, &quot;required&quot;: false} |
| Input: source-checksums-url | null | {&quot;description&quot;: &quot;URL of a \`shasum\`-format checksums file listing the SHA-256 of each\\n\`nix-installer-&lt;arch&gt;-&lt;os&gt;\` artifact. Used together with\\n\`source-checksums-sha256\` to verify the downloaded installer.\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | ef8a148080ab6020fd15196c2084a2eea5ff2d25 | 3138316df39ed29be04236d7ffc686fa525866aa |
| Selected tag | v22 | v23 |

## DeterminateSystems/update-flake-lock

[Previous source](https://github.com/DeterminateSystems/update-flake-lock/tree/834c491b2ece4de0bbd00d85214bb5e83b4da5c6/) · [Current source](https://github.com/DeterminateSystems/update-flake-lock/tree/da03c0f078bc4b2c37ee4f7e072d34bf8f188bb3/) · [Upstream code diff](https://github.com/DeterminateSystems/update-flake-lock/compare/834c491b2ece4de0bbd00d85214bb5e83b4da5c6...da03c0f078bc4b2c37ee4f7e072d34bf8f188bb3)

| Changed | Before | After |
| --- | --- | --- |
| Input: push-to-fork | null | {&quot;description&quot;: &quot;A fork of the checked out parent repository to which the pull request branch will be pushed. e.g. \`owner/repo-fork\`. The pull request will be created to merge the fork&#x27;s branch into the parent&#x27;s base.&quot;, &quot;required&quot;: false} |
| Selected SHA | 834c491b2ece4de0bbd00d85214bb5e83b4da5c6 | da03c0f078bc4b2c37ee4f7e072d34bf8f188bb3 |
| Selected tag | v28 | v29 |

## Added: gensecaihq/Shai-Hulud-2.0-Detector

[Source](https://github.com/gensecaihq/Shai-Hulud-2.0-Detector) — Detect Shai-Hulud npm supply chain attacks (2.0 + ChainDrop) - 1,240+ packages, SHA256 hashing, IDE persistence &amp; backdoor detection

New entries still require observed stability and fresh scan evidence before usage.

## github-community-projects/issue-metrics

[Previous source](https://github.com/github-community-projects/issue-metrics/tree/61084fa9599a62c7821f06602e180a42d1c7a205/) · [Current source](https://github.com/github-community-projects/issue-metrics/tree/a7dc2fb675661e208d4fc6fa321a6b95fc4a06f9/) · [Upstream code diff](https://github.com/github-community-projects/issue-metrics/compare/61084fa9599a62c7821f06602e180a42d1c7a205...a7dc2fb675661e208d4fc6fa321a6b95fc4a06f9)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 61084fa9599a62c7821f06602e180a42d1c7a205 | a7dc2fb675661e208d4fc6fa321a6b95fc4a06f9 |
| Selected tag | v5.0.1 | v5.0.2 |

## github/codeql-action

[Previous source](https://github.com/github/codeql-action/tree/cdf488f595d80d6e07e03d4674febd5ab45fa938/) · [Current source](https://github.com/github/codeql-action/tree/b96794f015dfd88f77b49b1c93e0fa7110f94c63/) · [Upstream code diff](https://github.com/github/codeql-action/compare/cdf488f595d80d6e07e03d4674febd5ab45fa938...b96794f015dfd88f77b49b1c93e0fa7110f94c63)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | cdf488f595d80d6e07e03d4674febd5ab45fa938 | b96794f015dfd88f77b49b1c93e0fa7110f94c63 |
| Selected tag | v4.37.9 | v4.38.0 |

## jfrog/frogbot

[Previous source](https://github.com/jfrog/frogbot/tree/6bd943187b61eba578e53b5316e804cd16fb5f9a/) · [Current source](https://github.com/jfrog/frogbot/tree/98d710f28baab51f18800cdbbada700f245e9933/) · [Upstream code diff](https://github.com/jfrog/frogbot/compare/6bd943187b61eba578e53b5316e804cd16fb5f9a...98d710f28baab51f18800cdbbada700f245e9933)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6bd943187b61eba578e53b5316e804cd16fb5f9a | 98d710f28baab51f18800cdbbada700f245e9933 |
| Selected tag | v3.6.0 | v3.7.0 |

## laminas/automatic-releases

[Previous source](https://github.com/laminas/automatic-releases/tree/ef538023efb250f43f96aa999a19188016534da7/) · [Current source](https://github.com/laminas/automatic-releases/tree/98204e32a52de981e1d75622d0d89a9520b6e87a/) · [Upstream code diff](https://github.com/laminas/automatic-releases/compare/ef538023efb250f43f96aa999a19188016534da7...98204e32a52de981e1d75622d0d89a9520b6e87a)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ef538023efb250f43f96aa999a19188016534da7 | 98204e32a52de981e1d75622d0d89a9520b6e87a |
| Selected tag | 1.27.0 | 1.28.0 |

## pyvista/setup-headless-display-action

[Previous source](https://github.com/pyvista/setup-headless-display-action/tree/b0bf9f57d62d2b3fee9f1c0e0c7e390f05e97a4e/) · [Current source](https://github.com/pyvista/setup-headless-display-action/tree/c103a2ff45650d38cb71684b5dc6cdfeb9442c79/) · [Upstream code diff](https://github.com/pyvista/setup-headless-display-action/compare/b0bf9f57d62d2b3fee9f1c0e0c7e390f05e97a4e...c103a2ff45650d38cb71684b5dc6cdfeb9442c79)

| Changed | Before | After |
| --- | --- | --- |
| Input: install-mesa3d-offscreen | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Installs Mesa3D off-screen renderer on Windows. Configures VTK to use it\\nby means of the \`VTK\_DEFAULT\_OPENGL\_WINDOW\` environment variable.\\nThis is only used on Windows.\\n&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Installs Mesa3D off-screen renderer on Windows. Configures VTK to use it\\nby means of the \`VTK\_DEFAULT\_OPENGL\_WINDOW\` environment variable, and\\nsets \`LP\_NUM\_THREADS=0\` so processes that rendered do not hang at exit.\\nThis is only used on Windows.\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | b0bf9f57d62d2b3fee9f1c0e0c7e390f05e97a4e | c103a2ff45650d38cb71684b5dc6cdfeb9442c79 |
| Selected tag | v5.0.0 | v5.1.0 |

## ruzickap/action-my-broken-link-checker

[Previous source](https://github.com/ruzickap/action-my-broken-link-checker) · [Current source](https://github.com/ruzickap/action-my-broken-link-checker/tree/3337ef0c9ac76042e776df6c44590dd6bf58dcaf/)

| Changed | Before | After |
| --- | --- | --- |
| Input: cmd\_params | null | {&quot;description&quot;: &quot;Command line parameters for URL checker&quot;} |
| Input: debug | null | {&quot;description&quot;: &quot;Debug mode&quot;} |
| Input: pages\_path | null | {&quot;description&quot;: &quot;Relative path to the directory with local web pages&quot;} |
| Input: url | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;URL which will be checked&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 3337ef0c9ac76042e776df6c44590dd6bf58dcaf |
| Selected tag | null | v3.0.1 |

## shogo82148/actions-setup-perl

[Previous source](https://github.com/shogo82148/actions-setup-perl/tree/53e33bb27be492a926eee378e8a5f7ff6618b061/) · [Current source](https://github.com/shogo82148/actions-setup-perl/tree/ac3202722f5744e62a8fa3af3e1aaaebb08861f3/) · [Upstream code diff](https://github.com/shogo82148/actions-setup-perl/compare/53e33bb27be492a926eee378e8a5f7ff6618b061...ac3202722f5744e62a8fa3af3e1aaaebb08861f3)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 53e33bb27be492a926eee378e8a5f7ff6618b061 | ac3202722f5744e62a8fa3af3e1aaaebb08861f3 |
| Selected tag | v1.43.1 | v1.44.0 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/d438492cf8a250514fa2d34b30bc3c0dc37c65ff/) · [Current source](https://github.com/taiki-e/install-action/tree/c3ec0de9ae7f1019cea21aa96aa0a895b9552063/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/d438492cf8a250514fa2d34b30bc3c0dc37c65ff...c3ec0de9ae7f1019cea21aa96aa0a895b9552063)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | d438492cf8a250514fa2d34b30bc3c0dc37c65ff | c3ec0de9ae7f1019cea21aa96aa0a895b9552063 |
| Selected tag | v2.87.8 | v2.87.9 |

## techpivot/terraform-module-releaser

[Previous source](https://github.com/techpivot/terraform-module-releaser/tree/5f3fc036202008b9a2d3ab5dbb1e4a734cd90e4d/) · [Current source](https://github.com/techpivot/terraform-module-releaser/tree/b5df513373777916d19dd842bf0b2b7461e7cf8f/) · [Upstream code diff](https://github.com/techpivot/terraform-module-releaser/compare/5f3fc036202008b9a2d3ab5dbb1e4a734cd90e4d...b5df513373777916d19dd842bf0b2b7461e7cf8f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5f3fc036202008b9a2d3ab5dbb1e4a734cd90e4d | b5df513373777916d19dd842bf0b2b7461e7cf8f |
| Selected tag | v2.2.0 | v2.2.1 |

## useblacksmith/stickydisk

[Previous source](https://github.com/useblacksmith/stickydisk/tree/74f3f01ab1392726dd6ee06904f0452b0ec1e151/) · [Current source](https://github.com/useblacksmith/stickydisk/tree/25e27b93b68733b532d9af6b201df28ffaf7dbfc/) · [Upstream code diff](https://github.com/useblacksmith/stickydisk/compare/74f3f01ab1392726dd6ee06904f0452b0ec1e151...25e27b93b68733b532d9af6b201df28ffaf7dbfc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 74f3f01ab1392726dd6ee06904f0452b0ec1e151 | 25e27b93b68733b532d9af6b201df28ffaf7dbfc |
| Selected tag | v1.6.0 | v1.7.0 |

## vmactions/freebsd-vm

[Previous source](https://github.com/vmactions/freebsd-vm/tree/f0552d3b69211736abd97f02ff3d4674c56b73b1/) · [Current source](https://github.com/vmactions/freebsd-vm/tree/8b0f1a8fc0ea0def307835c258940ca358fe6480/) · [Upstream code diff](https://github.com/vmactions/freebsd-vm/compare/f0552d3b69211736abd97f02ff3d4674c56b73b1...8b0f1a8fc0ea0def307835c258940ca358fe6480)

| Changed | Before | After |
| --- | --- | --- |
| Input: osname | {&quot;default&quot;: &quot;FreeBSD&quot;, &quot;description&quot;: &quot;The OS name&quot;, &quot;required&quot;: true} | {&quot;default&quot;: &quot;freebsd&quot;, &quot;description&quot;: &quot;The OS name&quot;, &quot;required&quot;: true} |
| Selected SHA | f0552d3b69211736abd97f02ff3d4674c56b73b1 | 8b0f1a8fc0ea0def307835c258940ca358fe6480 |
| Selected tag | v1.5.5 | v1.5.6 |

## WyriHaximus/github-action-get-previous-tag

[Previous source](https://github.com/WyriHaximus/github-action-get-previous-tag/tree/61819f33034117e6c686e6a31dba995a85afc9de/) · [Current source](https://github.com/WyriHaximus/github-action-get-previous-tag/tree/83f26fea93bc7efcbca2eb5591f5eaaf66b8f206/) · [Upstream code diff](https://github.com/WyriHaximus/github-action-get-previous-tag/compare/61819f33034117e6c686e6a31dba995a85afc9de...83f26fea93bc7efcbca2eb5591f5eaaf66b8f206)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 61819f33034117e6c686e6a31dba995a85afc9de | 83f26fea93bc7efcbca2eb5591f5eaaf66b8f206 |
| Selected tag | v2.0.0 | v2.1.0 |
