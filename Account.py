from math import inf

class Account:
    def __init__(self, id:str, balance:float):
        self.id:str = id
        self.list_of_transactions:list[tuple[str,float]] = []
        self.balance = balance
    
    def update_transactions(self, amount:float, description:str):
        self.list_of_transactions.append((description, amount))
    
    def withdraw(self, amount:float, description:str=""):
        if (type(amount) not in [float, int]) or amount > self.balance or amount <= 0:
            raise ValueError("You cant withdraw that amount")
        else:
            self.balance -= amount
            self.update_transactions(amount, "(w) " + description)

    def deposit(self, amount:float, description:str=""):
        if (type(amount) not in [float, int]) or amount <= 0 or amount == inf:
            raise ValueError("You cant deposit that amount")
        else:
            self.balance += amount
            self.update_transactions(amount, "(d) " + description)
    
    def display(self):
        # Get the maximum length of the strings to format the output
        length = max(len(f"Account Balance: {self.balance}"), len(f"Id: {self.id}"), len("Transaction History"), *[len(f"{transaction[0]}: {transaction[1]}") for transaction in self.list_of_transactions])
    
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
        for transaction in self.list_of_transactions:
            print(f"{transaction[0]}: {transaction[1]}")
        print("-" * length)