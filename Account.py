class Account:
    def __init__(self, name: str):
        self.account_name = name
        self.account_balance = 0
    # puts money into the account, fails to add money if amount is 0 or negative

    def deposit(self, amount: float):
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True
    # takes money out of the account, fails to take money if amount is 0 or negative

    def withdraw(self, amount):
        if amount <= 0:
            return False
        else:
            self.account_balance -= amount
            return True

    # returns the current monetary balance within the account

    def get_balance(self):
        return self.account_balance
    # returns the name connected to the created account

    def get_name(self):
        return self.account_name
