from playwright.sync_api import Page , expect

# Ek test function likho test_sort_price_high_to_low(page: Page):

# [https://www.saucedemo.com/](https://www.saucedemo.com/)
#  open karo aur standard_user / secret_sauce se login karo.

# Product sort dropdown ([data-test="product-sort-container"])
#  ko select karo using label: "Price (high to low)" (iski value "hilo" hoti hai).

# Verify karo ki dropdown ki value "hilo" ho chuki hai.

# Verify karo ki pehle product ka title 
# (page.locator(".inventory_item_name").first) 
# "Sauce Labs Fleece Jacket" hai ($49.99 wala).


def test_sort_price_high_to_low(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button" , name="Login").click()

    dropdown = page.locator("[data-test='product-sort-container']")
    dropdown.select_option(label="Price (high to low)")
    expect(dropdown).to_have_value("hilo")

    title = page.locator(".inventory_item_name").first
    expect(title).to_have_text("Sauce Labs Fleece Jacket")


# Internet practice site
#  [https://the-internet.herokuapp.com/checkboxes](https://the-internet.herokuapp.com/checkboxes) par:

# Page open karo.

# Page par 2 checkboxes hain (page.locator("input[type='checkbox']")).

# Pehle checkbox ko .check() karo aur verify karo ki woh checked ho gaya (to_be_checked()).

# Dusre checkbox ko .uncheck() karo aur verify karo ki woh unchecked ho gaya (not_to_be_checked()).

def test_checkbox(page:Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")

    checkbox = page.locator("checkbox" , name="checkbox 1")

    expect(checkbox).not_to_be_checked()
    
    # checkbox = page.get_by_role("checkbox" , name="checkbox 1")
    # checkbox.set_checked(False)