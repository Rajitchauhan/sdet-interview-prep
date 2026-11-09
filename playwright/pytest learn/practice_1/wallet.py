# wallet.py
class Wallet:

    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = initial_balance

    def add_cash(self, amount):
        if amount <= 0:
            raise ValueError("Amount to add must be positive")
        self.balance += amount
        return self.balance

    def spend_cash(self, amount):
        if amount <= 0:
            raise ValueError("Amount to spend must be positive")
        if self.balance < amount:
            raise RuntimeError("Insufficient balance to spend")
        self.balance -= amount
        return self.balance 