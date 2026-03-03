"""
Exercise 13.3b Account Factory

Provides implementations for instantiating bank accounts with valid id's and interest rates

Routine Listings
----------------
AccountAuthoriser
    class representing an account authorisation system that issues new accounts with an account number, interest rates, and limits
"""

import random

from Data import Account


class AccountAuthoriser:
    """
    Class representing a system for authorising accounts and issuing interest rates

    Attributes
    ----------
    savings_interest : int | float
        monthly interest applied to new savings accounts
    credit_interest : int | float
        monthly interest applied to new credit accounts
    """

    def __init__(self, account_system):
        """
        Create a new `AccountAuthoriser`

        Parameters
        ----------
        account_system : AccountSystem
            class that supports the Account System Data Management API
        """

        self.savings_interest = 0.01
        self.credit_interest = 0.10
        self.__account_number_string_length = 4
        self.__account_system = account_system

    def calculate_long_term_interest(self, term_limit):
        """
        Calculates the bonus interest assigned to a long term savings account

        Parameters
        ----------
        term_limit : int
            proposed term limit in weeks

        Returns
        -------
        float
            interest rate for a long-term savings account
        """
        term_contribution = (
            term_limit / Account.LongTermSavingsAccount.max_term_limit * (0.1)
        )
        return self.savings_interest + term_contribution

    def _generate_account_number(self):
        """
        Generates an account number

        The generated account number is a 16 character random
        alphanumeric string

        Returns
        -------
        str
            string representing a valid account number
        """
        account_number_string_tuple = (
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        )

        account_number = "".join(
            random.choices(
                account_number_string_tuple, k=self.__account_number_string_length
            )
        )
        return account_number

    def create_savings_account(self, account_holder):
        """
        Issue a new `SavingsAccount` to the account holder

        Parameters
        ---------
        account_holder : str
            Person whose name the account will be registered in

        Returns
        -------
        SavingsAccount
            The new savings account
        """
        return Account.SavingsAccount(
            self._generate_account_number(), account_holder, self.savings_interest
        )

    def create_long_term_savings_account(self, account_holder, term_limit):
        """
        Issue a new `LongTermSavingsAccount` to the account holder

        Parameters
        ----------
        account_holder : str
            Person whose name the account will be registered in. That person
            must hold at least one existing savings account
        term_limit : int
            term limit in weeks

        Returns
        -------
        LongTermSavingsAccount
            The new long term savings account

        Raises
        ------
        ValueError
            Raised if the term limit is invalid
        ValueError
            Raised if the account holder is not eligible for a long term deposit
        """
        if not Account.LongTermSavingsAccount.validate_term_limit(term_limit):
            raise ValueError("Invalid term limit")

        if not self._has_savings_account(account_holder):
            raise ValueError("Account holder does not have an active savings account")

        return Account.LongTermSavingsAccount(
            self._generate_account_number(),
            account_holder,
            self.calculate_long_term_interest(term_limit),
            term_limit,
        )

    def create_credit_account(self, account_holder, withdrawal_limit):
        """
        Issue a new credit account to the account holder

        Parameters
        ----------
        account_holder : str
            Person whose name the account will be registered in
        withdrawal_limit : int | float
            Maximum amount that can be withdrawn from the account

        Returns
        -------
        CreditAccount
            The new credit account

        Raises
        ------
        ValueError
            Raised if the account holder is not allowed to open the credit account
        """
        if not self._has_savings_account(account_holder):
            raise ValueError("Account holder does not have an active savings account")

        return Account.CreditAccount(
            self._generate_account_number(),
            account_holder,
            self.credit_interest,
            withdrawal_limit,
        )

    def _has_savings_account(self, account_holder):
        """
        Check if the account holder, holds any savings accounts

        Parameters
        ----------
        account_holder : str
            name of the person who holds accounts with the bank

        Returns
        -------
        bool
            `True` if the account holder has a savings account, else `False`
        """
        accounts = self.__account_system.find_users_accounts(account_holder)
        return any(map(lambda a: isinstance(a, Account.SavingsAccount), accounts))
