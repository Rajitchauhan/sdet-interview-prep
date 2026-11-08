"""API layer: har API client ka base."""
import requests

from framework.core.logger import get_logger

log = get_logger("api")


class BaseApiClient:
    def __init__(self, base_url: str, timeout: float, token: str | None = None):
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._session = requests.Session()
        if token:
            self._session.headers["Authorization"] = f"Bearer {token}"

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)        # timeout hamesha
        response = self._session.request(method, f"{self._base_url}{path}", **kwargs)
        log.info("%s %s -> %s", method.upper(), path, response.status_code)  # body/headers nahi (secrets)
        return response

    def close(self):
        self._session.close()
