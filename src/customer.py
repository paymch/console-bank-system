import account

my_account = account.BankAccount("123", 100)

print(my_account)

try:
    my_account.deposit(0)
except ValueError as e:
    print(e)

print(f"Баланс: {my_account.get_balance()}")