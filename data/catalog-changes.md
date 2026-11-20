# Latest catalog changes

12 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## anthropics/claude-code-action

[Previous source](https://github.com/anthropics/claude-code-action/tree/4fa93a88de49bbef68b10eb15aabedf28ca0e1ed/) · [Current source](https://github.com/anthropics/claude-code-action/tree/4d75e5f390ee76b2e09c1980ecc99ff3a2e088c8/) · [Upstream code diff](https://github.com/anthropics/claude-code-action/compare/4fa93a88de49bbef68b10eb15aabedf28ca0e1ed...4d75e5f390ee76b2e09c1980ecc99ff3a2e088c8)

| Changed | Before | After |
| --- | --- | --- |
| Findings | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\], \[&quot;template-injection&quot;, &quot;info&quot;, &quot;code injection via template expansion&quot;\]\] | \[\[&quot;github-env&quot;, &quot;error&quot;, &quot;dangerous use of environment file&quot;\]\] |
| Input: restrict\_untrusted\_prs | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;On pull requests whose author does not have write access, deny commands that commonly run code from the checkout (package managers, test runners, interpreters, shells), even if claude\_args allows them. Set to &#x27;false&#x27; to turn this off. See docs/security.md.&quot;, &quot;required&quot;: false} |
| Selected SHA | 4fa93a88de49bbef68b10eb15aabedf28ca0e1ed | 4d75e5f390ee76b2e09c1980ecc99ff3a2e088c8 |
| Selected tag | v1.0.271 | v1.0.275 |

## auscaster/silvertongue

[Previous source](https://github.com/auscaster/silvertongue) · [Current source](https://github.com/auscaster/silvertongue/tree/06fe432eac6f8420e30102cf7b7cdb13b03f282d/)

| Changed | Before | After |
| --- | --- | --- |
| Input: anthropic-api-key | null | {&quot;description&quot;: &quot;An Anthropic API key. Connect one model; a subscription token wins when both are given.&quot;} |
| Input: claude-code-oauth-token | null | {&quot;description&quot;: &quot;A Claude Pro or Max subscription, from \`claude setup-token\`. Reviews then count against the plan, with no API bill.&quot;} |
| Input: edge | null | {&quot;default&quot;: &quot;full&quot;, &quot;description&quot;: &quot;full keeps the voice&#x27;s swearing and dark humour where it has them; clean takes them out.&quot;} |
| Input: gemini-api-key | null | {&quot;description&quot;: &quot;A Gemini API key.&quot;} |
| Input: github-token | null | {&quot;default&quot;: &quot;${{ github.token }}&quot;, &quot;description&quot;: &quot;The token that reads the pull request and posts the review.&quot;} |
| Input: humour | null | {&quot;description&quot;: &quot;roast goes for the laugh on every line and still lands every fix. light is comic relief, a laugh where the code earns one. off plays it straight. Left empty, each voice does what you picked it for, so a comedian roasts and everyone else gives comic relief.&quot;} |
| Input: model | null | {&quot;description&quot;: &quot;The model to review with. Defaults to your plan&#x27;s model on a Claude subscription, or claude-opus-5-5, gpt-6.1-sol or gemini-4-argon for an API key.&quot;} |
| Input: openai-api-key | null | {&quot;description&quot;: &quot;An OpenAI API key.&quot;} |
| Input: post | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;false writes the review to the job summary and posts nothing.&quot;} |
| Input: pull-request | null | {&quot;description&quot;: &quot;The pull request number, for runs that do not come from a pull request event.&quot;} |
| Input: request-changes | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;When the verdict is reject or reshape, submit the review as \\&quot;changes requested\\&quot;. false always submits a comment.&quot;} |
| Input: voice | null | {&quot;default&quot;: &quot;marcus-aurelius&quot;, &quot;description&quot;: &quot;The reviewer, by its slug at silvertongue.dev/voices, such as gordon-ramsay, marcus-aurelius, ricky-gervais or brainrot.&quot;} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;review-url&quot;, &quot;verdict&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 06fe432eac6f8420e30102cf7b7cdb13b03f282d |
| Selected tag | null | v1.1.1 |

## danielroe/uppt

[Previous source](https://github.com/danielroe/uppt/tree/6c1a9b480b0f02a3f535dedaf1a113f590aa56f2/) · [Current source](https://github.com/danielroe/uppt/tree/427b736befa839b403dd145f2a7c16dbf3fd4482/) · [Upstream code diff](https://github.com/danielroe/uppt/compare/6c1a9b480b0f02a3f535dedaf1a113f590aa56f2...427b736befa839b403dd145f2a7c16dbf3fd4482)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 6c1a9b480b0f02a3f535dedaf1a113f590aa56f2 | 427b736befa839b403dd145f2a7c16dbf3fd4482 |
| Selected tag | v0.6.12 | v0.6.13 |

## getsentry/action-release

[Previous source](https://github.com/getsentry/action-release/tree/e6703d0b00208e0b3687ba660d18ab5af7892821/) · [Current source](https://github.com/getsentry/action-release/tree/d55c8c3b7375607e972b710f12926b676d89d7d2/) · [Upstream code diff](https://github.com/getsentry/action-release/compare/e6703d0b00208e0b3687ba660d18ab5af7892821...d55c8c3b7375607e972b710f12926b676d89d7d2)

| Changed | Before | After |
| --- | --- | --- |
| Input: debug\_files | null | {&quot;description&quot;: &quot;Space-separated list of paths to debug information files (e.g. dSYM, PDB,\\nELF, Breakpad). Uploaded with \\&quot;sentry-cli debug-files upload\\&quot;.\\nPaths cannot contain spaces. Omit to skip uploading debug files.&quot;, &quot;required&quot;: false} |
| Selected SHA | e6703d0b00208e0b3687ba660d18ab5af7892821 | d55c8c3b7375607e972b710f12926b676d89d7d2 |
| Selected tag | v3.7.2 | v3.8.0 |

## jdx/mise-action

[Previous source](https://github.com/jdx/mise-action/tree/b44d12e7d0d8ee7461bb893e1b1993500433185b/) · [Current source](https://github.com/jdx/mise-action/tree/d5574b52816a478f9d4e6529a3f6ff17a8a36785/) · [Upstream code diff](https://github.com/jdx/mise-action/compare/b44d12e7d0d8ee7461bb893e1b1993500433185b...d5574b52816a478f9d4e6529a3f6ff17a8a36785)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b44d12e7d0d8ee7461bb893e1b1993500433185b | d5574b52816a478f9d4e6529a3f6ff17a8a36785 |
| Selected tag | v5.2.7 | v5.2.8 |

## lukka/get-cmake

[Previous source](https://github.com/lukka/get-cmake/tree/f86dd60acae0d132056913e248bdabf0e0580b7a/) · [Current source](https://github.com/lukka/get-cmake/tree/16e8153a8b4918849d92aad131befe67a3705daa/) · [Upstream code diff](https://github.com/lukka/get-cmake/compare/f86dd60acae0d132056913e248bdabf0e0580b7a...16e8153a8b4918849d92aad131befe67a3705daa)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | f86dd60acae0d132056913e248bdabf0e0580b7a | 16e8153a8b4918849d92aad131befe67a3705daa |
| Selected tag | v4.4.5 | v4.5.0 |

## pullfrog/pullfrog

[Previous source](https://github.com/pullfrog/pullfrog/tree/0741f79ecebfa4469a010644d2aed2d96d32d489/) · [Current source](https://github.com/pullfrog/pullfrog/tree/8d512c34f4c6170374e7f139e5ffe0eede6db8f2/) · [Upstream code diff](https://github.com/pullfrog/pullfrog/compare/0741f79ecebfa4469a010644d2aed2d96d32d489...8d512c34f4c6170374e7f139e5ffe0eede6db8f2)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 0741f79ecebfa4469a010644d2aed2d96d32d489 | 8d512c34f4c6170374e7f139e5ffe0eede6db8f2 |
| Selected tag | v0.1.127 | v0.1.129 |

## reviewdog/action-shellcheck

[Previous source](https://github.com/reviewdog/action-shellcheck/tree/b4ffc0b2a69f857f82b74d1310cd3e62e932f9f7/) · [Current source](https://github.com/reviewdog/action-shellcheck/tree/950c9d71535c8c49e5c029c33a438ade63b9009c/) · [Upstream code diff](https://github.com/reviewdog/action-shellcheck/compare/b4ffc0b2a69f857f82b74d1310cd3e62e932f9f7...950c9d71535c8c49e5c029c33a438ade63b9009c)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | b4ffc0b2a69f857f82b74d1310cd3e62e932f9f7 | 950c9d71535c8c49e5c029c33a438ade63b9009c |
| Selected tag | v1.35.0 | v1.35.1 |

## reviewdog/action-tfsec

[Previous source](https://github.com/reviewdog/action-tfsec/tree/7ef25b204ff6e295faf22a9b675edac277d9996f/) · [Current source](https://github.com/reviewdog/action-tfsec/tree/56142d0fb18cf01ac356e04a63e574315a8483da/) · [Upstream code diff](https://github.com/reviewdog/action-tfsec/compare/7ef25b204ff6e295faf22a9b675edac277d9996f...56142d0fb18cf01ac356e04a63e574315a8483da)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 7ef25b204ff6e295faf22a9b675edac277d9996f | 56142d0fb18cf01ac356e04a63e574315a8483da |
| Selected tag | v1.33.0 | v1.33.1 |

## ruzickap/action-my-broken-link-checker

[Previous source](https://github.com/ruzickap/action-my-broken-link-checker/tree/5c84b4ee7ae993f10d8e5c7898ab669d4432f269/) · [Current source](https://github.com/ruzickap/action-my-broken-link-checker/tree/02d608dab6d54f73b6a0a04f7a9ad928d49eb2b2/) · [Upstream code diff](https://github.com/ruzickap/action-my-broken-link-checker/compare/5c84b4ee7ae993f10d8e5c7898ab669d4432f269...02d608dab6d54f73b6a0a04f7a9ad928d49eb2b2)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 5c84b4ee7ae993f10d8e5c7898ab669d4432f269 | 02d608dab6d54f73b6a0a04f7a9ad928d49eb2b2 |
| Selected tag | v3.0.3 | v3.0.4 |

## SonarSource/sonarqube-scan-action

[Previous source](https://github.com/SonarSource/sonarqube-scan-action/tree/e805d875275f728fac1885b413934be6d7c63f65/) · [Current source](https://github.com/SonarSource/sonarqube-scan-action/tree/59202af334b4ba7b5db01b701b8e79f8b3bef0f4/) · [Upstream code diff](https://github.com/SonarSource/sonarqube-scan-action/compare/e805d875275f728fac1885b413934be6d7c63f65...59202af334b4ba7b5db01b701b8e79f8b3bef0f4)

| Changed | Before | After |
| --- | --- | --- |
| Input: scannerVersion | {&quot;default&quot;: &quot;8.3.1.16491&quot;, &quot;description&quot;: &quot;Version of the Sonar Scanner CLI to use&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;8.4.0.16527&quot;, &quot;description&quot;: &quot;Version of the Sonar Scanner CLI to use&quot;, &quot;required&quot;: false} |
| Selected SHA | e805d875275f728fac1885b413934be6d7c63f65 | 59202af334b4ba7b5db01b701b8e79f8b3bef0f4 |
| Selected tag | v8.4.1 | v8.5.0 |

## tmatens/compose-lint

[Previous source](https://github.com/tmatens/compose-lint/tree/c73d88084090f034b1f6c63115ebfebfb8212e1b/) · [Current source](https://github.com/tmatens/compose-lint/tree/0f33c7adb0b49b03779eb623e35affb82188d272/) · [Upstream code diff](https://github.com/tmatens/compose-lint/compare/c73d88084090f034b1f6c63115ebfebfb8212e1b...0f33c7adb0b49b03779eb623e35affb82188d272)

| Changed | Before | After |
| --- | --- | --- |
| Input: sarif-file | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to write SARIF output (enables GitHub Code Scanning upload). Must stay inside the workspace; a parent directory that does not exist yet is created.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;Path to write SARIF output (enables GitHub Code Scanning upload). Must stay inside the workspace; a parent directory that does not exist yet is created. A path where a directory, a symbolic link or another non-regular file already exists is refused.&quot;, &quot;required&quot;: false} |
| Input: version | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;compose-lint version to install. Defaults to the version this action was released with, so a SHA-pinned \`uses:\` gets a reproducible check. Set to \\&quot;latest\\&quot; to track PyPI instead.&quot;, &quot;required&quot;: false} | {&quot;default&quot;: &quot;&quot;, &quot;description&quot;: &quot;compose-lint version to install. Defaults to the version this action was released with, installed with the dependency versions locked at that release (requirements.lock), so a SHA-pinned \`uses:\` gets a reproducible check. Set to \\&quot;latest\\&quot; to track PyPI instead; an explicit version or \\&quot;latest\\&quot; resolves its dependencies from PyPI.&quot;, &quot;required&quot;: false} |
| Selected SHA | c73d88084090f034b1f6c63115ebfebfb8212e1b | 0f33c7adb0b49b03779eb623e35affb82188d272 |
| Selected tag | v1.3.0 | v1.4.0 |
