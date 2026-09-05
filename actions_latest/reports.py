"""Readable maintenance evidence; ignore observation churn and never invent impact claims."""

from __future__ import annotations

import html
import json
from collections import Counter
from datetime import datetime
from urllib.parse import quote

from .models import ActionRecord, utc_now

REPO_URL = "https://github.com/pauljones0/actions-latest"


def cell(value) -> str:
    text = (
        value if isinstance(value, str) else json.dumps(value, sort_keys=True, ensure_ascii=False)
    )
    text = html.escape(text).replace("\\", "\\\\")
    for character in ("|", "[", "]", "`", "*", "_"):
        text = text.replace(character, "\\" + character)
    return text.replace("\n", " ")


def facts(record: ActionRecord, now: datetime) -> dict:
    state = record.state
    result = {
        "Selected tag": state.selected.tag if state.selected else None,
        "Selected SHA": state.selected.sha if state.selected else None,
        "Observed stability": state.selected.stability if state.selected else None,
        "Description": record.description,
        "Runtime": state.manifest.runtime if state.manifest else None,
        "Outputs": state.manifest.outputs if state.manifest else None,
        "Security": record.security_status(now),
        "Findings": sorted((f.rule, f.severity, f.message) for f in state.scan.findings)
        if state.scan
        else [],
        "Repository": state.repository_status,
        "Fetch error": state.update_error,
        "Scan error": state.scan_error,
    }
    if state.manifest:
        result.update({f"Input: {name}": value for name, value in state.manifest.inputs.items()})
    result.update(
        {
            f"Editorial: {name}": value
            for name, value in record.catalog.model_dump(exclude={"action", "reviewed_at"}).items()
        }
    )
    return result


def source(record: ActionRecord) -> str:
    selected = record.state.selected
    repository = record.catalog.repository
    subpath = "/".join(record.action.split("/")[2:])
    return (
        f"https://github.com/{repository}/tree/{selected.sha}/{quote(subpath)}"
        if selected
        else f"https://github.com/{repository}"
    )


def change_report(
    before: list[ActionRecord], after: list[ActionRecord], now: datetime | None = None
) -> str:
    now = now or utc_now()
    previous = {r.action.casefold(): r for r in before}
    current = {r.action.casefold(): r for r in after}
    sections = []
    service_changes = Counter()
    for key in sorted(previous.keys() | current.keys()):
        old, new = previous.get(key), current.get(key)
        record = new or old
        if old is None:
            sections.append(
                f"## Added: {cell(record.action)}\n\n[Source]({source(record)}) — {cell(record.description)}\n\nNew entries still require observed stability and fresh scan evidence before usage."
            )
        elif new is None:
            sections.append(
                f"## Removed from published catalog: {cell(record.action)}\n\nCheck the curated catalog or explicit exclusions; outages do not remove entries."
            )
        else:
            left, right = facts(old, now), facts(new, now)
            changed = [
                field
                for field in sorted(left.keys() | right.keys())
                if left.get(field) != right.get(field)
            ]
            if not changed:
                continue
            if all(
                field in {"Fetch error", "Scan error"}
                and (not left.get(field) or service_issue(left.get(field)))
                and (not right.get(field) or service_issue(right.get(field)))
                for field in changed
            ):
                for field in changed:
                    old_issue, new_issue = (
                        service_issue(left.get(field)),
                        service_issue(right.get(field)),
                    )
                    if old_issue != new_issue:
                        if old_issue:
                            service_changes[(old_issue, "recovered")] += 1
                        if new_issue:
                            service_changes[(new_issue, "affected")] += 1
                continue
            rows = [
                f"| {cell(field)} | {cell(left.get(field))} | {cell(right.get(field))} |"
                for field in changed
            ]
            links = f"[Previous source]({source(old)}) · [Current source]({source(new)})"
            if (
                old.state.selected
                and new.state.selected
                and old.state.selected.sha != new.state.selected.sha
            ):
                links += f" · [Upstream code diff](https://github.com/{record.catalog.repository}/compare/{old.state.selected.sha}...{new.state.selected.sha})"
            sections.append(
                f"## {cell(record.action)}\n\n{links}\n\n| Changed | Before | After |\n| --- | --- | --- |\n"
                + "\n".join(rows)
            )
    intro = (
        f"{len(sections)} actions have meaningful changes. Observation timestamps and popularity fluctuations are omitted."
        if sections
        else "No meaningful catalog changes. Only observation/scan timestamps or popularity may have changed."
    )
    if service_changes and not sections:
        intro = "No action content or policy changes; shared service status changed."
    shared = ""
    if service_changes:
        shared = "\n\n## Shared service changes\n\n" + "\n".join(
            f"- {issue}: {count} request-error transitions {transition}."
            for (issue, transition), count in sorted(service_changes.items())
        )
        shared += f"\n\nThese are grouped recovery items, not separate action-code reviews. [Current affected entries]({REPO_URL}/blob/main/data/review-queue.json)."
    return (
        "# Latest catalog changes\n\n"
        + intro
        + shared
        + ("\n\n" + "\n\n".join(sections) if sections else "")
        + "\n"
    )


def service_issue(error: str | None) -> str | None:
    value = (error or "").lower()
    if "github rate limit" in value:
        return "GitHub API rate limit"
    if "github rejected access" in value:
        return "GitHub access rejected"
    if "github transport failure" in value or "github server error" in value:
        return "GitHub transport/server failure"
    return None


def service_issues(records: list[ActionRecord]) -> dict[str, int]:
    counts = Counter()
    for record in records:
        for issue in {
            service_issue(record.state.update_error),
            service_issue(record.state.scan_error),
        } - {None}:
            counts[issue] += 1
    return dict(counts)


def review_queue(records: list[ActionRecord]) -> list[dict]:
    queue = []
    for record in records:
        errors = [e for e in (record.state.scan_error, record.state.update_error) if e]
        error = next((e for e in errors if not service_issue(e)), errors[0] if errors else None)
        status = record.guidance_status()
        if service_issue(error):
            priority, reason = 3, service_issue(error)
            next_step = "Use the shared service recovery item in the overview; no separate action-source review is required for this fetch failure."
        elif error:
            priority, reason = 0, "Fetch or scan failed"
            next_step = "Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean."
        elif status == "needs review after revision change":
            priority, reason = 1, "Previously reviewed guidance targets an older revision"
            next_step = "Compare old and selected revisions; update affected guidance, then record review for the selected SHA."
        elif status == "unreviewed":
            priority, reason = 2, "Historical editorial guidance has not been reviewed"
            next_step = "Review source-backed facts and human claims. Unsupported claims should be corrected or removed."
        else:
            continue
        queue.append(
            {
                "action": record.action,
                "priority": priority,
                "reason": reason,
                "detail": error or "",
                "next_step": next_step,
                "source": source(record),
                "stars": record.state.stars,
            }
        )
    return sorted(
        queue, key=lambda item: (item["priority"], -item["stars"], item["action"].casefold())
    )


def maintenance_summary(records: list[ActionRecord], health: dict) -> str:
    queue = review_queue(records)
    counts = {p: sum(item["priority"] == p for item in queue) for p in range(3)}
    counts[1] = sum(r.guidance_status() == "needs review after revision change" for r in records)
    counts[2] = sum(r.guidance_status() == "unreviewed" for r in records)
    shared = service_issues(records)
    failed_fetches = sum(bool(r.state.update_error) for r in records)
    lines = [
        "# Maintenance overview",
        "",
        "**Stored data: "
        + ("within freshness limits" if health["healthy"] else "needs attention")
        + "**",
        "",
        f"**Last refresh: partial ({failed_fetches} fetch failures)**"
        if failed_fetches
        else "**Last refresh: all repository observations succeeded**",
        "",
        f"{len(records)} catalog entries. {counts[0]} action-specific fetch/scan failures; {counts[1]} reviews invalidated by revision changes; {counts[2]} historical guidance reviews.",
        "",
        "Routine observations and compatible Python/tool maintenance are automatic. Historical editorial reviews are a backlog, not a reason to stop all updates.",
        "",
        f"[Latest meaningful changes]({REPO_URL}/blob/main/data/catalog-changes.md) · [All review items]({REPO_URL}/blob/main/data/review-queue.json) · [Maintenance guide]({REPO_URL}/blob/main/MAINTENANCE.md)",
        "",
        "## Next decisions",
        "",
        "| Action | Why it is here | Next step |",
        "| --- | --- | --- |",
    ]
    if shared:
        recovery = {
            "GitHub API rate limit": "Wait for quota reset or the next scheduled update; avoid repeated manual refreshes. Then run `uv run python manage.py refresh` once. Existing observations and scan evidence are retained.",
            "GitHub access rejected": "Inspect the read token's expiry/permissions and affected repository access, then rerun refresh once. Do not delete entries to clear access failures.",
            "GitHub transport/server failure": "Wait for GitHub/network recovery, then rerun refresh once. No separate source review is required for each affected action.",
        }
        insertion = [
            "## Shared service recovery",
            "",
            "| Cause | Affected entries | One recovery action |",
            "| --- | --- | --- |",
        ]
        insertion += [
            f"| {cause} | {count} | {recovery[cause]} |" for cause, count in sorted(shared.items())
        ]
        index = lines.index("## Next decisions")
        lines[index:index] = insertion + [""]
    for item in [entry for entry in queue if entry["priority"] != 3][:15]:
        lines.append(
            f"| [{cell(item['action'])}]({item['source']}) | {cell(item['reason'])}: {cell(item['detail'])} | {cell(item['next_step'])} Run `uv run python manage.py review {item['action']}`. |"
        )
    if health["reasons"]:
        lines += [
            "",
            "## Freshness failures",
            "",
            *["- " + cell(reason) for reason in health["reasons"]],
            "",
            "Open the failed workflow from the maintenance guide; its summary includes the recovery command.",
        ]
    return "\n".join(lines) + "\n"


def action_review(record: ActionRecord) -> str:
    catalog, state = record.catalog, record.state
    lines = [
        f"# Review {cell(record.action)}",
        "",
        f"[Immutable source]({source(record)})",
        "",
        f"Guidance: **{record.guidance_status()}**. Security: **{record.security_status()}** (manifest analysis only).",
        "",
        "## Source-backed facts",
        "",
        "| Fact | Current value |",
        "| --- | --- |",
    ]
    for name, value in {
        "Selected revision": state.selected.model_dump() if state.selected else None,
        "Runtime": state.manifest.runtime if state.manifest else None,
        "Source description": state.manifest.description if state.manifest else None,
        "Outputs": state.manifest.outputs if state.manifest else None,
        "Fetch error": state.update_error,
        "Scan error": state.scan_error,
    }.items():
        lines.append(f"| {name} | {cell(value)} |")
    if state.manifest and state.manifest.inputs:
        lines += [
            "",
            "## Manifest inputs",
            "",
            "| Input | Required | Default | Description |",
            "| --- | --- | --- | --- |",
        ]
        for name, value in state.manifest.inputs.items():
            lines.append(
                f"| {cell(name)} | {cell(value.get('required', False))} | {cell(value.get('default'))} | {cell(value.get('description', ''))} |"
            )
    lines += ["", "## Human claims to check", "", "| Claim | Current value |", "| --- | --- |"]
    for name in (
        "description",
        "match_logic",
        "requires",
        "conflicts",
        "permissions",
        "auth",
        "side_effects",
        "performance",
    ):
        lines.append(f"| {name} | {cell(getattr(catalog, name))} |")
    if catalog.reviewed_sha and state.selected and catalog.reviewed_sha != state.selected.sha:
        lines += [
            "",
            f"[Compare with last reviewed revision](https://github.com/{catalog.repository}/compare/{catalog.reviewed_sha}...{state.selected.sha})",
        ]
    lines += [
        "",
        "## Decision",
        "",
        "Correct or remove unsupported claims in `catalog.json`. Do not infer required permissions, authentication, or safety from a clean manifest scan.",
    ]
    if state.selected and state.manifest and catalog.origin == "curated":
        lines += [
            "",
            "After reviewing those claims, record the review for this exact revision:",
            "",
            f"```sh\nuv run python manage.py reviewed {record.action} --sha {state.selected.sha}\n```",
            "",
            "This records editorial review only. It cannot clear findings, change observation ages, or make an ineligible revision usable.",
        ]
    else:
        lines += [
            "",
            "No review acknowledgement is available until this is a curated entry with a parsed selected manifest.",
        ]
    return "\n".join(lines) + "\n"


def dependency_report(report: dict) -> str:
    validated = report["validated"]
    lines = [
        "# Dependency maintenance review",
        "",
        "**Validation: "
        + (
            "passed** — the workflow may publish these changes."
            if validated
            else "pending** — these are proposed changes; do not treat them as accepted."
        ),
        "",
        "Direct tools stay within their current major. Runtime dependencies stay within declared ranges; transitive upgrades follow parent constraints. Tests establish exercised compatibility, not a complete upstream code audit.",
        "",
        "| Package | Before | After | Upstream details |",
        "| --- | --- | --- | --- |",
    ]
    for item in report["changes"]:
        links = (
            " · ".join(
                f"[{cell(v)}](https://pypi.org/project/{quote(item['package'], safe='')}/{quote(v, safe='')}/)"
                for v in item["after"]
            )
            or "Removed"
        )
        lines.append(
            f"| {cell(item['package'])} | {cell(item['before'])} | {cell(item['after'])} | {links} |"
        )
    if not report.get("prepared", True):
        lines.append(
            "| Resolution has not completed | Unknown | Unknown | Inspect the first failed step; no finished proposal exists yet. |"
        )
    elif not report["changes"]:
        lines.append(
            "| No package version changes | — | — | Lock format/metadata may still change. |"
        )
    if report.get("base_commit"):
        lines += [
            "",
            "**Proposal base commit:** `"
            + report["base_commit"]
            + "`. Reproduce the downloaded patch from this exact commit, which can differ from the event that queued the run.",
        ]
    if report.get("held_tools"):
        lines += [
            "",
            "**Tool upgrades on hold:** "
            + cell(report["held_tools"])
            + ". Remove the hold in tooling.json after resolving the incompatibility.",
        ]
    if report.get("run_url"):
        lines += ["", f"[Checks and publication result]({report['run_url']})"]
    lines += [
        "",
        "## Decision",
        "",
        "No manual approval is needed when this routine maintenance passes all checks. The publication step can still fail on a concurrent push; use the run link to confirm it actually published.",
        "",
        "If validation fails, inspect the first failed check and download the `maintenance-proposal` artifact from the run. It contains the exact patch and review report, so you can reproduce the candidate without resolving newer versions. Nothing is published before validation succeeds.",
        "",
        "For a bad accepted update, pause the maintenance workflow, revert its maintenance commit, and correct the version constraints before resuming. See [the maintenance guide](../MAINTENANCE.md).",
    ]
    return "\n".join(lines) + "\n"
