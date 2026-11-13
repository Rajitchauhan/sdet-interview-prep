from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    expect(inventory.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    expect(inventory.cart_badge).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page)
    login.open()
    inventory = login.login_as("standard_user", "secret_sauce")
    inventory.add_to_cart("Backpack")
    cart = inventory.open_cart()
    done = cart.checkout()
    expect(done.heading).to_be_visible()
