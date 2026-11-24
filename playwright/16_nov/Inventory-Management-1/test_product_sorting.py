from playwright.sync_api import expect , Page

def test_product_sorting(auth_page):
    sort_dropdown = auth_page.locator(".product_sort_container")
    sort_dropdown.select_option(value="lohi")
    expect(sort_dropdown).to_have_value("lohi")

    price_text = auth_page.locator(".inventory_item_price").all_inner_texts()

    #pure python hai , expect() PW ka feature hai and assert pytest python ka 
    prices = [ float(p.replace("$" , "")) for p in price_text]
    assert prices == sorted(prices) , "failed select dropdown"
