from pages.login_page import LoginPage

def test_login_as_with_wrong_password(page):
    LoginPage(page).open().login_as("standard_user", "wrong-password")
