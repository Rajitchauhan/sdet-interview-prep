from playwright.sync_api import Page, expect

def test_product_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_label("Email").fill("testuser@example.com")
    page.get_by_label("Password").fill("Test@123")
    page.get_by_role("button" , name='Login').click()

    expect(page.get_by_text("Dashboard")).to_be_visible()

    page.get_by_placeholder("Search").fill("iPhone 15")
    page.get_by_role("button", name="Search").click()

    product_card = page.locator(".product-card").filter(has_text="iPhone 15")

    expect(product_card.locator(".product-name")).to_have_text("iPhone 15")
    expect(product_card.locator(".product-price")).to_have_text("$799")

    product_card.get_by_role("button", name="Add to Cart").click()

    page.get_by_role("link", name="Shopping Cart").click()

    product_items = page.locator(".cart-item").filter(has_text="iPhone 15")
    expect(product_items.locator(".product-name")).to_have_text("iPhone 15")
    expect(product_items.locator(".price")).to_have_text("$799")

