"""
Exercise 13.3 Account Selector

Provides an implementation of a graphical component for selecting Accounts from a list

Routine Listings
----------------
AccountSelector
    class providing a `tkinter` `Listbox` based widget for selecting an account
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
        self.listbox.grid(row=0, column=0)

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
