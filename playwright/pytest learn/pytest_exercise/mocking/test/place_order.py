def place_order(payment_service, email_service, amount):
    try:
        payment_result = payment_service.pay(amount)

        if payment_result != "success":
            return "payment_failed"

        email_service.send("Order placed successfully")

        return "order_placed"

    except TimeoutError:
        return "payment_timeout"