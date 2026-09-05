"""Bounded GitHub HTTP access with failures distinct from missing resources."""

from __future__ import annotations

import json
import os
import re
import threading
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

from .models import CatalogEntry


class GitHubError(RuntimeError):
    pass


class NotFound(GitHubError):
    pass


class RateLimited(GitHubError):
    pass


class AuthenticationError(GitHubError):
    pass


class TransientError(GitHubError):
    pass


class GitHubClient:
    def __init__(self, token: str | None = None, timeout: float = 15, retries: int = 2):
        self.token = token if token is not None else os.environ.get("GITHUB_TOKEN", "")
        self.timeout = timeout
        self.retries = retries
        self.rate_limited = threading.Event()

    def request(self, path: str, params: dict | None = None, *, raw: bool = False):
        if self.rate_limited.is_set():
            raise RateLimited("GitHub rate limit reached; retry in a later update")
        url = "https://api.github.com" + path
        if params:
            url += "?" + urlencode(params)
        headers = {
            "Accept": "application/vnd.github.raw+json" if raw else "application/vnd.github+json",
            "User-Agent": "actions-latest/0.3",
        }
        if self.token:
            headers["Authorization"] = "Bearer " + self.token
        for attempt in range(self.retries + 1):
            try:
                with urlopen(Request(url, headers=headers), timeout=self.timeout) as response:
                    body = response.read(2_000_001)
                    if len(body) > 2_000_000:
                        raise GitHubError("GitHub response exceeds 2 MB")
                    text = body.decode("utf-8")
                    return text if raw else json.loads(text)
            except HTTPError as exc:
                message = exc.read(65536).decode("utf-8", errors="replace").lower()
                if exc.code == 404:
                    raise NotFound("GitHub resource not found or inaccessible") from exc
                if exc.code == 429 or (
                    exc.code == 403
                    and (
                        exc.headers.get("X-RateLimit-Remaining") == "0"
                        or exc.headers.get("Retry-After")
                        or "rate limit" in message
                    )
                ):
                    self.rate_limited.set()
                    raise RateLimited(
                        "GitHub rate limit reached; retaining previous state"
                    ) from exc
                if exc.code in {401, 403}:
                    raise AuthenticationError(f"GitHub rejected access (HTTP {exc.code})") from exc
                if exc.code < 500:
                    raise GitHubError(f"GitHub request failed (HTTP {exc.code})") from exc
                failure = f"GitHub server error (HTTP {exc.code})"
            except (URLError, TimeoutError, ConnectionError) as exc:
                failure = f"GitHub transport failure ({type(exc).__name__})"
            except (ValueError, UnicodeError) as exc:
                raise GitHubError("GitHub returned an invalid response") from exc
            if attempt < self.retries:
                time.sleep(min(2**attempt, 4))
        raise TransientError(failure)

    def repository(self, repository: str) -> dict:
        data = self.request(f"/repos/{repository}")
        if not isinstance(data, dict) or "archived" not in data:
            raise GitHubError("Invalid repository response")
        return data

    def search_repositories(self, query: str, limit: int = 20) -> list[dict]:
        data = self.request(
            "/search/repositories",
            {"q": query, "sort": "updated", "order": "desc", "per_page": limit},
        )
        if not isinstance(data, dict) or not isinstance(data.get("items"), list):
            raise GitHubError("Invalid repository search response")
        if data.get("incomplete_results"):
            raise GitHubError("GitHub returned incomplete repository search results")
        return data["items"]

    def default_sha(self, repository: str, branch: str) -> str:
        data = self.request(f"/repos/{repository}/commits/{quote(branch, safe='')}")
        sha = data.get("sha") if isinstance(data, dict) else None
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise GitHubError("Invalid default-branch commit response")
        return sha

    def tags(self, repository: str) -> dict[str, str]:
        tags = {}
        for page in range(1, 51):
            data = self.request(f"/repos/{repository}/tags", {"per_page": 100, "page": page})
            if not isinstance(data, list):
                raise GitHubError("Invalid tags response")
            try:
                for tag in data:
                    tags[tag["name"]] = tag["commit"]["sha"]
            except (KeyError, TypeError) as exc:
                raise GitHubError("Invalid tag record") from exc
            if len(data) < 100:
                return tags
        raise GitHubError("Tag pagination exceeded 5,000 entries; refusing a partial observation")

    def is_prerelease(self, repository: str, tag: str) -> bool:
        try:
            data = self.request(f"/repos/{repository}/releases/tags/{quote(tag, safe='')}")
        except NotFound:
            return False  # Git tags need not have a GitHub Release.
        if not isinstance(data, dict) or not isinstance(data.get("prerelease"), bool):
            raise GitHubError("Invalid release response")
        return data["prerelease"] or bool(data.get("draft"))

    def manifest(self, action: str, sha: str) -> str:
        entry = CatalogEntry(action=action, description="")
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            raise ValueError("Manifest fetches require a full commit SHA")
        subpath = "/".join(action.split("/")[2:])
        for filename in ("action.yml", "action.yaml"):
            path = "/".join(filter(None, (subpath, filename)))
            try:
                return self.request(
                    f"/repos/{entry.repository}/contents/{quote(path, safe='/')}",
                    {"ref": sha},
                    raw=True,
                )
            except NotFound:
                continue
        raise NotFound(f"No action.yml or action.yaml at {action}@{sha}")
