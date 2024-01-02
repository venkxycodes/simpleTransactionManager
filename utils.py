def display_balance(balance):
    print(f"Current Balance: Rupees {balance:.2f}")


def log_transaction(message):
    with open("transactions.log", "a") as log_file:
        log_file.write(message + "\n")
