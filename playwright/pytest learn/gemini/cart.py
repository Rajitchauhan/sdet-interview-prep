def calculate_total_price(cart_items: list) -> float:
    # Har item ke price ko sum karta hai
    return sum(item["price"] for item in cart_items)