from playwright.sync_api import expect


def test_inventory_heading(auth_page):
    #  Products heading visible aur exact text verify karo.
    expect(auth_page.locator(".title")).to_be_visible()
    expect(auth_page.locator(".title")).to_have_text("Products")



def test_cart_visible(auth_page):
    #  Shopping Cart visible aur enabled verify karo.
    shoping_cart = auth_page.locator(".shopping_cart_link")
    expect(shoping_cart).to_be_visible()
    expect(shoping_cart).to_be_enabled()

def test_backpack_visible(auth_page):
    products = auth_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    product_name = products.locator(".inventory_item_name")
    expect(product_name).to_be_visible()
    price = products.locator(".inventory_item_price")
    expect(price).to_have_text("$29.99")
