from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage



def test_inventory_page(auth_page):
    inventory_page = InventoryPage(auth_page)
    expect(auth_page).to_have_title("Swag Labs")
    expect(inventory_page.page.get_by_role("heading", name="Products")).to_be_visible()
    expect(inventory_page.get_product_name("Sauce Labs Backpack")).to_be_visible()
    expect(inventory_page.get_product_price("Sauce Labs Backpack")).to_have_text("$29.99")
   
def test_authenticated_user_can_access_inventory(auth_page):
    inventory_page = InventoryPage(auth_page)
    expect(auth_page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(auth_page).to_have_title("Swag Labs")
    expect(inventory_page.page.get_by_role("heading", name="Products")).to_be_visible()

def test_product_can_be_added_to_cart(auth_page):

    inventory_page = InventoryPage(auth_page)

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = inventory_page.go_to_cart()

    expect(
        cart_page.get_cart_item_by_name("Sauce Labs Backpack")
    ).to_be_visible()

    expect(
        cart_page.get_cart_item_price("Sauce Labs Backpack")
    ).to_have_text("$29.99")


def test_user_can_complete_checkout(auth_page):

    inventory_page = InventoryPage(auth_page)

    # Add product
    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    # Go to cart
    cart_page = inventory_page.go_to_cart()

    # Validate cart
    expect(
        cart_page.get_cart_item_by_name("Sauce Labs Backpack")
    ).to_be_visible()

    expect(
        cart_page.get_cart_item_price("Sauce Labs Backpack")
    ).to_have_text("$29.99")

    # Checkout
    checkout_page = cart_page.go_to_checkout()

    checkout_page.fill_checkout_information(
        "Rajit",
        "Chauhan",
        "263..."
    )

    checkout_page.continue_to_overview()

    # Overview validations...