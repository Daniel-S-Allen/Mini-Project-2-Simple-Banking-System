from Account import Account 

accounts = []

while True:
    action = input("What would you like to do? (create, withdraw, deposit, view, quit): ")

    if action == "create":
        id = input("Enter the ID: ")
        balance = input("Enter the initial balance: ")
        if id in [account.id for account in accounts]:
            print("Account with that ID already exists.")
            continue
        accounts.append(Account(id=int(id)))
    
    elif action == "withdraw":
        id = input("Enter the ID: ")
        amount = input("Enter the amount to withdraw: ")
        for account in accounts:
            if account.id == int(id):
                account.withdraw(int(amount))
                continue
        print("No account with that ID exists.")
        
    
    elif action == "deposit":
        id = input("Enter the ID: ")
        amount = input("Enter the amount to deposit: ")
        for account in accounts:
            if account.id == int(id):
                account.deposit(int(amount))
                continue
        print("No account with that ID exists.")
    
    elif action == "view":
        id = input("Enter the ID: ")
        for account in accounts:
            if account.id == int(id):
                account.display()
                continue
        print("No account with that ID exists.")
    
    elif action == "quit":
        for account in accounts:
            account.save()
        break
    
    else:
        print("No such action. Try again.")