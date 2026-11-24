from playwright.sync_api import Page, expect

def test_add_remove_cart(auth_page: Page):
    product_card = auth_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    product_card.get_by_role("button", name="Add to cart").click()
    expect(auth_page.locator(".shopping_cart_badge")).to_have_text("1")
    product_card.get_by_role("button", name="Remove").click() 
    expect(product_card.get_by_role("button", name="Add to cart")).to_be_visible()
    expect(auth_page.locator(".shopping_cart_badge")).to_be_hidden()

