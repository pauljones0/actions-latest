"""MCP server exposing GitHub Actions versions and recommendations with a Unix-style interface."""

from __future__ import annotations

import json
import os
import shlex
import subprocess
import tempfile
import time
import re
from pathlib import Path
from typing import List, Optional

from mcp.server.fastmcp import FastMCP

from actions_latest.versions import (
    MetadataStore,
    get_db_path,
    fetch_action_manifest,
    generate_usage_snippet,
)

mcp = FastMCP("actions-latest")

# Initialize store
db_path = get_db_path()
store = MetadataStore(str(db_path))

HELP_TEXT = """Available commands:
  ls [owner]      - List available actions.
  cat [action]    - Show summary and usage snippet. (Accepts action from pipe)
  grep <query>    - Search actions.
  find --tag <T>  - Filter by high-signal tags.
  browse          - List categories.
  man <action>    - Fetch and display the action.yml manifest.
  audit <action>  - Run on-demand zizmor security scan on an action's manifest.
  help            - Show this help message.

Unix Chaining Supported:
  |   - Pipe: Passes output of first command as the main argument to the next.
  &&  - And:  Executes next command only if previous succeeded.
  ;   - Seq:  Executes next command regardless of success.

Example:
  run "grep setup | grep node | cat"
  run "grep deploy | cat | audit"
"""

def format_result(output: str, exit_code: int = 0, duration_ms: int = 0) -> str:
    """Layer 2: Presentation Layer for the LLM."""
    return f"{output}\n[exit:{exit_code} | {duration_ms}ms]"

def execute_internal(command_str: str, stdin: Optional[str] = None) -> tuple[str, int]:
    """Layer 1: Internal Unix Execution Layer."""
    try:
        args = shlex.split(command_str)
    except ValueError as e:
        return f"[error] Invalid command syntax: {e}", 1

    if not args:
        return HELP_TEXT, 0

    cmd = args[0]
    # If there's stdin from a pipe, and no args provided, use stdin as the first arg
    cmd_args = args[1:]
    if stdin and not cmd_args:
        cmd_args = [stdin.strip()]

    if cmd == "help":
        return HELP_TEXT, 0

    elif cmd == "ls":
        if not cmd_args:
            owners = store.list_owners()
            return "Action Owners:\n  " + "  ".join(owners), 0
        owner = cmd_args[0].rstrip("/")
        repos = store.list_repos(owner)
        if not repos:
            return f"[error] Owner {owner!r} not found. Use 'ls' to see available owners.", 1
        output = f"Actions in {owner}/:\n"
        for r in repos:
            security_marker = " 🚫" if r.zizmor_blocked else (" ⚠️" if not r.zizmor_ok else "")
            output += f"  {r.action.split('/')[-1]:<25} | {r.best_use_case or r.description} (⭐ {r.stars}){security_marker}\n"
        return output, 0

    elif cmd == "grep":
        if not cmd_args:
            return "[error] usage: grep <query>. Use 'browse' to see categories first.", 1
        query = " ".join(cmd_args)
        results = store.search(query)
        if not results:
            return f"No actions found matching {query!r}.", 0
        # If we are piping TO something, just return names. 
        # If we are the end of the chain, return full list.
        output = ""
        for r in results:
            output += f"{r.action}\n"
        return output.strip(), 0

    elif cmd == "find":
        if len(cmd_args) < 2 or cmd_args[0] != "--tag":
            return "[error] usage: find --tag <tag_name>. Try 'find --tag node'.", 1
        tag = cmd_args[1].lstrip("#")
        results = store.find_by_tag(tag)
        if not results:
            return f"No actions found with tag #{tag}.", 0
        output = ""
        for r in results:
            output += f"{r.action}\n"
        return output.strip(), 0

    elif cmd == "browse":
        categories = store.list_categories()
        return "Categories:\n- " + "\n- ".join(categories), 0

    elif cmd == "cat":
        if not cmd_args:
            return "[error] usage: cat <action>. Use 'grep' to find actions first.", 1
        # Handle multiple actions if piped (just take first one for now or loop)
        actions_list = cmd_args[0].splitlines()
        if not actions_list:
            return "[error] No action specified.", 1

        action = actions_list[0].split()[0]  # Take first word of first line
        info = store.get_info(action)
        if not info:
            return f"[error] Action {action!r} not found. Try 'grep {action}' to find similar.", 1

        # Build security badge from stored zizmor scan results.
        # Three tiers:
        #   BLOCKED  — has ERROR findings. Never recommended; shown for transparency.
        #   WARNING  — has WARNING findings. Show what they are.
        #   CLEAN    — no significant findings (INFO only, or not yet scanned).
        if info.zizmor_blocked:
            try:
                errs = json.loads(info.zizmor_error_findings)
            except Exception:
                errs = []
            security_line = (
                f"Security:   🚫 BLOCKED — {len(errs)} ERROR finding(s) — run 'audit {action}' for details\n"
                f"            DO NOT USE: this action has critical security issues in its manifest."
            )
        elif not info.zizmor_ok:
            try:
                warns = json.loads(info.zizmor_warning_findings)
                n = len(warns)
            except Exception:
                n = "?"
            security_line = f"Security:   ⚠️  {n} WARNING finding(s) — run 'audit {action}' for details"
        else:
            scanned_at = info.zizmor_scanned_at
            scan_note = f" (scanned {scanned_at[:10]}" + ")" if scanned_at else " (not yet scanned)"
            security_line = f"Security:   ✅ zizmor clean{scan_note}"

        # Show the ref we actually recommend (SHA for determinism, tag as label)
        sha_short = (info.latest_sha or "")[:8]
        ref_display = f"{info.latest_tag}" + (f"  [{sha_short}]" if sha_short else "")

        output = f"Action:     {info.action}\n"
        output += f"Latest:     {ref_display}\n"
        output += f"Category:   {info.category}\n"
        output += f"Popularity: ⭐ {info.stars} stars\n"
        output += f"{security_line}\n"
        output += f"Contract:   {info.description or 'No description'}\n"
        output += f"Match Logic:{info.match_logic or info.best_use_case}\n\n"

        output += "--- Operational Logic ---\n"
        output += f"Runtime:    {info.runtime or 'unknown'}\n"
        output += f"Auth Method:{info.auth or 'none'}\n"
        output += f"Requires:   {info.requires}\n"
        output += f"Conflicts:  {info.conflicts}\n"
        output += f"Permissions:{info.permissions}\n"
        output += f"Outputs:    {info.outputs}\n"
        output += f"Side Effects:{info.side_effects}\n"
        output += f"Performance:{info.performance}\n\n"

        output += f"Repo:       https://github.com/{info.action}\n\n"
        output += "Usage Example:\n"
        output += generate_usage_snippet(info.action, info.latest_tag)
        return output, 0

    elif cmd == "man":
        if not cmd_args:
            return "[error] usage: man <action>. Use 'cat' to see summary first.", 1
        action = cmd_args[0]
        manifest = fetch_action_manifest(action)
        return manifest, 0

    elif cmd == "audit":
        # Support piped input: 'cat actions/checkout | audit'
        action_arg = cmd_args[0] if cmd_args else (stdin or "").strip()
        if not action_arg:
            return "[error] usage: audit <action>. Example: audit actions/checkout", 1

        # Take the first token in case of multi-line pipe input
        action_arg = action_arg.splitlines()[0].split()[0]

        # Check if zizmor is available
        import sys
        venv_zizmor = Path(sys.executable).parent / "zizmor"
        zizmor_cmd = str(venv_zizmor) if venv_zizmor.exists() else "zizmor"

        try:
            zizmor_check = subprocess.run(
                [zizmor_cmd, "--version"], capture_output=True, text=True
            )
            zizmor_found = zizmor_check.returncode == 0
        except FileNotFoundError:
            zizmor_found = False

        if not zizmor_found:
            return (
                "[error] zizmor is not installed or not on PATH.\n"
                "Install it with: pip install zizmor  OR  uv tool install zizmor",
                1,
            )

        # Determine the ref to fetch at.
        # Prefer the stored commit SHA for determinism — if the floating tag
        # has moved since last update, we still audit what we actually recommend.
        info = store.get_info(action_arg)
        ref = (info.latest_sha or info.latest_tag) if info else ""

        manifest = fetch_action_manifest(action_arg, ref=ref)
        if manifest.startswith("[error]"):
            return manifest, 1

        # Use TemporaryDirectory so the file can be named action.yml.
        # zizmor relies on the filename to identify it as an action manifest instead of a workflow.
        import shutil
        tmp_dir = tempfile.mkdtemp(prefix="zizmor_audit_")
        tmp_path = Path(tmp_dir) / "action.yml"
        tmp_path.write_text(manifest)

        try:
            result = subprocess.run(
                [zizmor_cmd, "--format", "json", str(tmp_path)],
                capture_output=True, text=True, timeout=30
            )
            raw = result.stdout.strip()
            if not raw:
                return f"✅ zizmor: no findings for {action_arg}@{ref or 'HEAD'}", 0

            data = json.loads(raw)
            diagnostics = data if isinstance(data, list) else data.get("diagnostics", [])

            if not diagnostics:
                return f"✅ zizmor: no findings for {action_arg}@{ref or 'HEAD'}", 0

            # Bucket by severity
            errors, warnings, infos = [], [], []
            for d in diagnostics:
                rule = d.get("ident") or d.get("id") or d.get("check_name", "unknown")
                
                # Map determinations.severity (High/Critical -> error, Medium/Low -> warning, else info)
                det_severity = d.get("determinations", {}).get("severity")
                if det_severity:
                    det_sev_lower = det_severity.lower()
                    if det_sev_lower in ("high", "critical"):
                        severity = "error"
                    elif det_sev_lower in ("medium", "low"):
                        severity = "warning"
                    else:
                        severity = "info"
                else:
                    severity = (d.get("severity") or "info").lower()

                message = d.get("message", "") or d.get("desc", "") or ""
                location = ""
                locs = d.get("locations", [])
                if locs:
                    loc = locs[0]
                    # Try SARIF format first
                    loc_range = loc.get("physicalLocation", {}).get("region", {})
                    start_line = loc_range.get("startLine")
                    if start_line is None:
                        # Try custom JSON format
                        start_line = loc.get("concrete", {}).get("location", {}).get("start_point", {}).get("row", "?")
                    location = f" (line {start_line})"
                entry_str = f"  [{severity.upper()}] {rule}{location}: {message}"
                if severity == "error":
                    errors.append(entry_str)
                elif severity == "warning":
                    warnings.append(entry_str)
                else:
                    infos.append(entry_str)

            ref_label = (info.latest_tag if info else "") or ref or "HEAD"
            sha_label = (" @ " + (info.latest_sha or "")[:8]) if (info and info.latest_sha) else ""
            header = f"{action_arg}{sha_label} ({ref_label})"

            lines = []
            if errors:
                lines.append(f"🚫 BLOCKED — {header}: {len(errors)} ERROR finding(s)")
                lines.extend(errors)
                lines.append("")
            if warnings:
                lines.append(f"⚠️  {header}: {len(warnings)} WARNING finding(s)")
                lines.extend(warnings)
                lines.append("")
            if infos:
                lines.append(f"ℹ️   {header}: {len(infos)} INFO finding(s)")
                lines.extend(infos)
                lines.append("")
            if not lines:
                return f"✅ zizmor: no findings for {header}", 0

            lines.append(f"Run 'man {action_arg}' to inspect the full manifest.")
            return "\n".join(lines), 1 if errors else 0

        except json.JSONDecodeError:
            return f"[error] Could not parse zizmor output for {action_arg}", 1
        except subprocess.TimeoutExpired:
            return f"[error] zizmor timed out scanning {action_arg}", 1
        finally:
            try:
                shutil.rmtree(tmp_dir, ignore_errors=True)
            except Exception:
                pass

    else:
        return f"[error] unknown command: {cmd}\nAvailable: ls, cat, grep, find, browse, man, audit, help", 127

@mcp.tool()
def run(command: str) -> str:
    """
    Execute a Unix-style command chain in the GitHub Actions Navigator.
    
    Supported operators:
      |   (Pipe) - passes output to next command
      &&  (And)  - only runs next if previous succeeded
      ;   (Seq)  - runs next regardless
      
    Example: 'grep setup | grep node | cat'
    """
    start_time = time.time()
    
    # Split by operators but keep them
    # Simple regex to split while keeping delimiters
    parts = re.split(r"(\s\|\s|\s&&\s|\s;\s)", command)
    
    current_input = None
    final_output = ""
    exit_code = 0
    
    i = 0
    while i < len(parts):
        chunk = parts[i].strip()
        if not chunk: 
            i += 1
            continue
            
        if chunk in ["|", "&&", ";"]:
            # This is an operator, handled in the logic loop
            i += 1
            continue
            
        # Execute the command
        out, code = execute_internal(chunk, stdin=current_input)
        final_output = out
        exit_code = code
        current_input = out
        
        # Check next operator
        if i + 1 < len(parts):
            op = parts[i+1].strip()
            if op == "&&" and code != 0:
                break # Stop on failure
            if op == "|" and code != 0:
                break # Stop on failure
            # If op is ; or (&& and code 0) or (| and code 0), continue
        
        i += 2 # Move past command and operator

    duration = int((time.time() - start_time) * 1000)
    return format_result(final_output, exit_code=exit_code, duration_ms=duration)

def main() -> None:
    """Run the stdio MCP server."""
    mcp.run()

if __name__ == "__main__":
    main()
