from playwright.sync_api import expect , Page

def test_login(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button" , name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
   


def test_invalid_username(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button" , name="Login").click()
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_have_text("Epic sadface: Username and password do not match any user in this service") 

    expect(page).to_have_url("https://www.saucedemo.com/")




def test_invalid_password(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_sauce")

    page.get_by_role("button" , name="Login").click()

    error = page.locator("[data-test='error']")

    expect(error).to_be_visible()
    expect(error).to_have_text(
    "Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url("https://www.saucedemo.com/")


def test_locked_user(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button" , name="Login").click()
    
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_empty_username(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button" , name="Login").click()
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()

    expect(error).to_contain_text("Epic sadface: Username is required")
    expect(page).to_have_url("https://www.saucedemo.com/")

def test_empty_password(page : Page):

    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("")

    page.get_by_role("button" , name="Login").click()
    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()

    expect(error).to_contain_text("Epic sadface: Password is required")
    expect(page).to_have_url("https://www.saucedemo.com/")









