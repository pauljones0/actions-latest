# Maintenance overview

**Overall freshness checks: passing**

**Last refresh: no recorded fetch errors**

Stored observations outside the 72-hour window: 0.

586 catalog entries. 5 action-specific fetch/scan failures; 0 reviews invalidated by revision changes; 541 historical guidance reviews.

Routine observations and compatible Python/tool maintenance are automatic. Historical editorial reviews are a backlog, not a reason to stop all updates.

[Latest meaningful changes](https://github.com/pauljones0/actions-latest/blob/main/data/catalog-changes.md) · [All review items](https://github.com/pauljones0/actions-latest/blob/main/data/review-queue.json) · [Maintenance guide](https://github.com/pauljones0/actions-latest/blob/main/MAINTENANCE.md)

## Next decisions

| Action | Why it is here | Next step |
| --- | --- | --- |
| [asdf-vm/actions](https://github.com/asdf-vm/actions/tree/b7bcd026f18772e44fe1026d729e1611cc435d47/) | Fetch or scan failed: No action.yml or action.yaml at asdf-vm/actions@b7bcd026f18772e44fe1026d729e1611cc435d47 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review asdf-vm/actions`. |
| [actions/actions-sync](https://github.com/actions/actions-sync/tree/c813a122adc82b86e60cae8b0d19e3b3b530cbfa/) | Fetch or scan failed: No action.yml or action.yaml at actions/actions-sync@c813a122adc82b86e60cae8b0d19e3b3b530cbfa | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review actions/actions-sync`. |
| [ansible/ansible-content-actions](https://github.com/ansible/ansible-content-actions/tree/7dc7e15a53c2ae8bd092461e53dafd6627e34ac6/) | Fetch or scan failed: zizmor failed with exit 1 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review ansible/ansible-content-actions`. |
| [bitwarden/gh-actions](https://github.com/bitwarden/gh-actions/tree/c145aa56a48d77bb9c36162a07cc6a30b7f01f1f/) | Fetch or scan failed: No action.yml or action.yaml at bitwarden/gh-actions@c145aa56a48d77bb9c36162a07cc6a30b7f01f1f | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bitwarden/gh-actions`. |
| [bytecodealliance/actions](https://github.com/bytecodealliance/actions/tree/9152e710e9f7182e4c29ad218e4f335a7b203613/) | Fetch or scan failed: No action.yml or action.yaml at bytecodealliance/actions@9152e710e9f7182e4c29ad218e4f335a7b203613 | Inspect the immutable source. For a missing root manifest, check subdirectory actions; for a transient failure, rerun refresh. Never mark this clean. Run `uv run python manage.py review bytecodealliance/actions`. |
| [mikefarah/yq](https://github.com/mikefarah/yq/tree/c14f446382944492701b16c1ddb48bb9dbe683e3/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review mikefarah/yq`. |
| [super-linter/super-linter](https://github.com/super-linter/super-linter/tree/4ce20838b8ab83717e78138c5b3a1407148e0918/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review super-linter/super-linter`. |
| [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action/tree/19dda84776b3518d98b8798e591daee763049ed3/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review anthropics/claude-code-action`. |
| [actions/checkout](https://github.com/actions/checkout/tree/3d3c42e5aac5ba805825da76410c181273ba90b1/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/checkout`. |
| [appleboy/ssh-action](https://github.com/appleboy/ssh-action/tree/0ff4204d59e8e51228ff73bce53f80d53301dee2/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review appleboy/ssh-action`. |
| [Platane/snk](https://github.com/Platane/snk/tree/d8f6715049803e982ee5ff501b6b9b7d5deeb09b/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review Platane/snk`. |
| [softprops/action-gh-release](https://github.com/softprops/action-gh-release/tree/efb35369e0ad2afab669f228072c1b0d510eae64/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review softprops/action-gh-release`. |
| [actions/cache](https://github.com/actions/cache/tree/55cc8345863c7cc4c66a329aec7e433d2d1c52a9/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review actions/cache`. |
| [docker/build-push-action](https://github.com/docker/build-push-action/tree/53b7df96c91f9c12dcc8a07bcb9ccacbed38856a/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review docker/build-push-action`. |
| [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages/tree/84c30a85c19949d7eee79c4ff27748b70285e453/) | Historical editorial guidance has not been reviewed:  | Review source-backed facts and human claims. Unsupported claims should be corrected or removed. Run `uv run python manage.py review peaceiris/actions-gh-pages`. |
