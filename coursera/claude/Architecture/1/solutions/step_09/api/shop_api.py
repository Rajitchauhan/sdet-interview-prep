import requests

from api.base_client import BaseApiClient


class ShopApi(BaseApiClient):
    def get_cart(self) -> requests.Response:
        return self.request("GET", "/api/cart")

    def add_to_cart(self, product_id: str) -> requests.Response:
        return self.request("POST", "/api/cart", json={"product_id": product_id})

    def clear_cart(self) -> requests.Response:
        return self.request("DELETE", "/api/cart")

    def checkout(self) -> requests.Response:
        return self.request("POST", "/api/checkout")
