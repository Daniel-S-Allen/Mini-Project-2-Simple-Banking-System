from __future__ import annotations
import pickle
from Account import Account
import fcntl
from os import path

class Bank:
    accounts:dict[str, Account]
    
    def __init__(self, id:str | None = None, accounts:dict[str,Account]|None = None):
        self.accounts = accounts if accounts is not None else {}
        
    def get_account_ids(self) -> list[str]:
        return list(self.accounts)    
    
    def create_account(self, account_id:str|None = None, account_balance:float = 0) -> Account:
        """Create a new account with the specified id

        Args:
            account_id (str | None, optional): Name of the account.

        Raises:
            ValueError: If an account with the given ID already exists
        """
        if account_id is not None:
            if self.accounts.get(account_id, None) is not None:
                raise ValueError(f"Account with id {account_id} already exists!")
        new_account = Account(account_id, account_balance)
        self.accounts[new_account.get_id()] = new_account
        return new_account

    def add_account(self, account:Account):
        if self.accounts[account.get_id()] is not None:
            raise ValueError(f"Account with id {account.get_id()} already exists!")
        self.accounts[account.get_id()] = account
    
    def get_account(self, id:str):
        if self.accounts.get(id) is not None:
            return self.accounts[id]
        raise KeyError(f"No account found with the id \"{id}\"")
    
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
        with open(filepath, "rb") as file:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            bank:Bank = pickle.load(file)
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
            return bank
            
    @staticmethod
    def bank_to_file(bank:Bank, filepath:str, overwrite:bool = False):
        if path.exists(filepath) and overwrite == False:
            raise FileExistsError(f"File {filepath} already exists!")
        with open(filepath, "wb") as file:
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
            pickle.dump(bank,file)
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)

    def save(self, filepath:str):
        Bank.bank_to_file(self, filepath, True)