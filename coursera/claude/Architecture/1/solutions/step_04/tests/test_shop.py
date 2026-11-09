from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.order_complete_page import OrderCompletePage


def test_login_works(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    InventoryPage(page).wait_until_loaded()


def test_wrong_password_shows_error(page):
    login = LoginPage(page).open()
    login.login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page).open()
    login.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page).wait_until_loaded()
    inventory.add_to_cart("Backpack")
    inventory.open_cart()
    CartPage(page).wait_until_loaded().checkout()
    done = OrderCompletePage(page)
    expect(done.heading).to_be_visible()
