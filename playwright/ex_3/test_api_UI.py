import requests , pytest
from playwright.sync_api import Page, expect

@pytest.fixture
def post_order_request():
    url = "api/orders"

    payload = {
        "customer": "Rajit",
        "product": "iPhone 15",
        "quantity": 2,
        "price": 799
        }
    response = requests.post(url , json=payload)
    assert response.status_code == 201
    data = response.json()
    order_id = data['order_id']

    return order_id


def test_login(page:Page):
    page.goto("https://example.com/login")

    page.get_by_placeholder("Username").fill("testuser")
    page.get_by_placeholder("Password").fill("password123")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("dashboard")).to_be_visible()

def test_navigate_to_orders(page:Page):
    page.goto("https://example.com/dashboard")

    page.get_by_role("link", name="Orders").click()

    expect(page.get_by_text("Orders List")).to_be_visible()


def test_verify_order_in_ui(page:Page , post_order_request):
    page.goto("https://example.com/orders")

    order_id = post_order_request
    expect(page.get_by_text(order_id)).to_be_visible()
    page.get_by_text(order_id).click()
    
    expect(page.get_by_text("Rajit")).to_be_visible()
    expect(page.get_by_text("iPhone 15")).to_be_visible()
    expect(page.get_by_text("2")).to_be_visible()
    expect(page.get_by_text("$799")).to_be_visible()     


        