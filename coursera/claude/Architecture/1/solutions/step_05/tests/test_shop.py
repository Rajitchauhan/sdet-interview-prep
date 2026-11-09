from dataclasses import replace

from playwright.sync_api import expect

from data.products import BACKPACK
from data.users import get_user
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page):
    bad_user = replace(get_user("standard"), password="wrong-password")
    login = LoginPage(page).open()
    login.login(bad_user.username, bad_user.password)
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart(BACKPACK.name)
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    user = get_user("standard")
    login = LoginPage(page).open()
    login.login(user.username, user.password)
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart(BACKPACK.name)
    inventory.open_cart()
    CartPage(page).wait_until_loaded().checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
