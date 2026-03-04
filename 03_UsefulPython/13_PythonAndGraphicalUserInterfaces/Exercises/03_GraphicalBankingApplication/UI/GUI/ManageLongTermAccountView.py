"""
Exercise 13.3i Manage Long Term Account View

Provides a graphical component for managing a matured long-term savings account

Classes
-------
ManageLongTermAccountView
    Graphical component for managing a long term account. Designing to be
    located in a separate window
"""

import tkinter
import tkinter.messagebox

from Data import Account

from UI.GUI import AccountSelector, AccountView


class ManageLongTermAccountView:
    """
    Graphical widget for managing a long term account

    Provides the user with a list to select their other accounts. The user
    can then either reinvest the matured account or transfer the savings in
    the account into another account

    Attributes
    ----------
    frame
        the frame holding the graphical component
    """

    def __init__(self, root, account, account_system):
        """
        Create a new `ManageLongTermAccountView`

        Parameters
        ----------
        root
            parent widget
        account : Account.LongTermSavingsAccount
            The long term account being managed
        account_system : AccountSystem.AccountSystem
            The account system storing the system accounts
        """
        self._root = root
        self.__account_system = account_system
        self.__selected_transfer_account = None  # no transfer account to start
        self.__account = account

        self.frame = tkinter.Frame(root)

        # create the views for the long term account, the prospective
        # transfer account and the list to select other accounts
        # load the managed account into the view
        self._selector = AccountSelector.AccountSelector(self.frame, self)
        self._lt_view = AccountView.LongTermSavingsAccountView(self.frame)
        self._lt_view.load_into_view(self.__account)
        self._other_views = AccountView.account_views_dictionary
        self._other_view = self._other_views[Account.SavingsAccount.account_type](
            self.frame
        )
        self._lt_view_label = tkinter.Label(self.frame, text="Matured Account")
        self._other_view_label = tkinter.Label(self.frame, text="Transfer Account")
        self._selector_label = tkinter.Label(self.frame, text="Select Transfer Account")

        self._lt_view.frame.grid(
            sticky=tkinter.W + tkinter.N, row=1, column=0, padx=5, pady=5
        )
        self._other_view.frame.grid(
            sticky=tkinter.E + tkinter.N, row=1, column=1, padx=5, pady=5
        )
        self._selector.frame.grid(
            sticky=tkinter.E + tkinter.N, row=1, column=2, padx=5, pady=5
        )
        self._lt_view_label.grid(sticky=tkinter.W, row=0, column=0, padx=5, pady=5)
        self._other_view_label.grid(sticky=tkinter.E, row=0, column=1, padx=5, pady=5)
        self._selector_label.grid(sticky=tkinter.E, row=0, column=2, padx=5, pady=5)

        def dismiss():
            """
            binding to dismiss the parent window when the account is no longer being managed

            Returns
            -------
            None
            """
            self._root.grab_release()
            self._root.destroy()

        def reinvest():
            """
            binding to reinvest an account

            Returns
            -------
            None
            """
            self.__account.manage_account()
            tkinter.messagebox.showinfo(message="Reinvested account")
            dismiss()

        def transfer():
            """
            binding to transfer funds to another account

            Requires a selected transfer account. If one is selected will
            attempt to transfer the funds into that account

            Returns
            -------
            None
            """
            try:
                if self.__selected_transfer_account is None:
                    raise ValueError("No transfer account selected")
                self.__account.manage_account(self.__selected_transfer_account)
                tkinter.messagebox.showinfo(
                    message="Transferred funds from {0} to {1}".format(
                        self.__account.account_number,
                        self.__selected_transfer_account.account_number,
                    )
                )
            except ValueError as e:
                tkinter.messagebox.showerror(
                    message="Failed to transfer account:\n{0}".format(e)
                )
                return
            dismiss()

        button_frame = tkinter.Frame(self.frame)
        reinvest_button = tkinter.Button(
            button_frame, text="Reinvest", command=reinvest
        )
        reinvest_button.grid(sticky=tkinter.W, row=0, column=0, padx=5, pady=5)
        self._transfer_button = tkinter.Button(
            button_frame, text="Transfer", command=transfer
        )
        self._transfer_button.grid(sticky=tkinter.W, row=0, column=1, padx=5, pady=5)
        button_frame.grid(sticky=tkinter.E + tkinter.W, row=2, column=2, padx=5, pady=5)

    def got_selection(self, selection):
        """
        Handles the current selection being changed

        Loads the newly selected transfer account into the view and
        ensures the transfer button is enabled

        Parameters
        ----------
        selection : str
            account number for the selected transfer account

        Returns
        -------
        None
        """
        self._transfer_button.config(state=tkinter.NORMAL)
        self._other_view.frame.grid_forget()  # delete the existing view
        self.__selected_transfer_account = self.__account_system.get_account(selection)
        try:
            self._other_view = self._other_views[
                self.__selected_transfer_account.account_type
            ](self.frame)
        except KeyError:
            raise TypeError(
                "selection {0} has no corresponding AccountView".format(
                    self.__selected_transfer_account.account_type
                )
            )

        self._other_view.load_into_view(self.__selected_transfer_account)
        self._other_view.frame.grid(
            sticky=tkinter.E + tkinter.N, row=1, column=1, padx=5, pady=5
        )

    def populate_listbox(self, accounts):
        """
        Populate the selection list with the given accounts

        Attributes
        ----------
        accounts : list[Account.Account]
            list of accounts to populate the list with

        Returns
        -------
        None
        """
        self._selector.populate_listbox(list(accounts))
