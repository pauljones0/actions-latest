import json
import os
import subprocess
import sys
from pathlib import Path

from actions_latest.snapshot import load_records, publish_snapshot

ROOT = Path(__file__).resolve().parents[1]


def test_offline_rebuild_reconciles_catalog_and_check_detects_drift(tmp_path, record):
    catalog, snapshot = tmp_path / "catalog.json", tmp_path / "actions.db"
    publish_snapshot([record], snapshot)
    added = record.catalog.model_copy(update={"action": "new/action"})
    catalog.write_text(json.dumps([record.catalog.model_dump(), added.model_dump()]))
    command = [
        sys.executable,
        str(ROOT / "update.py"),
        "--catalog",
        str(catalog),
        "--snapshot",
        str(snapshot),
    ]
    result = subprocess.run([*command, "--check"], capture_output=True, text=True, timeout=20)
    assert result.returncode != 0 and "differs" in result.stderr
    subprocess.run([*command, "--rebuild"], check=True, capture_output=True, timeout=20)
    records = load_records(snapshot)
    assert len(records) == 2
    assert records[0].state == record.state
    assert records[1].state.selected is None
    subprocess.run([*command, "--check"], check=True, capture_output=True, timeout=20)


def test_concurrent_git_changes_are_preserved_by_push_guard(tmp_path):
    def git(path, *args):
        return subprocess.run(
            ["git", *args], cwd=path, check=True, capture_output=True, text=True, timeout=20
        )

    remote, update, human = tmp_path / "remote.git", tmp_path / "update", tmp_path / "human"
    git(tmp_path, "init", "--bare", "--initial-branch=main", str(remote))
    git(tmp_path, "clone", str(remote), str(update))
    git(update, "config", "user.name", "Test")
    git(update, "config", "user.email", "test@example.invalid")
    (update / "catalog.json").write_text('["example/a"]')
    (update / "actions.db").write_text("old snapshot")
    git(update, "add", ".")
    git(update, "commit", "-m", "initial")
    git(update, "push", "origin", "main")
    git(tmp_path, "clone", str(remote), str(human))
    git(human, "config", "user.name", "Test")
    git(human, "config", "user.email", "test@example.invalid")
    (update / "actions.db").write_text("new generated snapshot")
    git(update, "commit", "-am", "update")
    (human / "catalog.json").write_text('["example/a", "example/b"]')
    git(human, "commit", "-am", "add catalog entry")
    git(human, "push", "origin", "main")
    env = dict(os.environ, GITHUB_TOKEN="unused-local-test-token")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/push_snapshot.py")],
        cwd=update,
        env=env,
        capture_output=True,
        text=True,
        timeout=20,
    )
    assert result.returncode != 0
    assert "example/b" in git(remote, "show", "main:catalog.json").stdout
    assert "old snapshot" in git(remote, "show", "main:actions.db").stdout
    assert "unused-local-test-token" not in result.stdout + result.stderr
