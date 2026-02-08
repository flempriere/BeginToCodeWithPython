# Exercise 11.1b Account System
#
# Provides a class for managing and storing collections of accounts

import pickle

import Account


class AccountSystem:
    """
    Represents the account management system of a bank
    """

    def __init__(self):
        """
        Create a new `AccountSystem` instance
        """
        self.__account_dictionary = {}
        self.__account_name_dictionary = {}

    def __str__(self):
        print_string = ""
        for holder, accounts in self.__account_name_dictionary.items():
            print_string += "Client: " + str(holder) + "\n"
            account_list = "\n".join(map(str, accounts))
            print_string += account_list + "\n"
        return print_string

    def save(self, filename):
        """
        Save the `AccountSystem` to a given file

        `AccountSystem` is saved as a pickled binary file in the file given
        by `filename`. The file is created if it doesn't exist. If the file
        already exists it is overwritten

        Parameters
        ----------
        filename : str
            path to the file to save

        Returns
        -------
        None

        Raises
        ------
        Exceptions
            raised if the file fails to save

        See Also
        --------
        AccountSystem.load : load a `AccountSystem` object from a file
        """
        with open(filename, "wb") as output_file:
            pickle.dump(self, output_file)

    @staticmethod
    def load(filename):
        """
        Create an `AccountSystem` instance from a pickled binary file

        Parameters
        ----------
        filename : str
            path to a file containing pickled `FashionShop` data

        Returns
        -------
        AccountSystem
            the loaded `AccountSystem` instance

        Raises
        ------
        Exceptions
            raised if the file fails to load

        See Also
        --------
        AccountSystem.save : saves an `AccountSystem` instance
        """
        with open(filename, "rb") as input_file:
            accounts = pickle.load(input_file)
        return accounts

    def add_new_account(self, account):
        """
        Store a new account in the reference system

        The provided `account` can be indexed by it's `account_number` parameter

        Parameters
        ----------
        account : Account
            account to add to the inventory system

        Returns
        -------
        None

        Raises
        ------
        KeyError
            Raised if the accounts's `account_number` is already registered as a key
        """
        if account.account_number in self.__account_dictionary:
            raise KeyError("This account number is already in use")
        self.__account_dictionary[account.account_number] = account
        if account.account_holder in self.__account_name_dictionary:
            self.__account_name_dictionary[account.account_holder].append(account)
        else:
            self.__account_name_dictionary[account.account_holder] = [account]

    def get_account(self, account_number):
        """
        Get the account with the corresponding account number

        Parameters
        ----------
        account_number : str
            account_number of the account to find

        Returns
        -------
        Account | None
            Returns an `Account` with a matching `account_number` if it exists, else `None`
        """
        return self.__account_dictionary.get(account_number)

    def find_users_accounts(self, name):
        """
        Find the accounts associated with a given user

        Parameters
        ----------
        name : str
            account holder to search for

        Returns
        -------
        List[Account]
            list of accounts held by the given name, if there are no matches the list is empty
        """
        name = name.strip().lower()
        try:
            return self.__account_name_dictionary[name]
        except KeyError:
            return []


# Testing

account_system = AccountSystem()
account_system.add_new_account(Account.new_saving)
account_system.add_new_account(Account.new_long_term)
account_system.add_new_account(Account.new_credit)

print("Getting the account with a specific id")
print(account_system.get_account(1))
print("Getting all accounts associated with a specific client")
print(account_system.find_users_accounts("felix"))
print("Printing the entire system")
print(account_system)
