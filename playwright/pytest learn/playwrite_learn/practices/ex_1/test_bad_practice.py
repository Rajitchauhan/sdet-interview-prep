from playwright.async_api import Page  , expect
import time

# Is bad code ko theek karna hai:
def test_bad_practice(page:Page):
    page.goto("https://www.saucedemo.com/")
    time.sleep(5)
    page.locator("#user-name").fill("standard_user")
    time.sleep(2)
    page.locator("#login-button").click()
    time.sleep(5)
    assert page.title() == "Swag Labs"

def test_good_practice(page):
    page.goto("https://www.saucedemo.com/") 
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_role("button" , name="Login").click() 
    expect('title').to_have("Swag Labs")
