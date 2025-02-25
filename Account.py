class Account:
    def __init__(self, id, balance):
        self.id = id
        #self.account = account
        self.list_of_transectios = {}
        self.balance = balance
    
    def update_transection(self, desc, amm):
        self.list_of_transectios.update({desc : amm})
    
    def withdraw(self, with_am, desc):
        if with_am > self.balance:
            print('insufferable balance!!')
        else:
            self.balance -= with_am
            Account.update_transection(desc, with_am)

    def deposit (self, dep_am, desc):
        if dep_am < 0:
            print("you cant add negative ammount!!!")
        else:
            self.balance += dep_am
            Account.update_transection(desc, dep_am)