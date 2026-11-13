from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login_works(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_wrong_password_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong-password")
    expect(page.get_by_role("alert")).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.get_by_test_id("cart-count")).to_have_text("1")


def test_user_can_buy_backpack(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    page.get_by_role("button", name="View Cart").click()
    expect(page.get_by_role("heading", name="Your Cart")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
