"""
Exercise 13.3 Account View

Module providing Graphical View Components for different account types

Routine Listings
----------------
SavingsAccountView
    class providing a graphical view for a SavingsAccount
LongTermSavingsAccountView
    class providing a graphical view for a LongTermSavingsAccount
CreditAccountView
    class providing a graphical view for a CreditAccount
"""

import abc
import tkinter


class AccountView(abc.ABC):
    def __init__(self, root):
        self.frame = tkinter.Frame(root)

        self.account_number_label = tkinter.Label(self.frame, text="Account number:")
        self.account_number_label.grid(
            sticky=tkinter.E, row=0, column=0, padx=5, pady=5
        )

        self.balance_label = tkinter.Label(self.frame, text="Balance:")
        self.balance_label.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)

        self.interest_rate_label = tkinter.Label(self.frame, text="Interest rate:")
        self.interest_rate_label.grid(sticky=tkinter.E, row=2, column=0, padx=5, pady=5)

    @abc.abstractmethod
    def clear_view(self):
        self.account_number_label.config(text="Account number:")
        self.balance_label.config(text="Balance:")
        self.interest_rate_label.config(text="Interest rate:")

    @abc.abstractmethod
    def load_into_view(self, account):
        self.clear_view()
        self.account_number_label.config(
            text="Account number: {0}".format(account.account_number)
        )
        self.balance_label.config(text="Balance: {0}".format(account.balance))
        self.interest_rate_label.config(
            text="Interest rate: {0}".format(account.interest_rate)
        )


class SavingsAccountView(AccountView):
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
    def __init__(self, root):
        super().__init__(root)

        self.term_period_label = tkinter.Label(self.frame, text="Term period:")
        self.term_period_label.grid(sticky=tkinter.E, row=2, column=0, padx=5, pady=5)

        self.start_date_label = tkinter.Label(self.frame, text="Start date:")
        self.start_date_label.grid(sticky=tkinter.E, row=3, column=0, padx=5, pady=5)

        self.maturation_date_label = tkinter.Label(self.frame, text="Maturation date:")
        self.maturation_date_label.grid(
            sticky=tkinter.E, row=4, column=0, padx=5, pady=5
        )

    def clear_view(self):
        super().clear_view()
        self.term_period_label.config(text="Term period:")
        self.start_date_label.config(text="Start date:")
        self.maturation_date_label.config(text="Maturation date:")

    def load_into_view(self, account):
        super().load_into_view(account)
        self.term_period_label.config(
            text="Term Period: {0} weeks".format(account.term_period)
        )
        self.start_date_label.config(text="Start date: {0}".format(account.start_date))
        self.maturation_date_label.config(
            text="Maturation date: {0}".format(account.maturation_date)
        )


class CreditView(AccountView):
    def __init__(self, root):
        super().__init__(root)
        self.max_withdrawal_limit_label = tkinter.Label(
            self.frame, text="Maximum withdrawal limit:"
        )
        self.max_withdrawal_limit_label.grid(
            sticky=tkinter.E, row=2, column=0, padx=5, pady=5
        )

    def clear_view(self):
        super().clear_view()
        self.max_withdrawal_limit_label.config(text="Maximum withdrawal limit:")

    def load_into_view(self, account):
        super().load_into_view(account)
        self.max_withdrawal_limit_label.config(
            text="Maximum withdrawal limit: {0}".format(
                account.maximum_withdrawal_limit
            )
        )
