from math import inf, nan, pi
import random
import Account 
from Bank import Bank
import pytest
def test_deposit():
    account = Account.Account("Name1", 0)
    
    #### test for reasonable (non-failing) input ####
    # whole number
    account.deposit(10)
    assert(account.get_balance()  == 10), "Should be 10"
    # floating-point number
    account.deposit(11.5)
    assert(account.get_balance()  == 21.5), "Should be 21.5"
    # transcendental number
    account.deposit(pi)
    assert(account.get_balance()  == (21.5+pi)), "Should be 24.64159265"

    #### test for unreasonable (failing) input ####
    # test negative
    with pytest.raises(ValueError):
        account.withdraw(-5)
    # test infinity
    with pytest.raises(ValueError):
        account.deposit(inf)
    # test not a number
    with pytest.raises(TypeError):
        account.withdraw(nan)
    # test invalid type
    with pytest.raises(TypeError):
        account.deposit("test") # pyright: ignore[reportArgumentType]

def test_withdraw():
    account = Account.Account("Name1", 100)
    
    #### test for reasonable (non-failing) input ####
    # whole number
    account.withdraw(10)
    assert(account.get_balance() == 100-10), "Should be 90"
    # floating-point number
    account.withdraw(11.5)
    assert(account.get_balance()  == 100-21.5), "Should be 78.5"
    # transcendental number
    account.withdraw(pi)
    assert(account.get_balance()  == 100-21.5-pi), "Should be 75.35840735"
    
    #### test for unreasonable (failing) input ####
    # test above balance
    with pytest.raises(ValueError):
        account.withdraw(100)
    # test negative
    with pytest.raises(ValueError):
        account.withdraw(-5)
    # test infinity
    with pytest.raises(ValueError):
        account.withdraw(inf)
    # test not a number
    with pytest.raises(TypeError):
        account.withdraw(nan)
    # test invalid type
    with pytest.raises(TypeError):
        account.withdraw("test") # pyright: ignore[reportArgumentType]

def test_duplicate():
    bank = Bank()
    _ = bank.create_account("TestAccount")
    with pytest.raises(ValueError):
        _ = bank.create_account("TestAccount")

def test_save_and_load():
    bank = Bank()
    for _ in range(0, 10):
        account = bank.create_account()
        account.deposit(random.randint(500,1000))
        account.withdraw(random.randint(0,500))

    bank.save("banking_test.bank")
    second_bank = Bank.bank_from_file("banking_test.bank")

    for account in bank.get_account_ids():
        assert(bank.accounts[account] == second_bank.accounts[account])
            
_ = pytest.main()