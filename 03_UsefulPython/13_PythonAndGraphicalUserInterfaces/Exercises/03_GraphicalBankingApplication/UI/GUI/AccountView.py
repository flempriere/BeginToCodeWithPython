"""
Exercise 13.3g Account View

Module providing Graphical View Components for different account types

Classes
-------
AccountView
    abstract class for providing a  graphical view for an Account
SavingsAccountView
    class providing a graphical view for a SavingsAccount
LongTermSavingsAccountView
    class providing a graphical view for a LongTermSavingsAccount
CreditAccountView
    class providing a graphical view for a CreditAccount

Variables
---------
account_views_dictionary : dict[str, AccountView]
    dictionary mapping `Account.Account.account_type` strings to the corresponding
    `AccountView` subclass
"""

import abc
import tkinter

from Data import Account


class AccountView(abc.ABC):
    """
    Abstract class for providing a graphical display of an Account

    Handles displaying the attributes common to all accounts. Subclasses
    should extend this view with subclass specific attributes

    Attributes
    ----------
    frame
        frame containing this widget
    """

    def __init__(self, root):
        """
        Create a new `AccountView`

        Parameters
        ----------
        root
            parent widget
        """
        self.frame = tkinter.Frame(root)

        self._account_type_label = tkinter.Label(self.frame, text="")
        self._account_type_label.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, padx=5, pady=5
        )
        self._account_number_label = tkinter.Label(self.frame, text="Account number:")
        self._account_number_label.grid(
            sticky=tkinter.E, row=1, column=0, padx=5, pady=5
        )

        self._balance_label = tkinter.Label(self.frame, text="Balance:")
        self._balance_label.grid(sticky=tkinter.E, row=2, column=0, padx=5, pady=5)

        self._interest_rate_label = tkinter.Label(self.frame, text="Interest rate:")
        self._interest_rate_label.grid(
            sticky=tkinter.E, row=3, column=0, padx=5, pady=5
        )

    @abc.abstractmethod
    def clear_view(self):
        """
        Clear the current view

        Returns
        -------
        None
        """
        self._account_type_label.config(text="")
        self._account_number_label.config(text="Account number:")
        self._balance_label.config(text="Balance:")
        self._interest_rate_label.config(text="Interest rate:")

    @abc.abstractmethod
    def load_into_view(self, account):
        """
        Load an account into the view

        Parameters
        ----------
        account : `Account.Account`
            The account to display
        """
        self.clear_view()
        self._account_type_label.config(text="{0}".format(account.account_type))
        self._account_number_label.config(
            text="Account number: {0}".format(account.account_number)
        )
        self._balance_label.config(text="Balance: {0:.2f}".format(account.balance))
        self._interest_rate_label.config(
            text="Interest rate: {0:.4f}".format(account.interest_rate)
        )


class SavingsAccountView(AccountView):
    """
    Specific View implementation for a Savings Account
    """

    def __init__(self, root):
        """
        Create a new `SavingsAccountView`

        Parameters
        ----------
        root
            Tkinter root frame for the savings view
        """
        super().__init__(root)

    def clear_view(self):
        super().clear_view()

    def load_into_view(self, account):
        super().load_into_view(account)


class LongTermSavingsAccountView(AccountView):
    """
    Specific view implementation for a `LongTermSavingsAccount`
    """

    def __init__(self, root):
        """
        Create a new `LongTermSavingsAccountView`

        Parameters
        ----------
        root
            parent widget
        """
        super().__init__(root)

        self._term_period_label = tkinter.Label(self.frame, text="Term period:")
        self._term_period_label.grid(sticky=tkinter.E, row=4, column=0, padx=5, pady=5)

        self._start_date_label = tkinter.Label(self.frame, text="Start date:")
        self._start_date_label.grid(sticky=tkinter.E, row=5, column=0, padx=5, pady=5)

        self._maturation_date_label = tkinter.Label(self.frame, text="Maturation date:")
        self._maturation_date_label.grid(
            sticky=tkinter.E, row=6, column=0, padx=5, pady=5
        )

    def clear_view(self):
        super().clear_view()
        self._term_period_label.config(text="Term period:")
        self._start_date_label.config(text="Start date:")
        self._maturation_date_label.config(text="Maturation date:")

    def load_into_view(self, account):
        super().load_into_view(account)
        self._term_period_label.config(
            text="Term Period: {0} weeks".format(account.term_period)
        )
        self._start_date_label.config(text="Start date: {0}".format(account.start_date))
        self._maturation_date_label.config(
            text="Maturation date: {0}".format(account.maturation_date)
        )


class CreditView(AccountView):
    """
    Specific View implementation for a Credit Account
    """

    def __init__(self, root):
        """
        Create a new `CreditView`

        Parameters
        ----------
        root
            parent widget
        """
        super().__init__(root)
        self._max_withdrawal_limit_label = tkinter.Label(
            self.frame, text="Maximum withdrawal limit:"
        )
        self._max_withdrawal_limit_label.grid(
            sticky=tkinter.E, row=4, column=0, padx=5, pady=5
        )

    def clear_view(self):
        super().clear_view()
        self._max_withdrawal_limit_label.config(text="Maximum withdrawal limit:")

    def load_into_view(self, account):
        super().load_into_view(account)
        self._max_withdrawal_limit_label.config(
            text="Maximum withdrawal limit: {0}".format(
                account.maximum_withdrawal_limit
            )
        )


account_views_dictionary = {
    Account.SavingsAccount.account_type: SavingsAccountView,
    Account.LongTermSavingsAccount.account_type: LongTermSavingsAccountView,
    Account.CreditAccount.account_type: CreditView,
}
"""
Dictionary mapping `Account.Account.account_type` values to the respective `AccountView` subclass
"""
