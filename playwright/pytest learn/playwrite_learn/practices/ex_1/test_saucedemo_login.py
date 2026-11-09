from playwright.async_api import Page , expect

def test_saucedemo_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    # standard_user aur Password secret_sauce fill karo.
    page.get_by_role("button" , name="Login").click()

    page.get_by_role("heading" , name="???")
