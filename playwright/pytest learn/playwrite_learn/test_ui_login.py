# test_ui_login.py


def test_saucedemo_valid_login(page):
    # 1. Action: Website open karo
    page.goto("https://www.saucedemo.com/")

    # 2. Action: Credentials fill karo
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # 3. Action: Login button click karo
    page.locator("#login-button").click()

    # 4. Assertions: Verify URL & Dashboard Header
    assert "inventory.html" in page.url
    header_text = page.locator(".title").text_content()
    assert header_text == "Products"
    