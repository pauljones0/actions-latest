# Maintenance overview

**Stored data: within freshness limits**

**Last refresh: partial (292 fetch failures)**

549 catalog entries. 5 action-specific fetch/scan failures; 0 reviews invalidated by revision changes; 541 historical guidance reviews.

Routine observations and compatible Python/tool maintenance are automatic. Historical editorial reviews are a backlog, not a reason to stop all updates.

[Latest meaningful changes](https://github.com/pauljones0/actions-latest/blob/main/data/catalog-changes.md) · [All review items](https://github.com/pauljones0/actions-latest/blob/main/data/review-queue.json) · [Maintenance guide](https://github.com/pauljones0/actions-latest/blob/main/MAINTENANCE.md)

## Shared service recovery

| Cause | Affected entries | One recovery action |
| --- | --- | --- |
| GitHub API rate limit | 292 | Wait for quota reset or the next scheduled update; avoid repeated manual refreshes. Then run `uv run python manage.py refresh` once. Existing observations and scan evidence are retained. |

## Next decisions

| Action | Why it is here | Next step |
| --- | --- | --- |
| [asdf-vm/actions](https://github.com/asdf-vm/actions/tree/b7bcd026f18772e44fe1026d729e1611cc435d47/) | Fetch or scan failed: No action.yml or action.yaml at asdf-vm/actions@b7bcd026f18772e44fe1026d729e1611cc435d47 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review asdf-vm/actions`. |
| [actions/actions-sync](https://github.com/actions/actions-sync/tree/8d10c36b44c3f04fd062dd6801bc291a74fee723/) | Fetch or scan failed: No action.yml or action.yaml at actions/actions-sync@8d10c36b44c3f04fd062dd6801bc291a74fee723 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review actions/actions-sync`. |
| [ansible/ansible-content-actions](https://github.com/ansible/ansible-content-actions/tree/7dc7e15a53c2ae8bd092461e53dafd6627e34ac6/) | Fetch or scan failed: zizmor failed with exit 1 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review ansible/ansible-content-actions`. |
| [bitwarden/gh-actions](https://github.com/bitwarden/gh-actions/tree/c145aa56a48d77bb9c36162a07cc6a30b7f01f1f/) | Fetch or scan failed: No action.yml or action.yaml at bitwarden/gh-actions@c145aa56a48d77bb9c36162a07cc6a30b7f01f1f | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bitwarden/gh-actions`. |
| [bytecodealliance/actions](https://github.com/bytecodealliance/actions/tree/9152e710e9f7182e4c29ad218e4f335a7b203613/) | Fetch or scan failed: No action.yml or action.yaml at bytecodealliance/actions@9152e710e9f7182e4c29ad218e4f335a7b203613 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bytecodealliance/actions`. |
| [actions/checkout](https://github.com/actions/checkout/tree/de0fac2e4500dabe0009e67214ff5f5447ce83dd/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/checkout`. |
| [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action/tree/20c8abf165d5f85ab3fc970db9498436377dc9d1/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review anthropics/claude-code-action`. |
| [appleboy/ssh-action](https://github.com/appleboy/ssh-action/tree/0ff4204d59e8e51228ff73bce53f80d53301dee2/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review appleboy/ssh-action`. |
| [actions/cache](https://github.com/actions/cache/tree/27d5ce7f107fe9357f9df03efb73ab90386fccae/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/cache`. |
| [docker/build-push-action](https://github.com/docker/build-push-action/tree/bcafcacb16a39f128d818304e6c9c0c18556b85f/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review docker/build-push-action`. |
| [actions/github-script](https://github.com/actions/github-script/tree/3a2844b7e9c422d3c10d287c895573f7108da1b3/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/github-script`. |
| [actions/setup-node](https://github.com/actions/setup-node/tree/48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/setup-node`. |
| [anc95/ChatGPT-CodeReview](https://github.com/anc95/ChatGPT-CodeReview/tree/1e3df152c1b85c12da580b206c91ad343460c584/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review anc95/ChatGPT-CodeReview`. |
| [actions/upload-artifact](https://github.com/actions/upload-artifact/tree/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/upload-artifact`. |
| [anmol098/waka-readme-stats](https://github.com/anmol098/waka-readme-stats/tree/c6070c14861e6d8b553742b1f9e1ed9e7b53938a/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review anmol098/waka-readme-stats`. |
