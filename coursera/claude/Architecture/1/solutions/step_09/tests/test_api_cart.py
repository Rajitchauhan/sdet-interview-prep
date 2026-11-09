from data.products import BACKPACK


def test_add_product_to_cart(shop_api):
    response = shop_api.add_to_cart(BACKPACK.id)

    assert response.status_code == 201
    assert response.json() == {"items": [BACKPACK.id], "count": 1}


def test_unknown_product_is_rejected(shop_api):
    assert shop_api.add_to_cart("does-not-exist").status_code == 404


def test_checkout_with_empty_cart_is_rejected(shop_api):
    assert shop_api.checkout().status_code == 400
