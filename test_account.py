from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('John')
        self.account2 = Account('Jane')

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'John'
        assert self.account1.get_balance() == 0
        assert self.account2.get_name() == 'Jane'
        assert self.account2.get_balance() == 0

    def test_deposit(self):
        assert self.account1.deposit(230) == True
        assert self.account1.get_balance() == 230
        assert self.account2.deposit(-12) == False
        assert self.account1.deposit(0) == False
        assert self.account2.deposit(200021) == True

    def test_withdraw(self):
        assert self.account1.withdraw(230) == True
        assert self.account2.withdraw(-12) == False
        assert self.account1.withdraw(0) == False
        assert self.account2.withdraw(200021) == True

