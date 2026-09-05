"""Background snapshot refresh with atomic, schema-specific caches and offline fallback."""

from __future__ import annotations

import json
import os
import sqlite3
import threading
import zlib
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import Request, urlopen

from filelock import FileLock, Timeout

from .feed import MAX_COMPRESSED, atomic_write, decode_feed
from .models import SCHEMA_VERSION, Model, utc_now
from .snapshot import publish_snapshot, validate_snapshot

FEED_URL = f"https://raw.githubusercontent.com/pauljones0/actions-latest/main/data/snapshot-v{SCHEMA_VERSION}.json.gz"
CHECK_INTERVAL = timedelta(hours=6)
RETRY_INTERVAL = timedelta(hours=1)


class RefreshState(Model):
    last_attempt: datetime | None = None
    last_success: datetime | None = None
    published_at: datetime | None = None
    records_sha256: str | None = None
    error: str | None = None


def fetch_feed(url: str) -> bytes:
    with urlopen(Request(url, headers={"User-Agent": "actions-latest/0.4"}), timeout=5) as response:
        return response.read(MAX_COMPRESSED + 1)


class SnapshotManager:
    def __init__(
        self,
        bundled: Path,
        cache: Path | None = None,
        *,
        enabled: bool | None = None,
        fetch=fetch_feed,
    ):
        root = Path(os.environ.get("XDG_CACHE_HOME", str(Path.home() / ".cache")))
        self.cache = cache or root / "actions-latest" / f"schema-{SCHEMA_VERSION}"
        self.bundled = bundled
        self.database = self.cache / "actions.db"
        self.metadata = self.cache / "refresh.json"
        self.enabled = (
            os.environ.get("ACTIONS_LATEST_AUTO_REFRESH", "1") != "0"
            if enabled is None
            else enabled
        )
        self.fetch = fetch
        self._path = bundled
        self._thread: threading.Thread | None = None
        self._thread_lock = threading.Lock()
        self._error: str | None = None
        self._baseline = max(
            (r.state.checked_at for r in validate_snapshot(bundled) if r.state.checked_at),
            default=None,
        )
        if self.database.exists():
            try:
                validate_snapshot(self.database)
                self._path = self.database
            except (ValueError, OSError, sqlite3.Error, RuntimeError) as exc:
                self._error = f"Cached snapshot rejected: {exc}"

    @property
    def path(self) -> Path:
        return self._path

    def _state(self) -> dict:
        try:
            data = json.loads(self.metadata.read_text())
            state = RefreshState.model_validate(data)
            if state.published_at and state.published_at > utc_now() + timedelta(minutes=5):
                raise ValueError("Invalid cached publication date")
            return {
                key: value.isoformat() if isinstance(value, datetime) else value
                for key, value in state.model_dump().items()
            }
        except (ValueError, OSError):
            return {}

    def _due(self, now: datetime) -> bool:
        state = self._state()
        try:
            attempted = datetime.fromisoformat(state["last_attempt"])
            interval = RETRY_INTERVAL if state.get("error") else CHECK_INTERVAL
            return attempted > now or now - attempted >= interval
        except (KeyError, ValueError, TypeError):
            return True

    def kick(self) -> None:
        if self._path != self.database and self.database.exists():
            try:
                validate_snapshot(self.database)
                self._path = self.database
            except (ValueError, OSError, sqlite3.Error, RuntimeError):
                pass
        if not self.enabled or not self._due(utc_now()):
            return
        with self._thread_lock:
            if self._thread and self._thread.is_alive():
                return
            self._thread = threading.Thread(
                target=self.refresh, name="snapshot-refresh", daemon=True
            )
            self._thread.start()

    def refresh(self, *, force: bool = False, now: datetime | None = None) -> bool:
        now = now or utc_now()
        if not self.enabled or (not force and not self._due(now)):
            return False
        try:
            self.cache.mkdir(parents=True, exist_ok=True)
            with FileLock(str(self.cache / "refresh.lock"), timeout=0):
                # A different client may have refreshed while this one waited.
                if not force and not self._due(now):
                    if self.database.exists():
                        validate_snapshot(self.database)
                        self._path = self.database
                    return False
                state = self._state()
                state["last_attempt"] = now.isoformat()
                try:
                    feed = decode_feed(self.fetch(FEED_URL), now)
                    previous_date = state.get("published_at")
                    if self._baseline and feed.published_at < self._baseline:
                        raise ValueError("Refusing a snapshot older than the bundled observations")
                    if previous_date and feed.published_at < datetime.fromisoformat(previous_date):
                        raise ValueError("Refusing a snapshot older than the cached publication")
                    if (
                        state.get("records_sha256") != feed.records_sha256
                        or self._path != self.database
                    ):
                        publish_snapshot(feed.records, self.database)
                    self._path = self.database
                    state.update(
                        published_at=feed.published_at.isoformat(),
                        records_sha256=feed.records_sha256,
                        last_success=now.isoformat(),
                        error=None,
                    )
                    self._error = None
                    succeeded = True
                except (
                    ValueError,
                    OSError,
                    sqlite3.Error,
                    RuntimeError,
                    EOFError,
                    zlib.error,
                ) as exc:
                    state["error"] = f"{type(exc).__name__}: {exc}"
                    self._error = state["error"]
                    succeeded = False
                atomic_write(self.metadata, json.dumps(state, sort_keys=True).encode())
                return succeeded
        except Timeout:
            return False
        except (OSError, ValueError, sqlite3.Error, RuntimeError) as exc:
            self._error = f"Refresh unavailable: {exc}"
            return False

    def status(self) -> dict:
        state = self._state()
        return {
            **state,
            "enabled": self.enabled,
            "publication_stale": not state.get("published_at")
            or utc_now() - datetime.fromisoformat(state["published_at"]) > timedelta(hours=48),
            "source": "cache" if self._path == self.database else "bundled",
            "schema_version": SCHEMA_VERSION,
            "error": self._error or state.get("error"),
        }
