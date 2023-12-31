from account import Account
from transaction import perform_transaction


def main():
    account = Account(account_number="30052001", holder_name="Venkat", balance=3000.0)

    print("Welcome to SBI, ", account.holder_name)

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
