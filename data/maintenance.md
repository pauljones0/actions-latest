# Maintenance overview

**Stored data: within freshness limits**

**Last refresh: partial (549 fetch failures)**

549 catalog entries. 5 action-specific fetch/scan failures; 0 reviews invalidated by revision changes; 541 historical guidance reviews.

Routine observations and compatible Python/tool maintenance are automatic. Historical editorial reviews are a backlog, not a reason to stop all updates.

[Latest meaningful changes](https://github.com/pauljones0/actions-latest/blob/main/data/catalog-changes.md) · [All review items](https://github.com/pauljones0/actions-latest/blob/main/data/review-queue.json) · [Maintenance guide](https://github.com/pauljones0/actions-latest/blob/main/MAINTENANCE.md)

## Shared service recovery

| Cause | Affected entries | One recovery action |
| --- | --- | --- |
| GitHub API rate limit | 549 | Wait for quota reset or the next scheduled update; avoid repeated manual refreshes. Then run `uv run python manage.py refresh` once. Existing observations and scan evidence are retained. |

## Next decisions

| Action | Why it is here | Next step |
| --- | --- | --- |
| [asdf-vm/actions](https://github.com/asdf-vm/actions/tree/b7bcd026f18772e44fe1026d729e1611cc435d47/) | Fetch or scan failed: No action.yml or action.yaml at asdf-vm/actions@b7bcd026f18772e44fe1026d729e1611cc435d47 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review asdf-vm/actions`. |
| [actions/actions-sync](https://github.com/actions/actions-sync/tree/8d10c36b44c3f04fd062dd6801bc291a74fee723/) | Fetch or scan failed: No action.yml or action.yaml at actions/actions-sync@8d10c36b44c3f04fd062dd6801bc291a74fee723 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review actions/actions-sync`. |
| [ansible/ansible-content-actions](https://github.com/ansible/ansible-content-actions/tree/7dc7e15a53c2ae8bd092461e53dafd6627e34ac6/) | Fetch or scan failed: zizmor failed with exit 1 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review ansible/ansible-content-actions`. |
| [bitwarden/gh-actions](https://github.com/bitwarden/gh-actions/tree/c145aa56a48d77bb9c36162a07cc6a30b7f01f1f/) | Fetch or scan failed: No action.yml or action.yaml at bitwarden/gh-actions@c145aa56a48d77bb9c36162a07cc6a30b7f01f1f | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bitwarden/gh-actions`. |
| [bytecodealliance/actions](https://github.com/bytecodealliance/actions/tree/9152e710e9f7182e4c29ad218e4f335a7b203613/) | Fetch or scan failed: No action.yml or action.yaml at bytecodealliance/actions@9152e710e9f7182e4c29ad218e4f335a7b203613 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bytecodealliance/actions`. |
