# Example 9.2 Tiny Contacts Parallel Lists
#
# An implementation of Tiny Contacts that uses Parallel Lists to
# store contact data

import BTCInput

names = []
addresses = []
telephones = []


def new_contact():
    """
    Creates and adds a new contact to the contact book

    Returns
    -------
    None
    """
    print("Create the new contact")
    names.append(BTCInput.read_text("Enter the contact name: "))
    addresses.append(BTCInput.read_text("Enter the contact address: "))
    telephones.append(BTCInput.read_text("Enter the contact phone: "))


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
    name_index = 0
    for name in names:
        name = name.strip()
        name = name.lower()
        if name == search_name:
            break
        name_index = name_index + 1

    if name_index < len(names):
        print("Name: ", names[name_index])
        print("Address: ", addresses[name_index])
        print("Telephone: ", telephones[name_index])
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
