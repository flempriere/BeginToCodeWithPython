"""
Exercise 13.3e Account Creation

Provides Graphical widgets for creating bank accounts

Classes
-------
ApplicationForm
    Abstract class for providing a framework for providing forms to the user
SavingsAccountApplicationForm
    Class providing an application form for a Savings Account
LongTermSavingsAccountApplicationForm
    Class providing an application for for a LongTermSavingsAccount
CreditAccountApplication
    Class providing an application form for a CreditAccount
AccountCreationWidget
    Abstract class for providing an account creation widget. Designed to be
    used with a standalone window, and to present an `ApplicationForm`

Variables
---------
account_creation_dictionary : dict[str, ApplicationForm]
    Class mapping the `Account.Account.account_type` parameter to the
    corresponding `ApplicationForm` class
"""

import abc
import tkinter
import tkinter.messagebox

from Data import Account


class ApplicationForm(abc.ABC):
    """
    Abstract class representing an account application form

    This class should be overwritten with the required fields to get
    the information required from the user to apply for an account.

    The information should be accessed via the `get` method which should
    be overwritten by a class

    Attributes
    ----------
    frame
        frame containing the elements of the widget
    """

    def __init__(self, root):
        """
        create a new `ApplicationForm`

        This is an abstract class and the constructor should not be
        called directly

        Parameters
        ----------
        root
            parent widget
        """
        self.frame = tkinter.Frame(root)

    @abc.abstractmethod
    def get(self):
        """
        Return the details of an account application

        The details should be returned in the format of a dictionary
        containing key : value pairs where the key's are strings describing
        required attributes and the values are the associated values

        Returns
        -------
        dict[str, Any]
            key : value pairs describing an account application
        """
        return {}


class SavingsAccountApplicationForm(ApplicationForm):
    """
    Represents a graphical application form for a Savings Account
    """

    def get(self):
        """
        Return the details of an application for a savings account

        Returns
        -------
        dict[str, Any]
            empty dictionary
        """
        return {}


class LongTermSavingsAccountApplicationForm(ApplicationForm):
    """
    Represents a graphical application form for a Long Term Savings Account
    """

    def __init__(self, root):
        """
        Create a new `LongTermSavingsAccountApplicationForm`

        Parameters
        ----------
        root
            parent widget
        """
        super().__init__(root)
        self._term_limit_entry = tkinter.Entry(self.frame, width=10)
        term_limit_label = tkinter.Label(
            self.frame,
            text="Enter Term Limit ({0} - {1} weeks".format(
                Account.LongTermSavingsAccount.min_term_limit,
                Account.LongTermSavingsAccount.max_term_limit,
            ),
        )

        term_limit_label.grid(sticky=tkinter.E, row=0, column=0, padx=5, pady=5)
        self._term_limit_entry.grid(sticky=tkinter.E, row=0, column=1, padx=5, pady=5)

    def get(self):
        """
        Return the details of an application for a long term savings account

        Returns
        -------
        dict[str, int]
            dictionary containing the term limit keyed by "term_limit"
        """
        return {"term_limit": int(self._term_limit_entry.get())}


class CreditAccountApplicationForm(ApplicationForm):
    """
    Represents a graphical application form for a credit account
    """

    def __init__(self, root):
        """
        Create a new `CreditAccountApplicationForm`

        Parameters
        ----------
        root
            parent widget
        """
        super().__init__(root)
        self._withdrawal_limit_entry = tkinter.Entry(self.frame, width=10)
        withdrawal_limit_label = tkinter.Label(
            self.frame, text="Enter Withdrawal limit:"
        )

        withdrawal_limit_label.grid(sticky=tkinter.E, row=0, column=0, padx=5, pady=5)
        self._withdrawal_limit_entry.grid(
            sticky=tkinter.E, row=0, column=1, padx=5, pady=5
        )

    def get(self):
        """
        Return the details for a credit account

        Returns
        -------
        dict[str, int]
            dictionary containing the max withdrawal limit keyed by "withdrawal_limit"
        """
        return {"withdrawal_limit": int(self._withdrawal_limit_entry.get())}


class AccountCreationWidget:
    """
    Provides a basic widget for Account Creation

    This widget is designed to by contained in a separate dialog window. It displays
    a button for creating account, and logic for creating the account on click.

    The widget uses dependency injection and has a specific workflow,

    1. Create the AccountCreationWidget assigning its `root` as the dialog
       and a `receiver` to accept the `account_created(account)` message
    2. Create a widget to display to the user, to accept any required information.
       This widget should have the `AccountCreationWidget` as the parent, and be
       placed into the frame of the widget at `row=0, column=0` on the grid
    3. Define a function, that takes no arguments and creates an account. This function
       must use `ValueError` to indicate any failure conditions. The design intent
       is that this accesses any required input from the widget supplied in step 2
    4. Register the function by calling `register_account_creation_factory` and
       passing the function
    5. Accounts will now be created when the button is clicked, the call to
       `create_account` will defer to the registered function for account creation

    This allows the same generic window and user input validation logic to be
    used to display different account application forms. See the `ApplicationForm`
    class for an example widget designed to work with this class

    Attributes
    ----------
    frame
        the frame containing this component. The user should hook a widget onto
        this frame using the grid position `row=0, column=0`
    receiver
        object to receive the `account_created(account)` message
    """

    def __init__(self, root, receiver):
        """
        Create a new `AccountCreationWidget`

        Parameters
        ----------
        root
            parent widget
        receiver
            object to receive the `account_created(account)` message
        """
        if not hasattr(receiver, "account_created"):
            raise AttributeError(
                "receiver does not support the account_created(account) method"
            )
        self.frame = tkinter.Frame(root)
        self.receiver = receiver
        self._root = root
        self._factory_fn = None
        dialog_button = tkinter.Button(
            self.frame, text="Create account", command=self.create_account
        )
        dialog_button.grid(
            sticky=tkinter.E + tkinter.W, row=1, column=0, padx=5, pady=5
        )

    def register_account_creation_factory(self, account_creation_factory):
        """
        Register a function for `Account` creation

        The function should take no arguments and return an `Account` object
        when called, else raise `ValueError` if an object cannot be created

        Parameters
        ----------
        account_creation_factory : callable[None,Account.Account]
            factory function to create accounts. Must take no arguments and
            return an `Account` subclass on call. May raise `ValueError` to
            indicate failures

        Returns
        -------
        None
        """
        self._factory_fn = account_creation_factory

    def create_account(self):
        """
        Create a new account

        Defers to the registered factory function to create the account.
        Inform the user of the result and close the dialog box on success

        Returns
        -------
        None
        """
        try:
            if self._factory_fn is None:
                raise TypeError(
                    "AccountCreationWidget has no registered factory, did you forget to call register_account_creation_factory?"
                )
            account = self._factory_fn()
            tkinter.messagebox.showinfo(
                title="{0} created".format(account.account_type),
                message="Created a new {0}\n{1} - {2}".format(
                    account.account_type, account.account_holder, account.account_number
                ),
            )
            self.receiver.account_created(account)
            self._root.grab_release()
            self._root.destroy()
        except ValueError as e:
            tkinter.messagebox.showinfo(
                title="Account creation failed",
                message="Failed to create an account\n:{0}".format(e),
            )


account_creation_dictionary = {
    Account.SavingsAccount.account_type: SavingsAccountApplicationForm,
    Account.LongTermSavingsAccount.account_type: LongTermSavingsAccountApplicationForm,
    Account.CreditAccount.account_type: CreditAccountApplicationForm,
}
"""
Dictionary mapping `Account.account_type` values to the respective application form class
"""
