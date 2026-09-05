"""Observe tags, select aged revisions, enrich their manifests, publish a snapshot."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from pathlib import Path

from .github import GitHubClient, GitHubError, NotFound
from .models import (
    MIN_TAG_AGE,
    ActionRecord,
    ActionState,
    CatalogEntry,
    Revision,
    TagObservation,
    utc_now,
    version_key,
)
from .security import POLICY_VERSION, SCANNER_VERSION, ScanError, Scanner, parse_manifest
from .snapshot import digest, load_catalog, publish_snapshot, validate_snapshot


def observe_tags(
    tags: dict[str, str], previous: dict[str, TagObservation], now: datetime
) -> dict[str, TagObservation]:
    """A changed, disappeared, or reappearing mapping starts a new observation window."""
    result = {}
    for tag, sha in tags.items():
        if version_key(tag) is None:
            continue
        old = previous.get(tag)
        first = old.first_seen if old and old.sha == sha and old.last_seen <= now else now
        result[tag] = TagObservation(sha=sha, first_seen=first, last_seen=now)
    return result


def select_revision(
    observations: dict[str, TagObservation], current: Revision | None, now: datetime, is_prerelease
) -> Revision | None:
    current_key = version_key(current.tag) if current else None
    for tag in sorted(observations, key=lambda t: (version_key(t), t), reverse=True):
        observation = observations[tag]
        if current_key and version_key(tag) < current_key:
            continue
        if observation.last_seen != now or now - observation.first_seen < MIN_TAG_AGE:
            continue
        if is_prerelease(tag):
            continue
        return Revision(tag=tag, sha=observation.sha, stability="observed")
    return current


def refresh_action(
    catalog: CatalogEntry,
    previous: ActionState,
    client: GitHubClient,
    scanner: Scanner,
    now: datetime,
) -> ActionRecord:
    state = previous.model_dump()
    state["attempted_at"] = now
    state["update_error"] = None
    try:
        repository = client.repository(catalog.repository)
        tags = client.tags(catalog.repository)
        observations = observe_tags(tags, previous.observations, now)
        selected = select_revision(
            observations,
            previous.selected,
            now,
            lambda tag: client.is_prerelease(catalog.repository, tag),
        )
        state.update(
            observations=observations,
            selected=selected,
            stars=repository.get("stargazers_count", 0),
            robustness_score=int(
                repository.get("stargazers_count", 0) + repository.get("forks_count", 0) * 0.5
            ),
            pushed_at=repository.get("pushed_at"),
            checked_at=now,
            repository_status="archived" if repository["archived"] else "active",
        )
        if selected and (not previous.selected or selected.sha != previous.selected.sha):
            state.update(manifest=None, scan=None, scan_error=None, scan_attempted_at=None)
        if selected:
            scan = state["scan"]
            due = (
                not scan
                or not state["manifest"]
                or state["scan_error"]
                or scan["scanned_at"] > now
                or now - scan["scanned_at"] >= timedelta(days=7)
                or scan["scanner_version"] != SCANNER_VERSION
                or scan["policy_version"] != POLICY_VERSION
            )
            if due:
                state["scan_attempted_at"] = now
                try:
                    content = client.manifest(catalog.action, selected.sha)
                    state["manifest"] = parse_manifest(content, selected.sha)
                    state["scan"] = scanner.scan(content, selected.sha, now)
                    state["scan_error"] = None
                except (GitHubError, ScanError) as exc:
                    state["scan_error"] = str(exc)
    except GitHubError as exc:
        state["update_error"] = str(exc)
        if isinstance(exc, NotFound):
            state["repository_status"] = "not_found"
    return ActionRecord(catalog=catalog, state=ActionState.model_validate(state))


def update(
    catalog_path: Path,
    snapshot_path: Path,
    *,
    client: GitHubClient | None = None,
    scanner: Scanner | None = None,
    workers: int = 6,
    now: datetime | None = None,
) -> dict[str, int]:
    catalog = load_catalog(catalog_path)
    catalog_digest = digest([c.model_dump(mode="json") for c in catalog])
    previous = (
        {record.action.casefold(): record.state for record in validate_snapshot(snapshot_path)}
        if snapshot_path.exists()
        else {}
    )
    client = client or GitHubClient()
    scanner = scanner or Scanner()
    now = now or utc_now()
    catalog.sort(
        key=lambda c: (
            previous.get(c.action.casefold(), ActionState()).checked_at
            or datetime.min.replace(tzinfo=now.tzinfo),
            c.action.casefold(),
        )
    )
    records = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                refresh_action,
                entry,
                previous.get(entry.action.casefold(), ActionState()),
                client,
                scanner,
                now,
            )
            for entry in catalog
        ]
        for future in as_completed(futures):
            records.append(future.result())
    latest_catalog = load_catalog(catalog_path)
    if digest([c.model_dump(mode="json") for c in latest_catalog]) != catalog_digest:
        raise RuntimeError("Catalog changed during the update; rerun against the new inputs")
    publish_snapshot(records, snapshot_path)
    return {
        "actions": len(records),
        "updated": sum(
            r.state.selected != previous.get(r.action.casefold(), ActionState()).selected
            for r in records
        ),
        "update_errors": sum(r.state.update_error is not None for r in records),
        "scan_errors": sum(r.state.scan_error is not None for r in records),
        "blocked": sum(r.security_status(now) == "blocked" for r in records),
    }
