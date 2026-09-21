# Latest catalog changes

4 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## Added: jurplel/install-qt-action

[Source](https://github.com/jurplel/install-qt-action) — Install Qt on your Github Actions workflows with just one simple action

New entries still require observed stability and fresh scan evidence before usage.

## macalbert/envilder

[Previous source](https://github.com/macalbert/envilder) · [Current source](https://github.com/macalbert/envilder/tree/d1867bfc646d052bffd45969e0dfba73fbe34500/)

| Changed | Before | After |
| --- | --- | --- |
| Input: env-file | null | {&quot;description&quot;: &quot;Path to the .env file to generate&quot;, &quot;required&quot;: true} |
| Input: map-file | null | {&quot;description&quot;: &quot;Path to the JSON file mapping environment variables to secret paths&quot;, &quot;required&quot;: true} |
| Input: provider | null | {&quot;description&quot;: &quot;Cloud provider to use: aws or azure (default: aws). Can also be set via $config.provider in the map file.&quot;, &quot;required&quot;: false} |
| Input: vault-url | null | {&quot;description&quot;: &quot;Azure Key Vault URL (overrides $config.vaultUrl in map file)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;env-file-path&quot;\] |
| Runtime | null | composite |
| Security | unknown | clean |
| Selected SHA | null | d1867bfc646d052bffd45969e0dfba73fbe34500 |
| Selected tag | null | v0.13.2 |

## presubmit/ai-reviewer

[Previous source](https://github.com/presubmit/ai-reviewer) · [Current source](https://github.com/presubmit/ai-reviewer/tree/5f1290b6142b14b44cd2e8e3ffda84cd0a22e94f/)

| Changed | Before | After |
| --- | --- | --- |
| Input: github\_api\_url | null | {&quot;default&quot;: &quot;https://api.github.com&quot;, &quot;description&quot;: &quot;GitHub API URL for GitHub Enterprise Server (e.g., https://github.example.com/api/v3)&quot;, &quot;required&quot;: false} |
| Input: github\_server\_url | null | {&quot;default&quot;: &quot;https://github.com&quot;, &quot;description&quot;: &quot;GitHub Server URL for GitHub Enterprise Server (e.g., https://github.example.com)&quot;, &quot;required&quot;: false} |
| Input: style\_guide\_rules | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Custom style guide rules that will be enforced during review by generating critical comments&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node20 |
| Security | unknown | clean |
| Selected SHA | null | 5f1290b6142b14b44cd2e8e3ffda84cd0a22e94f |
| Selected tag | null | v0.2.5 |

## redhat-plumbers-in-action/differential-shellcheck

[Previous source](https://github.com/redhat-plumbers-in-action/differential-shellcheck) · [Current source](https://github.com/redhat-plumbers-in-action/differential-shellcheck/tree/d965e66ec0b3b2f821f75c8eff9b12442d9a7d1e/)

| Changed | Before | After |
| --- | --- | --- |
| Input: base | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Hash of base commit. This input is used when triggering-event is set to \\&quot;manual\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: diff-scan | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Input allowing to request specific type of scan. Input is taken into consideration only if \`triggering-event\` is set to \`manual\`.&quot;, &quot;required&quot;: false} |
| Input: display-engine | null | {&quot;default&quot;: &quot;csgrep&quot;, &quot;description&quot;: &quot;Tool used to display the defects in the output. Valid values are csgrep and sarif-fmt.&quot;, &quot;required&quot;: false} |
| Input: exclude-path | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;List of paths excluded from ShellCheck scanning.&quot;, &quot;required&quot;: false} |
| Input: external-sources | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Enable following of source statements even when the file is not specified as input. By default, shellcheck will only follow files specified on the command-line (plus /dev/null).\\nThis option allows following any file the script may source. This option may also be enabled using external-sources=true in .shellcheckrc. This flag takes precedence.\\n&quot;, &quot;required&quot;: false} |
| Input: head | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Hash of head commit. This input is used when triggering-event is set to \\&quot;manual\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: include-path | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;List of paths to files that will be scanned by ShellCheck.&quot;, &quot;required&quot;: false} |
| Input: merge-group-base | null | {&quot;default&quot;: &quot;${{ github.event.merge\_group.base\_sha }}&quot;, &quot;description&quot;: &quot;Hash of the merge group&#x27;s parent commit. This input is used when triggering-event is set to \\&quot;merge\_group\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: merge-group-head | null | {&quot;default&quot;: &quot;${{ github.event.merge\_group.head\_sha }}&quot;, &quot;description&quot;: &quot;Hash of the merge group commit. This input is used when triggering-event is set to \\&quot;merge\_group\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: pull-request-base | null | {&quot;default&quot;: &quot;${{ github.event.pull\_request.base.sha }}&quot;, &quot;description&quot;: &quot;Hash of top commit on base branch. This input is used when triggering-event is set to \\&quot;pull\_request\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: pull-request-head | null | {&quot;default&quot;: &quot;${{ github.event.pull\_request.head.sha }}&quot;, &quot;description&quot;: &quot;Hash of latest commit in Pull Request. This input is used when triggering-event is set to \\&quot;pull\_request\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: push-event-base | null | {&quot;default&quot;: &quot;${{ github.event.before }}&quot;, &quot;description&quot;: &quot;Hash of the last commit before push. This input is used when triggering-event is set to \\&quot;push\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: push-event-head | null | {&quot;default&quot;: &quot;${{ github.event.after }}&quot;, &quot;description&quot;: &quot;Hash of the last commit after push. This input is used when triggering-event is set to \\&quot;push\\&quot;.&quot;, &quot;required&quot;: false} |
| Input: scan-directory | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Directory to scan. If not specified, the root directory is scanned.&quot;, &quot;required&quot;: false} |
| Input: severity | null | {&quot;default&quot;: &quot;style&quot;, &quot;description&quot;: &quot;Specify minimum severity of errors to consider. Valid values in order of severity are error, warning, info and style. The default is style.&quot;, &quot;required&quot;: false} |
| Input: strict-check-on-push | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Differential ShellCheck performs full scans when running on a \`push\` event, but the Action fails only when new defects are added.\\nThis option allows overwriting this behavior. Hence when \`strict-check-on-push\` is set to \`true\` it will fail when any defect is discovered.\\n&quot;, &quot;required&quot;: false} |
| Input: token | null | {&quot;description&quot;: &quot;GitHub TOKEN used to upload SARIF data.&quot;, &quot;required&quot;: false} |
| Input: triggering-event | null | {&quot;default&quot;: &quot;${{ github.event\_name }}&quot;, &quot;description&quot;: &quot;The name of the event that triggered the workflow run. Supported values are (merge\_group \| pull\_request \| push \| manual).&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;html&quot;, &quot;sarif&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | d965e66ec0b3b2f821f75c8eff9b12442d9a7d1e |
| Selected tag | null | v5.5.6 |
