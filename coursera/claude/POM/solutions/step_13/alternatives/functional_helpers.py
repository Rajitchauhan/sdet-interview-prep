from playwright.sync_api import Locator, Page, expect


def login(page: Page, username: str, password: str) -> None:
    page.goto("/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading", name="Products")).to_be_visible()


def add_to_cart(page: Page, product_name: str) -> None:
    card = page.get_by_test_id("product").filter(has_text=product_name)
    card.get_by_role("button", name="Add to cart").click()


def cart_badge(page: Page) -> Locator:
    return page.get_by_test_id("cart-count")
