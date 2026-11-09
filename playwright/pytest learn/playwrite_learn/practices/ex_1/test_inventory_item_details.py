from playwright.sync_api import Page , expect


# def test_inventory_item_details(page: Page):
#     page.goto("https://www.saucedemo.com/")

#     # standard_user / secret_sauce
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")

#     page.get_by_role("button" , name="Login").click() 

#     # ele = page.get_by_role("link", name="Sauce Labs Backpack")
#     # ele.click()

#     # bt = page.get_by_role("button" , name="Add to cart")
#     # expect(bt).to_be_visible()
#     # page.get_by_text("Sauce Labs Backpack")

#     # 1. Product link pe click kiya
#     product_link = page.get_by_role("link", name="Sauce Labs Backpack")
#     product_link.click()

#     # 2. Details page par Add to cart button verify kiya
#     btn_add_to_cart = page.get_by_role("button", name="Add to cart")
#     expect(btn_add_to_cart).to_be_visible()
    

from playwright.sync_api import Page, expect

def test_inventory_item_details(page: Page):
    page.goto("https://www.saucedemo.com/")

    # Login
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click() 

    # Solution 1: Direct unique text pe click karo
    page.get_by_text("Sauce Labs Backpack").click()

    # Product details page par assertions
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    expect(page.get_by_role("button", name="Add to cart")).to_be_visible()
