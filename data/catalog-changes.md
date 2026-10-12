# Latest catalog changes

4 actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted.

## getsentry/action-release

[Previous source](https://github.com/getsentry/action-release/tree/ff07929a6537bac57790c3451cf4d364aca38528/) · [Current source](https://github.com/getsentry/action-release/tree/6fb9aeade7061441cf3864e34fbe11a1457ad7dc/) · [Upstream code diff](https://github.com/getsentry/action-release/compare/ff07929a6537bac57790c3451cf4d364aca38528...6fb9aeade7061441cf3864e34fbe11a1457ad7dc)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | ff07929a6537bac57790c3451cf4d364aca38528 | 6fb9aeade7061441cf3864e34fbe11a1457ad7dc |
| Selected tag | v3.7.0 | v3.7.1 |

## github-community-projects/contributors

[Previous source](https://github.com/github-community-projects/contributors) · [Current source](https://github.com/github-community-projects/contributors/tree/6bab24b098e0b692d679d59f97d73b9297c96c18/)

| Changed | Before | After |
| --- | --- | --- |
| Observed stability | null | observed |
| Outputs | null | \[\] |
| Runtime | null | docker |
| Security | unknown | clean |
| Selected SHA | null | 6bab24b098e0b692d679d59f97d73b9297c96c18 |
| Selected tag | null | v2.0.21 |

## jianruntech/geo-score

[Previous source](https://github.com/jianruntech/geo-score/tree/8123c129c93cb0bb4c80c5fbc974110f503d1066/) · [Current source](https://github.com/jianruntech/geo-score/tree/076c2dbf4aedd1ee882cb423bcad8da127fd5cbe/) · [Upstream code diff](https://github.com/jianruntech/geo-score/compare/8123c129c93cb0bb4c80c5fbc974110f503d1066...076c2dbf4aedd1ee882cb423bcad8da127fd5cbe)

| Changed | Before | After |
| --- | --- | --- |
| Selected SHA | 8123c129c93cb0bb4c80c5fbc974110f503d1066 | 076c2dbf4aedd1ee882cb423bcad8da127fd5cbe |
| Selected tag | v1.7.1 | v1.8.0 |

## mikepenz/xray-action

[Previous source](https://github.com/mikepenz/xray-action) · [Current source](https://github.com/mikepenz/xray-action/tree/93fcac936537e41c08c7191229e6106ae511f0da/)

| Changed | Before | After |
| --- | --- | --- |
| Input: combineInSingleTestExec | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;If no \`testExecKey\` is provided, it will generate a testExec with the first import, and reuse the same for all other imports.&quot;, &quot;required&quot;: false} |
| Input: continueOnImportError | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Defines if the action should continue after a single import error occurred.&quot;, &quot;required&quot;: false} |
| Input: failOnImportError | null | {&quot;default&quot;: &quot;false&quot;, &quot;description&quot;: &quot;Defines if the action should fail if an import error occurred.&quot;, &quot;required&quot;: false} |
| Input: fixVersion | null | {&quot;description&quot;: &quot;The Fix Version associated with the test execution (it supports only one value).&quot;, &quot;required&quot;: false} |
| Input: importParallelism | null | {&quot;default&quot;: &quot;2&quot;, &quot;description&quot;: &quot;Specifies the level of parallelism to import to Xray.&quot;, &quot;required&quot;: false} |
| Input: importRetryLimit | null | {&quot;default&quot;: &quot;2&quot;, &quot;description&quot;: &quot;Specifies the maximum number of retries for failed import requests. The default is 2.&quot;, &quot;required&quot;: false} |
| Input: password | null | {&quot;description&quot;: &quot;Xray API client secret (cloud) or Jira password (Server/DC). (Required for xrayCoud)&quot;, &quot;required&quot;: false} |
| Input: projectKey | null | {&quot;description&quot;: &quot;Key of the project where the Test Execution (if the testExecKey parameter was not provided) and the tests (if they are not created yet) are going to be created.&quot;, &quot;required&quot;: true} |
| Input: responseTimeout | null | {&quot;default&quot;: &quot;60000&quot;, &quot;description&quot;: &quot;Specifies the maximum duration for a request (in milliseconds) to wait for a response to execute before timing out. The default is 60 seconds.&quot;, &quot;required&quot;: false} |
| Input: revision | null | {&quot;description&quot;: &quot;Source code and documentation version used in the test execution.&quot;, &quot;required&quot;: false} |
| Input: testEnvironments | null | {&quot;description&quot;: &quot;A string containing a list of test environments separated by \\&quot;;\\&quot;. This is not supported for cloud.&quot;, &quot;required&quot;: false} |
| Input: testExecKey | null | {&quot;description&quot;: &quot;Key of the Test Execution.&quot;, &quot;required&quot;: true} |
| Input: testExecutionJson | null | {&quot;description&quot;: &quot;Links to a json file, defining the meta information to create the test execution ticket.&quot;, &quot;required&quot;: false} |
| Input: testFormat | null | {&quot;default&quot;: &quot;junit&quot;, &quot;description&quot;: &quot;The format of the to be imported data. \[\\&quot;xray\\&quot;, \\&quot;cucumber\\&quot;, \\&quot;behave\\&quot;, \\&quot;junit\\&quot;, \\&quot;testng\\&quot;, \\&quot;nunit\\&quot;, \\&quot;xunit\\&quot;, \\&quot;robot\\&quot;, \\&quot;bundle\\&quot;\].&quot;} |
| Input: testJson | null | {&quot;description&quot;: &quot;Links to a json file, defining the meta information to create the test tickets.&quot;, &quot;required&quot;: false} |
| Input: testMerge | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;When multiple test reports are found, they will be automatically merged into a single test report file. Only supported for: \[\\&quot;junit\\&quot;\]&quot;, &quot;required&quot;: false} |
| Input: testPaths | null | {&quot;default&quot;: &quot;\*\*/test-results/test/TEST-\*.xml&quot;, &quot;description&quot;: &quot;A \`glob\` pattern, to find all test results which should get imported.&quot;, &quot;required&quot;: true} |
| Input: testPlanKey | null | {&quot;description&quot;: &quot;Key of the Test Plan; if you specify the Test Plan, the Tests will be added automatically to the Test Plan if they are not part of it.&quot;, &quot;required&quot;: false} |
| Input: username | null | {&quot;description&quot;: &quot;Xray API client id (cloud) or Jira username (Server/DC). (Required for xrayCoud)&quot;, &quot;required&quot;: false} |
| Input: xrayBaseUrl | null | {&quot;description&quot;: &quot;Defines the base URL for Xray Server/DC, could be used to change XRay Data region for XRay Cloud (required if xrayCloud=\\&quot;false\\&quot;)&quot;, &quot;required&quot;: false} |
| Input: xrayCloud | null | {&quot;default&quot;: &quot;true&quot;, &quot;description&quot;: &quot;Defines which variant of Xray to target at \[cloud vs Server/DC\]&quot;, &quot;required&quot;: false} |
| Input: xrayToken | null | {&quot;description&quot;: &quot;Xray Personal Access Token. If provided username/password are ignored. (Xray Server/DC only)&quot;, &quot;required&quot;: false} |
| Observed stability | null | observed |
| Outputs | null | \[&quot;completed&quot;, &quot;count&quot;, &quot;errorMessage&quot;, &quot;errorStatusCode&quot;, &quot;failed&quot;\] |
| Runtime | null | node24 |
| Security | unknown | clean |
| Selected SHA | null | 93fcac936537e41c08c7191229e6106ae511f0da |
| Selected tag | null | v4.2.0 |
