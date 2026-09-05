"""Versioned portable snapshots: clients validate JSON before building local SQLite."""

from __future__ import annotations

import gzip
import io
import json
import os
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

from pydantic import Field

from .models import SCHEMA_VERSION, ActionRecord, Model, utc_now
from .snapshot import canonical, digest, validate_snapshot

MAX_COMPRESSED = 32 * 1024 * 1024
MAX_UNPACKED = 128 * 1024 * 1024


class SnapshotFeed(Model):
    schema_version: int
    published_at: datetime
    records_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    records: list[ActionRecord] = Field(max_length=20000)


def encode_feed(records: list[ActionRecord], published_at: datetime | None = None) -> bytes:
    records = sorted(records, key=lambda r: r.action.casefold())
    feed = SnapshotFeed(
        schema_version=SCHEMA_VERSION,
        published_at=published_at or utc_now(),
        records_sha256=digest([r.model_dump(mode="json") for r in records]),
        records=records,
    )
    return gzip.compress(canonical(feed.model_dump(mode="json")).encode(), mtime=0)


def decode_feed(payload: bytes, now: datetime | None = None) -> SnapshotFeed:
    if len(payload) > MAX_COMPRESSED:
        raise ValueError("Snapshot download exceeds size limit")
    with gzip.GzipFile(fileobj=io.BytesIO(payload)) as compressed:
        unpacked = compressed.read(MAX_UNPACKED + 1)
    if len(unpacked) > MAX_UNPACKED:
        raise ValueError("Snapshot expands beyond size limit")
    data = json.loads(unpacked)
    if not isinstance(data, dict) or data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("Incompatible snapshot schema; update the installed application")
    feed = SnapshotFeed.model_validate(data)
    if feed.published_at > (now or utc_now()) + timedelta(minutes=5):
        raise ValueError("Snapshot publication timestamp is in the future")
    names = [r.action.casefold() for r in feed.records]
    if len(names) != len(set(names)):
        raise ValueError("Snapshot contains duplicate actions")
    if feed.records_sha256 != digest([r.model_dump(mode="json") for r in feed.records]):
        raise ValueError("Snapshot content digest mismatch")
    return feed


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=".snapshot-")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def export_feed(snapshot: Path, destination: Path) -> None:
    payload = encode_feed(validate_snapshot(snapshot))
    decode_feed(payload)
    atomic_write(destination, payload)
