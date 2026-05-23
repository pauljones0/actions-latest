#!/usr/bin/env python3
"""Tests for actions_latest helpers."""

import unittest
from unittest.mock import patch

from actions_latest.versions import (
    latest_for_action,
    latest_major_tag,
    normalize_action_name,
    parse_versions,
    workflow_updates,
)


VERSIONS_TEXT = """
astral-sh/setup-uv@v7
actions/checkout@v6
actions/download-artifact@v8
actions/upload-artifact@v7
github/codeql-action@v4
"""


class TestActionsLatestVersions(unittest.TestCase):
    def test_parse_versions_ignores_non_version_tokens(self):
        versions = parse_versions(f"noise\n{VERSIONS_TEXT}\nactions/checkout@main\n")

        self.assertEqual(
            versions,
            {
                "actions/checkout": "v6",
                "actions/download-artifact": "v8",
                "actions/upload-artifact": "v7",
                "astral-sh/setup-uv": "v7",
                "github/codeql-action": "v4",
            },
        )

    def test_latest_major_tag_matches_simon_style(self):
        self.assertEqual(latest_major_tag(["v1.0.0", "v3", "v2", "v10.1.0"]), "v3")
        self.assertIsNone(latest_major_tag(["stable", "main", "v1.0.0"]))

    def test_normalize_action_name(self):
        self.assertEqual(normalize_action_name("checkout"), "actions/checkout")
        self.assertEqual(normalize_action_name("actions/checkout@v4"), "actions/checkout")
        self.assertEqual(normalize_action_name("uses: actions/upload-artifact@v4"), "actions/upload-artifact")

    def test_latest_for_action(self):
        versions = parse_versions(VERSIONS_TEXT)

        self.assertEqual(latest_for_action("checkout@v4", versions, refresh=False), ("actions/checkout", "v6"))
        self.assertEqual(latest_for_action("astral-sh/setup-uv@v6", versions, refresh=False), ("astral-sh/setup-uv", "v7"))
        self.assertEqual(latest_for_action("github/codeql-action/init@v3", versions, refresh=False), ("github/codeql-action", "v4"))
        self.assertIsNone(latest_for_action("softprops/action-gh-release", versions, refresh=False))

    @patch("actions_latest.versions.fetch_action_tags")
    def test_latest_for_third_party_action_uses_highest_major_tag(self, mock_fetch_tags):
        mock_fetch_tags.return_value = ["v3.0.0", "v3", "v2", "v1"]

        self.assertEqual(
            latest_for_action("softprops/action-gh-release@v2", parse_versions(VERSIONS_TEXT)),
            ("softprops/action-gh-release", "v3"),
        )

    def test_workflow_updates(self):
        workflow = """
jobs:
  test:
    steps:
      - uses: actions/checkout@v4
      - uses: actions/upload-artifact@v7
      - uses: softprops/action-gh-release@v2
      - uses: ./local-action
"""

        updates = workflow_updates(workflow, parse_versions(VERSIONS_TEXT), refresh=False)

        self.assertEqual(len(updates), 1)
        self.assertEqual(updates[0].action, "actions/checkout")
        self.assertEqual(updates[0].current, "v4")
        self.assertEqual(updates[0].latest, "v6")

    @patch("actions_latest.versions.fetch_action_tags")
    def test_workflow_updates_third_party_actions(self, mock_fetch_tags):
        mock_fetch_tags.side_effect = lambda action: {
            "softprops/action-gh-release": ["v3.0.0", "v3", "v2"],
            "Swatinem/rust-cache": ["v2.9.1", "v2", "v1"],
        }[action]
        workflow = """
jobs:
  release:
    steps:
      - uses: softprops/action-gh-release@v2
      - uses: Swatinem/rust-cache@v2
      - uses: dtolnay/rust-toolchain@stable
"""

        updates = workflow_updates(workflow, parse_versions(VERSIONS_TEXT))

        self.assertEqual(len(updates), 1)
        self.assertEqual(updates[0].action, "softprops/action-gh-release")
        self.assertEqual(updates[0].current, "v2")
        self.assertEqual(updates[0].latest, "v3")


if __name__ == "__main__":
    unittest.main()
