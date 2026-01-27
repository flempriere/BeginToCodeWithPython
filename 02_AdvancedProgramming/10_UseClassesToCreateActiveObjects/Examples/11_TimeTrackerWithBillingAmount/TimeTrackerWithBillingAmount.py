# Example 10.11 Time Tracker with Billing Amount
#
# Extends the Time Tracker app by adding functionality to track
# the amount to be billed to a client
#
# Provides additional support over the original example code for duplicates in
# the name search

import pickle

import BTCInput


class Contact:
    """
    Contact with a name, address and telephone number.
    Tracks the hours worked with a client

    Attributes
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).


    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """

    __min_session_length = 0.5
    __max_session_length = 3.5

    __open_fee = 30
    __hourly_fee = 50

    @staticmethod
    def valid_session_length(session_length):
        """
        Check a session length is valid

        Parameters
        ----------
        session_length : int | float
            length of a consult session in hours

        Returns
        -------
        bool
            `True` if the session length is valid else `False`
        """
        if (
            session_length < Contact.__min_session_length
            or session_length > Contact.__max_session_length
        ):
            return False
        return True

    __min_text_length = 4

    @staticmethod
    def valid_text(text):
        """
        Validates text to be stored in the contact storage

        Valid input must be have a length greater than or
        equal to `Contact.__min_text_length`

        Parameters
        ----------
        text : str
            text string to store

        Returns
        -------
        bool
            `True` if the text is valid, else `False`
        """
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        """
        name : str
            Contact Name

        Raises
        ------
        Exception
            raised if new name is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__name

    @name.setter
    def name(self, name):
        if not Contact.valid_text(name):
            raise Exception("Invalid name")
        self.__name = name

    @property
    def address(self):
        """
        address : str
            Contact Address

        Raises
        ------
        Exception
            raised if new address is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__address

    @address.setter
    def address(self, address):
        if not Contact.valid_text(address):
            raise Exception("Invalid address")
        self.__address = address

    @property
    def telephone(self):
        """
        telephone : str
            Contact Telephone

        Raises
        ------
        Exception
            raised if new telephone is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if not Contact.valid_text(telephone):
            raise Exception("Invalid telephone")
        self.__telephone = telephone

    @property
    def hours_worked(self):
        """
        hours_worked : int | float
            The hours worked on behalf of this Contact
        """
        return self.__hours_worked

    @property
    def billing_amount(self):
        """
        billing_amount : int | float
            The amount (in dollars) to bill a Contact
        """
        return self.__billing_amount

    def __init__(self, name, address, telephone):
        """
        Create a new `Contact` instance

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        """
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
        self.__billing_amount = 0

    def add_session(self, session_length):
        """
        Adds a session (in hours) to the Contacts hours

        Parameters
        ----------
        session_length : int | float
            time spent on session in hours

        Returns
        -------
        None

        Raises
        ------
        Exception
            Raised if invalid session length passed

        See Also
        --------
        Contact.valid_session_length : checks a session length is valid
        """
        if not Contact.valid_session_length(session_length):
            raise Exception("Invalid Session Length")
        self.__hours_worked = self.__hours_worked + session_length
        amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
        self.__billing_amount = self.__billing_amount + amount_to_bill


def new_contact():
    """
    Creates and adds a new contact to the contact book

    Returns
    -------
    None

    See Also
    --------
    Contact : class for storing contact information
    """
    print("Create the new contact")
    name = BTCInput.read_text("Enter the contact name: ")
    address = BTCInput.read_text("Enter the contact address: ")
    telephone = BTCInput.read_text("Enter the contact phone: ")

    try:
        contacts.append(Contact(name=name, address=address, telephone=telephone))
    except Exception as e:
        print("Invalid contact:", e)
        return


def find_contacts(search_name):
    """
    Finds the contacts with the matching name

    If the empty string is given, all contacts
    are matched

    Parameters
    ----------
    search_name : str
        Name to search for

    Returns
    -------
    list[Contact]
        list of contacts matching the name, if no
        matches exist the list is empty
    """
    search_name = search_name.strip().lower()
    results = []
    for contact in contacts:
        name = contact.name.strip().lower()
        if name.startswith(search_name):
            results.append(contact)
    return results


def display_contact(contact):
    """
    Displays the Contact details for the supplied contact

    Parameters
    ----------
    contact : Contact
        contact to display

    Returns
    -------
    None

    See Also
    --------
    display_contacts : Displays all contacts matching a search name
    """
    print("Name:", contact.name)
    print("Address:", contact.address)
    print("Telephone:", contact.telephone)
    print("Hours worked for this Contact:", contact.hours_worked)
    print("Amount to bill:", contact.billing_amount, "\n")


def display_contacts():
    """
    Prompts the user for a contact name and
    displays all matching contacts

    Returns
    -------
    None

    See Also
    --------
    display_contact : displays a single contact
    """
    print("Find contact")
    contacts = find_contacts(
        BTCInput.read_text("Enter the contact name (Press enter to display all): ")
    )
    if len(contacts) > 0:
        for contact in contacts:
            display_contact(contact)
    else:
        print("This name was not found")


def edit_contacts():
    """
    Allows user to edit contacts matching a provided name

    Reads in a name to search for and then allows the user to
    edit the details of the contact. If there are no matching contacts
    the function will indicate that the name was not found

    Returns
    -------
    None

    See Also
    --------
    find_contacts : returns contacts matching a search name
    """
    print("Edit Contact")
    contacts = find_contacts(
        BTCInput.read_text("Enter the contact name ((Press enter to edit all)): ")
    )

    print("Found", len(contacts), "matches")

    if len(contacts) > 0:
        for contact in contacts:
            display_contact(contact)
            edit = BTCInput.read_int_ranged(
                "Edit this contact? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            )
            if not edit:
                continue
            try:
                new_name = BTCInput.read_text(
                    "Enter new name or . to leave unchanged: "
                )
                if new_name != ".":
                    contact.name = new_name
                new_address = BTCInput.read_text(
                    "Enter new address or . to leave unchanged: "
                )
                if new_address != ".":
                    contact.address = new_address
                new_phone = BTCInput.read_text(
                    "Enter new telephone or . to leave unchanged: "
                )
                if new_phone != ".":
                    contact.telephone = new_phone
            except Exception as e:
                print("Edit failed:", e)
    else:
        print("This name was not found")


def save_contacts(file_name):
    """
    Saves the contacts to the given file name

    Contacts are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file to store the contacts data in

    Returns
    -------
    None

    Raises
    ------
        Exceptions are raised if contacts could not be saved

    See Also
    --------
    load_contacts : loads contacts from a pickled file
    """
    print("Save contacts")
    with open(file_name, "wb") as out_file:
        pickle.dump(contacts, out_file)


def load_contacts(file_name):
    """
    Loads the contacts from the given file

    Contacts are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the contacts data is stored

    Returns
    -------
    None
        Contact detail is loaded into the global `contacts` value

    Raises
    ------
        Exceptions if contacts failed to load

    See Also
    --------
    save_contacts : saves contacts to a pickled file
    """
    global contacts
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        contacts = pickle.load(input_file)


def add_session():
    """
    Prompts the user to add hours worked to contacts matching a search

    If the added hours are invalid, then the session is not added an
    an exception is raised

    Returns
    -------
    None

    Raises
    ------
    Exception
        Raised if session could not be added

    See Also
    --------
    Contact.add_session : add a session to a `Contact` instance
    find_contacts : returns contacts matching a search name
    """
    print("Add Hours")
    contacts = find_contacts(
        BTCInput.read_text("Enter the contact name ((Press enter to edit all)): ")
    )

    print("Found", len(contacts), "matches")
    if len(contacts) > 0:
        for contact in contacts:
            display_contact(contact)
            if BTCInput.read_int_ranged(
                "Add Session? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            ):
                try:
                    contact.add_session(
                        BTCInput.read_float("Enter session length (in hours): ")
                    )
                    print("Updated hours succeeded:", contact.hours_worked)
                except Exception as e:
                    print("Add failed:", e)

    else:
        print("This name was not found")


def sort_contacts():
    """
    Sorts the contacts list into alphabetical order

    Returns
    -------
    None
    """
    print("Sort contacts")
    for sort_pass in range(0, len(contacts)):
        done_swap = False
        for count in range(0, len(contacts) - 1 - sort_pass):
            if contacts[count].name > contacts[count + 1].name:
                temp = contacts[count]
                contacts[count] = contacts[count + 1]
                contacts[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


menu = """Tiny Contacts

1. New Contact
2. Find Contact
3. Edit Contact
4. Add Session
5. Sort Contacts
6. Exit Program

Enter your command: """

file_name = "contacts.pickle"
try:
    load_contacts(file_name)
except:  # noqa: E722
    print("Contacts file not found")
    contacts = []

while True:
    command = BTCInput.read_int_ranged(prompt=menu, min_value=1, max_value=6)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contacts()
    elif command == 3:
        edit_contacts()
    elif command == 4:
        add_session()
    elif command == 5:
        sort_contacts()
    elif command == 6:
        try:
            save_contacts(file_name)
        except:  # noqa: E722
            print("Contacts failed to save")
        break
    else:
        raise ValueError("Unexpected command id found: " + str(command))
