# bank.py
def withdraw_money(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero")
    if amount > balance:
        raise RuntimeError("Insufficient funds in account")
    return balance - amount