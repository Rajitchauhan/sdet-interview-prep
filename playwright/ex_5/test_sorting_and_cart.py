from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def auth_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
     # Verify successful authentication
    expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
    return page 

def test_inventory(auth_page: Page):
    expect(auth_page.get_by_text("Products")).to_be_visible()


def test_select_product_sorting(auth_page: Page):
    # Sort products by Price (low to high)
    select = auth_page.locator(".product_sort_container")
    select.select_option(value="lohi")
    expect(select).to_have_value("lohi")
    prices = auth_page.locator(".inventory_item_price").all_text_contents()
    print("Prices after sorting (low to high):", prices)       
    prices_float = [float(price.replace("$", "")) for price in prices]
    assert prices_float == sorted(prices_float), "Prices are not sorted in ascending order"    

# def test_inventory(auth_page: Page):
#     expect(auth_page.get_by_text("Products")).to_be_visible()

#     product_card = auth_page.locator(
#         ".inventory_item"
#     ).filter(
#         has_text="Sauce Labs Backpack"
#     )

#     expect(
#         product_card.get_by_text("Sauce Labs Backpack")
#     ).to_be_visible()

#     expect(
#         product_card.get_by_text("$29.99")
#     ).to_be_visible()


def test_add_product_to_cart(auth_page: Page):
    product_card = auth_page.locator(
        ".inventory_item"
    ).filter(
        has_text="Sauce Labs Backpack"
    )

    product_card.get_by_role(
        "button",
        name="Add to cart"
    ).click()

    auth_page.get_by_role(
        "link",
        name="Shopping Cart"
    ).click()

    cart_item = auth_page.locator(
        ".cart_item"
    ).filter(
        has_text="Sauce Labs Backpack"
    )

    expect(
        cart_item.get_by_text("Sauce Labs Backpack")
    ).to_be_visible()

    expect(
        cart_item.get_by_text("$29.99")
    ).to_be_visible()


def test_product_details(auth_page: Page):
    auth_page.get_by_role(
        "link",
        name="Sauce Labs Backpack"
    ).click()

    expect(
        auth_page.get_by_text("Sauce Labs Backpack")
    ).to_be_visible()

    expect(
        auth_page.get_by_text("$29.99")
    ).to_be_visible()

    expect(
        auth_page.get_by_text(
            "carry.allTheThings() with the sleek, streamlined Sly Pack"
        )
    ).to_be_visible()


# prices = ["$2.99", "$3.22", "$1.98", "$10.50"]

# # key parameter har element ko evaluate karega float value par
# sorted_prices = sorted(prices, key=lambda x: float(x.replace("$", "")))

# print("Approach 1 Result:", sorted_prices)
# # Output: ['$1.98', '$2.99', '$3.22', '$10.50']

# prices = ["$2.99", "$3.22", "$1.98", "$10.50"]

# # x[1:] pehle character '$' ko chhod kar baaki string utha leta hai
# sorted_prices = sorted(prices, key=lambda x: float(x[1:]))

# print("Approach 2 Result:", sorted_prices)
# # Output: ['$1.98', '$2.99', '$3.22', '$10.50']





