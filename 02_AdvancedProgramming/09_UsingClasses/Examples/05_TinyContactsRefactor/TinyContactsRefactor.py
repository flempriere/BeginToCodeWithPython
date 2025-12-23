# Example 9.5 Tiny Contacts Refactor
#
# Refactored version of Tiny Contacts that seperates out the search
# functionality from the display functionality

import BTCInput


class Contact:
    """
    Stores Contact Information

    Attributes
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).
    """

    pass


contacts = []


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
    new_contact = Contact()
    new_contact.name = BTCInput.read_text("Enter the contact name: ")  # type: ignore
    new_contact.address = BTCInput.read_text("Enter the contact address: ")  # type: ignore
    new_contact.telephone = BTCInput.read_text("Enter the contact phone: ")  # type: ignore
    contacts.append(new_contact)


def find_contacts(search_name):
    """
    Finds the contacts with the matching name

    Parameters
    ----------
    search_name : str
        Name to search for (uses prefix matching)

    Returns
    -------
    list[Contact]
        list of contacts matching the `search_name`, if no
        matches exist the list is empty
    """
    search_name = search_name.strip().lower()
    results = []
    for contact in contacts:
        name = contact.name.strip().lower()
        if name.startswith(search_name):
            results.append(contact)
    return results


def display_contacts():
    """
    Prompts the user for a contact name and
    displays all matching contacts

    Returns
    -------
    None
    """
    print("Find contact")
    contacts = find_contacts(BTCInput.read_text("Enter the contact name: "))
    if len(contacts) > 0:
        for contact in contacts:
            print("Name: ", contact.name)
            print("Address: ", contact.address)
            print("Telephone: ", contact.telephone, "\n")
    else:
        print("This name was not found")


menu = """Tiny Contacts

1. New Contact
2. Find Contact
3. Exit Program

Enter your command: """

while True:
    command = BTCInput.read_int_ranged(prompt=menu, min_value=1, max_value=3)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contacts()
    elif command == 3:
        break
    else:
        raise ValueError("Unexpected command id found: " + str(command))
