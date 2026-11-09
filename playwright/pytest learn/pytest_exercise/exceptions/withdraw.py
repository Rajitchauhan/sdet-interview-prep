def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than zero")

    if amount > balance:
        raise RuntimeError("Insufficient balance")

    return balance - amount

