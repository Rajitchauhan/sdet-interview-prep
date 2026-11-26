# TC-01: Checkout navigation
# 1. auth_page fixture se login karo.
# 2. Sauce Labs Backpack cart mein add karo.
# 3. Shopping cart open karo.
# 4. Checkout click karo.

from playwright.sync_api import expect

def test_checkout_navigate(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    
    auth_page.locator(".shopping_cart_link").click() 

    cart_footer = auth_page.locator(".cart_footer")
    cart_footer.get_by_role("button" , name="Checkout").click()
    
    # 👇 Final Validation: वेरिफाई करें कि सही पेज और हेडिंग लोड हुई है
    expect(auth_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
   
   #First Name, Last Name aur Zip/Postal Code fields visible hon.
    form_group = auth_page.locator(".form_group")
    
    first_name = form_group.get_by_placeholder("First Name")
    expect(first_name).to_be_visible()
    
    last_name = form_group.get_by_placeholder("last name")
    expect(last_name).to_be_visible()
    
    zip_code = form_group.get_by_placeholder("Zip/Postal Code")
    expect(zip_code).to_be_visible()
    
    


# TC-02: Checkout information submission
# 1. Backpack cart mein add karo.
# 2. Checkout Information page par jao.
# 3. Details fill karo:
#    - First Name: Rajit
#    - Last Name: Chauhan
#    - Zip Code: 282001
# 4. Continue click karo.


# Checkout Overview page open ho.
# Backpack visible ho.
# Price   $29.99 ho.
    

def test_checkout(auth_page):
    product_item = auth_page.locator(".inventory_item")
    product_item.filter(has_text="Sauce Labs Backpack").get_by_role("button" , name="Add to cart").click()
    
    auth_page.locator(".shopping_cart_link").click() 

    cart_footer = auth_page.locator(".cart_footer")
    cart_footer.get_by_role("button" , name="Checkout").click()
    
    expect(auth_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
       
   
    #First Name, Last Name aur Zip/Postal Code fields visible hon.
    form_group = auth_page.locator(".form_group")
        
    form_group.get_by_placeholder("First Name").fill("Rajit")
    form_group.get_by_placeholder("last name").fill("Chauhan")
    form_group.get_by_placeholder("Zip/Postal Code").fill("282001")
    
    checkout = auth_page.locator(".checkout_buttons")
    checkout.get_by_role("button" , name="Continue").click()
    
    # 2. Backpack visible ho & 3. Price $29.99 ho
    overview_item = auth_page.locator(".cart_item").filter(has_text="Sauce Labs Backpack")
    expect(overview_item.locator(".inventory_item_name")).to_be_visible()
    expect(overview_item.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
    expect(overview_item.locator(".inventory_item_price")).to_have_text("$29.99")
  