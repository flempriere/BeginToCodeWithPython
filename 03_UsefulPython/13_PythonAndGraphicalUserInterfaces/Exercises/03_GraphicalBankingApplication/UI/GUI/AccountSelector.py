"""
Exercise 13.3f Account Selector

Provides graphical components for selecting Accounts from a list

Classes
-------
AccountSelector
    class providing a `tkinter` `Listbox` based widget for selecting an account
AccountTypeSelection
    Provides a widget for selecting a new account type
"""

import tkinter


class AccountSelector:
    """
    Widget providing a list selection for Accounts

    Parameters
    -----------
    receiver
        A receiver object that is informed of any change in selection.
        The receiver must support a method, `got_selection(str)`
    frame : tkinter.Frame
        The tkinter `Frame` this component is contained in
    listbox : tkinter.Listbox
        list box to populate with stock item references
    """

    def __init__(self, root, receiver):
        """
        Create a new `AccountSelector`

        Parameters
        ----------
        root
            The parent frame or window to attach this component to
        receiver
            Object to send a message to when the selection changes.
            Must support a method `got_selection(str)`

        Raises
        ------
        AttributeError
            raised if `receiver` does not support `got_selection`
        """
        if not hasattr(receiver, "got_selection"):
            raise AttributeError(
                "Supplied receiver does not support got_selection(str)"
            )
        self.receiver = receiver
        self.frame = tkinter.Frame(root)
        self.listbox = tkinter.Listbox(self.frame)
        self.listbox.grid(
            sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S, row=0, column=0
        )

        def on_select(event):
            """
            Find the selected text in the Listbox and send it to the
            receiving object

            Bound to the `ListboxSelect` event

            Parameters
            ----------
            event
                event that triggered the function

            Returns
            -------
            None
            """
            lb = event.widget
            index = int(lb.curselection()[0])
            receiver.got_selection(lb.get(index))

        self.listbox.bind("<<ListboxSelect>>", on_select)

    def populate_listbox(self, accounts):
        """
        Populate the Listbox with a list of Accounts

        Parameters
        ----------
        accounts : list[Account]
            a list of accounts to add to the selection

        Returns
        -------
        None
        """
        self.listbox.delete(0, tkinter.END)
        for account in accounts:
            self.listbox.insert(tkinter.END, account.account_number)


class AccountTypeSelection:
    """
    Class for selecting an account type

    Provides a drop-down option menu for selecting an account type and
    a button for confirming a choice. Will then prompt a dialog for the
    user to  create that account type

    Attributes
    ----------
    frame
        parent widget
    receiver
        object to be notified when a new account is created. Must
        support the `account_created(account)` method
    """

    def __init__(self, root, values):
        """
        Create a new `AccountTypeSelection` widget

        Parameters
        ----------
        root
            parent widget
        values : list[str]
            values to populate the option menu with, corresponding
            to `Account` class acount_type values

        Raises
        ------
        AttributeError
            raised if receiver does not support the `account_created(account)` method
        """

        self.frame = tkinter.Frame(root)

        self._current_account_option = tkinter.StringVar(self.frame)

        self._account_type_option_menu = tkinter.OptionMenu(
            self.frame, self._current_account_option, *values
        )
        self._account_type_option_menu.grid(
            sticky=tkinter.E, row=1, column=0, padx=5, pady=5
        )

    def get(self):
        """
        Get the currently selected option

        Returns
        -------
        str
            Currently selected account option
        """
        return self._current_account_option.get()
