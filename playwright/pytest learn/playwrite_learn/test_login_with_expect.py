from playwright.sync_api import expect


def test_login_with_expect(page):
    page.goto("https://www.saucedemo.com/")

    # User-facing locators
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # Web-First Assertions (Auto-retrying)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products") 