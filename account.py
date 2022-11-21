class Account:
    def __init__(self, name: str):
        """

        :param name: The name to be given to the new account.
        """
        self.__account_name = name
        self.__account_balance = 0
    # puts money into the account, fails to add money if amount is 0 or negative

    def deposit(self, amount: float):
        """

        :param amount: The numeric value to be added to the account
        :return: Whether the transfer was successful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    # takes money out of the account, fails to take money if amount is 0 or negative

    def withdraw(self, amount: float):
        """
        :param amount: The numeric value to be subtracted from the account
        :return: Whether the transfer was successful or not
        """
        if amount <= 0:
            return False
        elif self.__account_balance - amount == 0:
            return False
        else:
            self.__account_balance -= amount
            return True

    # returns the current monetary balance within the account

    def get_balance(self):
        return self.__account_balance
    # returns the name connected to the created account

    def get_name(self):
        return self.__account_name

