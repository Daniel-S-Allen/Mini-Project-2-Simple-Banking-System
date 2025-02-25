from math import inf, pi
import Account 
import pytest
def test_deposit():
    account = Account.Account("Name1", 0)
    # test for 'reasonable' input
    account.deposit(10)
    assert(account.balance == 10), "Should be 10"
    account.deposit(11.5)
    assert(account.balance == 21.5), "Should be 21.5"
    account.deposit(pi)
    assert(account.balance == (21.5+pi)), "Should be 24.64159265"

    # test for malicious input
    with pytest.raises(Exception):
        account.withdraw(-5)
    with pytest.raises(Exception):
        account.deposit(inf)
    with pytest.raises(Exception):
        account.deposit("test")

def test_withdraw():
    account = Account.Account("Name1", 100)
    # test for 'reasonable' input
    account.withdraw(10)
    assert(account.balance == 100-10)
    account.withdraw(11.5)
    assert(account.balance == 100-21.5)
    account.withdraw(pi)
    assert(account.balance == 100-(21.5+pi))
    
    # test for malicious input
    with pytest.raises(ValueError):
        account.withdraw(-5)
    with pytest.raises(ValueError):
        account.withdraw(inf)
    with pytest.raises(ValueError):
        account.withdraw("test")

test_deposit()
test_withdraw()