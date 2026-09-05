from unittest.mock import Mock

import pytest
from conftest import MANIFEST, SHA

from actions_latest.commands import Navigator, parse_chain
from actions_latest.models import ActionRecord, ActionState, CatalogEntry
from actions_latest.security import ScanError
from actions_latest.snapshot import publish_snapshot
from actions_latest.versions import MetadataStore


@pytest.fixture
def navigator(tmp_path, record):
    path = tmp_path / "actions.db"
    irrelevant = ActionRecord(
        catalog=CatalogEntry(action="other/node", description="node deployment")
    )
    publish_snapshot([record, irrelevant], path)
    client, scanner = Mock(), Mock()
    client.manifest.return_value = MANIFEST
    scanner.scan.return_value = record.state.scan
    return Navigator(MetadataStore(path), client, scanner)


def test_pipes_refine_and_preserve_identity_through_cat(navigator):
    result = navigator.run("grep setup|grep node|cat|audit")
    assert result.code == 0
    navigator.client.manifest.assert_called_once_with("example/setup-node", SHA)
    navigator.scanner.scan.assert_called_once_with(MANIFEST, SHA)
    assert "other/node" not in result.text


def test_pipe_refinement_happens_before_result_limit(tmp_path, record):
    rows = [record]
    for i in range(30):
        rows.append(
            ActionRecord(
                catalog=CatalogEntry(action=f"other/setup-{i}", description="setup"),
                state=ActionState(robustness_score=100000),
            )
        )
    path = tmp_path / "actions.db"
    publish_snapshot(rows, path)
    result = Navigator(MetadataStore(path)).run("grep setup | grep node | cat")
    assert result.code == 0 and "example/setup-node" in result.text


def test_conditional_and_sequence_do_not_forward_stdin(navigator):
    result = navigator.run("help&&ls")
    assert result.code == 0 and "Owners:" in result.text
    assert navigator.run("missing && audit example/setup-node").code == 127
    navigator.scanner.scan.assert_not_called()
    result = navigator.run("missing && cat unknown/repo ; browse")
    assert result.code == 0 and "Categories:" in result.text
    result = navigator.run("missing | audit example/setup-node ; ls")
    assert result.code == 0
    navigator.scanner.scan.assert_not_called()


def test_empty_pipe_does_not_treat_no_matches_as_action(navigator):
    result = navigator.run("grep nonexistent | cat | audit")
    assert result.code == 0 and "No action candidates" in result.text
    navigator.client.manifest.assert_not_called()


@pytest.mark.parametrize("query", ['grep "a | b"', "grep '&&'", r"grep a\;b", "grep '|'"])
def test_quoted_operators_are_data(query, navigator):
    assert len(parse_chain(query)[0]) == 1
    assert navigator.run(query).code == 0


@pytest.mark.parametrize(
    "query", ['grep "unclosed', "grep x || cat", "grep x ;", "| cat", "ls & cat"]
)
def test_invalid_chains_are_errors(query, navigator):
    assert navigator.run(query).code != 0


def test_man_and_audit_use_same_sha_as_snippet(navigator):
    result = navigator.run("cat example/setup-node ; man example/setup-node")
    assert f"@{SHA}" in result.text and result.code == 0
    navigator.client.manifest.assert_called_with("example/setup-node", SHA)
    navigator.scanner.scan.side_effect = ScanError("scanner failed")
    result = navigator.run("audit example/setup-node")
    assert result.code == 1 and "scanner failed" in result.text
    assert "No manifest findings" not in result.text


def test_database_failure_is_user_visible(tmp_path):
    result = Navigator(MetadataStore(tmp_path / "absent.db")).run("grep node")
    assert result.code == 1 and "[error]" in result.text
