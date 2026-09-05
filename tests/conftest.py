from datetime import datetime, timezone

import pytest

from actions_latest.models import (
    ActionRecord,
    ActionState,
    CatalogEntry,
    Manifest,
    Revision,
    ScanEvidence,
)
from actions_latest.security import SCANNER_VERSION

NOW = datetime.now(timezone.utc)
SHA = "a" * 40
NEW_SHA = "b" * 40
MANIFEST = """name: example
description: example action
inputs:
  version:
    description: version to install
    required: true
outputs:
  installed-version:
    description: installed version
runs:
  using: node24
  main: dist/index.js
"""


@pytest.fixture
def record():
    return ActionRecord(
        catalog=CatalogEntry(
            action="example/setup-node",
            description="Setup node with caching",
            category="Setup",
            tags=["node", "cache"],
            match_logic="Install node",
        ),
        state=ActionState(
            selected=Revision(tag="v1.0.0", sha=SHA, stability="observed"),
            manifest=Manifest(sha=SHA, runtime="node24", outputs=["installed-version"]),
            scan=ScanEvidence(sha=SHA, scanner_version=SCANNER_VERSION, scanned_at=NOW),
        ),
    )
