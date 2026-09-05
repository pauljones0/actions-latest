"""Validated catalog inputs and revision-specific observations.

Editorial claims live in CatalogEntry. Everything fetched or inferred by the
updater lives in ActionState and is published in a single SQLite snapshot.
"""

from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

SCHEMA_VERSION = 2
SCANNER_VERSION = "1.30.0"
POLICY_VERSION = 1
MIN_TAG_AGE = timedelta(days=7)
SCAN_MAX_AGE = timedelta(days=14)
SHA_PATTERN = r"^[0-9a-f]{40}$"
ACTION_PATTERN = r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*$"


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_assignment=True)

    @field_validator("*", mode="after")
    @classmethod
    def aware_dates(cls, value):
        if isinstance(value, datetime):
            if value.tzinfo is None or value.utcoffset() is None:
                raise ValueError("timestamps must include a timezone")
            return value.astimezone(timezone.utc)
        return value


class CatalogEntry(Model):
    action: str = Field(pattern=ACTION_PATTERN)
    description: str
    category: str = "General"
    tags: list[str] = Field(default_factory=list)
    match_logic: str = ""
    requires: list[str] = Field(default_factory=list)
    conflicts: list[str] = Field(default_factory=list)
    permissions: dict[str, str] = Field(default_factory=dict)
    auth: str = ""
    side_effects: list[str] = Field(default_factory=list)
    performance: str = ""
    origin: Literal["curated", "discovered"] = "curated"
    source_url: str | None = None
    reviewed_sha: str | None = Field(default=None, pattern=SHA_PATTERN)
    reviewed_at: datetime | None = None

    @field_validator("action")
    @classmethod
    def safe_action(cls, value: str) -> str:
        if any(part in {".", ".."} for part in value.split("/")):
            raise ValueError("action paths cannot contain traversal components")
        return value

    @property
    def repository(self) -> str:
        return "/".join(self.action.split("/")[:2])


class Revision(Model):
    tag: str = Field(min_length=1)
    sha: str = Field(pattern=SHA_PATTERN)
    # Imported historical pins have no evidence of tag stability.
    stability: Literal["unverified", "observed"] = "unverified"


class TagObservation(Model):
    sha: str = Field(pattern=SHA_PATTERN)
    first_seen: datetime
    last_seen: datetime

    @model_validator(mode="after")
    def ordered(self):
        if self.last_seen < self.first_seen:
            raise ValueError("last_seen precedes first_seen")
        return self


class Manifest(Model):
    sha: str = Field(pattern=SHA_PATTERN)
    name: str = ""
    description: str = ""
    runtime: str = Field(min_length=1)
    inputs: dict[str, dict] = Field(default_factory=dict)
    outputs: list[str] = Field(default_factory=list)


class Finding(Model):
    rule: str
    severity: Literal["info", "warning", "error"]
    message: str = ""
    line: int | None = Field(default=None, ge=1)


class ScanEvidence(Model):
    sha: str = Field(pattern=SHA_PATTERN)
    scanner_version: str = Field(min_length=1)
    policy_version: int = POLICY_VERSION
    scanned_at: datetime
    findings: list[Finding] = Field(default_factory=list)


class ActionState(Model):
    selected: Revision | None = None
    observations: dict[str, TagObservation] = Field(default_factory=dict)
    stars: int = Field(default=0, ge=0)
    robustness_score: int = Field(default=0, ge=0)
    pushed_at: datetime | None = None
    checked_at: datetime | None = None
    attempted_at: datetime | None = None
    repository_status: Literal["unknown", "active", "archived", "not_found"] = "unknown"
    update_error: str | None = None
    manifest: Manifest | None = None
    scan: ScanEvidence | None = None
    scan_attempted_at: datetime | None = None
    scan_error: str | None = None

    @model_validator(mode="after")
    def matching_revision(self):
        for evidence in (self.manifest, self.scan):
            if evidence and (not self.selected or evidence.sha != self.selected.sha):
                raise ValueError("manifest and scan evidence must match the selected SHA")
        return self


class ActionRecord(Model):
    catalog: CatalogEntry
    state: ActionState = Field(default_factory=ActionState)

    @property
    def action(self) -> str:
        return self.catalog.action

    @property
    def description(self) -> str:
        if self.state.manifest and self.state.manifest.description:
            return self.state.manifest.description
        return self.catalog.description

    def guidance_status(self) -> str:
        if self.catalog.origin == "discovered":
            return "source-derived"
        if not self.catalog.reviewed_sha:
            return "unreviewed"
        if self.state.selected and self.catalog.reviewed_sha == self.state.selected.sha:
            return "reviewed for selected SHA"
        return "needs review after revision change"

    def security_status(self, now: datetime | None = None) -> str:
        now = now or utc_now()
        scan = self.state.scan
        # A failed rescan never erases known blocking evidence for the same SHA.
        if scan and any(f.severity == "error" for f in scan.findings):
            return "blocked"
        if self.state.scan_error:
            return "error"
        if not scan:
            return "unknown"
        version = version_key(scan.scanner_version)
        minimum = version_key(SCANNER_VERSION)
        if (
            version is None
            or minimum is None
            or version[0] != minimum[0]
            or version < minimum
            or scan.policy_version != POLICY_VERSION
        ):
            return "stale"
        if scan.scanned_at > now or now - scan.scanned_at > SCAN_MAX_AGE:
            return "stale"
        return "warning" if any(f.severity == "warning" for f in scan.findings) else "clean"

    def usage_ready(self, now: datetime | None = None) -> bool:
        return bool(
            self.state.selected
            and self.state.selected.stability == "observed"
            and self.state.manifest
            and self.security_status(now) in {"clean", "warning"}
        )


def version_key(tag: str) -> tuple[int, ...] | None:
    """Numeric stable-looking tags only; release prerelease flags are checked separately."""
    if not re.fullmatch(r"v?\d+(?:\.\d+){0,2}", tag):
        return None
    parts = tuple(int(x) for x in tag.removeprefix("v").split("."))
    return (*parts, *(0 for _ in range(3 - len(parts))), len(parts))
