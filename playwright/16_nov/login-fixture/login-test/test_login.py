from playwright.sync_api import expect , Page
import pytest

def login(page: Page, username: str, password: str):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button" , name="Login").click()

@pytest.fixture
def auth_page(page:Page):
    login(page , "standard_user" , "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
    return page 


def test_inventory_heading(auth_page):
    #Products heading visible
    expect(auth_page.locator(".title")).to_be_visible()
    expect(auth_page.locator(".title")).to_have_text("Products")

def test_backpack_visible(auth_page):
    #Sauce Labs Backpack visible
    #Sauce Labs Backpack product visible hai.
    # Us product ki price $29.99 hai.
        
    products = auth_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    product_name = products.locator(".inventory_item_name")
    expect(product_name).to_be_visible()
    price = products.locator(".inventory_item_price")
    expect(price).to_have_text("$29.99")


def test_cart_visible(auth_page):
    #Shopping cart link visible
    # Shopping Cart link visible hai.
    # Link enabled hai
    shoping_cart = auth_page.locator(".shopping_cart_link")
    expect(shoping_cart).to_be_visible()
    expect(shoping_cart).to_be_enabled()

    