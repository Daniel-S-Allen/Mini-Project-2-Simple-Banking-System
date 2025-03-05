from __future__ import annotations
from math import inf, isnan
from typing import override
from csv import writer
import uuid

class Account:
    _list_of_transactions:list[tuple[str,float]] = []
    _id:str
    def __init__(self, id:str|None = None, balance:float = 0):
        if type(id) is str:
            self._id = id
        else:
            self._id = str(uuid.uuid4())
        self._balance:float = balance
    
    def update_transactions(self, amount:float, description:str):
        """Append a new transaction to this account

        Args:
            amount (float): The amount of money transferred
            description (str): The description of the transaction
        """
        self._list_of_transactions.append((description, amount))
    
    def withdraw(self, amount:float, description:str=""):
        """Withdraw money from this account

        Args:
            amount (float): Amount of money to withdraw
            description (str, optional): Description of transaction

        Raises:
            TypeError: If amount is not a number
            ValueError: If amount is negative or is larger than available balance
        """
        if type(amount) not in [float, int] or isnan(amount):
            raise TypeError("Amount must be a number")
        elif amount > self._balance:
            raise ValueError("Can't withdraw more than available balance")
        elif amount <= 0:
            raise ValueError("Amount must be positive")
        else:
            self._balance -= amount
            self.update_transactions(amount, "(w) " + description)

    def deposit(self, amount:float, description:str=""):
        """Deposit money to this account

        Args:
            amount (float): Amount of money to deposit
            description (str, optional): Description of transaction

        Raises:
            TypeError: If amount is not a number
            ValueError: If amount is negative or infinity
        """
        if type(amount) not in [float, int] or isnan(amount):
            raise TypeError("Amount must be a number")
        elif amount == inf:
            raise ValueError("Can't deposit infinity")
        elif amount <= 0:
            raise ValueError("Amount must be positive")
        else:
            self._balance += amount
            self.update_transactions(amount, "(d) " + description)
    
    def get_balance(self):
        return self._balance
    
    def save(self):
        with open('data.csv', 'a', newline='') as file:
            w = writer(file)
            w.writerow([self._id, self._balance, self._list_of_transactions]) 

    
    def display(self):
        # Get the maximum length of the strings to format the output
        length = max(len(f"Account Balance: {self._balance}"), len(f"Id: {self._id}"), len("Transaction History"), *[len(f"{transaction[0]}: {transaction[1]}") for transaction in self._list_of_transactions])
    
        # Print the output with the correct formatting
        print("-" * length)
        print("Account Details")
        print("-" * length)
        print(f"Account Balance: {self._balance}")
        print(f"Id: {self._id}")
        if len(self._list_of_transactions) == 0:
            print("No transactions yet.")
        print()
        print("-" * length)
        print("Transaction History")
        print("-" * length)
        for transaction in self._list_of_transactions:
            print(f"{transaction[0]}: {transaction[1]}")
        print("-" * length)
        
    def get_id(self):
        return self._id    
    
    @override
    def __eq__(self, other:object):
        """Compares this account to an object

        Args:
            other (object): An object

        Returns:
            bool: True if both objects are an Account and their IDs are the same, false otherwise
        """
        if type(other) == type(self):
            return self._id == other._id
        return False