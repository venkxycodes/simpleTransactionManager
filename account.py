from utils import display_balance, log_transaction


class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        display_balance(self.balance)
        log_transaction(f"Deposit: + Rupees {amount:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            display_balance(self.balance)
            log_transaction(f"Withdrawal: -Rupees {amount:.2f}")

    def get_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        display_balance(self.balance)
