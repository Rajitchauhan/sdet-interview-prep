import requests


class BaseApiClient:
    def __init__(self, base_url: str, token: str | None = None, timeout: float = 10):
        self._base_url = base_url.rstrip("/")
        self._timeout = timeout
        self._session = requests.Session()
        if token:
            self._session.headers["Authorization"] = f"Bearer {token}"

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        kwargs.setdefault("timeout", self._timeout)
        return self._session.request(method, f"{self._base_url}{path}", **kwargs)

    def close(self):
        self._session.close()
