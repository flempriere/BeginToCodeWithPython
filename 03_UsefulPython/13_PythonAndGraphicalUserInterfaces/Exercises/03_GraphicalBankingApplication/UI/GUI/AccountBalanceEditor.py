"""
Exercise 13.3d Account Balance Editor

Provides a graphical component for withdrawing and depositing into a Bank Account

Classes
-------
AccountBalanceEditor
    tkinter widget providing an entry box and two buttons for withdrawing or depositing to an account
"""

import tkinter
import tkinter.messagebox

from Data import Account


class AccountBalanceEditor:
    """
    Class representing a graphical account balance editor

    Attributes
    ----------
    receiver
        object to notify when an account balance in modified.
        Must support the `balance_changed()` method
    frame
        the widget frame containing the component
    """

    def __init__(self, root, receiver):
        """
        Create a new `AccountBalanceEditor`

        Parameters
        ----------
        root :
            parent widget
        receiver :
            object supporting the `balance_changed` method to be notified
            when a balance changes

        Raises
        ------
        AttributeError
            raised if receiver does not support `balance_changed`
        """
        if not hasattr(receiver, "balance_changed"):
            raise AttributeError(
                "Supplied receiver does not support balance_changed method"
            )
        self.receiver = receiver
        self._current_account = None
        self.frame = tkinter.Frame(root)

        self._change_balance_entry = tkinter.Entry(self.frame, width=10)
        self._change_balance_entry.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, columnspan=2, padx=5, pady=5
        )

        def modify_balance(fn, error_title="Balance Modification Failed"):
            """
            binding function for modifying a balance by a provided function `fn`

            Takes an input function `fn` to control how the balance is modified,
            but handles validating the state and cleaning up the GUI

            Parameters
            ----------
            fn : function
                function to call to modify the balance
            error_title : str, optional
                string to use to title the message box
                if any errors are reported, by default "Balance Modification Failed"

            Returns
            -------
            None

            Notes
            -----
            Errors will result in a message box being displayed to the user
            """
            try:
                fn(float(self._change_balance_entry.get()))
                self.receiver.balance_changed()
                self._change_balance_entry.delete(0, tkinter.END)
            except ValueError as e:
                tkinter.messagebox.showerror(title=error_title, message=str(e))

        def deposit():
            """
            Provides a binding to the deposit method on the current account

            Returns
            -------
            None
            """
            modify_balance(self._current_account.deposit, error_title="Deposit failed")  # type: ignore

        def withdraw():
            """
            Provides a binding to the withdraw method on the current account

            Returns
            -------
            None
            """
            modify_balance(
                self._current_account.withdraw,  # type: ignore
                error_title="Withdraw failed",
            )

        self._deposit_button = tkinter.Button(
            self.frame, text="Deposit", command=deposit
        )
        self._deposit_button.grid(sticky=tkinter.W, row=1, column=0, padx=5, pady=5)
        self._deposit_button.config(state=tkinter.DISABLED)

        self._withdraw_button = tkinter.Button(
            self.frame, text="Withdraw", command=withdraw
        )
        self._withdraw_button.grid(sticky=tkinter.E, row=1, column=1, padx=5, pady=5)
        self._withdraw_button.config(state=tkinter.DISABLED)

    @property
    def account(self):
        """
        account : Account
            the account being edited

        Raises
        ------
        TypeError
            raised when attempting to set `account` to a type that is not a subclass of `Account.Account`
        """
        return self._current_account

    @account.setter
    def account(self, account):
        if not isinstance(account, Account.Account) and account is not None:
            raise TypeError("account must be a subclass of Account or None")
        self._current_account = account
        if self._current_account is None:
            self._withdraw_button.config(state=tkinter.DISABLED)
            self._deposit_button.config(state=tkinter.DISABLED)
        else:
            self._withdraw_button.config(state=tkinter.NORMAL)
            self._deposit_button.config(state=tkinter.NORMAL)
