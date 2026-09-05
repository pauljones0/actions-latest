"""Fresh publication is insufficient: measure observation and scan coverage separately."""

from datetime import datetime, timedelta

from .models import ActionRecord, utc_now


def health_report(
    records: list[ActionRecord], published_at: datetime | None, now: datetime | None = None
) -> dict:
    now = now or utc_now()
    stale = [
        r.action
        for r in records
        if not r.state.checked_at
        or not timedelta(0) <= now - r.state.checked_at <= timedelta(hours=72)
    ]
    scan_errors = [r.action for r in records if r.state.scan_error]
    update_errors = [r.action for r in records if r.state.update_error]
    reasons = []
    if not published_at or not timedelta(0) <= now - published_at <= timedelta(hours=48):
        reasons.append("No publication within 48 hours")
    if not records or len(stale) / len(records) > 0.2:
        reasons.append("More than 20% of actions lack a successful observation within 72 hours")
    if records and len(scan_errors) / len(records) > 0.2:
        reasons.append("More than 20% of actions have scanner failures")
    return {
        "checked_at": now.isoformat(),
        "published_at": published_at.isoformat() if published_at else None,
        "healthy": not reasons,
        "reasons": reasons,
        "actions": len(records),
        "stale_observations": stale,
        "update_errors": update_errors,
        "scan_errors": scan_errors,
        "security_counts": {
            status: sum(r.security_status(now) == status for r in records)
            for status in ("clean", "warning", "blocked", "unknown", "stale", "error")
        },
        "editorial_review_queue": [
            r.action
            for r in records
            if r.guidance_status() not in {"source-derived", "reviewed for selected SHA"}
        ],
    }


def include_discovery(report: dict, discovery: dict, now: datetime | None = None) -> dict:
    now = now or utc_now()
    try:
        checked = datetime.fromisoformat(discovery["checked_at"])
        recent = timedelta(0) <= now - checked <= timedelta(hours=48)
    except (KeyError, ValueError, TypeError):
        recent = False
    if not recent or discovery.get("errors"):
        report["healthy"] = False
        report["reasons"].append("Discovery is stale or its repository searches failed")
    report["discovery_errors"] = discovery.get("errors", [])
    return report
