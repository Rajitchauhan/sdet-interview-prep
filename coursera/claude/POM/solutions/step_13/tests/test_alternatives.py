import pytest
from playwright.sync_api import expect

from alternatives.app import ShopApp
from alternatives.functional_helpers import add_to_cart, cart_badge, login
from alternatives.screenplay import Actor, AddToCart, CartBadge, Login


def test_alt_plain_functions(page):
    login(page, "standard_user", "secret_sauce")
    add_to_cart(page, "Backpack")
    expect(cart_badge(page)).to_have_text("1")


def test_alt_screenplay_lite(page):
    asha = Actor("Asha", page)
    asha.attempts_to(Login("standard_user", "secret_sauce"), AddToCart("Backpack"))
    expect(asha.sees(CartBadge())).to_have_text("1")


@pytest.fixture
def app(page) -> ShopApp:
    return ShopApp(page)


def test_alt_app_facade(app):
    inventory = app.login.open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    expect(inventory.cart_badge).to_have_text("1")
