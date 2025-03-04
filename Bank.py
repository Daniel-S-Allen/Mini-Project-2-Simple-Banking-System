from __future__ import annotations
from typing import Any
from Account import Account
import json
from os import path
class Bank:
    _accounts:dict[str,Account]
    _filepath:str|None
    def __init__(self):
        self._accounts = {}

    def add_account(self, account:Account):
        if self._accounts[account.id] is not None:
            raise ValueError(f"Account with id {account.id} already exists!")
        self._accounts[account.id] = account
    
    def get_account(self, id:str):
        return self._accounts[id]
    
    @staticmethod
    def deserialize(filepath:str):
        if path.exists(filepath)
            raise FileExistsError(f"File {filepath} already exists and is not owned by this bank!")
        with open(filepath, "r") as file:
            bank:Bank = json.load(file)
            bank._filepath = filepath
            
    @staticmethod
    def serialize(bank:Bank, filepath:str|None):
        if filepath == None:
            pass
        else:
            if path.exists(filepath)
                raise FileExistsError(f"File {filepath} already exists and is not owned by this bank!")
            with open(filepath, "w") as file:
                json.dump(bank, file)
            
    def import_from_file(self,filepath:str):
        self._filepath = filepath
        if path.exists(filepath):
            with open(filepath, "r") as file:
                deserialized:Bank = json.load(file)
                self._accounts = deserialized._accounts
                    
    def write_to_file(self, filepath:str):
        if path.exists(filepath)
            raise FileExistsError(f"File {filepath} already exists and is not owned by this bank!")
        with open(filepath, "w") as file:
            json.dump(self, file)