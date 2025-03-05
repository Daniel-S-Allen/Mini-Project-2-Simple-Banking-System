from __future__ import annotations
import uuid
from Account import Account
import json
import fcntl
from os import path

class Bank:
    accounts:dict[str, Account]
    
    def __init__(self, id:str | None = None):
        self.accounts = {}
        
    def get_account_ids(self) -> list[str]:
        return list(self.accounts)    
    
    def create_account(self, account_id:str|None = None) -> Account:
        """Create a new account with the specified id. If the ID is ``None``, generate a new random UUID.

        Args:
            account_id (str | None, optional): Name of the account.

        Raises:
            ValueError: If an account with the given ID already exists
        """
        if account_id is not None:
            if self.accounts.get(account_id, None) is not None:
                raise ValueError(f"Account with id {account_id} already exists!")
        new_account = Account(account_id)
        self.accounts[new_account.get_id()] = new_account
        return new_account

    def add_account(self, account:Account):
        if self.accounts[account.get_id()] is not None:
            raise ValueError(f"Account with id {account.get_id()} already exists!")
        self.accounts[account.get_id()] = account
    
    def get_account(self, id:str):
        return self.accounts[id]
    
    @staticmethod
    def bank_from_file(filepath:str):
        """Deserialize a bank from a file

        Args:
            filepath (str): File to read from

        Raises:
            FileNotFoundError: If the file does not exist or cannot be read

        Returns:
            _type_: A new bank created from the deserialized data
        """
        with open(filepath, "r") as file:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            bank:Bank = json.load(file)
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
            return bank
            
    @staticmethod
    def bank_to_file(bank:Bank, filepath:str, overwrite:bool = False):
        if path.exists(filepath) and overwrite == False:
            raise FileExistsError(f"File {filepath} already exists!")
        with open(filepath, "w") as file:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            json.dump(bank, file, indent=1)
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)

    def save(self, filepath:str):
        Bank.bank_to_file(self, filepath, True)