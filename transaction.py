def perform_transaction(account, transaction_type, amount):
    if transaction_type == "deposit":
        account.deposit(amount)
        print('amount deposited')
    elif transaction_type == "withdraw":
        account.withdraw(amount)
    else:
        print("Please enter a valid transaction type!")
