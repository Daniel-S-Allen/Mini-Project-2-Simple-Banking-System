from Account import Account
class Bank:
    _accounts:dict[str,Account]
    def __init__(self, filepath:str|None):
        self._accounts = {}

    def import_account(self, account:Account):
        if self._accounts[account.id] is not None:
            raise LookupError(f"Account with id {account.id} already exists!")
        self._accounts[account.id] = account
    
    