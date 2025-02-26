from math import inf, nan, pi
import Account 
import pytest
def test_deposit():
    account = Account.Account("Name1", 0)
    
    #### test for reasonable (non-failing) input ####
    # whole number
    account.deposit(10)
    assert(account.balance == 10), "Should be 10"
    # floating-point number
    account.deposit(11.5)
    assert(account.balance == 21.5), "Should be 21.5"
    # transcendental number
    account.deposit(pi)
    assert(account.balance == (21.5+pi)), "Should be 24.64159265"

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
    assert(account.balance == 100-10), "Should be 90"
    # floating-point number
    account.withdraw(11.5)
    assert(account.balance == 100-21.5), "Should be 78.5"
    # transcendental number
    account.withdraw(pi)
    assert(account.balance == 100-21.5-pi), "Should be 75.35840735"
    
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
    account1 = Account.Account("Name1", 100)
    account2 = Account.Account("Name2", 100)
    account3 = Account.Account("Name1", 50)
    account4 = Account.Account("Name1", 100)
    assert(account1 != account2)
    assert(account3 == account1)
    assert(account4 == account1)
    

_ = pytest.main()