import json

import pytest

from api.auth_api import AuthApi
from api.shop_api import ShopApi
from data.users import User, get_user
from pages.inventory_page import InventoryPage


@pytest.fixture
def user() -> User:
    return get_user("standard")


@pytest.fixture
def api_token(base_url, user) -> str:
    client = AuthApi(base_url)
    try:
        return client.get_token(user)
    finally:
        client.close()


@pytest.fixture
def shop_api(base_url, api_token):
    client = ShopApi(base_url, token=api_token)
    yield client
    client.clear_cart()
    client.close()


@pytest.fixture
def authenticated_page(page, api_token):
    page.add_init_script(f"window.localStorage.setItem('token', {json.dumps(api_token)});")
    return page


@pytest.fixture
def inventory_page(authenticated_page) -> InventoryPage:
    return InventoryPage(authenticated_page).open()
