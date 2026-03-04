"""
Exercise 13.3h Bank Account Application

Provides an implementations for a graphics-based user interface to a Bank Account System

Classes
-------
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

from Data import Account, AccountFactory

from UI.GUI import (
    AccountBalanceEditor,
    AccountCreation,
    AccountSelector,
    AccountView,
    ManageLongTermAccountView,
)


class BankAccountApplication:
    """
    Provides a graphical interface for a Bank Account System
    """

    def __init__(self, filename, storage_class):
        """
        Create a new `BanAccountApplication`

        Parameters
        ----------
        filename : str
            file to save the system in, the program will try to load
            from the file
        storage_class : AccountSystem
            class to use for the underlying data storage. The data will
            first attempt to be loaded, otherwise a new instance is
            created
        """
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
        self.__authoriser = AccountFactory.AccountAuthoriser(
            self.__account_system
        )  # validates and creates new accounts

        self._username = ""  # no user to start
        self._selected_account = None  # no account to start

        self._setup_UI()

    def _setup_UI(self):
        """
        Configure and setup the user interface

        Returns
        -------
        None
        """
        # set up program title
        self._root = tkinter.Tk()
        title_label = tkinter.Label(self._root, text=self._program_title)
        title_label.grid(sticky=tkinter.E + tkinter.W, row=0, column=0, padx=5, pady=5)

        # configure the widgets
        self._setup_views()
        self._setup_selector()
        self._setup_balance_editor()
        self._setup_account_creation()

        # configure the button to launch long-term account management
        def launch_manage_long_term_view():
            """
            Binding function that launches the manage long term account
            window for the currently selected long term account

            Returns
            -------
            None
            """
            if self._selected_account is None:
                tkinter.messagebox.showerror(message="No account selected")
                return
            dlg = tkinter.Toplevel(self._root)
            manage_view = ManageLongTermAccountView.ManageLongTermAccountView(
                dlg, self._selected_account, self.__account_system
            )
            manage_view.frame.grid()
            other_accounts = set(
                self.__account_system.find_users_accounts(self._username)
            ).difference({self._selected_account})
            manage_view.populate_listbox(other_accounts)
            dlg.transient(self._root)
            dlg.wait_visibility()
            dlg.grab_set()
            dlg.wait_window()

        self._manage_long_term_button = tkinter.Button(
            self._root, text="Manage Term Account", command=launch_manage_long_term_view
        )
        self._manage_long_term_button.grid(
            sticky=tkinter.W, row=4, column=1, padx=5, pady=5
        )
        self._manage_long_term_button.config(state=tkinter.DISABLED)

    def _setup_views(self):
        """
        Setup and configure the Account Display section of the program

        Returns
        -------
        None
        """
        # store the possible views
        # set default to a blank savings account
        self._views = AccountView.account_views_dictionary
        self._view = self._views[Account.SavingsAccount.account_type](self._root)
        self._view.frame.grid(
            sticky=tkinter.E + tkinter.W, row=2, column=1, columnspan=2, padx=5, pady=5
        )

    def _setup_selector(self):
        """
        Setup the Account Selection Listbox and the User Entry

        Returns
        -------
        None
        """
        # setup the selection widget
        self._selector = AccountSelector.AccountSelector(self._root, self)
        self._selector.frame.grid(
            sticky=tkinter.N + tkinter.S, row=2, column=0, rowspan=2, padx=5, pady=5
        )

        # populate the initial list of accounts
        self._filter_user_accounts()

        # add the entry box for the username
        self._username_entry = tkinter.Entry(self._root, width=40)
        self._username_entry.grid(
            sticky=tkinter.E + tkinter.W, row=1, column=1, padx=5, pady=5
        )

        # and connect to the button
        def update_username():
            """
            Binding function handling when the username is changed

            This function has to update the current username and then,

            1. Set the list of viewable accounts
            2. clear the currently selected account and view

            Returns
            -------
            None
            """
            self._username = self._username_entry.get()
            self._filter_user_accounts()

            self._selected_account = None
            self._view.clear_view()

        user_button = tkinter.Button(
            self._root, text="Select Account Holder:", command=update_username
        )
        user_button.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)

    def _setup_balance_editor(self):
        """
        Setup and configure the component for withdrawing and depositing into accounts

        Returns
        -------
        None
        """
        self._balance_editor = AccountBalanceEditor.AccountBalanceEditor(
            self._root, self
        )
        self._balance_editor.frame.grid(
            sticky=tkinter.E + tkinter.W, row=3, column=1, padx=5, pady=5
        )
        self._balance_editor.account = self._selected_account

    def _setup_account_creation(self):
        """
        Setup and configure the component for creating new accounts

        Returns
        -------
        None
        """
        creation_frame = tkinter.Frame(self._root)

        # create account label and the account selection option menu
        create_account_label = tkinter.Label(creation_frame, text="Open a New Account")
        create_account_label.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, columnspan=2, padx=5, pady=5
        )
        account_creator = AccountSelector.AccountTypeSelection(
            creation_frame, Account.account_dictionary.keys()
        )
        account_creator.frame.grid(
            sticky=tkinter.E + tkinter.W, row=1, column=0, padx=5, pady=5
        )

        creation_frame.grid(sticky=tkinter.E, row=4, column=0, padx=5, pady=5)

        def applied_for_account():
            """
            binding function that takes the current selected account type
            and creates the appropriate window for creating a new account

            Returns
            -------
            None
            """
            if self._username == "":
                tkinter.messagebox.showerror(
                    message="Could not create account\nNo account holder selected"
                )
                return

            try:
                account_type = account_creator.get()

                # set up the window to display the application form
                dlg = tkinter.Toplevel(self._root)
                dialog_widget = AccountCreation.AccountCreationWidget(dlg, self)

                # create the application form and add it to the window
                application_form = AccountCreation.account_creation_dictionary[
                    account_type
                ](dialog_widget.frame)
                application_form.frame.grid(
                    sticky=tkinter.E + tkinter.W, row=0, column=0, padx=5, pady=5
                )

                def factory_fn():
                    """
                    Factory function for creating a new account

                    Get's the appropriate factory method from the authoriser
                    and links to the application form widget to receive any
                    additional input

                    Implicitly assumes that the returned dictionary keys
                    correspond to the function arguments so that they can be
                    expanded out with `**`

                    Returns
                    -------
                    Account.Account
                        A new account object
                    """
                    return self.__authoriser.factory_map[account_type](
                        self._username, **application_form.get()
                    )

                dialog_widget.register_account_creation_factory(factory_fn)
                dialog_widget.frame.grid()
                dlg.transient(self._root)
                dlg.wait_visibility()
                dlg.grab_set()
                dlg.wait_window()

            except KeyError as e:
                tkinter.messagebox.showerror(
                    message="Could not create account:\n{0}".format(e)
                )

        new_account_button = tkinter.Button(
            creation_frame, text="Apply for account", command=applied_for_account
        )
        new_account_button.grid(
            sticky=tkinter.E + tkinter.W, row=2, column=0, padx=5, pady=5
        )

    def _filter_user_accounts(self):
        """
        Populate the account selection list with the accounts associated
        with the current user

        Returns
        -------
        None
        """
        self._selector.populate_listbox(
            self.__account_system.find_users_accounts(self._username)
        )

    def got_selection(self, selection):
        """
        Handles the selection in the account list changing

        This method removes the old account view, and then installs the
        new one loading the selected account. If the account is a matured
        long term account the button to manage a long term account is activated,
        else it is disabled.

        Parameters
        ----------
        selection : str
            account number of the selected account

        Returns
        -------
        None

        Raises
        ------
        TypeError
            Raised if there is matching View for the returned account
        """
        # clear the current view and construct the relevant new one
        self._view.frame.grid_forget()  # delete the existing view
        self._selected_account = self.__account_system.get_account(selection)
        try:
            self._view = self._views[self._selected_account.account_type](self._root)
            if (
                self._selected_account.account_type
                == Account.LongTermSavingsAccount.account_type
                and self._selected_account.has_matured()
            ):
                # activate the manage long term button if a long term
                # account is selected and has matured
                self._manage_long_term_button.config(state=tkinter.NORMAL)
            else:
                # keep it disabled
                self._manage_long_term_button.config(state=tkinter.DISABLED)
        except KeyError:
            raise TypeError(
                "Selection {0} has no corresponding AccountView".format(
                    self._selected_account.account_type
                )
            )

        self._view.frame.grid(
            sticky=tkinter.E + tkinter.W, row=2, column=1, padx=5, pady=5
        )
        # ensure that all subcomponents have the correct selected account
        self._view.load_into_view(self._selected_account)
        self._balance_editor.account = self._selected_account

    def balance_changed(self):
        """
        Handles the selected account balance changing

        Reloads the view to update the displayed balance

        Returns
        -------
        None
        """
        self._view.load_into_view(self._selected_account)

    def account_created(self, account):
        """
        Handles a new account being created

        Stores the new account in the storage class and reloads the
        list of accounts

        Parameters
        ----------
        account : Account.Account
            newly created account

        Returns
        -------
        None
        """
        self.__account_system.add_new_account(account)
        self._filter_user_accounts()

    def main_menu(self):
        """
        Display and run the program

        Run the main program. Saves the changes on exit

        Returns
        -------
        None
        """
        self._root.mainloop()
        self.__account_system.save(BankAccountApplication.__filename)
