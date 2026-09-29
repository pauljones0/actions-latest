# Latest catalog changes

17 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## apisec-inc/AI-Surface

[Previous source](https://github.com/apisec-inc/AI-Surface) · [Current source](https://github.com/apisec-inc/AI-Surface/tree/2a44c23db5043868aad8a096971c8a6945224b3d/)

| Changed | Before | After |
| --- | --- | --- |
| Input: comment-on-pr | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Post (or update) a PR comment with the AI surface report. Set to \\&quot;false\\&quot; to disable.&quot;, &quot;required&quot;: false} |
| Input: fail-on | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Severity-threshold gate: fail the build if a finding is at or above this severity (critical\|high\|medium\|low). On PRs with a base ref, gates only on NEWLY introduced findings. Recommended: high.&quot;, &quot;required&quot;: false} |
| Input: fail-on-risk | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Exit non-zero if any risk indicators are detected. Aggressive; prefer fail-on for a severity threshold.&quot;, &quot;required&quot;: false} |
| Input: github-token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;Token used to post PR comments. Defaults to the workflow GITHUB\_TOKEN.&quot;, &quot;required&quot;: false} |
| Input: path | null | {&quot;default&quot;: &quot;.&quot;, &quot;description&quot;: &quot;Directory to scan, relative to the repository root.&quot;, &quot;required&quot;: false} |
| Input: write-inventory | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Write .ai-inventory.md back to the workspace.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;json-report&quot;, &quot;risk-count&quot;, &quot;surfaces-count&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 2a44c23db5043868aad8a096971c8a6945224b3d |
| Selected tag | null | v1.1.0 |

## astral-sh/setup-uv

[Previous source](https://github.com/astral-sh/setup-uv/tree/bec219d24cd3e171d82865faccec33120bb574f4/) · [Current source](https://github.com/astral-sh/setup-uv/tree/c18668ad3cf93ea998bef934396af7bb5c839dc7/) · [Upstream code diff](https://github.com/astral-sh/setup-uv/compare/bec219d24cd3e171d82865faccec33120bb574f4...c18668ad3cf93ea998bef934396af7bb5c839dc7)

| Changed | Before | After |
| --- | --- | --- |
| Input: save-cache | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether to save the cache after the run.&quot;} | {&quot;default&quot;: &quot;auto&quot;, &quot;description&quot;: &quot;Whether to save the cache after the run. &#x27;auto&#x27; disables saving for merge\_group events.&quot;} |
| Selected SHA | bec219d24cd3e171d82865faccec33120bb574f4 | c18668ad3cf93ea998bef934396af7bb5c839dc7 |
| Selected tag | v10.1.0 | v10.2.0 |

## Added: calibreapp/image-actions

[Source](https://github.com/calibreapp/image-actions) — Compresses Images for the Web

New entries still require observed stability and fresh scan evidence before usage.

## cloudflare/wrangler-action

[Previous source](https://github.com/cloudflare/wrangler-action) · [Current source](https://github.com/cloudflare/wrangler-action/tree/ebbaa1584979971c8614a24965b4405ff95890e0/)

| Changed | Before | After |
| --- | --- | --- |
| Input: accountId | null | {&quot;description&quot;: &quot;Your Cloudflare Account ID&quot;, &quot;required&quot;: false} |
| Input: apiToken | null | {&quot;description&quot;: &quot;Your Cloudflare API Token&quot;, &quot;required&quot;: false} |
| Input: command | null | {&quot;description&quot;: &quot;The Wrangler command (along with any arguments) you wish to run. Multiple Wrangler commands can be run by separating each command with a newline. Defaults to \`\\&quot;deploy\\&quot;\`.&quot;, &quot;required&quot;: false} |
| Input: environment | null | {&quot;description&quot;: &quot;The environment you&#x27;d like to deploy your Workers project to - must be defined in wrangler.toml&quot;} |
| Input: gitHubToken | null | {&quot;description&quot;: &quot;GitHub Token&quot;, &quot;required&quot;: false} |
| Input: packageManager | null | {&quot;description&quot;: &quot;The package manager you&#x27;d like to use to install and run wrangler. If not specified, the preferred package manager will be inferred based on the presence of a lockfile or fallback to using npm if no lockfile is found. Valid values are \`npm\` \| \`pnpm\` \| \`yarn\` \| \`bun\`.&quot;, &quot;required&quot;: false} |
| Input: postCommands | null | {&quot;description&quot;: &quot;Commands to execute after deploying the Workers project&quot;, &quot;required&quot;: false} |
| Input: preCommands | null | {&quot;description&quot;: &quot;Commands to execute before deploying the Workers project&quot;, &quot;required&quot;: false} |
| Input: quiet | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Supresses output from Wrangler commands, defaults to \`false\`&quot;, &quot;required&quot;: false} |
| Input: secrets | null | {&quot;description&quot;: &quot;A string of environment variable names, separated by newlines. These will be bound to your Worker as Secrets and must match the names of environment variables declared in \`env\` of this workflow.&quot;, &quot;required&quot;: false} |
| Input: vars | null | {&quot;description&quot;: &quot;A string of environment variable names, separated by newlines. These will be bound to your Worker using the values of matching environment variables declared in \`env\` of this workflow.&quot;, &quot;required&quot;: false} |
| Input: workingDirectory | null | {&quot;description&quot;: &quot;The relative path which Wrangler commands should be run from&quot;, &quot;required&quot;: false} |
| Input: wranglerVersion | null | {&quot;description&quot;: &quot;The version of Wrangler you&#x27;d like to use to deploy your Workers project&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;command-output&quot;, &quot;command-stderr&quot;, &quot;deployment-url&quot;, &quot;pages-deployment-alias-url&quot;, &quot;pages-deployment-id&quot;, &quot;pages-environment&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | ebbaa1584979971c8614a24965b4405ff95890e0 |
| Selected tag | null | v4.0.0 |

## Added: CodelyTV/pr-size-labeler

[Source](https://github.com/CodelyTV/pr-size-labeler) — Label a PR based on the amount of changes

New entries still require observed stability and fresh scan evidence before usage.

## conda-incubator/setup-miniconda

[Previous source](https://github.com/conda-incubator/setup-miniconda/tree/8ee1f361103df19b6f8c8655fd3967a8ecb162d5/) · [Current source](https://github.com/conda-incubator/setup-miniconda/tree/be893c923ea9cf1cf7cd510fbdde27c7e18cbdcb/) · [Upstream code diff](https://github.com/conda-incubator/setup-miniconda/compare/8ee1f361103df19b6f8c8655fd3967a8ecb162d5...be893c923ea9cf1cf7cd510fbdde27c7e18cbdcb)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 8ee1f361103df19b6f8c8655fd3967a8ecb162d5 | be893c923ea9cf1cf7cd510fbdde27c7e18cbdcb |
| Selected tag | v4.0.1 | v4.1.0 |

## crowdin/github-action

[Previous source](https://github.com/crowdin/github-action/tree/9af557de76d70c480f88065d336f445a362f402b/) · [Current source](https://github.com/crowdin/github-action/tree/df474cdfb9f41d6ae777118749477c2cdf7cacc8/) · [Upstream code diff](https://github.com/crowdin/github-action/compare/9af557de76d70c480f88065d336f445a362f402b...df474cdfb9f41d6ae777118749477c2cdf7cacc8)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 9af557de76d70c480f88065d336f445a362f402b | df474cdfb9f41d6ae777118749477c2cdf7cacc8 |
| Selected tag | v3.1.0 | v3.2.0 |

## danielroe/uppt

[Previous source](https://github.com/danielroe/uppt/tree/09882a5a0a1a20a0e802613a77ad59fcb1c1611c/) · [Current source](https://github.com/danielroe/uppt/tree/65a86313a63b10a6793de6c4ff8614b18e127a71/) · [Upstream code diff](https://github.com/danielroe/uppt/compare/09882a5a0a1a20a0e802613a77ad59fcb1c1611c...65a86313a63b10a6793de6c4ff8614b18e127a71)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 09882a5a0a1a20a0e802613a77ad59fcb1c1611c | 65a86313a63b10a6793de6c4ff8614b18e127a71 |
| Selected tag | v0.6.9 | v0.6.10 |

## derberg/manage-files-in-multiple-repositories

[Previous source](https://github.com/derberg/manage-files-in-multiple-repositories) · [Current source](https://github.com/derberg/manage-files-in-multiple-repositories/tree/b64d9c8480606c15f957cdda078f0122815512b8/)

| Changed | Before | After |
| --- | --- | --- |
| Input: bot\_branch\_name | null | {&quot;description&quot;: &quot;Use it if you do not want this action to create a new branch and new pull request with every run. By default branch names are generated. This means every single change is a separate commit. Such a static hardcoded branch name has an advantage that if you make a lot of changes, instead of having 5 PRs merged with 5 commits, you get one PR that is updated with new changes as long as the PR is not yet merged. If you use static name, and by mistake someone closed a PR, without merging and removing branch, this action will not fail but update the branch and open a new PR. Example value that you could provide: \`bot\_branch\_name: bot/update-files-from-global-repo\`.\\n&quot;, &quot;required&quot;: false} |
| Input: branches | null | {&quot;description&quot;: &quot;By default, action creates branch from default branch and opens PR only against default branch. With this property you can override this behaviour. You can provide a comma-separated list of branches this action shoudl work agains. You can also provide regex, but without comma as list of branches is split in code by comma.\\n&quot;, &quot;required&quot;: false} |
| Input: commit\_message | null | {&quot;default&quot;: &quot;Update global workflows&quot;, &quot;description&quot;: &quot;It is used as a commit message when pushing changes with global workflows.  It is also used as a title of the pull request that is created by this action.\\n&quot;, &quot;required&quot;: false} |
| Input: committer\_email | null | {&quot;default&quot;: &quot;noreply@github.com&quot;, &quot;description&quot;: &quot;The email of the committer that will be used in the commit of changes in the workflow file in specific repository. In the format \`noreply@github.com\`.\\n&quot;, &quot;required&quot;: false} |
| Input: committer\_username | null | {&quot;default&quot;: &quot;web-flow&quot;, &quot;description&quot;: &quot;The username (not display name) of the committer that will be used in the commit of changes in the workflow file in specific repository. In the format \`web-flow\`.\\n&quot;, &quot;required&quot;: false} |
| Input: destination | null | {&quot;description&quot;: &quot;Name of the directory where all files matching \\&quot;patterns\_to\_include\\&quot; will be copied. It doesn&#x27;t work with \\&quot;patterns\_to\_remove\\&quot;. In the format \`.github/workflows\`.\\n&quot;, &quot;required&quot;: false} |
| Input: exclude\_forked | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Boolean value on whether to exclude forked repositories from this action.\\n&quot;, &quot;required&quot;: false} |
| Input: exclude\_private | null | {&quot;default&quot;: false, &quot;description&quot;: &quot;Boolean value on whether to exclude private repositories from this action.\\n&quot;, &quot;required&quot;: false} |
| Input: github\_token | null | {&quot;description&quot;: &quot;Token to use GitHub API. It must have \\&quot;repo\\&quot; and \\&quot;workflow\\&quot; scopes so it can push to repo and edit workflows. It cannot be the default GitHub Actions token GITHUB\_TOKEN. GitHub Action token&#x27;s permissions are limited to the repository that contains your workflows. Provide token of the user that has rights to push to the repos that this action is suppose to update. \\n&quot;, &quot;required&quot;: true} |
| Input: patterns\_to\_ignore | null | {&quot;description&quot;: &quot;Comma-separated list of file paths or directories that should be handled by this action and updated in other repositories. This option is useful if you use \\&quot;patterns\_to\_include\\&quot; or \\&quot;patterns\_to\_remove\\&quot; with large amount of files, and some of them you want to ignore. In the format \`./github/workflows/another\_file.yml\`.\\n&quot;, &quot;required&quot;: true} |
| Input: patterns\_to\_include | null | {&quot;description&quot;: &quot;Comma-separated list of file paths or directories that should be handled by this action and copied or updated in other repositories. This option cannot be used at the same time with \\&quot;patterns\_to\_remove\\&quot;, these fields are mutually exclusive. In the format \`.github/workflows\`.\\n&quot;, &quot;required&quot;: true} |
| Input: patterns\_to\_remove | null | {&quot;description&quot;: &quot;Comma-separated list of file paths or directories that should be handled by this action and removed from other repositories. This option do not perform any removal of files that are located in repository there this action is used. This option cannot be used at the same time with \\&quot;patterns\_to\_include\\&quot;, these fields are mutually exclusive. In the format \`./github/workflows\`.\\n&quot;, &quot;required&quot;: true} |
| Input: repos\_to\_ignore | null | {&quot;description&quot;: &quot;Comma-separated list of repositories that should not get updates from this action. Action already ignores the repo in which the action is triggered so you do not need to add it explicitly. In the format \`repo1,repo2\`.\\n&quot;, &quot;required&quot;: false} |
| Input: sleep\_pr\_creation | null | {&quot;default&quot;: 0, &quot;description&quot;: &quot;Sleep time in seconds between processing each pull request. This is useful to avoid overwhelming CI/CD pipelines with too many PRs created at once. Set to 0 to disable sleep.\\n&quot;, &quot;required&quot;: false} |
| Input: topics\_to\_include | null | {&quot;description&quot;: &quot;Comma-separated list of topics that should get updates from this action.  Repos that do not contain one of the specified topics will get appended to the repos\_to\_ignore list.  In the format topic1,topic2.\\n&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | b64d9c8480606c15f957cdda078f0122815512b8 |
| Selected tag | null | v3.1.2 |

## devops-infra/action-commit-push

[Previous source](https://github.com/devops-infra/action-commit-push) · [Current source](https://github.com/devops-infra/action-commit-push/tree/f066ea8e19660de57d3d3a4a0b9d294ea2612e20/)

| Changed | Before | After |
| --- | --- | --- |
| Input: add\_timestamp | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to add timestamp to a new branch name&quot;, &quot;required&quot;: false} |
| Input: allow\_empty\_commit | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to allow creating an empty commit when there are no file changes.&quot;, &quot;required&quot;: false} |
| Input: amend | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to make amendment to the previous commit (--amend). Can be combined with commit\_message to change the message.&quot;, &quot;required&quot;: false} |
| Input: base\_branch | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Base branch name used for branch sync/reset (defaults to auto-detected main/master).&quot;, &quot;required&quot;: false} |
| Input: commit\_message | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Commit message to set&quot;, &quot;required&quot;: false} |
| Input: commit\_prefix | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Prefix added to commit message&quot;, &quot;required&quot;: false} |
| Input: fail\_on\_rebase\_conflict | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether to fail when branch rebase onto base branch conflicts.&quot;, &quot;required&quot;: false} |
| Input: force | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to use force push (--force). Use only when you need to overwrite remote changes. Potentially dangerous.&quot;, &quot;required&quot;: false} |
| Input: force\_with\_lease | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to use force push with lease (--force-with-lease). Safer than force as it checks for remote changes.&quot;, &quot;required&quot;: false} |
| Input: github\_token | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Personal Access Token for GitHub for pushing the code&quot;, &quot;required&quot;: true} |
| Input: no\_edit | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to not edit commit message when using amend&quot;, &quot;required&quot;: false} |
| Input: organization\_domain | null | {&quot;default&quot;: &quot;github.com&quot;, &quot;description&quot;: &quot;Name of GitHub Enterprise organization&quot;, &quot;required&quot;: false} |
| Input: repository\_path | null | {&quot;default&quot;: &quot;.&quot;, &quot;description&quot;: &quot;Relative path under GITHUB\_WORKSPACE to the checked-out repository (use when actions/checkout path is set)&quot;, &quot;required&quot;: false} |
| Input: reset\_target\_branch | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether to hard-reset target branch to origin/base\_branch before committing.&quot;, &quot;required&quot;: false} |
| Input: signing\_key | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Signing key material. For gpg use an ASCII-armored private key export; for ssh use a private key in OpenSSH or PEM format.&quot;, &quot;required&quot;: false} |
| Input: signing\_mode | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Commit signing mode. Supported values are gpg and ssh.&quot;, &quot;required&quot;: false} |
| Input: signing\_passphrase | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional passphrase for the signing key.&quot;, &quot;required&quot;: false} |
| Input: target\_branch | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Name of a new branch to push the code into (skipped when no changes and amend is false)&quot;, &quot;required&quot;: false} |
| Input: user\_email | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Git user.email to use for created commits. Defaults to GITHUB\_ACTOR@users.noreply.&lt;organization\_domain&gt; when empty.&quot;, &quot;required&quot;: false} |
| Input: user\_name | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Git user.name to use for created commits. Defaults to GITHUB\_ACTOR when empty.&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;branch\_name&quot;, &quot;files\_changed&quot;\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | f066ea8e19660de57d3d3a4a0b9d294ea2612e20 |
| Selected tag | null | v1.5.0 |

## github/branch-deploy

[Previous source](https://github.com/github/branch-deploy) · [Current source](https://github.com/github/branch-deploy/tree/97edad089bbbe0c0ad13db7bf9ac085eaa47e255/)

| Changed | Before | After |
| --- | --- | --- |
| Input: admins | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;A comma separated list of GitHub usernames or teams that should be considered admins by this Action. Admins can deploy pull requests without the need for branch protection approvals. Example: \\&quot;monalisa,octocat,my-org/my-team\\&quot;&quot;, &quot;required&quot;: false} |
| Input: admins\_pat | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;A GitHub personal access token with \\&quot;read:org\\&quot; scopes. This is only needed if you are using the \\&quot;admins\\&quot; option with a GitHub org team. For example: \\&quot;my-org/my-team\\&quot;&quot;, &quot;required&quot;: false} |
| Input: allow\_forks | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Allow branch deployments to run on repository forks. Default is \\&quot;false\\&quot;. Set to \\&quot;true\\&quot; only when your workflow intentionally supports deployments from forked pull requests.&quot;, &quot;required&quot;: false} |
| Input: allow\_non\_default\_target\_branch\_deployments | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether or not to allow deployments of pull requests that target a branch other than the default branch (aka stable branch) as their merge target. By default, this Action would reject the deployment of a branch named \\&quot;feature-branch\\&quot; if it was targeting \\&quot;foo\\&quot; instead of \\&quot;main\\&quot; (or whatever your default branch is). This option allows you to override that behavior and be able to deploy any branch in your repository regardless of the target branch. This option is potentially unsafe and should be used with caution as most default branches contain branch protection rules. Often times non-default branches do not contain these same branch protection rules. Follow along in this issue thread to learn more https://github.com/github/branch-deploy/issues/340&quot;, &quot;required&quot;: false} |
| Input: allow\_sha\_deployments | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to \\&quot;true\\&quot;, then you can deploy a specific sha instead of a branch. Example: \\&quot;.deploy 1234567890abcdef1234567890abcdef12345678 to production\\&quot; - This is dangerous and potentially unsafe, view the docs to learn more: https://github.com/github/branch-deploy/blob/main/docs/sha-deployments.md&quot;, &quot;required&quot;: false} |
| Input: checks | null | {&quot;default&quot;: &quot;all&quot;, &quot;description&quot;: &quot;This input defines how the branch-deploy Action will handle the status of CI checks on your PR/branch before deployments can continue. \`\\&quot;all\\&quot;\` requires that all CI checks must pass in order for a deployment to be triggered. \`\\&quot;required\\&quot;\` only waits for required CI checks to be passing. You can also pass in the names of your CI jobs in a comma separated list. View the documentation (docs/checks.md) for more details.&quot;, &quot;required&quot;: false} |
| Input: commit\_verification | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether or not to enforce commit verification before a deployment can continue. Default is \\&quot;false\\&quot;&quot;, &quot;required&quot;: false} |
| Input: deploy\_message\_path | null | {&quot;default&quot;: &quot;.github/deployment\_message.md&quot;, &quot;description&quot;: &quot;The repository-relative path to a trusted Markdown template for custom deployment messages. The file is fetched from the repository at the exact workflow SHA. Example: \\&quot;.github/deployment\_message.md\\&quot;&quot;, &quot;required&quot;: false} |
| Input: deployment\_confirmation | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether or not to require an additional confirmation before a deployment can continue. Default is \\&quot;false\\&quot;. If your project requires elevated security, it is highly recommended to enable this option - especially in open source projects where you might be deploying forks. docs/deployment-confirmation.md&quot;, &quot;required&quot;: false} |
| Input: deployment\_confirmation\_timeout | null | {&quot;default&quot;: &quot;60&quot;, &quot;description&quot;: &quot;The number of seconds to wait for a deployment confirmation before timing out. Must be a positive integer. Default is \\&quot;60\\&quot; seconds (1 minute).&quot;, &quot;required&quot;: false} |
| Input: deployment\_order\_scope | null | {&quot;default&quot;: &quot;all&quot;, &quot;description&quot;: &quot;Controls which deployment history records are considered by enforced deployment order. \\&quot;all\\&quot; uses the newest deployment from any system. \\&quot;branch-deploy\\&quot; uses the newest deployment whose payload identifies it as Branch Deploy and ignores newer deployments from other systems. Use \\&quot;branch-deploy\\&quot; only when Branch Deploy is authoritative for promotion.&quot;, &quot;required&quot;: false} |
| Input: disable\_lock | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to \\&quot;true\\&quot;, all deployment locking is disabled. Useful for workflows where concurrent deployments are safe (e.g. iOS/Android builds uploaded to TestFlight). When disabled, lock-related commands return an informational message instead of modifying lock state.&quot;, &quot;required&quot;: false} |
| Input: disable\_naked\_commands | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to \\&quot;true\\&quot;, then naked commands will be disabled. Example: \\&quot;.deploy\\&quot; will not trigger a deployment. Instead, you must use \\&quot;.deploy to production\\&quot; to trigger a deployment. This is useful if you want to prevent accidental deployments from happening. Read more about naked commands here: https://github.com/github/branch-deploy/blob/main/docs/naked-commands.md&quot;, &quot;required&quot;: false} |
| Input: draft\_permitted\_targets | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional environments which can allow \\&quot;draft\\&quot; pull requests to be deployed. By default, this input option is empty and no environments allow deployments sourced from a pull request in a \\&quot;draft\\&quot; state. Examples: \\&quot;development,staging\\&quot;&quot;, &quot;required&quot;: false} |
| Input: enforced\_deployment\_order | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of environments that must be deployed in a specific order. Example: \`\\&quot;development,staging,production\\&quot;\`. If this is set then you cannot deploy to latter environments unless the former ones have a successful and active deployment on the latest commit first.&quot;, &quot;required&quot;: false} |
| Input: environment | null | {&quot;default&quot;: &quot;production&quot;, &quot;description&quot;: &quot;The name of the default environment to deploy to. Example: by default, if you type \`.deploy\`, it will assume \\&quot;production\\&quot; as the default environment&quot;, &quot;required&quot;: false} |
| Input: environment\_targets | null | {&quot;default&quot;: &quot;production,development,staging&quot;, &quot;description&quot;: &quot;Optional (or additional) target environments to select for use with deployments. Example, \\&quot;production,development,staging\\&quot;. Example  usage: \`.deploy to development\`, \`.deploy to production\`, \`.deploy to staging\`&quot;, &quot;required&quot;: false} |
| Input: environment\_url\_in\_comment | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;If the environment\_url detected in the deployment should be appended to the successful deployment comment or not. Examples: \\&quot;true\\&quot; or \\&quot;false\\&quot;&quot;, &quot;required&quot;: false} |
| Input: environment\_urls | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Optional target environment URLs to use with deployments. This input option is a mapping of environment names to URLs and the environment names must match the \\&quot;environment\_targets\\&quot; input option. This option is a comma separated list with pipes (\|) separating the environment from the URL. Note: \\&quot;disabled\\&quot; is a special keyword to disable an environment url if you enable this option. Format: \\&quot;&lt;environment1&gt;\|&lt;url1&gt;,&lt;environment2&gt;\|&lt;url2&gt;,etc\\&quot; Example: \\&quot;production\|https://myapp.com,development\|https://dev.myapp.com,staging\|disabled\\&quot;&quot;, &quot;required&quot;: false} |
| Input: failed\_deploy\_labels | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of labels to add to the pull request when a deployment fails. Example: \\&quot;failed,deploy-failed\\&quot;&quot;, &quot;required&quot;: false} |
| Input: failed\_noop\_labels | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of labels to add to the pull request when a noop deployment fails. Example: \\&quot;failed,noop-failed\\&quot;&quot;, &quot;required&quot;: false} |
| Input: github\_token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;The GitHub token used to create an authenticated client - Provided for you by default!&quot;, &quot;required&quot;: true} |
| Input: global\_lock\_flag | null | {&quot;default&quot;: &quot;--global&quot;, &quot;description&quot;: &quot;The flag to pass into the lock command to lock all environments. Example: \\&quot;--global\\&quot;&quot;, &quot;required&quot;: false} |
| Input: help\_trigger | null | {&quot;default&quot;: &quot;.help&quot;, &quot;description&quot;: &quot;The string to look for in comments as an IssueOps help trigger. Example: \\&quot;.help\\&quot;&quot;, &quot;required&quot;: false} |
| Input: ignored\_checks | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of checks that will be ignored when determining if a deployment can continue. This setting allows you to skip failing, pending, or incomplete checks regardless of the \`checks\` setting above. Example: \\&quot;lint,markdown-formatting,update-pr-label\\&quot;. View the documentation (docs/checks.md) for more details.&quot;, &quot;required&quot;: false} |
| Input: lock\_info\_alias | null | {&quot;default&quot;: &quot;.wcid&quot;, &quot;description&quot;: &quot;An alias or shortcut to get details about the current lock (if it exists) Example: \\&quot;.info\\&quot;&quot;, &quot;required&quot;: false} |
| Input: lock\_trigger | null | {&quot;default&quot;: &quot;.lock&quot;, &quot;description&quot;: &quot;The string to look for in comments as an IssueOps lock trigger. Used for locking branch deployments on a specific branch. Example: \\&quot;.lock\\&quot;&quot;, &quot;required&quot;: false} |
| Input: merge\_deploy\_mode | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;This advanced alternate mode controls deployment after changes reach the default branch. The &#x27;continue&#x27; output is &#x27;false&#x27; only when the newest identifiable Branch Deploy deployment for the environment is active and its commit tree matches the current default branch. Missing, inactive, failed, pending, malformed, or different-tree deployment history sets &#x27;continue&#x27; to &#x27;true&#x27;. The &#x27;environment&#x27; output is also set for subsequent steps.&quot;, &quot;required&quot;: false} |
| Input: noop\_trigger | null | {&quot;default&quot;: &quot;.noop&quot;, &quot;description&quot;: &quot;The string to look for in comments as an IssueOps noop trigger. Example: \\&quot;.noop\\&quot;&quot;, &quot;required&quot;: false} |
| Input: outdated\_mode | null | {&quot;default&quot;: &quot;strict&quot;, &quot;description&quot;: &quot;The mode to use for determining if a branch is up-to-date or not before allowing deployments. This option is closely related to the \\&quot;update\_branch\\&quot; input option above. There are three available modes to choose from \\&quot;pr\_base\\&quot;, \\&quot;default\_branch\\&quot;, or \\&quot;strict\\&quot;. The default is \\&quot;strict\\&quot; to help ensure that deployments are using the most up-to-date code. Please see the docs/outdated\_mode.md document for more details.&quot;, &quot;required&quot;: false} |
| Input: param\_separator | null | {&quot;default&quot;: &quot;\|&quot;, &quot;description&quot;: &quot;The separator to use for parsing parameters in comments in deployment requests. Parameters will are saved as outputs and can be used in subsequent steps&quot;, &quot;required&quot;: false} |
| Input: permissions | null | {&quot;default&quot;: &quot;write,admin&quot;, &quot;description&quot;: &quot;The allowed GitHub permissions an actor can have to invoke IssueOps commands - Example: \\&quot;write,admin\\&quot;&quot;, &quot;required&quot;: true} |
| Input: production\_environments | null | {&quot;default&quot;: &quot;production&quot;, &quot;description&quot;: &quot;A comma separated list of environments that should be treated as \\&quot;production\\&quot;. GitHub defines \\&quot;production\\&quot; as an environment that end users or systems interact with. Example: \\&quot;production,production-eu\\&quot;. By default, GitHub will set the \\&quot;production\_environment\\&quot; to \\&quot;true\\&quot; if the environment name is \\&quot;production\\&quot;. This option allows you to override that behavior so you can use \\&quot;prod\\&quot;, \\&quot;prd\\&quot;, \\&quot;main\\&quot;, \\&quot;production-eu\\&quot;, etc. as your production environment name. ref: https://github.com/github/branch-deploy/issues/208&quot;, &quot;required&quot;: false} |
| Input: reaction | null | {&quot;default&quot;: &quot;eyes&quot;, &quot;description&quot;: &quot;If set, the specified emoji \\&quot;reaction\\&quot; is put on the comment to indicate that the trigger was detected. For example, \\&quot;rocket\\&quot; or \\&quot;eyes\\&quot;&quot;, &quot;required&quot;: false} |
| Input: required\_contexts | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Manually enforce commit status checks before a deployment can continue. Only use this option if you wish to manually override the settings you have configured for your branch protection settings for your GitHub repository. Default is \\&quot;false\\&quot; - Example value: \\&quot;context1,context2,context3\\&quot; - In most cases you will not need to touch this option&quot;, &quot;required&quot;: false} |
| Input: skip\_ci | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of environments that will not use passing CI as a requirement for deployment. Use this option to explicitly bypass branch protection settings for a certain environment in your repository. Default is an empty string \\&quot;\\&quot; - Example: \\&quot;development,staging\\&quot;&quot;, &quot;required&quot;: false} |
| Input: skip\_completing | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to true, bypass the entire post-action completion path. The workflow must manage final deployment status, comments, reactions, labels, and non-sticky lock cleanup. Default is false.&quot;, &quot;required&quot;: false} |
| Input: skip\_reviews | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of environment that will not use reviews/approvals as a requirement for deployment. Use this options to explicitly bypass branch protection settings for a certain environment in your repository. Default is an empty string \\&quot;\\&quot; - Example: \\&quot;development,staging\\&quot;&quot;, &quot;required&quot;: false} |
| Input: skip\_successful\_deploy\_labels\_if\_approved | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether or not the post run logic should skip adding successful deploy labels if the pull request is approved. This can be useful if you add a label such as \\&quot;ready-for-review\\&quot; after a .deploy completes but want to skip adding that label in situations where the pull request is already approved.&quot;, &quot;required&quot;: false} |
| Input: skip\_successful\_noop\_labels\_if\_approved | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Whether or not the post run logic should skip adding successful noop labels if the pull request is approved. This can be useful if you add a label such as \\&quot;ready-for-review\\&quot; after a .noop completes but want to skip adding that label in situations where the pull request is already approved.&quot;, &quot;required&quot;: false} |
| Input: stable\_branch | null | {&quot;default&quot;: &quot;main&quot;, &quot;description&quot;: &quot;The name of a stable branch to deploy to (rollbacks). Example: \\&quot;main\\&quot;&quot;, &quot;required&quot;: false} |
| Input: status | null | {&quot;default&quot;: &quot;${{ job.status }}&quot;, &quot;description&quot;: &quot;The status of the GitHub Actions - For use in the post run workflow - Provided for you by default!&quot;, &quot;required&quot;: true} |
| Input: sticky\_locks | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to \\&quot;true\\&quot;, locks will not be released after a deployment run completes. This applies to both successful, and failed deployments. Sticky locks are also known as \\&quot;hubot style deployment locks\\&quot;. They will persist until they are manually released by a user, or if you configure another workflow with the \\&quot;unlock on merge\\&quot; mode to remove them automatically on PR merge.&quot;, &quot;required&quot;: false} |
| Input: sticky\_locks\_for\_noop | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If set to \\&quot;true\\&quot;, then sticky\_locks will also be used for noop deployments. This can be useful in some cases but it often leads to locks being left behind when users test noop deployments.&quot;, &quot;required&quot;: false} |
| Input: successful\_deploy\_labels | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of labels to add to the pull request when a deployment is successful. Example: \\&quot;deployed,success\\&quot;&quot;, &quot;required&quot;: false} |
| Input: successful\_noop\_labels | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;A comma separated list of labels to add to the pull request when a noop deployment is successful. Example: \\&quot;noop,success\\&quot;&quot;, &quot;required&quot;: false} |
| Input: trigger | null | {&quot;default&quot;: &quot;.deploy&quot;, &quot;description&quot;: &quot;The string to look for in comments as an IssueOps trigger. Example: \\&quot;.deploy\\&quot;&quot;, &quot;required&quot;: false} |
| Input: unlock\_on\_merge\_mode | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;This is an advanced option that is an alternate workflow bundled into this Action. You can optionally use this mode in a custom workflow to automatically release all locks that came from a pull request when the pull request is merged. This is useful if you want to ensure that locks are not left behind when a pull request is merged.&quot;, &quot;required&quot;: false} |
| Input: unlock\_trigger | null | {&quot;default&quot;: &quot;.unlock&quot;, &quot;description&quot;: &quot;The string to look for in comments as an IssueOps unlock trigger. Used for unlocking branch deployments. Example: \\&quot;.unlock\\&quot;&quot;, &quot;required&quot;: false} |
| Input: update\_branch | null | {&quot;default&quot;: &quot;warn&quot;, &quot;description&quot;: &quot;Determine how you want this Action to handle \\&quot;out-of-date\\&quot; branches. Available options: \\&quot;disabled\\&quot;, \\&quot;warn\\&quot;, \\&quot;force\\&quot;. \\&quot;disabled\\&quot; means that the Action will not care if a branch is out-of-date. \\&quot;warn\\&quot; means that the Action will warn the user that a branch is out-of-date and exit without deploying. \\&quot;force\\&quot; means that the Action will force update the branch. Note: The \\&quot;force\\&quot; option is not recommended due to Actions not being able to re-run CI on commits originating from Actions itself&quot;, &quot;required&quot;: false} |
| Input: use\_security\_warnings | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Whether or not to leave security related warnings in log messages during deployments. Default is \\&quot;true\\&quot;&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;actor&quot;, &quot;actor\_handle&quot;, &quot;approved\_reviews\_count&quot;, &quot;base\_ref&quot;, &quot;comment\_body&quot;, &quot;comment\_id&quot;, &quot;commit\_status&quot;, &quot;commit\_verified&quot;, &quot;continue&quot;, &quot;decision&quot;, &quot;default\_branch\_tree\_sha&quot;, &quot;deployment\_id&quot;, &quot;environment&quot;, &quot;environment\_url&quot;, &quot;fork&quot;, &quot;fork\_checkout&quot;, &quot;fork\_full\_name&quot;, &quot;fork\_label&quot;, &quot;fork\_ref&quot;, &quot;global\_lock\_claimed&quot;, &quot;global\_lock\_released&quot;, &quot;initial\_comment\_id&quot;, &quot;initial\_reaction\_id&quot;, &quot;is\_outdated&quot;, &quot;issue\_number&quot;, &quot;merge\_state\_status&quot;, &quot;needs\_to\_be\_deployed&quot;, &quot;non\_default\_target\_branch\_used&quot;, &quot;noop&quot;, &quot;params&quot;, &quot;parsed\_params&quot;, &quot;reason\_code&quot;, &quot;ref&quot;, &quot;result&quot;, &quot;review\_decision&quot;, &quot;sha&quot;, &quot;sha\_deployment&quot;, &quot;total\_seconds&quot;, &quot;triggered&quot;, &quot;type&quot;, &quot;unlocked\_environments&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 97edad089bbbe0c0ad13db7bf9ac085eaa47e255 |
| Selected tag | null | v12.0.1 |

## hashicorp/actions-generate-metadata

[Previous source](https://github.com/hashicorp/actions-generate-metadata/tree/a43468dfb100445f2c2aa52cdc3d57b2c982a0f3/) · [Current source](https://github.com/hashicorp/actions-generate-metadata/tree/780b17558ee4b93391b26a9e08d7cb858d9ae1e8/) · [Upstream code diff](https://github.com/hashicorp/actions-generate-metadata/compare/a43468dfb100445f2c2aa52cdc3d57b2c982a0f3...780b17558ee4b93391b26a9e08d7cb858d9ae1e8)

| Changed | Before | After |
| --- | --- | --- |
| Input: releaseSubDir | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Sub-directory name under .release/ that holds the ci.hcl for this sub-product (e.g. \\&quot;alpha-plugin\\&quot;). The CRT orchestrator uses this value to load .release/&lt;releaseSubDir&gt;/ci.hcl instead of the legacy .release/ci.hcl. Leave empty (default) for single-product repos.\\n&quot;, &quot;required&quot;: false} |
| Selected SHA | a43468dfb100445f2c2aa52cdc3d57b2c982a0f3 | 780b17558ee4b93391b26a9e08d7cb858d9ae1e8 |
| Selected tag | v1.2.0 | v1.3.0 |

## korthout/backport-action

[Previous source](https://github.com/korthout/backport-action/tree/2e830a1d0b8269505846ddd407a70876913ad1f8/) · [Current source](https://github.com/korthout/backport-action/tree/6b65649031ac6d18ffdfd0c0820e9436f3fde22b/) · [Upstream code diff](https://github.com/korthout/backport-action/compare/2e830a1d0b8269505846ddd407a70876913ad1f8...6b65649031ac6d18ffdfd0c0820e9436f3fde22b)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 2e830a1d0b8269505846ddd407a70876913ad1f8 | 6b65649031ac6d18ffdfd0c0820e9436f3fde22b |
| Selected tag | v4.6.0 | v4.6.1 |

## Mic92/hestia

[Previous source](https://github.com/Mic92/hestia) · [Current source](https://github.com/Mic92/hestia/tree/dfed9ced335d28978ba74e513939a10db1f71025/)

| Changed | Before | After |
| --- | --- | --- |
| Input: binary | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to a pre-built hestia binary (e.g. the result of \`nix build\`). Takes precedence over \`version\`.\\n&quot;, &quot;required&quot;: false} |
| Input: drain-timeout | null | {&quot;default&quot;: &quot;300&quot;, &quot;description&quot;: &quot;Maximum number of seconds the post-job step waits for the final upload (chunking, pack upload, manifest commit).\\n&quot;, &quot;required&quot;: false} |
| Input: filter-drv-closures | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Apply upstream-cache-filter to registered derivation closures. Requires \`upstream-cache-filter\`; use \`hestia prefetch\` to retain bulk closure fetching.\\n&quot;, &quot;required&quot;: false} |
| Input: github-token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;Token for the attestation API lookup that verifies downloaded release binaries, and for the daemon&#x27;s upfront check which cached packs were evicted (needs \`actions: read\`; skipped without it).\\n&quot;, &quot;required&quot;: false} |
| Input: listen | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Address the substituter HTTP server listens on. Defaults to 127.0.0.1 with a free port picked per invocation, so the action can run more than once in a job without the daemons colliding.\\n&quot;, &quot;required&quot;: false} |
| Input: no-closure | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Cache built paths only, without their runtime closure (dependencies stay on upstream caches).\\n&quot;, &quot;required&quot;: false} |
| Input: read-only | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Substitute from the cache but never write to it: no post-build-hook, no drain, and the daemon refuses uploads. For jobs that should only consume what a central job cached.\\n&quot;, &quot;required&quot;: false} |
| Input: socket | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Unix socket path for the post-build-hook listener. Defaults to a per-invocation path under the runner&#x27;s temp directory.\\n&quot;, &quot;required&quot;: false} |
| Input: upstream-cache-filter | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Skip paths signed by an upstream cache (cache.nixos.org by default) instead of caching them. Saves GHA cache quota for projects with big nixpkgs closures.\\n&quot;, &quot;required&quot;: false} |
| Input: upstream-cache-key-names | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Space-separated signing key names treated as upstream caches by \`upstream-cache-filter\`.\\n&quot;, &quot;required&quot;: false} |
| Input: version | null | {&quot;default&quot;: &quot;latest&quot;, &quot;description&quot;: &quot;Hestia release tag to download from GitHub releases (e.g. \\&quot;v0.1.0-beta.1\\&quot;), or \\&quot;latest\\&quot; to auto-resolve the newest release.  The downloaded binary is verified against GitHub&#x27;s build provenance attestations before it runs.\\n&quot;, &quot;required&quot;: false} |
| Input: wait-manifest-version | null | {&quot;default&quot;: &quot;0&quot;, &quot;description&quot;: &quot;Wait up to 60s at daemon startup until the cache manifest has at least this version. Matrix build jobs pass the eval job&#x27;s \`manifest-version\` output so the just-uploaded drv closures are visible despite GHA cache lookup lag.\\n&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | dfed9ced335d28978ba74e513939a10db1f71025 |
| Selected tag | null | v3.1.0 |

## reviewdog/action-actionlint

[Previous source](https://github.com/reviewdog/action-actionlint/tree/320fcdd9c860767cf17fab3b20e22e739d5d02b8/) · [Current source](https://github.com/reviewdog/action-actionlint/tree/5be522b94290e249dba9f5daded2f7157733e3d2/) · [Upstream code diff](https://github.com/reviewdog/action-actionlint/compare/320fcdd9c860767cf17fab3b20e22e739d5d02b8...5be522b94290e249dba9f5daded2f7157733e3d2)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 320fcdd9c860767cf17fab3b20e22e739d5d02b8 | 5be522b94290e249dba9f5daded2f7157733e3d2 |
| Selected tag | v1.76.0 | v1.76.1 |

## shaftoe/pi-coding-agent-action

[Previous source](https://github.com/shaftoe/pi-coding-agent-action/tree/853a9af5ac64e79c79fa6bb3958314aa1acf7e92/) · [Current source](https://github.com/shaftoe/pi-coding-agent-action/tree/8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4/) · [Upstream code diff](https://github.com/shaftoe/pi-coding-agent-action/compare/853a9af5ac64e79c79fa6bb3958314aa1acf7e92...8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4)

| Changed | Before | After |
| --- | --- | --- |
| Input: cache\_warming | null | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Prompt cache-warming mode. Keeps expensive prompt-cache prefixes alive with cost-aware one-token refreshes so pauses (e.g. long tool runs) don&#x27;t pay full input price again. One of \`off\`, \`streaming\` (refresh during long tool executions; the default), or \`idle\` (also refresh between prompts). Refreshes are billed as a cache read plus one output token and only fire when expected savings exceed the cost.&quot;, &quot;required&quot;: false} |
| Selected SHA | 853a9af5ac64e79c79fa6bb3958314aa1acf7e92 | 8faf601af3a91f4526c8fc0f4b50cea0ef67b5d4 |
| Selected tag | v2.28.1 | v2.29.0 |

## voidzero-dev/setup-vp

[Previous source](https://github.com/voidzero-dev/setup-vp/tree/24d870228786dc83ae73482406bdd1e7befaec14/) · [Current source](https://github.com/voidzero-dev/setup-vp/tree/3754dd7dbdb32bd8f6d28b6043de13ad3a75f21f/) · [Upstream code diff](https://github.com/voidzero-dev/setup-vp/compare/24d870228786dc83ae73482406bdd1e7befaec14...3754dd7dbdb32bd8f6d28b6043de13ad3a75f21f)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 24d870228786dc83ae73482406bdd1e7befaec14 | 3754dd7dbdb32bd8f6d28b6043de13ad3a75f21f |
| Selected tag | v1.21.0 | v1.21.1 |
