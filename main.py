from os.path import exists
from Account import Account 
from Bank import Bank
current_account: Account|None = None
bank:Bank = Bank.bank_from_file("database.bank") if exists("database.bank") else Bank()

while True:
    try:
        # Get the user action
        action = input("What would you like to do? (create, select, withdraw, deposit, view, quit): ").lower()

        # Wish that switch cases were a thing in Python
        # they are https://www.geeksforgeeks.org/python-match-case-statement/
        if action == "create":
            # Get the account parameters
            id = input("Enter the ID: ")
            balance = int(input("Enter the initial balance: "))
            try:
                current_account = bank.create_account(id,balance)
            except Exception as e:
                print(e)
        
        # Change the current_account to the account with the given ID
        elif action == "select":
            # Get the account ID to select
            id = input("Enter the ID: ")
            try:
                current_account = bank.get_account(id)
            except Exception as e:
                print(e)

        elif action == "list":
            print(bank.get_account_ids())

        # check if an account is selected, all other actions require a selected account
        elif current_account is None:
            print("No account selected. Please create or select an account first.")
        
        # Withdraw the given amount from the current account
        elif action == "withdraw":
            amount = input("Enter the amount to withdraw: ")
            description = input("Enter the description: ")
            try:
                current_account.withdraw(amount=int(amount), description=description)
            except Exception as e:
                print(e)
            
        # Deposit the given amount to the current account
        elif action == "deposit":
            amount = input("Enter the amount to deposit: ")
            description = input("Enter the description: ")
            try:
                current_account.deposit(amount=int(amount), description=description)
            except Exception as e:
                print(e)
        
        # Display the current account balance and transaction history
        elif action == "view":
            current_account.display()
        
        # Save all accounts and exit the program
        elif action == "quit":
            bank.save("database.bank")
            break

        # Catch invalid input
        else:
            print("No such action. Try again.")
    except KeyboardInterrupt as e:
        print("Keyboard Interrupt - Saving...")
        bank.save("database.bank")
        print("Saved")
        exit()