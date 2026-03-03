"""
Exercise 13.3 Bank Account Application

Provides an implementations for a graphics-based user interface to a Bank Account System

Routine Listings
----------------
BankAccountApplication
    Class wrapping a storage class in a graphics-based user interface layer.
    Assumes the storage class supports the `Data.Account.Account` interface
    for it's underlying items

See Also
--------
Data : Package defining storage and Account modules for a Bank
"""

import tkinter
import tkinter.messagebox

from Data import Account

from UI.GUI import AccountSelector, AccountView


class BankAccountApplication:
    def __init__(self, filename, storage_class):
        BankAccountApplication.__filename = filename
        self._program_title = "Bank Account System"
        try:
            self.__account_system = storage_class.load(filename)
        except:  # noqa: E722
            tkinter.messagebox.showwarning(
                title=self._program_title,
                message="Failed to load Accounts\nCreating a new database",
            )
            self.__account_system = storage_class()

        self._username = "alice"
        self._selected_account = None

        self._setup_UI()

    def _setup_UI(self):
        self._root = tkinter.Tk()
        title_label = tkinter.Label(self._root, text=self._program_title)
        title_label.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, columnspan=2, padx=5, pady=5
        )

        self._setup_views()
        self._setup_selector()

    def _setup_views(self):
        self._views = {
            "Savings": AccountView.SavingsAccountView(self._root),
            "LongTerm": AccountView.LongTermSavingsAccountView(self._root),
            "Credit": AccountView.CreditView(self._root),
        }
        self._view = None

    def _setup_selector(self):
        self._selector = AccountSelector.AccountSelector(self._root, self)
        self._selector.frame.grid(
            sticky=tkinter.N + tkinter.S, row=2, column=0, rowspan=2, padx=5, pady=5
        )
        self._filter_stock_items()

    def _filter_stock_items(self):
        self._selector.populate_listbox(
            self.__account_system.find_users_accounts(self._username)
        )

    def got_selection(self, selection):
        self._selected_account = self.__account_system.get_account(selection)
        if isinstance(self._selected_account, Account.LongTermSavingsAccount):
            self._view = self._views["LongTerm"]
        elif isinstance(self._selected_account, Account.SavingsAccount):
            self._view = self._views["Savings"]
        elif isinstance(self._selected_account, Account.CreditAccount):
            self._view = self._views["Credit"]
        else:
            raise TypeError("selection has no corresponding AccountView")

        self._view.frame.grid(
            sticky=tkinter.E + tkinter.W, row=2, column=1, padx=5, pady=5
        )
        self._view.load_into_view(self._selected_account)

    def main_menu(self):
        self._root.mainloop()
        self.__account_system.save(BankAccountApplication.__filename)
