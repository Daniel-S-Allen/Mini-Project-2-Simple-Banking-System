class Account:
    def __init__(self, id, balance):
        self.id = id
        self.list_of_transactions = {}
        self.balance = balance
    
    def update_transection(self, desc, amm):
        self.list_of_transactions.update({desc : amm})
    
    def withdraw(self, with_am, desc):
        if with_am > self.balance:
            raise ValueError("You dont have enough balance to withdraw that ammount")
        else:
            self.balance -= with_am
            self.update_transection(desc, -with_am)

    def deposit(self, dep_am, desc):
        if dep_am < 0:
            raise ValueError("You dont have enough balance to deposit that ammount")
        else:
            self.balance += dep_am
            self.update_transection(desc, dep_am)
    
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