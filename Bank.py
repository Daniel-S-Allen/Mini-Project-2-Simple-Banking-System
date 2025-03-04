from __future__ import annotations
from typing import override
from Account import Account
import json
import fcntl
from os import path

class BankSerializer(json.JSONEncoder):
    @override
    def default(self, o:Bank):
        result:dict[str,object] = {
            'Accounts': o._accounts # pyright: ignore[reportPrivateUsage]
        }
        return result

class Bank:
    _accounts:dict[str,Account]
    _filepath:str|None
    def __init__(self, filepath:str|None = None):
        self._accounts = {}
        self._filepath = filepath
        if filepath is not None:
            if path.exists(filepath):
                self.load(filepath)

    def create_account(self, account_id:str|None = None):
        if account_id is not None:
            if self._accounts.get(account_id, None) is not None:
                raise ValueError(f"Account with id {account_id} already exists!")
        new_account = Account(account_id)
        self._accounts[new_account.get_id()] = new_account

    def add_account(self, account:Account):
        if self._accounts[account.get_id()] is not None:
            raise ValueError(f"Account with id {account.get_id()} already exists!")
        self._accounts[account.get_id()] = account
    
    def get_account(self, id:str):
        return self._accounts[id]
    
    @staticmethod
    def bank_from_file(filepath:str):
        """Deserialize a bank from a file

        Args:
            filepath (str): File to read from

        Raises:
            FileExistsError: If the file does not exist or cannot be read

        Returns:
            _type_: A new bank created from the deserialized data
        """
        if path.exists(filepath):
            raise FileExistsError(f"File {filepath} already exists and is not owned by this bank!")
        with open(filepath, "r") as file:
            bank:Bank = json.load(file)
            bank._filepath = filepath
            return bank
            
    @staticmethod
    def bank_to_file(bank:Bank, filepath:str, overwrite:bool = False):
        if path.exists(filepath) and overwrite == False:
            raise FileExistsError(f"File {filepath} already exists!")
        with open(filepath, "w") as file:
            json.dump(bank, file, cls=BankSerializer, indent=1)
            
    def load(self,filepath:str, append:bool = False):
        self._filepath = filepath
        if path.exists(filepath):
            with open(filepath, "r") as file:
                fcntl.flock(file.fileno(), fcntl.LOCK_EX)
                try:
                    deserialized:dict[str,Account] = json.load(file)
                    if append:
                        self._accounts = deserialized # TODO make this work
                    else:
                        self._accounts = deserialized 
                        self._filepath = filepath
                except:
                    pass
                fcntl.flock(file.fileno(), fcntl.LOCK_UN)

    def save(self):
        if self._filepath is None:
            raise ValueError("Filepath is not set!")
        Bank.bank_to_file(self, self._filepath, True)
        
    def getFilePath(self):
        return self._filepath