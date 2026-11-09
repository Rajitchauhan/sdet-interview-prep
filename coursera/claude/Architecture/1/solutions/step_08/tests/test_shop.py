from dataclasses import replace

import pytest
from playwright.sync_api import expect

from data.products import ALL_PRODUCTS, BACKPACK, ONESIE
from flows.shopping_flow import ShoppingFlow
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_works(page, user):
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page, user):
    bad_user = replace(user, password="wrong-password")
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(inventory_page):
    inventory_page.add_to_cart(BACKPACK.name)
    expect(inventory_page.cart_badge).to_have_text("1")


@pytest.mark.parametrize("product", ALL_PRODUCTS, ids=lambda p: p.id)
def test_user_can_buy_each_product(page, inventory_page, product):
    done = ShoppingFlow(page).buy(inventory_page, [product.name])
    expect(done.heading).to_be_visible()


def test_user_can_buy_two_products(page, inventory_page):
    done = ShoppingFlow(page).buy(inventory_page, [BACKPACK.name, ONESIE.name])
    expect(done.heading).to_be_visible()
