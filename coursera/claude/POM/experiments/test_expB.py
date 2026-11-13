import time
from playwright.sync_api import expect
from pages.login_page import LoginPage

def _slow_login(page):
    def handler(route):
        time.sleep(0.5)
        route.continue_()
    page.route("**/api/login", handler)

def test_plain_assert_on_inner_text(page):
    _slow_login(page)
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    assert login.error.inner_text() == "Username and password do not match"

def test_expect_on_locator(page):
    _slow_login(page)
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Username and password do not match")

def test_expect_wrong_text_message(page):
    login = LoginPage(page).open()
    login.attempt_login("standard_user", "wrong-password")
    expect(login.error).to_have_text("Kuch aur likha hai", timeout=1500)
