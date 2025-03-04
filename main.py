from Account import Account 
accounts:list[Account] = []
current_account = None 



while True:
    # Get the user action
    action = input("What would you like to do? (create, select, withdraw, deposit, view, quit): ").lower()

    # Wish that switch cases were a thing in Python
    # they are https://www.geeksforgeeks.org/python-match-case-statement/
    if action == "create":
        # Get the account parameters
        id = input("Enter the ID: ")
        balance = int(input("Enter the initial balance: "))

        # Check if an account with that ID already exists
        if id in [account.id for account in accounts]:
            print("Account with that ID already exists.")
            continue
        
        # Create the account and add it as the current account
        accounts.append(Account(id=id, balance=balance))
        current_account = accounts[-1]
    
    # Change the current_account to the account with the given ID
    elif action == "select":
        # Get the account ID to select
        id = input("Enter the ID: ")

        # Loop until account is found or end of list 
        for account in accounts:
            if account.id == id:
                current_account = account
                break
        else:
            print("Error: Account with that ID does not exist.")

    # check if an account is selected, all other actions require a selected account
    elif current_account is None:
        print("No account selected. Please create or select an account first.")
    
    # Withdraw the given amount from the current account
    elif action == "withdraw":
        amount = input("Enter the amount to withdraw: ")
        description = input("Enter the description: ")
        try:
            current_account.withdraw(amount=int(amount), description=description)
        except ValueError:
            print("Error: Invalid withdraw amount.")
        
    # Deposit the given amount to the current account
    elif action == "deposit":
        amount = input("Enter the amount to deposit: ")
        description = input("Enter the description: ")
        current_account.deposit(amount=int(amount), description=description)
    
    # Display the current account balance and transaction history
    elif action == "view":
        current_account.display()
    
    # Save all accounts and exit the program
    elif action == "quit":
        for account in accounts:
            account.save()
        quit()
    

    # Catch invalid input
    else:
        print("No such action. Try again.")
    