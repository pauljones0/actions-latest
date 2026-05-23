# actions-latest

Keeping track of the latest versions of various GitHub Actions

https://raw.githubusercontent.com/pauljones0/actions-latest/main/versions.txt

Access that URL for a trusted list of the official Actions belonging to the [GitHub Actions](https://github.com/actions) organization, plus additional actions listed in `trusted-actions.txt`, along with their latest version tags.

The broader community list is published separately:

https://raw.githubusercontent.com/pauljones0/actions-latest/main/community-versions.txt

You can point coding agents such as Claude Code and Codex CLI at this URL so they know the most recent Actions versions to use in their workflow files.

## MCP server

This fork can also run as a stdio MCP server for coding agents:

```json
{
  "mcpServers": {
    "actions-latest": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/pauljones0/actions-latest.git",
        "actions-latest-mcp"
      ]
    }
  }
}
```

Available tools:

- `latest_github_actions_versions`: returns trusted `versions.txt` content by default. Pass `include_untrusted=true` to include `community-versions.txt`.
- `latest_github_action_version`: looks up one action, such as `checkout`, `actions/checkout@v4`, or `softprops/action-gh-release@v2`.
- `check_github_actions_workflow`: checks workflow YAML text for outdated GitHub Action references. Pass `include_untrusted=true` to check against the broader community list.

Version recommendations follow the same style as Simon's original `versions.txt`: the highest floating major tag that matches `vN`, such as `actions/checkout@v6`, not exact release tags such as `v6.0.2`. Existing `@stable` branch refs are treated as already intentionally stable.

Set `GITHUB_TOKEN` to avoid GitHub API rate limits when checking actions outside the generated snapshots. Set `ACTIONS_LATEST_URL` to override the trusted versions source, `ACTIONS_LATEST_COMMUNITY_URL` to override the community source, or `ACTIONS_LATEST_OFFLINE=1` to use the packaged snapshots instead of fetching live URLs.

<!-- VERSIONS_START -->
## Latest trusted versions

```
actions/actions-sync@v202601271539
actions/attest@v4
actions/cache@v5
actions/checkout@v6
actions/configure-pages@v6
actions/create-github-app-token@v3
actions/create-release@v1
actions/delete-package-versions@v5
actions/dependency-review-action@v3
actions/deploy-pages@v5
actions/download-artifact@v8
actions/first-interaction@v3
actions/github-script@v9
actions/go-dependency-submission@v2
actions/hello-world-docker-action@v2
actions/hello-world-javascript-action@v1
actions/javascript-action@v1
actions/jekyll-build-pages@v1
actions/labeler@v6
actions/publish-immutable-action@v0
actions/setup-dotnet@v5
actions/setup-elixir@v1
actions/setup-go@v6
actions/setup-haskell@v1
actions/setup-java@v5
actions/setup-node@v6
actions/setup-python@v6
actions/setup-ruby@v1
actions/stale@v10
actions/upload-artifact@v7
actions/upload-code-coverage@v1
actions/upload-pages-artifact@v5
actions/upload-release-asset@v1
astral-sh/ruff-action@v3
astral-sh/setup-uv@v7
github/ai-moderator@v1
github/branch-deploy@v11
github/codeql-action@v4
github/codeql-coding-standards@v2
github/command@v2
github/copilot-release-notes@v1
github/dependabot-action@v3
github/lock@v3
github/update-project-action@v4
github/webpack-bundlesize-compare-action@v1
```
<!-- VERSIONS_END -->

<!-- COMMUNITY_VERSIONS_START -->
## Latest community versions

```
abatilo/actions-poetry@v4
actions-rust-lang/setup-rust-toolchain@v1
ad-m/github-push-action@v1
AlbertHernandez/working-label-action@v1
Amadevus/pwsh-script@v2
amannn/action-semantic-pull-request@v6
amondnet/vercel-action@v42
anchore/scan-action@v7
andresz1/size-limit-action@v1
Andrew-Chen-Wang/github-wiki-action@v5
anoopt/ms-graph-create-event@v1
anothrNick/github-tag-action@v1
appleboy/jenkins-action@v1
appleboy/scp-action@v1
appleboy/ssh-action@v1
ArtiomTr/jest-coverage-report-action@v2
artis3n/ansible_galaxy_collection@v3
ashutoshgngwr/validate-fastlane-supply-metadata@v2
avto-dev/markdown-lint@v1
aws-actions/amazon-ecr-login@v2
aws-actions/amazon-ecs-deploy-task-definition@v2
aws-actions/amazon-ecs-render-task-definition@v1
aws-actions/configure-aws-credentials@v6
Azure/docker-login@v2
Azure/functions-action@v1
Azure/k8s-deploy@v6
Azure/login@v3
Azure/static-web-apps-deploy@v1
Azure/webapps-deploy@v3
benc-uk/workflow-dispatch@v1
benjefferies/branch-protection-bot@v1
benmatselby/gollum-page-watcher-action@v1
boasiHQ/interactive-inputs@v2
bobheadxi/deployments@v1
bobheadxi/gobenchdata@v1
Borales/actions-yarn@v5
Burnett01/rsync-deployments@v8
c-hive/fresh-bot@v1
c-hive/gha-remove-artifacts@v1
cachix/install-nix-action@v31
cloudflare/wrangler-action@v4
codecov/codecov-action@v6
CodelyTV/pr-size-labeler@v1
conda-incubator/setup-miniconda@v4
cpina/github-action-push-to-another-repository@v1
crazy-max/ghaction-chocolatey@v4
crazy-max/ghaction-github-labeler@v6
crazy-max/ghaction-github-pages@v5
crazy-max/ghaction-github-status@v5
crazy-max/ghaction-import-gpg@v7
crazy-max/ghaction-upx@v4
crazy-max/ghaction-virustotal@v5
crazy-max/ghaction-xgo@v4
cyprieng/github-breakout@v1
czl9707/gh-space-shooter@v2
dawidd6/action-download-artifact@v21
dawidd6/action-send-mail@v17
dessant/lock-threads@v6
DeterminateSystems/nix-installer-action@v22
Dirrk/terraform-docs@v1
docker/bake-action@v7
docker/build-push-action@v7
docker/login-action@v4
docker/metadata-action@v6
docker/setup-buildx-action@v4
docker/setup-qemu-action@v4
dorny/paths-filter@v4
dorny/test-reporter@v3
easimon/maximize-build-space@v10
elgohr/Github-Release-Action@v5
elgohr/Publish-Docker-Github-Action@v5
EndBug/add-and-commit@v10
EnricoMi/publish-unit-test-result-action@v2
esamattis/npm-release@v2
expo/expo-github-action@v8
fabasoad/jsonbin-action@v3
fabasoad/nsfw-detection-action@v3
fabasoad/pascal-action@v1
fabasoad/setup-brainfuck-action@v1
fabasoad/setup-cobol-action@v1
fabasoad/setup-mint-action@v1
fabasoad/translation-action@v4
fabasoad/twilio-voice-call-action@v3
fcakyon/conda-publish-action@v1
FirebaseExtended/action-hosting-deploy@v0
flowwer-dev/pull-request-stats@v1
foo-software/lighthouse-check-action@v1
FranzDiebold/github-env-vars-action@v2
gabrielfalcao/pyenv-action@v18
gautamkrishnar/blog-post-workflow@v1
gcarreno/setup-lazarus@v3
github-community-projects/issue-metrics@v4
gitleaks/gitleaks-action@v2
go-task/setup-task@v2
goanpeca/setup-miniconda@v2
google-github-actions/auth@v3
google-github-actions/deploy-appengine@v3
google-github-actions/deploy-cloudrun@v3
google-github-actions/run-gemini-cli@v0
google-github-actions/setup-gcloud@v3
google-github-actions/upload-cloud-storage@v3
goreleaser/goreleaser-action@v7
gradle/actions@v6
HaaLeo/publish-vscode-extension@v2
hashicorp/setup-terraform@v4
hashicorp/vault-action@v4
haythem/public-ip@v1
helm/chart-releaser-action@v1
helm/chart-testing-action@v2
helm/kind-action@v1
ilammy/msvc-dev-cmd@v1
ilammy/setup-nasm@v1
InVisionApp/private-action-loader@v5
JamesIves/github-pages-deploy-action@v4
jonelantha/gatsby-s3-action@v4
JS-DevTools/npm-publish@v4
julia-actions/julia-runtest@v1
julia-actions/setup-julia@v3
kishikawakatsumi/xcresulttool@v1
koenrh/dnscontrol-action@v3
luckyPipewrench/pipelock@v2
lycheeverse/lychee-action@v2
machulav/ec2-github-runner@v2
madhead/check-gradle-version@v1
MarceloPrado/has-changed-path@v1
mathieudutour/github-tag-action@v5
maxim-lobanov/setup-cocoapods@v1
maxim-lobanov/setup-xamarin@v1
maxim-lobanov/setup-xcode@v1
metcalfc/changelog-generator@v4
mgrachev/action-dotenv-linter@v3
micnncim/action-label-syncer@v1
microsoft/setup-msbuild@v3
mikepenz/action-junit-report@v6
mikepenz/release-changelog-builder-action@v6
mxschmitt/action-tmate@v3
nick-fields/assert-action@v2
nick-fields/retry@v4
nwtgck/actions-comment-run@v3
nwtgck/actions-netlify@v3
oven-sh/setup-bun@v2
peaceiris/actions-gh-pages@v4
peaceiris/actions-hugo@v3
peaceiris/actions-mdbook@v2
peakoss/anti-slop@v0
peter-evans/autopep8@v2
peter-evans/create-issue-from-file@v6
peter-evans/create-or-update-comment@v5
peter-evans/create-pull-request@v8
peter-evans/dockerhub-description@v5
peter-evans/repository-dispatch@v4
peter-evans/slash-command-dispatch@v5
Platane/snk@v3
pnpm/action-setup@v6
pulumi/actions@v7
r-lib/actions@v2
ReactiveCircus/android-emulator-runner@v2
release-drafter/release-drafter@v7
Renato66/auto-label@v3
repo-sync/github-sync@v2
reviewdog/action-eslint@v1
reviewdog/action-golangci-lint@v2
reviewdog/action-misspell@v1
reviewdog/action-shellcheck@v1
reviewdog/action-stylelint@v1
reviewdog/action-tflint@v1
reviewdog/action-tfsec@v1
reviewdog/action-vint@v1
rlespinasse/git-commit-data-action@v1
rossjrw/pr-preview-action@v1
rtCamp/action-slack-notify@v2
samuelmeuli/lint-action@v2
satackey/action-docker-layer-caching@v0
say8425/aws-secrets-manager-actions@v2
schdck/create-env-json@v2
sergioramos/yarn-actions@v6
shivammathur/setup-php@v2
slackapi/slack-github-action@v3
snok/install-poetry@v1
snyk/actions@v1
softprops/action-gh-release@v3
softprops/turnstyle@v3
SonarSource/sonarqube-scan-action@v8
SpicyPizza/create-envfile@v2
stefanzweifel/git-auto-commit-action@v7
step-security/harden-runner@v2
subosito/flutter-action@v2
super-linter/super-linter@v8
Swatinem/rust-cache@v2
tauri-apps/tauri-action@v0
technote-space/toc-generator@v4
test-summary/action@v2
tgymnich/fork-sync@v2
thollander/actions-comment-pull-request@v3
TimonVS/pr-labeler-action@v5
tj-actions/changed-files@v47
treosh/lighthouse-ci-action@v12
trilom/file-changes-action@v1
trstringer/manual-approval@v1
TryGhost/action-deploy-theme@v1
tylermurry/github-pr-landmine@v1
tzkhan/pr-update-action@v2
uraimo/run-on-arch-action@v3
wagoid/commitlint-github-action@v6
wangyoucao577/go-release-action@v1
wearerequired/lint-action@v2
webbertakken/unity-test-runner@v4
whoan/docker-build-with-cache-action@v8
WyriHaximus/github-action-create-milestone@v1
WyriHaximus/github-action-get-previous-tag@v2
WyriHaximus/github-action-next-semvers@v1
WyriHaximus/github-action-wait-for-status@v1
wzieba/Firebase-Distribution-Github-Action@v1
xen0l/iam-lint@v2
xt0rted/block-autosquash-commits-action@v2
xt0rted/stylelint-problem-matcher@v1
xu-cheng/latex-action@v4
yaananth/run-notebook@v2
zerotier/github-action@v1
zyborg/gh-action-buildnum@v2
```
<!-- COMMUNITY_VERSIONS_END -->
