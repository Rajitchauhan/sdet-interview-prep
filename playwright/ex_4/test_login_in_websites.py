import pytest
from playwright.sync_api import Page, expect


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

    product_card = auth_page.locator(
        ".inventory_item"
    ).filter(
        has_text="Sauce Labs Backpack"
    )

    expect(
        product_card.get_by_text("Sauce Labs Backpack")
    ).to_be_visible()

    expect(
        product_card.get_by_text("$29.99")
    ).to_be_visible()


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





















# from playwright.sync_api import Page, sync_playwright , expect 
# import pytest
# # def test_login():
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=False, slow_mo=500)
# #         context = browser.new_context()
# #         page = context.new_page()
# #         page.goto("https://www.saucedemo.com/")

# #         expect(page.get_by_text("Swag Labs")).to_be_visible()

# #         page.get_by_placeholder("Username").fill("standard_user")
# #         page.get_by_placeholder("Password").fill("secret_sauce")    
# #         page.get_by_role("button", name="Login").click()

# #         # context.storage_state(path="state.json") abhi iski need nhi hai

       
# #         browser.close()

# # def test_invetry(page:Page):
# #     pass

# @pytest.fixture
# def auth_page(page: Page):
#     page.goto("https://www.saucedemo.com/")
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")    
#     page.get_by_role("button", name="Login").click()   

#     expect(page).to_have_url(
#         "https://www.saucedemo.com/inventory.html"
#     )

#     return page

# def test_inventory(auth_page):
#     expect(auth_page.get_by_text("Products")).to_be_visible()
#     product_card = auth_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
#     expect(product_card.get_by_text("Sauce Labs Backpack")).to_be_visible()
#     expect(product_card.get_by_text("$29.99")).to_be_visible()
#     product_card.get_by_role("button", name="Add to cart").click()




