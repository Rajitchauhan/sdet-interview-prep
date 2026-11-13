from playwright.sync_api import expect


def test_login_works(inventory_page):
    expect(inventory_page.cart_badge).to_have_text("0")


def test_wrong_password_shows_error(login_page):
    login_page.attempt_login("standard_user", "wrong-password")
    expect(login_page.error).to_have_text("Username and password do not match")


def test_add_to_cart_updates_badge(inventory_page):
    inventory_page.product("Backpack").add_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")


def test_product_card_shows_price_and_toggles_button(inventory_page):
    backpack = inventory_page.product("Backpack")
    expect(backpack.price).to_have_text("$29.99")
    expect(backpack.action_button).to_have_text("Add to cart")
    backpack.add_to_cart()
    expect(backpack.action_button).to_have_text("Remove")


def test_products_are_listed_alphabetically(inventory_page):
    expect(inventory_page.names).to_have_text(["Backpack", "Bike Light", "Onesie"])


def test_user_can_buy_backpack(inventory_page):
    inventory_page.product("Backpack").add_to_cart()
    done = inventory_page.open_cart().checkout()
    expect(done.heading).to_be_visible()
