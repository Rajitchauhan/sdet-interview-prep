from playwright.sync_api import Page, expect

def test_product_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_label("Email").fill("testuser@example.com")
    page.get_by_label("Password").fill("Test@123")
    page.get_by_role("button" , name='Login').click()

    expect(page.get_by_text("Dashboard")).to_be_visible()

    