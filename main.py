# main.py
from account import Account
from transaction import perform_transaction


def main():
    account = Account(account_number="123456", holder_name="John Doe", balance=1000.0)

    print("Welcome to the Simple Banking System")

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            perform_transaction(account, "deposit", amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            perform_transaction(account, "withdraw", amount)
        elif choice == "3":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
