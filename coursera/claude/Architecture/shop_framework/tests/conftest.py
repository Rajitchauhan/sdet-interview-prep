"""FIXTURES layer: framework ke saare layers ko tests se jodta hai (wiring)."""
import json

import pytest
from playwright.sync_api import expect

from framework.api.auth_api import AuthApi
from framework.api.shop_api import ShopApi
from framework.config.settings import Settings, get_settings
from framework.data.users import User, get_user
from framework.pages.inventory_page import InventoryPage

_FOLDER_MARKERS = ("ui", "api", "hybrid", "architecture")


def pytest_collection_modifyitems(items):
    """Folder ke naam se marker apne aap: tests/ui/... -> @pytest.mark.ui"""
    for item in items:
        parts = set(item.path.parts)
        for name in _FOLDER_MARKERS:
            if name in parts:
                item.add_marker(getattr(pytest.mark, name))


# ---------- config ----------
@pytest.fixture(scope="session")
def settings() -> Settings:
    return get_settings()


@pytest.fixture(scope="session")
def base_url(settings: Settings) -> str:
    """pytest-playwright ka base_url fixture override: page.goto('/') isi URL par jaayega."""
    return settings.base_url


@pytest.fixture(scope="session", autouse=True)
def _expect_timeout(settings: Settings):
    expect.set_options(timeout=settings.ui_timeout_ms)


@pytest.fixture(autouse=True)
def _page_timeout(request, settings: Settings):
    if "page" in request.fixturenames:
        request.getfixturevalue("page").set_default_timeout(settings.ui_timeout_ms)


# ---------- data ----------
@pytest.fixture
def user() -> User:
    return get_user("standard")


# ---------- API ----------
@pytest.fixture
def auth_api(settings: Settings):
    client = AuthApi(settings.api_url, settings.api_timeout_s)
    yield client
    client.close()


@pytest.fixture
def api_token(auth_api: AuthApi, user: User) -> str:
    """Har test ko apna token (apna cart) => tests ek doosre se independent."""
    return auth_api.get_token(user)


@pytest.fixture
def shop_api(settings: Settings, api_token: str):
    client = ShopApi(settings.api_url, settings.api_timeout_s, token=api_token)
    yield client
    client.clear_cart()          # cleanup: test ne cart gandha kiya ho to saaf
    client.close()


# ---------- UI (logged in) ----------
@pytest.fixture
def authenticated_page(page, api_token: str):
    """Login UI se nahi, API se. Token browser ke localStorage me har navigation par daal do."""
    page.add_init_script(f"window.localStorage.setItem('token', {json.dumps(api_token)});")
    return page


@pytest.fixture
def inventory_page(authenticated_page) -> InventoryPage:
    return InventoryPage(authenticated_page).open()
