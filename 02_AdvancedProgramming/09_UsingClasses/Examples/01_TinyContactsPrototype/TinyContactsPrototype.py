# Example 9.1 Tiny Contacts Prototype
#
# Simple stub implementation of the Tiny Contacts Prototype

import BTCInput


def new_contact():
    """
    Creates and adds a new contact to the contact book

    Returns
    -------
    None
    """
    print("Create the new contact")
    BTCInput.read_text("Enter the contact name: ")
    BTCInput.read_text("Enter the contact address: ")
    BTCInput.read_text("Enter the contact phone: ")


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
    name = BTCInput.read_text("Enter the contact name: ")
    if name == "Rob Miles":
        print("Name: Rob Miles")
        print("Address: 18 Pussycat News, London, NE1 410S")
        print("Phone: +44(1234) 56789")
    else:
        print("This name was not found.")


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
