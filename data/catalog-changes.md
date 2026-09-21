# Latest catalog changes

26 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## Aletheore/Aletheore

[Previous source](https://github.com/Aletheore/Aletheore/tree/2b13b27348d1b110dd44055202b75acc0a48ffaa/) · [Current source](https://github.com/Aletheore/Aletheore/tree/e1eb71895c7ce2a01df7be98a1ac41ef70656884/) · [Upstream code diff](https://github.com/Aletheore/Aletheore/compare/2b13b27348d1b110dd44055202b75acc0a48ffaa...e1eb71895c7ce2a01df7be98a1ac41ef70656884)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2b13b27348d1b110dd44055202b75acc0a48ffaa | e1eb71895c7ce2a01df7be98a1ac41ef70656884 |
| Selected tag | v0.9.16 | v0.9.18 |

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/56cf60fde42f7b19c3abfd5c9c48b69a1288461f/) · [Current source](https://github.com/anthropics/claude-code-action/tree/9cdae7f0d995e3ba7c33f226087fdf82a59cd520/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/56cf60fde42f7b19c3abfd5c9c48b69a1288461f...9cdae7f0d995e3ba7c33f226087fdf82a59cd520)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 56cf60fde42f7b19c3abfd5c9c48b69a1288461f | 9cdae7f0d995e3ba7c33f226087fdf82a59cd520 |
| Selected tag | v1.0.222 | v1.0.223 |

## asklokesh/loki-mode

[Previous source](https://github.com/asklokesh/loki-mode/tree/79da41f8ff4c4ae3382d628c7c5d0cdc024d4fc7/) · [Current source](https://github.com/asklokesh/loki-mode/tree/9dfb18d246623b2e4209329f9e227af108e67bf4/) · [Upstream code diff](https://github.com/asklokesh/loki-mode/compare/79da41f8ff4c4ae3382d628c7c5d0cdc024d4fc7...9dfb18d246623b2e4209329f9e227af108e67bf4)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 79da41f8ff4c4ae3382d628c7c5d0cdc024d4fc7 | 9dfb18d246623b2e4209329f9e227af108e67bf4 |
| Selected tag | v9.39.0 | v9.50.1 |

## conda-incubator/setup-miniconda

[Previous source](https://github.com/conda-incubator/setup-miniconda) · [Current source](https://github.com/conda-incubator/setup-miniconda/tree/8ee1f361103df19b6f8c8655fd3967a8ecb162d5/)

| Changed | Before | After |
| --- | --- | --- |
| Input: activate-environment | null | {&quot;default&quot;: &quot;test&quot;, &quot;description&quot;: &quot;Environment name (or path) to activate on all shells. Default is \`test\` which will be created in \`$CONDA/envs/test\`. If an empty string is used, no environment is activated by default (For \`base\` activation see the \`auto-activate-base\` option). If the environment does not exist, it will be created and activated. If \`environment-file\` is used and you want that to be the environment used, you need to explicitely provide the name of that environment on \`activate-environment\`. If using sh/bash/cmd.exe shells please read the IMPORTANT! section on the README.md! to properly activate conda environments on these shells.&quot;, &quot;required&quot;: false} |
| Input: add-anaconda-token | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. When the channel alias is Anaconda.org or an Anaconda Server GUI, you can set the system configuration so that users automatically see private packages. Anaconda.org was formerly known as binstar.org. This uses the Anaconda command-line client, which you can install with conda install anaconda-client, to automatically add the token to the channel URLs. The default is \\&quot;true\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#add-anaconda-org-token-to-automatically-see-private-packages-add-anaconda-token for more information.&quot;, &quot;required&quot;: false} |
| Input: add-pip-as-python-dependency | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Add pip, wheel, and setuptools as dependencies of Python. This ensures that pip, wheel, and setuptools are always installed any time Python is installed. The default is \\&quot;true\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#add-pip-as-python-dependency-add-pip-as-python-dependency for more information.&quot;, &quot;required&quot;: false} |
| Input: allow-softlinks | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. When allow\_softlinks is \\&quot;true\\&quot;, conda uses hard-links when possible and soft-links---symlinks---when hard-links are not possible, such as when installing on a different file system than the one that the package cache is on. When allow\_softlinks is \\&quot;false\\&quot;, conda still uses hard-links when possible, but when it is not possible, conda copies files. Individual packages can override this option, specifying that certain files should never be soft-linked. The default is \\&quot;true\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#disallow-soft-linking-allow-softlinks for more information.&quot;, &quot;required&quot;: false} |
| Input: architecture | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Architecture of Miniconda that should be installed. This is automatically detected by the runner. If you want to override it, you can use \\&quot;x64\\&quot;, \\&quot;x86\\&quot;, \\&quot;arm64\\&quot;, \\&quot;aarch64\\&quot;, \\&quot;s390x\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: auto-activate | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Conda configuration. If you’d prefer that conda’s default environment not be activated on startup, set the to \\&quot;false\\&quot;. Default is \\&quot;true\\&quot;. This setting always overrides if set to \\&quot;true\\&quot; or \\&quot;false\\&quot;. If you want to use the \\&quot;condarc-file\\&quot; setting pass an empty string. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/ for more information.&quot;, &quot;required&quot;: false} |
| Input: auto-activate-base | null | {&quot;default&quot;: &quot;legacy-placeholder&quot;, &quot;description&quot;: &quot;(deprecated in favor of \`auto-activate\`) &#x27;Conda configuration. If you’d prefer that conda’s base environment not be activated on startup, set the to \\&quot;false\\&quot;. Default is \\&quot;true\\&quot;. This setting always overrides if set to \\&quot;true\\&quot; or \\&quot;false\\&quot;. If you want to use the \\&quot;condarc-file\\&quot; setting pass an empty string. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/ for more information.&#x27;&quot;, &quot;required&quot;: false} |
| Input: auto-update-conda | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Conda configuration. When \\&quot;true\\&quot;, conda updates itself any time a user updates or installs a package in the base environment. When \\&quot;false\\&quot;, conda updates itself only if the user manually issues a conda update command. The default is \\&quot;false\\&quot;.  This setting always overrides if set to \\&quot;true\\&quot; or \\&quot;false\\&quot;. If you want to use the \\&quot;condarc-file\\&quot; setting pass and empty string. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/ for more information.&quot;, &quot;required&quot;: false} |
| Input: channel-alias | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Whenever you use the -c or --channel flag to give conda a channel name that is not a URL, conda prepends the channel\_alias to the name that it was given. The default channel\_alias is https://conda.anaconda.org. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#set-a-channel-alias-channel-alias for more information.&quot;, &quot;required&quot;: false} |
| Input: channel-priority | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Accepts values of \\&quot;strict\\&quot;, \\&quot;flexible\\&quot;, and \\&quot;disabled\\&quot;. The default value is \\&quot;flexible\\&quot;. With strict channel priority, packages in lower priority channels are not considered if a package with the same name appears in a higher priority channel. With flexible channel priority, the solver may reach into lower priority channels to fulfill dependencies, rather than raising an unsatisfiable error. With channel priority disabled, package version takes precedence, and the configured priority of channels is used only to break ties. In previous versions of conda, this parameter was configured as either \\&quot;true\\&quot; or \\&quot;false\\&quot;. \\&quot;true\\&quot; is now an alias to \\&quot;flexible\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html#strict-channel-priority for more information.&quot;, &quot;required&quot;: false} |
| Input: channels | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Comma separated list of channels to use in order of priority. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/ for more information.&quot;, &quot;required&quot;: false} |
| Input: clean-patched-environment-file | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether a patched environment-file (if created) should be cleaned&quot;, &quot;required&quot;: false} |
| Input: conda-build-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Version of conda build to install. If not provided conda-build is not installed. See https://anaconda.org/anaconda/conda-build for available \\&quot;conda-build\\&quot; versions.&quot;, &quot;required&quot;: false} |
| Input: conda-remove-defaults | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Postprocess channels list to remove &#x27;defaults&#x27; if it was added implicitly to the &#x27;channels&#x27; setting. Will default to &#x27;true&#x27; to align with related changes in conda 25.3.0.&quot;, &quot;required&quot;: false} |
| Input: conda-solver | null | {&quot;default&quot;: &quot;libmamba&quot;, &quot;description&quot;: &quot;Which conda solver plugin to use. Only applies to the \`conda\` client, not \`mamba\`. Starting with Miniconda 23.5.2 and Miniforge 23.3.1, you can choose between \`classic\` and \`libmamba\`.&quot;, &quot;required&quot;: false} |
| Input: conda-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Specific version of Conda to install after miniconda is located or installed. See https://anaconda.org/anaconda/conda for available \\&quot;conda\\&quot; versions.&quot;, &quot;required&quot;: false} |
| Input: condarc-file | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Path to a conda configuration file to use for the runner. This file will be copied to \\&quot;~/.condarc\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/ for more information.&quot;, &quot;required&quot;: false} |
| Input: environment-file | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Environment.yml to create an environment. See https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file for more information.&quot;, &quot;required&quot;: false} |
| Input: installation-dir | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If provided, the installer will be installed in the given directory.&quot;, &quot;required&quot;: false} |
| Input: installer-url | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If provided, this installer will be used instead of a miniconda installer, and cached based on its full URL Visit https://github.com/conda/constructor for more information on creating installers&quot;, &quot;required&quot;: false} |
| Input: mamba-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Use mamba (https://github.com/QuantStack/mamba) as a faster drop-in replacement for conda installs. Disabled by default. To enable, use \\&quot;\*\\&quot; or a \\&quot;x.y\\&quot; version string.&quot;, &quot;required&quot;: false} |
| Input: miniconda-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If provided, this version of Miniconda3 will be downloaded and installed. Visit https://repo.continuum.io/miniconda/ for more information on available versions.&quot;, &quot;required&quot;: false} |
| Input: miniforge-variant | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If provided, this variant of Miniforge will be downloaded and installed. If \`miniforge-version\` is not provided, the \`latest\` version will be used. Currently-known values: Miniforge3 (default), Miniforge-pypy3. Visit https://github.com/conda-forge/miniforge/releases/ for more information on available variants.&quot;, &quot;required&quot;: false} |
| Input: miniforge-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If provided, this version of the given Miniforge variant will be downloaded and installed. If \`miniforge-variant\` is not provided, \`Miniforge3\` will be used. Visit https://github.com/conda-forge/miniforge/releases/ for more information on available versions&quot;, &quot;required&quot;: false} |
| Input: pkgs-dirs | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Comma separated list of package directories (\\&quot;pkgs\_dirs\\&quot;) to configure conda. See https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/use-condarc.html#specify-pkg-directories for more information.&quot;, &quot;required&quot;: false} |
| Input: python-version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Exact version of a Python version to use on \\&quot;activate-environment\\&quot;. If provided, this will be installed before the \\&quot;environment-file\\&quot;. See https://anaconda.org/anaconda/python for available \\&quot;python\\&quot; versions.&quot;, &quot;required&quot;: false} |
| Input: remove-profiles | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Advanced. Prior to runnning \\&quot;conda init\\&quot; all shell profiles will be removed from the runner. Default is \\&quot;true\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: run-init | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Advanced. Whether to run \\&quot;conda init\\&quot; and modify shell profiles. Set to \\&quot;false\\&quot; to prevent any modifications to ~/.profile, ~/.bashrc, and other shell profiles. When disabled, you must manually source conda in each step. Default is \\&quot;true\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: run-post | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Set this option to \\&quot;false\\&quot; to disable running the post cleanup step of the action. Default is \\&quot;true\\&quot;&quot;, &quot;required&quot;: false} |
| Input: show-channel-urls | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Show channel URLs when displaying what is going to be downloaded and in conda list. The default is \\&quot;false\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#show-channel-urls-show-channel-urls for more information.&quot;, &quot;required&quot;: false} |
| Input: use-mamba | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Use mamba as soon as available (either as provided by \`mamba-in-installer\` or installation by \`mamba-version\`)&quot;, &quot;required&quot;: false} |
| Input: use-only-tar-bz2 | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Conda configuration. Conda 4.7 introduced a new .conda package file format. .conda is a more compact and faster alternative to .tar.bz2 packages. It is thus the preferred file format to use where available. Nevertheless, it is possible to force conda to only download .tar.bz2 packages by setting the use\_only\_tar\_bz2 boolean to \\&quot;true\\&quot;. The default is \\&quot;false\\&quot;. See https://docs.conda.io/projects/conda/en/latest/user-guide/configuration/use-condarc.html#force-conda-to-download-only-tar-bz2-packages-use-only-tar-bz2 for more information.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;environment-file&quot;, &quot;environment-file-content&quot;, &quot;environment-file-was-patched&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 8ee1f361103df19b6f8c8655fd3967a8ecb162d5 |
| Selected tag | null | v4.0.1 |

## cross-platform-actions/action

[Previous source](https://github.com/cross-platform-actions/action/tree/faa0c6197e94aacf1c5956460152c8380d3560a5/) · [Current source](https://github.com/cross-platform-actions/action/tree/e0b9770014ba65d5e0815f15b74031c3a635f641/) · [Upstream code diff](https://github.com/cross-platform-actions/action/compare/faa0c6197e94aacf1c5956460152c8380d3560a5...e0b9770014ba65d5e0815f15b74031c3a635f641)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | faa0c6197e94aacf1c5956460152c8380d3560a5 | e0b9770014ba65d5e0815f15b74031c3a635f641 |
| Selected tag | v1.5.0 | v1.6.0 |

## duriantaco/skylos

[Previous source](https://github.com/duriantaco/skylos/tree/9f0dfc74cb9c7cc7d73e187a74b655eb396d57f2/) · [Current source](https://github.com/duriantaco/skylos/tree/2d899e605b98f935b86476ab2e0e208c5bbf5062/) · [Upstream code diff](https://github.com/duriantaco/skylos/compare/9f0dfc74cb9c7cc7d73e187a74b655eb396d57f2...2d899e605b98f935b86476ab2e0e208c5bbf5062)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9f0dfc74cb9c7cc7d73e187a74b655eb396d57f2 | 2d899e605b98f935b86476ab2e0e208c5bbf5062 |
| Selected tag | v4.36.1 | v4.37.0 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/7ba7c2e9daf9ed6d2e86866f1d05067e4d54bd52/) · [Current source](https://github.com/pullfrog/pullfrog/tree/a86b83b9a671a9fdb156f386cbcc28d665a6b36b/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/7ba7c2e9daf9ed6d2e86866f1d05067e4d54bd52...a86b83b9a671a9fdb156f386cbcc28d665a6b36b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 7ba7c2e9daf9ed6d2e86866f1d05067e4d54bd52 | a86b83b9a671a9fdb156f386cbcc28d665a6b36b |
| Selected tag | v0.1.77 | v0.1.78 |

## renovatebot/github-action

[Previous source](https://github.com/renovatebot/github-action/tree/c314dda4a9a93b08239ec978f2043b9a433b9ac4/) · [Current source](https://github.com/renovatebot/github-action/tree/dcfba84a42d1b5d5e49bf131b1bf53511851a123/) · [Upstream code diff](https://github.com/renovatebot/github-action/compare/c314dda4a9a93b08239ec978f2043b9a433b9ac4...dcfba84a42d1b5d5e49bf131b1bf53511851a123)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | c314dda4a9a93b08239ec978f2043b9a433b9ac4 | dcfba84a42d1b5d5e49bf131b1bf53511851a123 |
| Selected tag | v46.3.0 | v46.3.1 |

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/d290e336d5a743810aef4404f757dc862276d2ae/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/8b682e1e7e512151d73a6b9449cbff173846226e/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/d290e336d5a743810aef4404f757dc862276d2ae...8b682e1e7e512151d73a6b9449cbff173846226e)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | d290e336d5a743810aef4404f757dc862276d2ae | 8b682e1e7e512151d73a6b9449cbff173846226e |
| Selected tag | v1.73.4 | v1.74.0 |

## reviewdog/action-cpplint

[Previous source](https://github.com/reviewdog/action-cpplint/tree/9552c62f4bd516c1e3a6f84eae56bd864cc304c6/) · [Current source](https://github.com/reviewdog/action-cpplint/tree/5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d/) · [Upstream code diff](https://github.com/reviewdog/action-cpplint/compare/9552c62f4bd516c1e3a6f84eae56bd864cc304c6...5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9552c62f4bd516c1e3a6f84eae56bd864cc304c6 | 5f1bbc6ecc3dc6d9b2cb8ddae490464240ae415d |
| Selected tag | v1.11.0 | v1.12.0 |

## reviewdog/action-detect-secrets

[Previous source](https://github.com/reviewdog/action-detect-secrets/tree/964728f040a48396239d7fbe5e2746f7209df406/) · [Current source](https://github.com/reviewdog/action-detect-secrets/tree/aa401448f8afc3c826140059b40e614b8ae0081b/) · [Upstream code diff](https://github.com/reviewdog/action-detect-secrets/compare/964728f040a48396239d7fbe5e2746f7209df406...aa401448f8afc3c826140059b40e614b8ae0081b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 964728f040a48396239d7fbe5e2746f7209df406 | aa401448f8afc3c826140059b40e614b8ae0081b |
| Selected tag | v0.29.8 | v0.30.0 |

## reviewdog/action-eslint

[Previous source](https://github.com/reviewdog/action-eslint/tree/556a3fdaf8b4201d4d74d406013386aa4f7dab96/) · [Current source](https://github.com/reviewdog/action-eslint/tree/5eb89b1e6e94ca33e91c3814c34b25a8370bba46/) · [Upstream code diff](https://github.com/reviewdog/action-eslint/compare/556a3fdaf8b4201d4d74d406013386aa4f7dab96...5eb89b1e6e94ca33e91c3814c34b25a8370bba46)

| Changed | Before | After |
| --- | --- | --- |
| Input: only\_changed | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Run eslint only on changed (and added) files, for speedup \[true, false\].\\nDefault: false.\\nWill fetch the tip of the base branch with depth 1 from remote origin if it is not available.\\nIf you use different remote name or customize the checkout otherwise, make the tip of the base branch available before this action.\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | 556a3fdaf8b4201d4d74d406013386aa4f7dab96 | 5eb89b1e6e94ca33e91c3814c34b25a8370bba46 |
| Selected tag | v1.34.0 | v1.35.0 |

## reviewdog/action-hadolint

[Previous source](https://github.com/reviewdog/action-hadolint/tree/2d0eb7c86a0ddd94eb625485f4cc2730e105edd8/) · [Current source](https://github.com/reviewdog/action-hadolint/tree/9d9a44af664599d7fe5ed5ee3d66d2d236cb7f8f/) · [Upstream code diff](https://github.com/reviewdog/action-hadolint/compare/2d0eb7c86a0ddd94eb625485f4cc2730e105edd8...9d9a44af664599d7fe5ed5ee3d66d2d236cb7f8f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2d0eb7c86a0ddd94eb625485f4cc2730e105edd8 | 9d9a44af664599d7fe5ed5ee3d66d2d236cb7f8f |
| Selected tag | v1.53.0 | v1.54.0 |

## reviewdog/action-misspell

[Previous source](https://github.com/reviewdog/action-misspell/tree/ba7ac4030fa6812f8c8b2d4e516af8bc99553c32/) · [Current source](https://github.com/reviewdog/action-misspell/tree/da40ce414be6ce320a9322aa2bae10bd3b9e6ef3/) · [Upstream code diff](https://github.com/reviewdog/action-misspell/compare/ba7ac4030fa6812f8c8b2d4e516af8bc99553c32...da40ce414be6ce320a9322aa2bae10bd3b9e6ef3)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ba7ac4030fa6812f8c8b2d4e516af8bc99553c32 | da40ce414be6ce320a9322aa2bae10bd3b9e6ef3 |
| Selected tag | v1.28.0 | v1.29.0 |

## reviewdog/action-shellcheck

[Previous source](https://github.com/reviewdog/action-shellcheck/tree/0722bbdb0d47f04c1b53b8734d2422ac63a45ec6/) · [Current source](https://github.com/reviewdog/action-shellcheck/tree/a94d585085f1f5215ae65f4de34e7bbd0523d550/) · [Upstream code diff](https://github.com/reviewdog/action-shellcheck/compare/0722bbdb0d47f04c1b53b8734d2422ac63a45ec6...a94d585085f1f5215ae65f4de34e7bbd0523d550)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 0722bbdb0d47f04c1b53b8734d2422ac63a45ec6 | a94d585085f1f5215ae65f4de34e7bbd0523d550 |
| Selected tag | v1.32.1 | v1.33.0 |

## reviewdog/action-stylelint

[Previous source](https://github.com/reviewdog/action-stylelint/tree/086959bc5cd70db1b4954f45d8d396d9e3786bbb/) · [Current source](https://github.com/reviewdog/action-stylelint/tree/c94fa6098ba80ac301ab1f2ff5a7a5f3a2f6e241/) · [Upstream code diff](https://github.com/reviewdog/action-stylelint/compare/086959bc5cd70db1b4954f45d8d396d9e3786bbb...c94fa6098ba80ac301ab1f2ff5a7a5f3a2f6e241)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 086959bc5cd70db1b4954f45d8d396d9e3786bbb | c94fa6098ba80ac301ab1f2ff5a7a5f3a2f6e241 |
| Selected tag | v1.31.0 | v1.32.0 |

## reviewdog/action-tflint

[Previous source](https://github.com/reviewdog/action-tflint/tree/54a5e5aed57dcfbb4662ec548de876df33d6288d/) · [Current source](https://github.com/reviewdog/action-tflint/tree/ac21f7671251b29bbeb280ede595cb9c5b8710c7/) · [Upstream code diff](https://github.com/reviewdog/action-tflint/compare/54a5e5aed57dcfbb4662ec548de876df33d6288d...ac21f7671251b29bbeb280ede595cb9c5b8710c7)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 54a5e5aed57dcfbb4662ec548de876df33d6288d | ac21f7671251b29bbeb280ede595cb9c5b8710c7 |
| Selected tag | v1.25.0 | v1.26.0 |

## reviewdog/action-tfsec

[Previous source](https://github.com/reviewdog/action-tfsec/tree/a2f2edbf61c6bb22849de705d304b9d2af5f69cd/) · [Current source](https://github.com/reviewdog/action-tfsec/tree/ade3cd012981486a988fb56351d6d42b6bb7d3c9/) · [Upstream code diff](https://github.com/reviewdog/action-tfsec/compare/a2f2edbf61c6bb22849de705d304b9d2af5f69cd...ade3cd012981486a988fb56351d6d42b6bb7d3c9)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | a2f2edbf61c6bb22849de705d304b9d2af5f69cd | ade3cd012981486a988fb56351d6d42b6bb7d3c9 |
| Selected tag | v1.30.0 | v1.31.0 |

## reviewdog/action-vint

[Previous source](https://github.com/reviewdog/action-vint/tree/7d853f6a655c6940837973e80c2b63fce67c9c8e/) · [Current source](https://github.com/reviewdog/action-vint/tree/101f3104da66cf84d81438957b83e07c530c8ce3/) · [Upstream code diff](https://github.com/reviewdog/action-vint/compare/7d853f6a655c6940837973e80c2b63fce67c9c8e...101f3104da66cf84d81438957b83e07c530c8ce3)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 7d853f6a655c6940837973e80c2b63fce67c9c8e | 101f3104da66cf84d81438957b83e07c530c8ce3 |
| Selected tag | v1.18.0 | v1.19.0 |

## reviewdog/action-yamllint

[Previous source](https://github.com/reviewdog/action-yamllint/tree/de68272fdca5f2a961fb309e0d2e13c2eb186d9e/) · [Current source](https://github.com/reviewdog/action-yamllint/tree/6803b0dc8f295034a6156b924814053acb2e6f5a/) · [Upstream code diff](https://github.com/reviewdog/action-yamllint/compare/de68272fdca5f2a961fb309e0d2e13c2eb186d9e...6803b0dc8f295034a6156b924814053acb2e6f5a)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | de68272fdca5f2a961fb309e0d2e13c2eb186d9e | 6803b0dc8f295034a6156b924814053acb2e6f5a |
| Selected tag | v1.23.1 | v1.24.0 |

## sersoft-gmbh/xcodebuild-action

[Previous source](https://github.com/sersoft-gmbh/xcodebuild-action) · [Current source](https://github.com/sersoft-gmbh/xcodebuild-action/tree/3a8a748098f979d21942e2b0d036517780ae6847/)

| Changed | Before | After |
| --- | --- | --- |
| Input: action | null | {&quot;default&quot;: &quot;test&quot;, &quot;description&quot;: &quot;The action to perform (e.g. build, test, ...). Can also contain multiple actions.&quot;, &quot;required&quot;: true} |
| Input: all-targets | null | {&quot;description&quot;: &quot;If \`true\`, all targets will be built. See also \`xcodebuild\`&#x27;s \`-allTargets\`.&quot;, &quot;required&quot;: false} |
| Input: allow-provisioning-device-registration | null | {&quot;description&quot;: &quot;Whether provisioning device registrations are allowed. See also \`xcodebuild\`&#x27;s \`-allowProvisioningDeviceRegistration\`.&quot;, &quot;required&quot;: false} |
| Input: allow-provisioning-updates | null | {&quot;description&quot;: &quot;Whether provisioning updates are allowed. See also \`xcodebuild\`&#x27;s \`-allowProvisioningUpdates\`.&quot;, &quot;required&quot;: false} |
| Input: arch | null | {&quot;description&quot;: &quot;The architecture to use for building. See also \`xcodebuild\`&#x27;s \`-arch\`.&quot;, &quot;required&quot;: false} |
| Input: archive-path | null | {&quot;description&quot;: &quot;The path to where archives are created. See also \`xcodebuild\`&#x27;s \`-archivePath\`.&quot;, &quot;required&quot;: false} |
| Input: build-settings | null | {&quot;description&quot;: &quot;Arbitrary, space separated build settings (e.g. PLATFORM\_NAME=iphonesimulator).&quot;, &quot;required&quot;: false} |
| Input: cloned-source-packages-path | null | {&quot;description&quot;: &quot;The path that should be used for the cloning of remote packages. See also \`xcodebuild\`&#x27;s \`-clonedSourcePackagesDirPath\`.&quot;, &quot;required&quot;: false} |
| Input: configuration | null | {&quot;description&quot;: &quot;The configuration to build. See also \`xcodebuild\`&#x27;s \`-configuration\`.&quot;, &quot;required&quot;: false} |
| Input: create-xcframework | null | {&quot;description&quot;: &quot;Whether an xcframework should be created. See also \`xcodebuild\`&#x27;s \`-create-xcframework\`.&quot;, &quot;required&quot;: false} |
| Input: default-package-registry-url | null | {&quot;description&quot;: &quot;The default package registry URL. See also \`xcodebuild\`&#x27;s \`-defaultPackageRegistryURL\`.&quot;, &quot;required&quot;: false} |
| Input: derived-data-path | null | {&quot;description&quot;: &quot;The path that should be used for derived data. See also \`xcodebuild\`&#x27;s \`-derivedDataPath\`.&quot;, &quot;required&quot;: false} |
| Input: destination | null | {&quot;description&quot;: &quot;The destination specifier to build. See also \`xcodebuild\`&#x27;s \`-destination\`.&quot;, &quot;required&quot;: false} |
| Input: disable-automatic-package-resolution | null | {&quot;description&quot;: &quot;Whether automatic package resolution should be disabled. See also \`xcodebuild\`&#x27;s \`-disableAutomaticPackageResolution\`.&quot;, &quot;required&quot;: false} |
| Input: disable-enum-input-validation | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether the input validation for enums should be disabled. Usually only needed if new values are added to the enums in the future.&quot;, &quot;required&quot;: false} |
| Input: disable-package-repository-cache | null | {&quot;description&quot;: &quot;Whether the package repository cache should be disabled. See also \`xcodebuild\`&#x27;s \`-disablePackageRepositoryCache\`.&quot;, &quot;required&quot;: false} |
| Input: dry-run | null | {&quot;description&quot;: &quot;&lt;TEST ONLY&gt; Whether the commands should only be composed and not actually run. Only used in test.&quot;, &quot;required&quot;: false} |
| Input: enable-address-sanitizer | null | {&quot;description&quot;: &quot;Whether the address sanitizer should be enabled. See also \`xcodebuild\`&#x27;s \`-enableAddressSanitizer\`.&quot;, &quot;required&quot;: false} |
| Input: enable-code-coverage | null | {&quot;description&quot;: &quot;If \`true\`, code coverage is enabled while testing. See also \`xcodebuild\`&#x27;s \`-enableCodeCoverage\`.&quot;, &quot;required&quot;: false} |
| Input: enable-thread-sanitizer | null | {&quot;description&quot;: &quot;Whether the thread sanitizer should be enabled. See also \`xcodebuild\`&#x27;s \`-enableThreadSanitizer\`.&quot;, &quot;required&quot;: false} |
| Input: enable-undefined-behavior-sanitizer | null | {&quot;description&quot;: &quot;Whether the undefined behavior sanitizer should be enabled. See also \`xcodebuild\`&#x27;s \`-enableUndefinedBehaviorSanitizer\`.&quot;, &quot;required&quot;: false} |
| Input: export-archive | null | {&quot;description&quot;: &quot;Whether an archive should be exported. See also \`xcodebuild\`&#x27;s \`-exportArchive\`.&quot;, &quot;required&quot;: false} |
| Input: export-notarized-app | null | {&quot;description&quot;: &quot;Whether the app should be exported notarized. See also \`xcodebuild\`&#x27;s \`-exportNotarizedApp\`.&quot;, &quot;required&quot;: false} |
| Input: export-options-plist | null | {&quot;description&quot;: &quot;The path to an export options plist. See also \`xcodebuild\`&#x27;s \`-exportOptionsPlist\`.&quot;, &quot;required&quot;: false} |
| Input: hide-shell-script-environment | null | {&quot;description&quot;: &quot;If \`true\`, xcodebuild won&#x27;t print the environment for shell build scripts. See also \`xcodebuild\`&#x27;s \`-hideShellScriptEnvironment\`.&quot;, &quot;required&quot;: false} |
| Input: jobs | null | {&quot;description&quot;: &quot;The number of jobs to use for building. See also \`xcodebuild\`&#x27;s \`-jobs\`.&quot;, &quot;required&quot;: false} |
| Input: maximum-concurrent-test-device-destinations | null | {&quot;description&quot;: &quot;The maximum number of device destinations to run in parallel. See also \`xcodebuild\`&#x27;s \`-maximum-concurrent-test-device-destinations\`.&quot;, &quot;required&quot;: false} |
| Input: maximum-concurrent-test-simulator-destinations | null | {&quot;description&quot;: &quot;The maximum number of simulator destinations to run in parallel. See also \`xcodebuild\`&#x27;s \`-maximum-concurrent-test-simulator-destinations\`.&quot;, &quot;required&quot;: false} |
| Input: only-test-configuration | null | {&quot;description&quot;: &quot;A (line-separated) list of test configurations to run. See also \`xcodebuild\`&#x27;s \`-only-test-configuration\`.&quot;, &quot;required&quot;: false} |
| Input: only-testing | null | {&quot;description&quot;: &quot;A (line-separated) list of tests to run. See also \`xcodebuild\`&#x27;s \`-only-testing\`.&quot;, &quot;required&quot;: false} |
| Input: output-formatter | null | {&quot;description&quot;: &quot;The output formatter to use (e.g. xcpretty, xcbeautify, ...). The xcodebuild output will be piped into this formatter.&quot;, &quot;required&quot;: false} |
| Input: package-cache-path | null | {&quot;description&quot;: &quot;The path of caches used for package support. See also \`xcodebuild\`&#x27;s \`-packageCachePath\`.&quot;, &quot;required&quot;: false} |
| Input: package-dependency-scm-to-registry-transformation | null | {&quot;description&quot;: &quot;The package dependency SCM to registry transformation. See also \`xcodebuild\`&#x27;s \`-packageDependencySCMToRegistryTransformation\`.&quot;, &quot;required&quot;: false} |
| Input: package-fingerprint-policy | null | {&quot;description&quot;: &quot;The package fingerprint checking policy. See also \`xcodebuild\`&#x27;s \`-packageFingerprintPolicy\`.&quot;, &quot;required&quot;: false} |
| Input: package-signing-entity-policy | null | {&quot;description&quot;: &quot;The package signing entity policy. See also \`xcodebuild\`&#x27;s \`-packageSigningEntityPolicy\`.&quot;, &quot;required&quot;: false} |
| Input: parallel-testing-enabled | null | {&quot;description&quot;: &quot;If \`true\`, tests are executed in parallel. See also \`xcodebuild\`&#x27;s \`-parallel-testing-enabled\`.&quot;, &quot;required&quot;: false} |
| Input: parallelize-targets | null | {&quot;description&quot;: &quot;If \`true\`, the targets will be built in parallel. See also \`xcodebuild\`&#x27;s \`-parallelizeTargets\`.&quot;, &quot;required&quot;: false} |
| Input: project | null | {&quot;description&quot;: &quot;The path to the xcodeproj to build. Mutually exclusive with \`workspace\` and \`spm-package\`. See also \`xcodebuild\`&#x27;s \`-project\`.&quot;, &quot;required&quot;: false} |
| Input: quiet | null | {&quot;description&quot;: &quot;If \`true\`, xcodebuild won&#x27;t print anything except warnings and errors. See also \`xcodebuild\`&#x27;s \`-quiet\`.&quot;, &quot;required&quot;: false} |
| Input: result-bundle-path | null | {&quot;description&quot;: &quot;The path that should be used for the result bundle. See also \`xcodebuild\`&#x27;s \`-resultBundlePath\`.&quot;, &quot;required&quot;: false} |
| Input: result-bundle-version | null | {&quot;description&quot;: &quot;The version that should be used for the result bundle. See also \`xcodebuild\`&#x27;s \`-resultBundleVersion\`.&quot;, &quot;required&quot;: false} |
| Input: retry-tests-on-failure | null | {&quot;description&quot;: &quot;Whether tests should be retried on failure. See also \`xcodebuild\`&#x27;s \`-retry-tests-on-failure\`.&quot;, &quot;required&quot;: false} |
| Input: run-tests-until-failure | null | {&quot;description&quot;: &quot;Whether tests should be run until failure. See also \`xcodebuild\`&#x27;s \`-run-tests-until-failure\`.&quot;, &quot;required&quot;: false} |
| Input: scheme | null | {&quot;description&quot;: &quot;The scheme to build. Required when using a workspace. See also \`xcodebuild\`&#x27;s \`-scheme\`.&quot;, &quot;required&quot;: false} |
| Input: sdk | null | {&quot;description&quot;: &quot;The SDK to use for building. See also \`xcodebuild\`&#x27;s \`-sdk\`.&quot;, &quot;required&quot;: false} |
| Input: skip-macro-validation | null | {&quot;description&quot;: &quot;Whether macro validation should be skipped. See also \`xcodebuild\`&#x27;s \`-skipMacroValidation\`.&quot;, &quot;required&quot;: false} |
| Input: skip-package-plugin-validation | null | {&quot;description&quot;: &quot;Whether package plugin validation should be skipped. See also \`xcodebuild\`&#x27;s \`-skipPackagePluginValidation\`.&quot;, &quot;required&quot;: false} |
| Input: skip-package-updates | null | {&quot;description&quot;: &quot;Whether package updates should be skipped. See also \`xcodebuild\`&#x27;s \`-skipPackageUpdates\`.&quot;, &quot;required&quot;: false} |
| Input: skip-test-configuration | null | {&quot;description&quot;: &quot;A (line-separated) list of test configurations to skip. See also \`xcodebuild\`&#x27;s \`-skip-test-configuration\`.&quot;, &quot;required&quot;: false} |
| Input: skip-testing | null | {&quot;description&quot;: &quot;A (line-separated) list of tests to skip. See also \`xcodebuild\`&#x27;s \`-skip-testing\`.&quot;, &quot;required&quot;: false} |
| Input: skip-unavailable-actions | null | {&quot;description&quot;: &quot;Whether unavailable actions should be skipped instead of failing the execution. See also \`xcodebuild\`&#x27;s \`-skipUnavailableActions\`.&quot;, &quot;required&quot;: false} |
| Input: spm-package | null | {&quot;description&quot;: &quot;The path to the SPM package (folder containing Package.swift) to build. Mutually exclusive with \`workspace\` and \`project\`.&quot;, &quot;required&quot;: false} |
| Input: target | null | {&quot;description&quot;: &quot;The target to build. See also \`xcodebuild\`&#x27;s \`-target\`.&quot;, &quot;required&quot;: false} |
| Input: test-iterations | null | {&quot;description&quot;: &quot;The number of iterations to run the tests. See also \`xcodebuild\`&#x27;s \`-test-iterations\`.&quot;, &quot;required&quot;: false} |
| Input: test-language | null | {&quot;description&quot;: &quot;The language to use for testing. See also \`xcodebuild\`&#x27;s \`-testLanguage\`.&quot;, &quot;required&quot;: false} |
| Input: test-plan | null | {&quot;description&quot;: &quot;The name of the test plan associated with the scheme to use for testing. See also \`xcodebuild\`&#x27;s \`-testPlan\`.&quot;, &quot;required&quot;: false} |
| Input: test-region | null | {&quot;description&quot;: &quot;The region to use for testing. See also \`xcodebuild\`&#x27;s \`-testRegion\`.&quot;, &quot;required&quot;: false} |
| Input: toolchain | null | {&quot;description&quot;: &quot;The toolchain identifier or name to use for building. See also \`xcodebuild\`&#x27;s \`-toolchain\`.&quot;, &quot;required&quot;: false} |
| Input: workspace | null | {&quot;description&quot;: &quot;The path to the xcworkspace to build. Mutually exclusive with \`project\` and \`spm-package\`. See also \`xcodebuild\`&#x27;s \`-workspace\`.&quot;, &quot;required&quot;: false} |
| Input: xcconfig | null | {&quot;description&quot;: &quot;The path to an xcconfig file with build settings overrides. See also \`xcodebuild\`&#x27;s \`-xcconfig\`.&quot;, &quot;required&quot;: false} |
| Input: xcroot | null | {&quot;description&quot;: &quot;The path to a .xcroot to use for building and/or testing. See also \`xcodebuild\`&#x27;s \`-xcroot\`.&quot;, &quot;required&quot;: false} |
| Input: xctestrun | null | {&quot;description&quot;: &quot;The path to a test run specification. See also \`xcodebuild\`&#x27;s \`-xctestrun\`.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;executed-command&quot;, &quot;unprocessed-command&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 3a8a748098f979d21942e2b0d036517780ae6847 |
| Selected tag | null | v4.0.0 |

## shalzz/zola-deploy-action

[Previous source](https://github.com/shalzz/zola-deploy-action) · [Current source](https://github.com/shalzz/zola-deploy-action/tree/1be083648a1db2853ce4970e381740c0e2fd06de/)

| Changed | Before | After |
| --- | --- | --- |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 1be083648a1db2853ce4970e381740c0e2fd06de |
| Selected tag | null | v0.23.6 |

## taiki-e/install-action

[Previous source](https://github.com/taiki-e/install-action/tree/9534c84618278caac52cb373bb164ed464dbd8af/) · [Current source](https://github.com/taiki-e/install-action/tree/3f74d7c16a4242f1c95561e98edc25d36adb4375/) · [Upstream code diff](https://github.com/taiki-e/install-action/compare/9534c84618278caac52cb373bb164ed464dbd8af...3f74d7c16a4242f1c95561e98edc25d36adb4375)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9534c84618278caac52cb373bb164ed464dbd8af | 3f74d7c16a4242f1c95561e98edc25d36adb4375 |
| Selected tag | v2.87.11 | v2.87.12 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/d0434054779e9026c6082bc47ecc818ec2aa981d/) · [Current source](https://github.com/tmatens/compose-lint/tree/34fa9ae3fc89217b270668522dfa13855b91581a/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/d0434054779e9026c6082bc47ecc818ec2aa981d...34fa9ae3fc89217b270668522dfa13855b91581a)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | d0434054779e9026c6082bc47ecc818ec2aa981d | 34fa9ae3fc89217b270668522dfa13855b91581a |
| Selected tag | v0.28.0 | v0.29.0 |

## voidzero-dev/setup-vp

[Previous source](https://github.com/voidzero-dev/setup-vp/tree/49c3e4e92c52e7f8392712a9267bbe71c5ab30e5/) · [Current source](https://github.com/voidzero-dev/setup-vp/tree/9fd26ff49f9b5e6276c2b493da4454ad4527f7f4/) · [Upstream code diff](https://github.com/voidzero-dev/setup-vp/compare/49c3e4e92c52e7f8392712a9267bbe71c5ab30e5...9fd26ff49f9b5e6276c2b493da4454ad4527f7f4)

| Changed | Before | After |
| --- | --- | --- |
| Input: node-manager | {&quot;description&quot;: &quot;Control Vite+&#x27;s Node.js version manager. When unset, the Vite+ installer decides (enabled on CI). Set to \`false\` to keep the Node.js already on the runner (e.g. from actions/setup-node or the runner image): shim creation is skipped and vp commands prefer the system Node.js. Set to \`true\` to force-enable the managed Node.js. Cannot be \`false\` together with node-version or node-version-file.&quot;, &quot;required&quot;: false} | {&quot;description&quot;: &quot;Control Vite+&#x27;s Node.js version manager. When unset, the Vite+ installer decides (enabled on CI). Set to \`false\` to keep the Node.js already on the runner (e.g. from actions/setup-node or the runner image): after installation, vp commands prefer the system Node.js. Set to \`true\` to leave the installer default unchanged. Cannot be \`false\` together with node-version or node-version-file.&quot;, &quot;required&quot;: false} |
| Input: package-manager | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Control Vite+ package-manager management (0.3.1+). Accepts true, false, or a YAML mapping of npm, pnpm, yarn, and bun to booleans. Unspecified managers keep the installer default (enabled on CI). Any explicit configuration requires 0.3.1+. False prefers the system package manager. Independent of node-manager.&quot;, &quot;required&quot;: false} |
| Selected SHA | 49c3e4e92c52e7f8392712a9267bbe71c5ab30e5 | 9fd26ff49f9b5e6276c2b493da4454ad4527f7f4 |
| Selected tag | v1.19.0 | v1.20.0 |

## yokawasa/action-setup-kube-tools

[Previous source](https://github.com/yokawasa/action-setup-kube-tools) · [Current source](https://github.com/yokawasa/action-setup-kube-tools/tree/b16d49b2c459d33cf9d4c300a220ef0bcdbc730a/)

| Changed | Before | After |
| --- | --- | --- |
| Input: arch-type | null | {&quot;description&quot;: &quot;Optional. The processor architecture type of the tool binary to setup. The action will auto-detect the architecture (\\&quot;amd64\\&quot; or \\&quot;arm64\\&quot;) and use it as appropriate at runtime. Specify the architecture type (\\&quot;amd64\\&quot; or \\&quot;arm64\\&quot;) only if you need to force it.&quot;, &quot;required&quot;: false} |
| Input: conftest | null | {&quot;description&quot;: &quot;conftest version or &#x27;latest&#x27; (default: 0.67.1)&quot;, &quot;required&quot;: false} |
| Input: fail-fast | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;the action immediately fails when it fails to download (ie. due to a bad version)&quot;, &quot;required&quot;: false} |
| Input: helm | null | {&quot;description&quot;: &quot;helm version or &#x27;latest&#x27; (default: 3.20.1)&quot;, &quot;required&quot;: false} |
| Input: kube-score | null | {&quot;description&quot;: &quot;kube-score version or &#x27;latest&#x27; (default: 1.20.0)&quot;, &quot;required&quot;: false} |
| Input: kubeconform | null | {&quot;description&quot;: &quot;kubeconform version or &#x27;latest&#x27; (default: 0.7.0)&quot;, &quot;required&quot;: false} |
| Input: kubectl | null | {&quot;description&quot;: &quot;kubectl version or &#x27;latest&#x27; (default: 1.35.3)&quot;, &quot;required&quot;: false} |
| Input: kubeval | null | {&quot;description&quot;: &quot;kubeval version or &#x27;latest&#x27; (default: 0.16.1)&quot;, &quot;required&quot;: false} |
| Input: kustomize | null | {&quot;description&quot;: &quot;kustomize version or &#x27;latest&#x27; (default: 5.8.1)&quot;, &quot;required&quot;: false} |
| Input: rancher | null | {&quot;description&quot;: &quot;rancher cli version or &#x27;latest&#x27; (default: 2.13.3)&quot;, &quot;required&quot;: false} |
| Input: setup-tools | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;List of tool name to setup. By default, the action download and setup all supported Kubernetes tools. By specifying \\&quot;setup-tools\\&quot; you can choose which tools the action setup. Supported separator is return in multi-line string. Supported tools are \\&quot;kubectl\\&quot;, \\&quot;kustomize\\&quot;, \\&quot;helm\\&quot;, \\&quot;kubeval\\&quot;, \\&quot;kubeconform\\&quot;, \\&quot;conftest\\&quot;, \\&quot;yq\\&quot;, \\&quot;rancher\\&quot;, \\&quot;tilt\\&quot;, \\&quot;skaffold\\&quot;, \\&quot;kube-score\\&quot;&quot;, &quot;required&quot;: false} |
| Input: skaffold | null | {&quot;description&quot;: &quot;skaffold version or &#x27;latest&#x27; (default: 2.18.1)&quot;, &quot;required&quot;: false} |
| Input: tilt | null | {&quot;description&quot;: &quot;tilt version or &#x27;latest&#x27; (default: 0.37.0)&quot;, &quot;required&quot;: false} |
| Input: version-file | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional. Path to a \\&quot;.tool-versions\\&quot; (asdf/mise) style file. For each supported tool that has an entry in the file, that version is used, unless the tool&#x27;s own version input is explicitly set. Resolution order is: explicit tool input &gt; version-file entry &gt; built-in default. Each line is \\&quot;&lt;tool&gt; &lt;version&gt;\\&quot;; \\&quot;#\\&quot; comments, blank lines, and unsupported tool names are ignored.&quot;, &quot;required&quot;: false} |
| Input: yq | null | {&quot;description&quot;: &quot;yq version or &#x27;latest&#x27; (default: 4.52.5)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;conftest-path&quot;, &quot;helm-path&quot;, &quot;kube-score-path&quot;, &quot;kubectl-path&quot;, &quot;kubeval-path&quot;, &quot;kustomize-path&quot;, &quot;rancher-path&quot;, &quot;skaffold-path&quot;, &quot;tilt-path&quot;, &quot;yq-path&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | b16d49b2c459d33cf9d4c300a220ef0bcdbc730a |
| Selected tag | null | v0.14.0 |
