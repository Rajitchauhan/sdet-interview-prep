from playwright.sync_api import expect


def test_login_works(page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def test_add_to_cart_updates_badge(page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.get_by_test_id("cart-count")).to_have_text("1")


def test_user_can_buy_backpack(page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()
    page.get_by_test_id("product").filter(has_text="Backpack").get_by_role("button", name="Add to cart").click()
    page.get_by_role("button", name="View Cart").click()
    expect(page.get_by_role("heading", name="Your Cart")).to_be_visible()
    page.get_by_role("button", name="Checkout").click()
    expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()
