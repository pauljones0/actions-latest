import io
import json
from email.message import Message
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError

import pytest
from conftest import SHA

from actions_latest.github import (
    AuthenticationError,
    GitHubClient,
    GitHubError,
    NotFound,
    RateLimited,
    TransientError,
)


def response(data):
    return io.BytesIO(json.dumps(data).encode())


def http_error(code, headers=None, message="failure"):
    values = Message()
    for key, value in (headers or {}).items():
        values[key] = value
    return HTTPError(
        "https://api.github.com/test",
        code,
        message,
        values,
        io.BytesIO(json.dumps({"message": message}).encode()),
    )


def test_transient_failure_retries_and_recovers():
    client = GitHubClient(token="", timeout=3, retries=2)
    with (
        patch(
            "actions_latest.github.urlopen",
            side_effect=[http_error(503), URLError("offline"), response({"ok": True})],
        ) as open_url,
        patch("actions_latest.github.time.sleep"),
    ):
        assert client.request("/test") == {"ok": True}
        assert open_url.call_count == 3
        assert all(call.kwargs["timeout"] == 3 for call in open_url.call_args_list)


def test_exhausted_retry_is_explicit():
    with (
        patch("actions_latest.github.urlopen", side_effect=URLError("offline")) as open_url,
        patch("actions_latest.github.time.sleep"),
    ):
        with pytest.raises(TransientError):
            GitHubClient(token="", retries=1).request("/test")
        assert open_url.call_count == 2


@pytest.mark.parametrize(
    "code,headers,message,error_type",
    [
        (404, {}, "missing", NotFound),
        (401, {}, "bad credentials", AuthenticationError),
        (403, {}, "forbidden", AuthenticationError),
        (403, {"X-RateLimit-Remaining": "0"}, "limit", RateLimited),
        (403, {}, "secondary rate limit", RateLimited),
        (429, {}, "limit", RateLimited),
    ],
)
def test_http_error_categories(code, headers, message, error_type):
    client = GitHubClient(token="")
    with patch(
        "actions_latest.github.urlopen", side_effect=http_error(code, headers, message)
    ) as open_url:
        with pytest.raises(error_type):
            client.request("/test")
        assert open_url.call_count == 1
        if error_type is RateLimited:
            with pytest.raises(RateLimited):
                client.request("/test")
            assert open_url.call_count == 1


def test_invalid_json_is_not_missing():
    with patch("actions_latest.github.urlopen", return_value=io.BytesIO(b"not json")):
        with pytest.raises(GitHubError, match="invalid response"):
            GitHubClient(token="").request("/test")


def test_tag_pagination_and_partial_failure():
    client = GitHubClient(token="")
    first = [{"name": f"v1.0.{i}", "commit": {"sha": SHA}} for i in range(100)]
    client.request = Mock(side_effect=[first, [{"name": "v2", "commit": {"sha": SHA}}]])
    assert len(client.tags("owner/repo")) == 101
    assert client.request.call_args.args[1]["page"] == 2
    client.request = Mock(side_effect=[first, TransientError("page two failed")])
    with pytest.raises(TransientError):
        client.tags("owner/repo")


def test_manifest_subpath_sha_and_yaml_fallback():
    client = GitHubClient(token="")
    client.request = Mock(side_effect=[NotFound("no yml"), "name: manifest"])
    assert client.manifest("owner/repo/setup", SHA) == "name: manifest"
    assert client.request.call_args.args == (
        "/repos/owner/repo/contents/setup/action.yaml",
        {"ref": SHA},
    )
    assert client.request.call_args.kwargs == {"raw": True}
    with pytest.raises(ValueError, match="SHA"):
        client.manifest("owner/repo", "main")
    client.request = Mock(side_effect=TransientError("offline"))
    with pytest.raises(TransientError):
        client.manifest("owner/repo", SHA)
    assert client.request.call_count == 1


def test_request_encoding_and_token_stays_in_header():
    client = GitHubClient(token="test-token")
    with patch("actions_latest.github.urlopen", return_value=response({})) as open_url:
        client.request("/test", {"ref": "release/v1 + x"})
    request = open_url.call_args.args[0]
    assert request.get_header("Authorization") == "Bearer test-token"
    assert "test-token" not in request.full_url
    assert "ref=release%2Fv1+%2B+x" in request.full_url


def test_rate_limit_preserves_authoritative_reset_for_later_skipped_requests():
    from datetime import timedelta

    from conftest import NOW

    reset = NOW + timedelta(minutes=10)
    client = GitHubClient(token="")
    with patch(
        "actions_latest.github.urlopen",
        side_effect=http_error(
            403, {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": str(int(reset.timestamp()))}
        ),
    ) as request:
        messages = []
        for path in ("/first", "/skipped"):
            with pytest.raises(RateLimited) as failure:
                client.request(path)
            messages.append(str(failure.value))
        assert messages[0] == messages[1]
        assert reset.replace(microsecond=0).isoformat() in messages[0]
        request.assert_called_once()
