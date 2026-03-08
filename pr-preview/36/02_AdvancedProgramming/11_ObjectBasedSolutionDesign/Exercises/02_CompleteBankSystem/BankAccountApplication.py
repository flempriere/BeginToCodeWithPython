# Exercise 11.2 c Bank Account Application
#
# Terminal based wrapper around the Account System

import random

import Account
import AccountSystem
import BTCInput


class BankAccountApplication:
    """
    Provides a text-based interface for Bank Account Management

    Class Attributes
    ----------------
    savings_account_interest : float
        current interest rate on newly opened savings accounts
    credit_account_interest : float
        current interest rate on newly opened credit accounts
    """

    savings_account_interest = 0.01
    credit_account_interest = 0.10

    @staticmethod
    def calculate_long_term_interest(term_limit):
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
        return BankAccountApplication.savings_account_interest + term_contribution

    def __init__(self, filename):
        """
        Creates a new `BankAccountApplication`

        Attempts to load an existing application from the provided file.
        Otherwise an empty instance is created

        Parameters
        ----------
        filename : str
            path to a file containing pickled `AccountSystem` data

        See Also
        --------
        AccountSystem : Main class for handling bank accounts
        """
        self.__filename = filename
        try:
            self.__accounts = AccountSystem.AccountSystem.load(filename)
        except:  # noqa: E722
            print("Failed to load accounts")
            print("Creating an empty instance")
            self.__accounts = AccountSystem.AccountSystem()

    def main_menu(self):
        """
        Provides a looping main menu

        Users are able to
        1. Create a new account
        2. Deposit into an account
        3. Withdraw from an account
        4. View an account
        5. View all accounts associated with a name
        6. Manage a matured long term savings account
        7. Apply interest to all accounts
        8. Exit

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid command is received. Should not arise in
            production. Report if encountered
        """

        prompt = """Account Management System

1. Create a new account
2. Deposit into an account
3. Withdraw from an account
4. View an account
5. View all accounts associated with a name
6. Manage a matured long term savings account
7. Apply interest to all accounts
8. Exit

Enter your command: """

        while True:
            command = BTCInput.read_int_ranged(prompt, 1, 8)
            if command == 1:
                self.create_new_account()
            elif command == 2:
                self.deposit_into_account()
            elif command == 3:
                self.withdraw_from_account()
            elif command == 4:
                self.view_account()
            elif command == 5:
                self.view_accounts_for_name()
            elif command == 6:
                self.manage_matured_long_term_savings()
            elif command == 7:
                self.__accounts.apply_interest()
            elif command == 8:
                self.__accounts.save(self.__filename)
                print("Accounts saved")
                break
            else:
                raise ValueError(
                    "Invalid command id {0} encountered in main menu! Please report!".format(
                        command
                    )
                )

    def create_new_account(self):
        """
        Create a new account and add it to the system

        Prompts the user for the type of account to create and
        the necessary descriptors of the item. The account is
        then added to the system

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid account type id is encountered.
            Should not arise in production, please report if found.
        """
        menu = """Create New Account

1. Savings Account
2. Long Term Savings Account
3. Credit Account

Enter account type: """

        def generate_account_number():
            """
            Generates an account number

            The generated account number is a 16 character random
            alphanumeric string

            Returns
            -------
            str
                string representing a valid account number
            """
            account_number_string_length = 4
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
                    account_number_string_tuple, k=account_number_string_length
                )
            )
            return account_number

        account_type = BTCInput.read_int_ranged(menu, 1, 3)
        if account_type < 1 or account_type > 3:
            raise ValueError(
                "Invalid account type id {0} encountered while creating account".format(
                    account_type
                )
            )

        account_number = generate_account_number()
        account_holder = BTCInput.read_text("Enter account holder: ")

        if account_type == 1:
            print("Creating a savings account")
            account = Account.SavingsAccount(
                account_number,
                account_holder,
                BankAccountApplication.savings_account_interest,
            )
            print("Created a new savings account {0}".format(account_number))
        elif account_type == 2:
            print("Creating a long-term savings account")
            while True:
                term_limit = BTCInput.read_int_ranged(
                    "Enter term limit ({0} - {1}): ".format(
                        Account.LongTermSavingsAccount.min_term_limit,
                        Account.LongTermSavingsAccount.max_term_limit,
                    ),
                    Account.LongTermSavingsAccount.min_term_limit,
                    Account.LongTermSavingsAccount.max_term_limit,
                )
                if Account.LongTermSavingsAccount.validate_term_limit(term_limit):
                    break
            account = Account.LongTermSavingsAccount(
                account_number,
                account_holder,
                BankAccountApplication.calculate_long_term_interest(term_limit),
                term_limit,
            )
            print("Created a new long-term savings account {0}".format(account_number))
        elif account_type == 3:
            print("Creating a  credit account")
            withdrawal_limit = BTCInput.read_float("Enter max withdrawal limit: ")
            account = Account.CreditAccount(
                account_number,
                account_holder,
                BankAccountApplication.credit_account_interest,
                withdrawal_limit,
            )
            print("Created a new credit account {0}".format(account_number))
        self.__accounts.add_new_account(account)  # type: ignore

    def get_account(self):
        """
        Prompts the user for an account number and returns any match

        Returns
        -------
        Account | None
            Account is the account number matches, else `None`
        """
        account_number = BTCInput.read_text("Enter account number: ").upper().strip()
        return self.__accounts.get_account(account_number)

    def deposit_into_account(self):
        """
        Deposit into a user-prompted account

        User is prompted for an account, if the account exists,
        the user is then prompted for how much to deposit

        Returns
        -------
        None
        """
        print("Deposit into account")

        account = self.get_account()

        if account is None:
            print("Account not found")
            return
        print("Depositing")
        print(account)

        try:
            amount = BTCInput.read_float(
                "Enter amount to deposit (Current balance: {0}): ".format(
                    account.balance
                )
            )
            account.deposit(amount)
        except ValueError as e:
            print(e)

    def withdraw_from_account(self):
        """
        Withdraw from a user-prompted account

        User is prompted for an account, if the account exists,
        the user is then prompted for how much to withdraw

        Returns
        -------
        None
        """
        print("Withdraw from account")

        account = self.get_account()
        if account is None:
            print("Account not found")
            return
        print("Withdrawing")
        print(account)

        try:
            amount = BTCInput.read_float(
                "Enter amount to withdraw (Current balance: {0}): ".format(
                    account.balance
                )
            )
            account.withdraw(amount)
        except ValueError as e:
            print(e)

    def view_account(self):
        """
        Display a user-specified account

        Returns
        -------
        None
        """
        print("View account")

        account = self.get_account()
        if account is None:
            print("Account not found")
            return
        print(account)

    def view_accounts_for_name(self):
        """
        Find and display accounts for a user prompted name

        Names are converted to lower case and stripped of
        leading and trailing whitespace

        Returns
        -------
        None
        """
        print("View account holders accounts")

        accounts = self.__accounts.find_users_accounts(
            BTCInput.read_text("Enter account holder: ")
        )
        print("\n".join(map(str, accounts)))

    def manage_matured_long_term_savings(self):
        """
        Close out or reinvest a user specified matured long-term account

        Returns
        -------
        None
        """

        account_number = BTCInput.read_text("Enter account number: ").upper().strip()

        account = self.__accounts.get_account(account_number)
        if account is None:
            print("Account not found")
            return
        if not isinstance(account, Account.LongTermSavingsAccount):
            print("Account is not a long term savings account")
            return
        if not account.has_matured():
            print("Account cannot be managed: has not matured")
            return

        reinvest = BTCInput.read_int_ranged(
            "Reinvest this account? (1 - yes, 0 - no): ", 0, 1
        )
        if reinvest:
            account.manage_account()
            return

        holder = account.account_holder
        other_accounts = set(self.__accounts.find_users_accounts(holder)).difference(
            {account}
        )
        if len(other_accounts) == 0:
            print("Account cannot be closed: No accounts to transfer to")
            return
        print("\n".join(map(str, other_accounts)))

        account_number = (
            BTCInput.read_text("Enter transfer account number: ").upper().strip()
        )

        transfer_account = self.__accounts.get_account(account_number)
        if transfer_account is None:
            print("Account not found")
            return
        if transfer_account.account_holder != holder:
            print("Could not transfer, account holder does not match")
            return
        try:
            account.manage_account(transfer_account)
            print(
                "Funds in account {0} transferred to account {1}".format(
                    account.account_number, transfer_account.account_number
                )
            )
        except ValueError as e:
            print("Failed to close account:", e)


ui = BankAccountApplication("accounts.pkl")
ui.main_menu()
