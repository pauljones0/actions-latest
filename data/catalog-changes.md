# Latest catalog changes

7 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## danielroe/provenance-action

[Previous source](https://github.com/danielroe/provenance-action) · [Current source](https://github.com/danielroe/provenance-action/tree/fcc45fd5a5b818c477432b32c838dcd0c79cd2dd/)

| Changed | Before | After |
| --- | --- | --- |
| Input: base-ref | null | {&quot;description&quot;: &quot;Git ref to compare against (e.g., origin/main)&quot;, &quot;required&quot;: false} |
| Input: fail-on-downgrade | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Fail behavior: true\|false\|any\|only-provenance-loss (default: true)&quot;, &quot;required&quot;: false} |
| Input: fail-on-provenance-change | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Fail job when provenance repository/branch changes (default: false)&quot;, &quot;required&quot;: false} |
| Input: lockfile | null | {&quot;description&quot;: &quot;Path to lockfile (pnpm-lock.yaml, package-lock.json, yarn.lock)&quot;, &quot;required&quot;: false} |
| Input: workspace-path | null | {&quot;default&quot;: &quot;.&quot;, &quot;description&quot;: &quot;Path to workspace root (default: GITHUB\_WORKSPACE)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;changed&quot;, &quot;downgraded&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | fcc45fd5a5b818c477432b32c838dcd0c79cd2dd |
| Selected tag | null | v0.2.0 |

## laminas/automatic-releases

[Previous source](https://github.com/laminas/automatic-releases) · [Current source](https://github.com/laminas/automatic-releases/tree/ef538023efb250f43f96aa999a19188016534da7/)

| Changed | Before | After |
| --- | --- | --- |
| Input: command-name | null | {&quot;description&quot;: &quot;Command to execute: one of\\n \* \`laminas:automatic-releases:release\`\\n \* \`laminas:automatic-releases:create-merge-up-pull-request\`\\n \* \`laminas:automatic-releases:switch-default-branch-to-next-minor\`\\n&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | ef538023efb250f43f96aa999a19188016534da7 |
| Selected tag | null | 1.27.0 |

## Added: macalbert/envilder

[Source](https://github.com/macalbert/envilder) — Pull secrets from AWS SSM or Azure Key Vault into .env files for your CI/CD workflows

New entries still require observed stability and fresh scan evidence before usage.

## Added: presubmit/ai-reviewer

[Source](https://github.com/presubmit/ai-reviewer) — AI-powered code reviews that detect issues, provide summaries, and suggest auto-fixes on PRs.

New entries still require observed stability and fresh scan evidence before usage.

## Added: redhat-plumbers-in-action/differential-shellcheck

[Source](https://github.com/redhat-plumbers-in-action/differential-shellcheck) — GitHub Action for performing differential scans using ShellCheck linter.

New entries still require observed stability and fresh scan evidence before usage.

## upptime/uptime-monitor

[Previous source](https://github.com/upptime/uptime-monitor) · [Current source](https://github.com/upptime/uptime-monitor/tree/2e53e7570ad597ccf3f251d43502846a042165d2/)

| Changed | Before | After |
| --- | --- | --- |
| Input: command | null | {&quot;default&quot;: &quot;update&quot;, &quot;description&quot;: &quot;Command to run (see README for commands)&quot;, &quot;required&quot;: true} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 2e53e7570ad597ccf3f251d43502846a042165d2 |
| Selected tag | null | v1.44.0 |

## vladopajic/go-test-coverage

[Previous source](https://github.com/vladopajic/go-test-coverage) · [Current source](https://github.com/vladopajic/go-test-coverage/tree/f94bcf0d6b9fa5fb8b783830b22648f6c17475e2/)

| Changed | Before | After |
| --- | --- | --- |
| Input: badge-file-name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;If specified, a coverage badge will be generated and saved to the given file path.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: breakdown-file-name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;File name of go-test-coverage breakdown file, which can be used to analyze coverage difference. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-bucket-name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Name of the CDN bucket where the badge will be saved.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-endpoint | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;URL endpoint for CDN where the badge will be uploaded.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-file-name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Filename (including path) for storing the badge on the CDN.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-force-path-style | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Forces path-style URL access in the CDN.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;boolean&quot;} |
| Input: cdn-key | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;API key for CDN access.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-region | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Specifies the CDN region for the badge upload.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: cdn-secret | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;API secret key for CDN. If specified, the badge will be uploaded to the CDN.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: config | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to the configuration file (.testcoverage.yml), which defines test coverage settings and thresholds.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: debug | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Prints additional debugging output when running action.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;boolean&quot;} |
| Input: diff-base-breakdown-file-name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;File name of go-test-coverage breakdown file used to calculate coverage difference from current (head).&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: diff-threshold | null | {&quot;default&quot;: -101, &quot;description&quot;: &quot;Allowed coverage difference from the base, from -100 to 100. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot;} |
| Input: git-branch | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Repository branch where the badge file will be saved.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: git-file-name | null | {&quot;default&quot;: &quot;.badges/${{ github.ref\_name }}/coverage.svg&quot;, &quot;description&quot;: &quot;File name (including path) for storing the badge in the specified repository.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: git-repository | null | {&quot;default&quot;: &quot;${{ github.repository }}&quot;, &quot;description&quot;: &quot;Target GitHub repository in {owner}/{repository} format where the badge will be stored.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: git-token | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;GitHub token for authorization. If provided, the badge will be uploaded to the specified GitHub repository.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: local-prefix | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;DEPRECATED! not used anymore.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: profile | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to the coverage profile file. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: source-dir | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Sets relative path to source files.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Input: threshold-file | null | {&quot;default&quot;: -1, &quot;description&quot;: &quot;Minimum coverage percentage required for individual files. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot;} |
| Input: threshold-package | null | {&quot;default&quot;: -1, &quot;description&quot;: &quot;Minimum coverage percentage required for each package. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot;} |
| Input: threshold-total | null | {&quot;default&quot;: -1, &quot;description&quot;: &quot;Minimum overall project coverage percentage required. Overrides value from configuration.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;number&quot;} |
| Input: version | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Not used by docker action. Accepted for interface compatibility with source action.&quot;, &quot;required&quot;: false, &quot;type&quot;: &quot;string&quot;} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;badge-color&quot;, &quot;badge-text&quot;, &quot;report&quot;, &quot;total-coverage&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | f94bcf0d6b9fa5fb8b783830b22648f6c17475e2 |
| Selected tag | null | v2.19.0 |
