from Account import Account 

accounts = []
current_account = None 

while True:
    action = input("What would you like to do? (create, select, withdraw, deposit, view, quit): ")

    if action == "create":
        id = int(input("Enter the ID: "))
        balance = int(input("Enter the initial balance: "))
        if id in [account.id for account in accounts]:
            print("Account with that ID already exists.")
            continue
        accounts.append(Account(id=id, balance=balance))
        current_account = accounts[-1]
    
    elif action == "select":
        id = int(input("Enter the ID: "))
        for account in accounts:
            if account.id == id:
                current_account = account
                break
        else:
            print("Error: Account with that ID does not exist.")

    elif current_account is None:
        print("No account selected. Please create or select an account first.")
    
    elif action == "withdraw":
        amount = input("Enter the amount to withdraw: ")
        try:
            current_account.withdraw(int(amount))
        except:
            print("Error: Invalid withdraw amount.")
        
    
    elif action == "deposit":
        amount = input("Enter the amount to deposit: ")
        current_account.deposit(int(amount))
    
    elif action == "view":
        amount = input("Enter the amount to deposit: ")
        current_account.display(int(amount))
    
    elif action == "quit":
        for account in accounts:
            account.save()
        break
    
    else:
        print("No such action. Try again.")