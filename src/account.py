
from datetime import datetime

class BankAccount:
    def __init__(self, account_number: str, balance:float = 0.0):
        self.account_number = account_number
        self.balance = balance

        self.transactions_history = list[dict]



    def deposit(self, amount: float) -> None:
        if 0 > amount:
            raise ValueError("Сумма пополнения должна быть больше 0.")

