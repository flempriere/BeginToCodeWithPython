# Example 9.4 Tiny Contacts Class
#
# Implementation of Tiny Contacts that uses a
# basic Contact class to containerise the information

import BTCInput


class Contact:
    """
    Stores Contact Information
    """

    pass


contacts = []


def new_contact():
    """
    Creates and adds a new contact to the contact book

    Returns
    -------
    None
    """
    print("Create the new contact")
    new_contact = Contact()
    new_contact.name = BTCInput.read_text("Enter the contact name: ")  # type: ignore
    new_contact.address = BTCInput.read_text("Enter the contact address: ")  # type: ignore
    new_contact.telephone = BTCInput.read_text("Enter the contact phone: ")  # type: ignore
    contacts.append(new_contact)


def find_contact():
    """
    Prompts the user for a name, and searches the contacts list.
    If the contact is found in the list, their full contact details
    are displayed

    Returns
    -------
    None
    """
    print("Find contact")
    search_name = BTCInput.read_text("Enter the contact name: ")
    search_name = search_name.strip()
    search_name = search_name.lower()
    result = None
    for contact in contacts:
        name = contact.name
        name = name.strip()
        name = name.lower()
        if name.startswith(search_name):
            result = contact
            break

    if result is not None:
        print("Name: ", result.name)
        print("Address: ", result.address)
        print("Telephone: ", result.telephone)
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
        find_contact()
    elif command == 3:
        break
    else:
        raise ValueError("Unexpected command id found: " + str(command))
