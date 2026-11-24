from playwright.sync_api import Page , expect

def login(page:Page ,username: str, password: str):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button" , name="Login").click()