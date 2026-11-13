import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.playground_page import PlaygroundPage

# Demo credentials. Asli project me password environment variable se lo.
STANDARD_USER = ("standard_user", "secret_sauce")


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page).open()


@pytest.fixture
def inventory_page(login_page) -> InventoryPage:
    username, password = STANDARD_USER
    return login_page.login_as(username, password)


@pytest.fixture
def playground(page) -> PlaygroundPage:
    return PlaygroundPage(page).open()
