

from playwright import Page  , expect

def test_product(page : Page):
    page.get_by_placeholder("Search").fill("iPhone 15")
    page.get_by_role("button", name="Search").click()


    product_card = page.locator(".product-card", has_text="iPhone 15")
    expect(product_card.get_by_text("iPhone 15")).to_be_visible()
    expect(product_card.locator(".price")).to_have_text("$799")
    product_card.get_by_role("button", name="Add to Cart").click()
    expect(product_card).to_have_count(1)
