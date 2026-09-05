"""Small command language over typed action identities, never a system shell."""

from __future__ import annotations

import shlex
import sqlite3
import time
from dataclasses import dataclass

from pydantic import ValidationError

from .github import GitHubClient, GitHubError
from .models import ActionRecord
from .security import ScanError, Scanner
from .snapshot import SnapshotError
from .versions import MetadataStore, generate_usage_snippet

HELP_TEXT = """GitHub Actions Navigator
  browse            List categories
  ls [owner]        List owners or actions
  grep <words>      Search intent; refine candidates when piped
  find --tag <tag>  Match an exact catalog tag
  cat <action...>   Inspect candidate revisions, security, and pinned usage
  man <action...>   Fetch manifests at the stored commit SHAs
  audit <action...> Scan those exact manifests with pinned zizmor
  help              Show this help

Search returns candidates, including unscanned actions; use cat to assess them.
Known blocked actions are excluded from grep and find.
Pipes pass action identities. && runs on success. ; runs regardless.
Examples: grep setup | grep node | cat
          grep deploy | cat | audit
          help && ls
No shell commands, expansion, redirection, or scripts are executed.
"""


@dataclass(frozen=True)
class CommandResult:
    text: str
    code: int = 0
    actions: tuple[str, ...] | None = None


def parse_chain(command: str) -> tuple[list[str], list[str]]:
    if len(command) > 8192:
        raise ValueError("command exceeds 8192 characters")
    chunks, operators = [], []
    start, index, quote = 0, 0, None
    while index < len(command):
        char = command[index]
        if char == "\\" and quote != "'":
            index += 2
            continue
        if quote:
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif char in "|&;":
            op = "&&" if command[index : index + 2] == "&&" else char
            if op == "&":
                raise ValueError("Only |, &&, and ; operators are supported")
            chunks.append(command[start:index].strip())
            operators.append(op)
            index += len(op)
            start = index
            continue
        index += 1
    chunks.append(command[start:].strip())
    if quote:
        raise ValueError("Unclosed quote")
    if any(not chunk for chunk in chunks) and operators:
        raise ValueError("An operator must have a command on both sides")
    if len(chunks) > 20:
        raise ValueError("A chain may contain at most 20 commands")
    # Validate even skipped commands, so malformed input is rejected consistently.
    for chunk in chunks:
        shlex.split(chunk)
    return chunks, operators


def render_record(record: ActionRecord) -> str:
    catalog, state = record.catalog, record.state
    selected = state.selected
    lines = [
        f"Action: {record.action}",
        f"Category: {catalog.category}",
        f"Popularity: {state.stars} stars",
        f"Repository: {state.repository_status}",
    ]
    if selected:
        lines.extend(
            [f"Selected: {selected.tag} @ {selected.sha}", f"Tag stability: {selected.stability}"]
        )
    else:
        lines.append("Selected: none; waiting for an observed stable tag")
    lines.append(f"Security: {record.security_status().upper()} (manifest checks only)")
    if state.scan:
        label = (
            "Historical blocking evidence"
            if state.scan.policy_version == 0
            else "Last successful scan"
        )
        lines.append(
            f"{label}: {state.scan.scanned_at.isoformat()} with zizmor {state.scan.scanner_version}"
        )
        lines.extend(f"  [{f.severity.upper()}] {f.rule}" for f in state.scan.findings)
    if state.scan_error:
        lines.append(f"Scan failure: {state.scan_error}")
    if state.update_error:
        lines.append(f"Update failure: {state.update_error}")
    lines.append(
        f"Last repository check: {state.checked_at.isoformat() if state.checked_at else 'unknown'}"
    )
    lines.extend(
        [
            f"Description (editorial): {catalog.description}",
            f"Match guidance (editorial): {catalog.match_logic}",
            f"Runtime: {state.manifest.runtime if state.manifest else 'unknown'}",
            f"Outputs: {', '.join(state.manifest.outputs) if state.manifest else 'unknown'}",
            f"Auth guidance: {catalog.auth or 'unspecified'}",
            f"Permissions guidance: {catalog.permissions}",
            f"Requires: {catalog.requires}",
            f"Conflicts: {catalog.conflicts}",
            f"Side effects: {catalog.side_effects}",
            f"Performance: {catalog.performance}",
            f"Repo: https://github.com/{catalog.repository}",
            "",
            generate_usage_snippet(record),
        ]
    )
    return "\n".join(lines)


class Navigator:
    def __init__(
        self,
        store: MetadataStore,
        client: GitHubClient | None = None,
        scanner: Scanner | None = None,
    ):
        self.store = store
        self.client = client
        self.scanner = scanner

    def execute(
        self, command: str, stdin: CommandResult | None = None, *, defer_limit: bool = False
    ) -> CommandResult:
        try:
            args = shlex.split(command)
            if not args:
                return CommandResult(HELP_TEXT)
            name, args = args[0], args[1:]
            if name == "help":
                return CommandResult(HELP_TEXT)
            if name == "browse":
                return CommandResult("Categories:\n" + "\n".join(self.store.list_categories()))
            if name == "ls":
                if not args:
                    return CommandResult("Owners:\n" + "\n".join(self.store.list_owners()))
                rows = self.store.list_repos(args[0])
                return CommandResult(
                    "\n".join(f"{r.action} [{r.security_status()}]" for r in rows)
                    or "No actions found.",
                    actions=tuple(r.action for r in rows),
                )
            if name in {"grep", "find"}:
                if name == "grep":
                    if not args:
                        raise ValueError("usage: grep <words>")
                    rows = self.store.search(
                        " ".join(args), limit=10000 if stdin or defer_limit else 10
                    )
                else:
                    if len(args) != 2 or args[0] != "--tag":
                        raise ValueError("usage: find --tag <tag>")
                    rows = self.store.find_by_tag(
                        args[1].lstrip("#"), limit=10000 if stdin or defer_limit else 10
                    )
                if stdin is not None:
                    if stdin.actions is None:
                        raise ValueError("Piped input must contain action candidates")
                    allowed = {action.casefold() for action in stdin.actions}
                    rows = [row for row in rows if row.action.casefold() in allowed]
                if not defer_limit:
                    rows = rows[:10]
                return CommandResult(
                    "\n".join(row.action for row in rows) or "No actions matched.",
                    actions=tuple(row.action for row in rows),
                )
            if name not in {"cat", "man", "audit"}:
                return CommandResult(f"[error] Unknown command: {name}. Use help.", 127)
            identities = tuple(args) if args else (stdin.actions if stdin else None)
            if identities is None:
                raise ValueError(f"usage: {name} <action...>")
            if not identities:
                return CommandResult("No action candidates.", actions=())
            if len(identities) > 20:
                raise ValueError("Inspect at most 20 actions per command")
            texts, resolved, code = [], [], 0
            client = self.client or GitHubClient()
            for action in identities:
                record = self.store.get_info(action)
                if record is None:
                    raise ValueError(f"Unknown action: {action}")
                resolved.append(record.action)
                if name == "cat":
                    texts.append(render_record(record))
                    continue
                revision = record.state.selected
                if revision is None:
                    raise ValueError(f"{action} has no selected commit SHA yet")
                content = client.manifest(record.action, revision.sha)
                if name == "man":
                    texts.append(f"# {action}@{revision.sha} ({revision.stability})\n{content}")
                else:
                    evidence = (self.scanner or Scanner()).scan(content, revision.sha)
                    blocked = any(f.severity == "error" for f in evidence.findings)
                    code = max(code, int(blocked))
                    lines = [f"Audit: {action}@{revision.sha}; zizmor {evidence.scanner_version}"]
                    lines.extend(
                        f"[{f.severity.upper()}] {f.rule}"
                        + (f" (line {f.line})" if f.line else "")
                        + f": {f.message}"
                        for f in evidence.findings
                    )
                    if not evidence.findings:
                        lines.append(
                            "No manifest findings. Referenced code and dependencies were not audited."
                        )
                    texts.append("\n".join(lines))
            return CommandResult("\n\n".join(texts), code, tuple(resolved))
        except (
            ValueError,
            ValidationError,
            GitHubError,
            ScanError,
            SnapshotError,
            sqlite3.Error,
            OSError,
        ) as exc:
            return CommandResult(f"[error] {exc}", 1)

    def run(self, command: str) -> CommandResult:
        started = time.monotonic()
        try:
            chunks, operators = parse_chain(command)
        except ValueError as exc:
            return CommandResult(f"[error] {exc}\n[exit:1]", 1)
        output, previous, skip = [], None, False
        result = CommandResult("")
        for index, chunk in enumerate(chunks):
            before = operators[index - 1] if index else None
            if before == ";":
                skip = False
            elif before == "&&" and result.code:
                skip = True
            elif before == "|" and result.code:
                skip = True
            if not skip:
                after = operators[index] if index < len(operators) else None
                defer_limit = after == "|" and shlex.split(chunks[index + 1])[0] in {"grep", "find"}
                result = self.execute(
                    chunk, previous if before == "|" else None, defer_limit=defer_limit
                )
                previous = result
                after = operators[index] if index < len(operators) else None
                if after != "|" or result.code:
                    output.append(result.text)
        duration = int((time.monotonic() - started) * 1000)
        text = "\n\n".join(output)
        if len(text) > 60000:
            text = text[:60000] + "\n[output truncated; inspect fewer actions]"
        return CommandResult(
            f"{text}\n[exit:{result.code} | {duration}ms]", result.code, result.actions
        )
