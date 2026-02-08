# Exercise 11.2a Account
#
# Implements the Account class framework for a Bank Account management
# system

import abc
import datetime


class Account(abc.ABC):
    """
    Abstract class representing a single account

    Subclasses are expected to overwrite the `deposit`,
    `withdraw` and `apply_interest` abstract methods

    Attributes:
    -----------
    account_holder : str
        name of the account owner
    interest_rate : int | float
        monthly interest rate applied to the account

    """

    def __init__(self, account_number, account_holder, interest_rate):
        """
        Creates a new `Account` instance

        `Account` is abstract and should never be called directly

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            monthly interest rate applied to the account
        """
        self.__account_number = account_number
        self.account_holder = account_holder.strip().lower()
        self.interest_rate = interest_rate
        self.__balance = 0

    def __str__(self):
        template = """Account Number: {0}
Account Holder: {1}
Interest Rate: {2}
Balance: ${3}"""
        return template.format(
            self.account_number, self.account_holder, self.interest_rate, self.balance
        )

    @property
    def account_number(self):
        """
        account_number : str
            Unique account number
        """
        return self.__account_number

    @property
    def balance(self):
        """
        balance: int | float
            account balance in dollars
        """
        return self.__balance

    @abc.abstractmethod
    def deposit(self, amount):
        """
        Deposit money in an account

        Parameters
        ----------
        amount : int | float
            amount in dollars to deposit in the account

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` cannot be deposited
        """
        self.__balance += amount

    @abc.abstractmethod
    def withdraw(self, amount):
        """
        Withdraw money from an account

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` cannot be withdrawn
        """
        self.__balance -= amount

    @abc.abstractmethod
    def apply_interest(self):
        """
        Apply the interest rate to the account and update the balance

        Returns
        -------
        None
        """
        self.__balance += self.__balance * self.interest_rate


class SavingsAccount(Account):
    """
    Represents a standard savings account

    Savings accounts must have non-negative balances, and
    have interest paid on their balances

    See Also
    --------
    Account : Parent Class
    """

    def __init__(self, account_number, account_holder, interest_rate):
        """
        Creates a new `SavingsAccount` instance

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        """
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """==Savings Account==
{0}"""
        return template.format(super().__str__())

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit must be a non-negative number")
        super().deposit(amount)

    def withdraw(self, amount):
        """
        Withdraw money from an account

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance
        """
        if amount <= 0:
            raise ValueError("A withdrawal must be a non-negative number")
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than the account balance")
        super().withdraw(amount)

    def apply_interest(self):
        super().apply_interest()


class LongTermSavingsAccount(SavingsAccount):
    """
    Represents a long term savings account

    An account in which money cannot be withdrawn before the term limit expires.
    After the term limit has expired a reduced interest rate is applied.

    Class Attributes
    ----------------
    min_term_limit: int
        minimum term limit in weeks
    max_term_limit: int
        maximum term limit in weeks

    See Also
    --------
    SavingsAccount : Parent class
    """

    min_term_limit = 12
    max_term_limit = 156

    @staticmethod
    def validate_term_limit(term_limit):
        """
        Validates a proposed term limit

        Parameters
        ----------
        term_limit : int
            proposed term limit in weeks

        Returns
        -------
        bool
            `True` if the proposed term limit is valid, else `False`
        """
        return (
            LongTermSavingsAccount.min_term_limit
            <= term_limit
            <= LongTermSavingsAccount.max_term_limit
        )

    def __init__(
        self, account_number, account_holder, interest_rate, term_period_in_weeks
    ):
        """
        Creates a new `LongTermSavingsAccount` instance

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        term_period_in_weeks : int
            length of the high yield savings term in weeks
        """
        self.__start_date = datetime.date.today()
        self.__term_period = term_period_in_weeks
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """{0}
Term Period: {1} weeks
Start Date: {2}
Maturation Date: {3}
Has matured? {4}"""
        formatted = template.format(
            super().__str__(),
            self.term_period,
            self.start_date,
            self.maturation_date,
            self.has_matured(),
        )
        return formatted.replace("Savings Account", "Long Term Savings Account")

    @property
    def start_date(self):
        """
        start_date : datetime.date
            date the current term period started
        """
        return self.__start_date

    @property
    def term_period(self):
        """
        term_period : int
            length of the term in weeks
        """
        return self.__term_period

    @property
    def maturation_date(self):
        """
        maturation_date : datetime.date
            date the account matures
        """
        return self.__start_date + datetime.timedelta(weeks=self.__term_period)

    def has_matured(self):
        """
        Indicates if an account has matured

        Returns
        -------
        `True` if the account has matured else, `False`
        """
        return datetime.date.today() >= self.maturation_date

    def withdraw(self, amount):
        """
        Withdraw money from a Long Term Savings Account

        Money cannot be withdrawn unless the account has matured

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance.
        ValueError
            Raised if the account has not
            yet matured
        """
        if not self.has_matured():
            raise ValueError("Cannot withdraw from an immature account")
        super().withdraw(amount)

    def apply_interest(self):
        """
        Apply interest to a Long Term Savings Account

        The applied interest for a Long Term Savings account is quartered
        if the account has matured

        Returns
        -------
        None
        """
        effective_rate = self.interest_rate
        if self.has_matured():
            effective_rate /= 4
        self.deposit(self.balance * effective_rate)

    def manage_account(self, transfer_account=None):
        """
        Manage a matured long term savings account

        A mature long term savings account can be closed
        by providing an alternate account to transfer the
        balance into. Alternately if no account is provided
        the account is reinvested and a new term starts.

        The owner of the long term savings account and the
        account to transfer into must be the same

        Parameters
        ----------
        transfer_account : Account, optional
            account to transfer into, pass None to reinvest instead, by default None

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised in attempting to manage an immature account
        ValueError:
            Could not transfer to the new account
        """
        if not self.has_matured():
            raise ValueError("Cannot manage an immature account")
        if transfer_account is None:
            self.__start_date = datetime.date.today()
        else:
            balance = self.balance
            try:
                self.withdraw(balance)
                transfer_account.deposit(balance)
            except ValueError as e:
                # need to ensure balances preserved
                if not self.balance == balance:
                    self.deposit(balance - self.balance)
                    raise ValueError(str(e))


class CreditAccount(Account):
    """
    Represents a basic credit account

    Savings accounts must have non-positive balances, and
    charge interest on their debts

    See Also
    --------
    Account : Parent Class
    """

    def __init__(
        self, account_number, account_holder, interest_rate, max_withdrawal_limit
    ):
        """
        Creates a new `CreditAccount` instance

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        max_withdrawal_limit : int | float
            maximum account that can be loaned out at once
        """
        self.__max_withdrawal_limit = max_withdrawal_limit
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """==Credit Account==
{0}
Maximum Withdrawal Limit: {1}"""
        formatted_string = template.format(
            super().__str__(), self.__max_withdrawal_limit
        )
        return formatted_string.replace("Balance", "Balance owed").replace("$-", "-$")

    def deposit(self, amount):
        """
        Pay off a Credit loan

        Parameters
        ----------
        amount : int | float
            amount to pay off in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if 1amount` is not a positive integer
        ValueError
            Raised if deposit is greater than the current debt
        """
        if amount <= 0:
            raise ValueError("A deposit must be a non-negative number")
        if amount + self.balance > 0:
            raise ValueError(
                "Exceeded max deposit limit: {0}".format(-1 * self.balance)
            )
        super().deposit(amount)

    def withdraw(self, amount):
        """
        Take out a loan of credit

        Parameters
        ----------
        amount : int | float
            amount to loan from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance
        """
        if amount <= 0:
            raise ValueError("A withdrawal must be a non-negative number")
        if self.balance - amount < -1 * self.__max_withdrawal_limit:
            raise ValueError("Cannot exceed withdrawal limit")
        super().withdraw(amount)

    def apply_interest(self):
        """
        Applies interest to any loans

        Returns
        -------
        None
        """
        super().apply_interest()
