import random


class BankAccount:
    def __init__(self):
        self.account_number = random.randint(1, 999999)
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")
        else:
            print("Invalid withdraw amount.")


class Customer:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.bank_account = BankAccount()

    def show_account_info(self):
        print(f"Customer: {self.firstName}")
        print(f"Account Number: {self.bank_account.account_number}")
        print(f"Balance: ${self.bank_account.balance}")
