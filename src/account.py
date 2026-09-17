
from datetime import datetime

class BankAccount:
    def __init__(self, account_number: str, balance:float = 0.0):
        self.account_number = account_number
        self.balance = balance

        self.transactions_history: list[dict] = []


    def __str__(self) -> str:
        return f"Номер счета: {self.account_number}| Баланс: {self.balance:.2f}"


    def deposit(self, amount: float) -> bool:
        if 0 >= amount:
           raise ValueError("Сумма пополнения должна быть больше 0.")

        self.balance += amount

        transaction: dict = {
            "type": "deposit",
            "amount": amount,
            "datetime": datetime.now()
        }

        self.transactions_history.append(transaction)

        return True

    def get_balance(self) -> float:
        return self.balance

    def withdraw(self, amount: float) -> bool:
        if amount < self.balance:
            raise ValueError("Суммы на балансе не хватает что-бы совершить операцию.")

        self.balance -= amount
        transaction: dict = {
            "type": "withdraw",
            "amount": -amount,
            "datetime": datetime.now()
        }

        self.transactions_history.append(transaction)
        return True


