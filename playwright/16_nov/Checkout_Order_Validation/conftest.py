from login_helper import login 
from playwright.sync_api import Page  , expect
import pytest 

@pytest.fixture
def auth_page(page:Page):
    login( page, "standard_user" , "secret_sauce" )
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_title("Swag Labs")
    return page