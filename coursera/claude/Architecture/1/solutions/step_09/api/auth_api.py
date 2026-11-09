import requests

from api.base_client import BaseApiClient
from data.users import User


class AuthApi(BaseApiClient):
    def login(self, username: str, password: str) -> requests.Response:
        return self.request("POST", "/api/login", json={"username": username, "password": password})

    def get_token(self, user: User) -> str:
        response = self.login(user.username, user.password)
        response.raise_for_status()
        return response.json()["token"]
