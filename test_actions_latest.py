#!/usr/bin/env python3
"""Tests for actions_latest helpers."""

import unittest

from actions_latest.versions import (
    latest_for_action,
    normalize_action_name,
    parse_versions,
    workflow_updates,
)


VERSIONS_TEXT = """
actions/checkout@v6
actions/download-artifact@v8
actions/upload-artifact@v7
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
            },
        )

    def test_normalize_action_name(self):
        self.assertEqual(normalize_action_name("checkout"), "actions/checkout")
        self.assertEqual(normalize_action_name("actions/checkout@v4"), "actions/checkout")
        self.assertEqual(normalize_action_name("uses: actions/upload-artifact@v4"), "actions/upload-artifact")

    def test_latest_for_action(self):
        versions = parse_versions(VERSIONS_TEXT)

        self.assertEqual(latest_for_action("checkout@v4", versions), ("actions/checkout", "v6"))
        self.assertIsNone(latest_for_action("softprops/action-gh-release", versions))

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

        updates = workflow_updates(workflow, parse_versions(VERSIONS_TEXT))

        self.assertEqual(len(updates), 1)
        self.assertEqual(updates[0].action, "actions/checkout")
        self.assertEqual(updates[0].current, "v4")
        self.assertEqual(updates[0].latest, "v6")


if __name__ == "__main__":
    unittest.main()
