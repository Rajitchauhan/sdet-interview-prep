# store.py
class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int = 1):
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1")
        self.items.append(
            {"name": name, "price": price, "quantity": quantity}
        )

    def calculate_subtotal(self) -> float:
        return sum(item["price"] * item["quantity"] for item in self.items)

    def apply_coupon(self, coupon_code: str) -> float:
        subtotal = self.calculate_subtotal()
        if coupon_code == "FLAT100":
            return max(0.0, subtotal - 100)
        elif coupon_code == "DISCOUNT10":
            return subtotal * 0.90
        return subtotal