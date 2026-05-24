"""MCP server exposing GitHub Actions versions and recommendations with a Unix-style interface."""

from __future__ import annotations

import shlex
import time
import re
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
  help            - Show this help message.

Unix Chaining Supported:
  |   - Pipe: Passes output of first command as the main argument to the next.
  &&  - And:  Executes next command only if previous succeeded.
  ;   - Seq:  Executes next command regardless of success.

Example:
  run "grep setup | grep node | cat"
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
            output += f"  {r.action.split('/')[-1]:<25} | {r.best_use_case or r.description} (⭐ {r.stars})\n"
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
        actions = cmd_args[0].splitlines()
        if not actions: return "[error] No action specified.", 1
        
        action = actions[0].split()[0] # Take first word of first line
        info = store.get_info(action)
        if not info:
            return f"[error] Action {action!r} not found. Try 'grep {action}' to find similar.", 1
        
        output = f"Action:     {info.action}\n"
        output += f"Latest:     {info.latest_tag}\n"
        output += f"Category:   {info.category}\n"
        output += f"Popularity: ⭐ {info.stars} stars\n"
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

    else:
        return f"[error] unknown command: {cmd}\nAvailable: ls, cat, grep, find, browse, man, help", 127

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
