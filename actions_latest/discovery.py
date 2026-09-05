"""Bounded automatic action admission with immutable source provenance and exclusions."""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path

from pydantic import Field

from .feed import atomic_write
from .github import GitHubClient, GitHubError, NotFound
from .models import CatalogEntry, Model, utc_now, version_key
from .security import ScanError, Scanner, parse_manifest
from .snapshot import load_catalog


class DiscoveryPolicy(Model):
    enabled: bool = True
    minimum_stars: int = Field(default=50, ge=0)
    maximum_inactive_days: int = Field(default=365, ge=1)
    admissions_per_run: int = Field(default=10, ge=0, le=25)
    candidates_per_query: int = Field(default=20, ge=1, le=100)
    excluded_actions: list[str] = Field(default_factory=list)


def load_policy(path: Path | None) -> DiscoveryPolicy:
    return (
        DiscoveryPolicy.model_validate_json(path.read_text())
        if path and path.exists()
        else DiscoveryPolicy()
    )


def combined_catalog(
    curated: Path, discovered: Path | None = None, policy_path: Path | None = None
) -> list[CatalogEntry]:
    entries = (
        {c.action.casefold(): c for c in load_catalog(discovered)}
        if discovered and discovered.exists()
        else {}
    )
    entries.update({c.action.casefold(): c for c in load_catalog(curated)})
    excluded = {name.casefold() for name in load_policy(policy_path).excluded_actions}
    return sorted(
        (entry for name, entry in entries.items() if name not in excluded),
        key=lambda c: c.action.casefold(),
    )


def discover(
    curated: Path,
    registry: Path,
    report_path: Path,
    policy_path: Path,
    client: GitHubClient,
    scanner: Scanner,
    now: datetime | None = None,
) -> dict:
    now = now or utc_now()
    policy = load_policy(policy_path)
    known = {c.action.casefold() for c in combined_catalog(curated, registry, policy_path)}
    excluded = {name.casefold() for name in policy.excluded_actions}
    entries = load_catalog(registry) if registry.exists() else []
    history = (
        json.loads(report_path.read_text()).get("candidates", {}) if report_path.exists() else {}
    )
    admitted, errors, inspected = [], [], 0
    cutoff = now - timedelta(days=policy.maximum_inactive_days)
    queries = [
        f"topic:{topic} archived:false fork:false stars:>={policy.minimum_stars} pushed:>={cutoff.date()}"
        for topic in ("github-action", "github-actions")
    ]
    if policy.enabled:
        for query in queries:
            if len(admitted) >= policy.admissions_per_run:
                break
            try:
                candidates = client.search_repositories(query, policy.candidates_per_query)
            except GitHubError as exc:
                errors.append(str(exc))
                continue
            for candidate in candidates:
                if len(admitted) >= policy.admissions_per_run:
                    break
                action = candidate.get("full_name", "")
                if not action or action.casefold() in known | excluded:
                    continue
                prior = history.get(action, {})
                try:
                    elapsed = now - datetime.fromisoformat(prior["checked_at"])
                    cooldown = (
                        timedelta(hours=6) if prior.get("status") == "error" else timedelta(days=7)
                    )
                    if timedelta(0) <= elapsed < cooldown:
                        continue
                except (KeyError, TypeError, ValueError):
                    pass
                inspected += 1
                outcome = {"checked_at": now.isoformat(), "status": "rejected"}
                try:
                    if (
                        candidate.get("archived")
                        or candidate.get("fork")
                        or candidate.get("private")
                    ):
                        raise ValueError("Repository must be public, active, and not a fork")
                    if candidate.get("stargazers_count", 0) < policy.minimum_stars:
                        raise ValueError("Repository is below the configured popularity floor")
                    pushed = datetime.fromisoformat(candidate["pushed_at"].replace("Z", "+00:00"))
                    if pushed < cutoff:
                        raise ValueError("Repository has not been maintained recently")
                    CatalogEntry(action=action, description="")  # Validate before using the slug.
                    sha = client.default_sha(action, candidate["default_branch"])
                    manifest_text = client.manifest(action, sha)
                    manifest = parse_manifest(manifest_text, sha)
                    if not manifest.name or not manifest.description:
                        raise ValueError("Action must have a name and source description")
                    if not any(version_key(tag) for tag in client.tags(action)):
                        raise ValueError("No supported numeric version tags to observe")
                    scan = scanner.scan(manifest_text, sha, now)
                    if any(f.severity == "error" for f in scan.findings):
                        raise ValueError("Default-branch action manifest has blocking findings")
                    topics = candidate.get("topics", [])
                    tags = sorted(
                        {
                            t
                            for t in topics
                            if isinstance(t, str) and t not in {"github-action", "github-actions"}
                        }
                    )
                    entry = CatalogEntry(
                        action=action,
                        description=manifest.description,
                        category="Discovered",
                        tags=tags,
                        origin="discovered",
                        source_url=f"https://github.com/{action}/tree/{sha}",
                    )
                    entries.append(entry)
                    known.add(action.casefold())
                    admitted.append(action)
                    outcome.update(
                        status="admitted", source_sha=sha, scanner_version=scan.scanner_version
                    )
                except (GitHubError, ScanError, ValueError, KeyError, TypeError) as exc:
                    outcome["reason"] = str(exc)
                    if isinstance(exc, (GitHubError, ScanError)) and not isinstance(exc, NotFound):
                        outcome["status"] = "error"
                history[action] = outcome
    result = {
        "checked_at": now.isoformat(),
        "admitted": admitted,
        "inspected": inspected,
        "errors": errors,
        "candidates": history,
    }
    atomic_write(
        registry,
        (
            json.dumps(
                [
                    c.model_dump(mode="json")
                    for c in sorted(entries, key=lambda c: c.action.casefold())
                ],
                indent=2,
            )
            + "\n"
        ).encode(),
    )
    atomic_write(report_path, (json.dumps(result, indent=2, sort_keys=True) + "\n").encode())
    return result
