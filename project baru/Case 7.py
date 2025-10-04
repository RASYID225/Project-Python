class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return "Invalid withdrawal amount or insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

print("# Case 7 Output")
account = BankAccount("Name")
print(account.deposit(1000))   # Deposited 1000. New balance: 1000
print(account.withdraw(500))   # Withdrew 500. New balance: 500
print(account.withdraw(600))   # Invalid withdrawal amount or insufficient funds
print()