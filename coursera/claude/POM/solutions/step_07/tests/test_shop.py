from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    expect(inventory.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(page):
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    expect(inventory.cart_badge).to_have_text("1")


def test_product_card_shows_price_and_toggles_button(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    backpack = inventory.product("Backpack")
    expect(backpack.price).to_have_text("$29.99")
    expect(backpack.action_button).to_have_text("Add to cart")
    backpack.add_to_cart()
    expect(backpack.action_button).to_have_text("Remove")


def test_products_are_listed_alphabetically(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    expect(inventory.names).to_have_text(["Backpack", "Bike Light", "Onesie"])


def test_user_can_buy_backpack(page):
    inventory = LoginPage(page).open().login_as("standard_user", "secret_sauce")
    inventory.product("Backpack").add_to_cart()
    done = inventory.open_cart().checkout()
    expect(done.heading).to_be_visible()
