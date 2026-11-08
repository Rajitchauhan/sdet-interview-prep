import allure
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

pytestmark = pytest.mark.demo_flaky


@allure.epic("ShopDemo")
@allure.feature("Reliability")
@allure.title("Flaky demo: pehli baar fail, retry par pass")
def test_flaky_first_attempt_fails(request, page: Page, base_url):
    LoginPage(page, base_url).open()
    # pytest-rerunfailures har run par execution_count badhata hai (1, 2, ...)
    if request.node.execution_count == 1:
        expect(page.get_by_role("heading", name="Ye heading exist nahi karti")).to_be_visible(timeout=800)
    expect(page.get_by_role("heading", name="Login")).to_be_visible()
