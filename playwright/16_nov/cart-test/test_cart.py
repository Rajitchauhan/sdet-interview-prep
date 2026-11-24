from playwright.sync_api import expect

def test_add_cart(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    product_item.filter(has_text="Sauce Labs Bike Light").get_by_role("button" , name="Add to cart").click()

    shopping_cart = auth_page.locator(".shopping_cart_link")
    expect(shopping_cart).to_have_text("2")

def test_cart_product(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    product_item.filter(has_text="Sauce Labs Bike Light").get_by_role("button" , name="Add to cart").click()

    auth_page.locator(".shopping_cart_link").click()
    
    cart_item = auth_page.locator(".cart_item")


    backpack = cart_item.filter(has_text="Sauce Labs Backpack")
    cart_item_name = backpack.locator(".inventory_item_name")
    cart_item_price = backpack.locator(".inventory_item_price")
    qty = backpack.locator(".cart_quantity")

    expect(cart_item_name).to_have_text("Sauce Labs Backpack")
    expect(cart_item_price).to_have_text("$29.99")
    expect(qty).to_have_text("1")

    bikelight = cart_item.filter(has_text="Sauce Labs Bike Light")
    cart_item_name =  bikelight.locator(".inventory_item_name")
    cart_item_price =  bikelight.locator(".inventory_item_price")
    qty = bikelight.locator(".cart_quantity")

    expect(cart_item_name).to_have_text("Sauce Labs Bike Light")
    expect(cart_item_price).to_have_text("$9.99")
    expect(qty).to_have_text("1")


def test_remove_cart_product(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    product_item.filter(has_text="Sauce Labs Bike Light").get_by_role("button" , name="Add to cart").click()
    
    auth_page.locator(".shopping_cart_link").click()
    
    cart_item = auth_page.locator(".cart_item")
    backpack = cart_item.filter(has_text="Sauce Labs Backpack")
    backpack.get_by_role("button" , name="Remove").click()
    
    expect(backpack).to_have_count(0)
    
    # 5. Bike Light present rehna chahiye
    bike_light = cart_item.filter(has_text="Sauce Labs Bike Light")
    expect(bike_light).to_be_visible()
    expect(bike_light.locator(".inventory_item_name")).to_have_text("Sauce Labs Bike Light")

    # 6. Cart badge 1 hona chahiye (isi page par upar dikhta hai)
    expect(auth_page.locator(".shopping_cart_badge")).to_have_text("1")
    
   
def test_continue_shopping(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    product_item.filter(has_text="Sauce Labs Bike Light").get_by_role("button" , name="Add to cart").click()
    
    auth_page.locator(".shopping_cart_link").click()
    
    cart_footer = auth_page.locator(".cart_footer")
    cart_footer.get_by_role("button" , name="Continue Shopping").click()
    
    expect(auth_page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    
