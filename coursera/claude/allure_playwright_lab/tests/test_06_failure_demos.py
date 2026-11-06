import allure
import pytest
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

pytestmark = pytest.mark.demo_failure   # ye tests jaan-boojh ke fail hote hain


@allure.epic("ShopDemo")
@allure.feature("Failure evidence")
class TestFailureDemos:

    @allure.title("FAILED: cart badge galat count (BUG mode)")
    def test_assertion_failure(self, page: Page, base_url):
        login = LoginPage(page, base_url)
        login.open("/?bug=1")
        login.login("standard_user", "secret_sauce")
        inv = InventoryPage(page)
        inv.add_to_cart("Backpack")
        expect(inv.cart_count).to_have_text("1", timeout=2000)

    @allure.title("BROKEN: locator mila hi nahi (Timeout)")
    def test_broken_locator(self, page: Page, base_url):
        login = LoginPage(page, base_url)
        login.open()
        page.get_by_role("button", name="Button jo exist nahi karta").click(timeout=1500)

    @allure.title("FAILED in fixture (setup phase)")
    def test_setup_failure(self, page: Page, base_url, broken_fixture):
        pass

    @allure.title("SKIPPED: condition poori nahi")
    @pytest.mark.skip(reason="feature abhi ready nahi")
    def test_skipped(self):
        pass

    @allure.title("XFAIL: known bug (expected failure)")
    @pytest.mark.xfail(reason="BUG-123: known issue", strict=False)
    def test_known_bug(self):
        assert 1 + 1 == 3


@pytest.fixture
def broken_fixture(page: Page, base_url):
    page.goto(base_url)
    assert False, "login fixture hi toot gaya"
