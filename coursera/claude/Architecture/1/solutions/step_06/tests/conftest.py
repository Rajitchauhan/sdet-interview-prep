import pytest

from data.users import User, get_user
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def user() -> User:
    return get_user("standard")


@pytest.fixture
def inventory_page(page, user) -> InventoryPage:
    LoginPage(page).open().login(user.username, user.password)
    return InventoryPage(page).wait_until_loaded()
