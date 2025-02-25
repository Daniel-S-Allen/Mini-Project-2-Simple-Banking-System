class Account:
    def __init__(self, id:str, balance:float):
        self.id:str = id
        self.list_of_transactions:list[tuple[str,float]] = {}
        self.balance = balance
    
    def update_transection(self, amount:float, description:str):
        self.list_of_transactions.update({description : amount})
    
    def withdraw(self, amount:float, description:str):
        if amount > self.balance:
            raise ValueError("You dont have enough balance to withdraw that ammount")
        else:
            self.balance -= amount
            self.update_transection(amount, description)

    def deposit(self, amount:float, description:str):
        if amount < 0:
            raise ValueError("You dont have enough balance to deposit that ammount")
        else:
            self.balance += amount
            self.update_transection(amount, description)
    
    def display(self):
        # Get the maximum length of the strings to format the output
        length = max(len(f"Account Balance: {self.balance}"), len(f"Id: {self.id}"), len("Transaction History"), *[len(f"{transaction[0]}: {transaction[1]}") for transaction in self.list_of_transactions.items()])
    
        # Print the output with the correct formatting
        print("-" * length)
        print("Account Details")
        print("-" * length)
        print(f"Account Balance: {self.balance}")
        print(f"Id: {self.id}")
        if len(self.list_of_transactions) == 0:
            print("No transactions yet.")
        print()
        print("-" * length)
        print("Transaction History")
        print("-" * length)
        for transaction in self.list_of_transactions.items():
            print(f"{transaction[0]}: {transaction[1]}")
        print("-" * length)