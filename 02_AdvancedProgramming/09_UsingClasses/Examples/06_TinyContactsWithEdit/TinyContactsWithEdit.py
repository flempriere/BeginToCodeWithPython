# Example 9.6 Tiny Contacts with Edit
#
# An improved version of Tiny Contacts that supports editing
# existing contacts. Expands the book implementation with the
# additional capability to support duplicates

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


def find_contacts(search_name):
    """
    Finds the contacts with the matching name

    Params
    ------
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


def edit_contacts():
    """
    Reads in a name to search for and then allows the user to
    edit the details of the contact.

    If there are no matching contacts the function will indicate
    that the name was not found

    Returns
    -------
    None
    """
    print("Edit Contact")
    contacts = find_contacts(BTCInput.read_text("Enter the contact name: "))

    print("Found", len(contacts), "matches")

    if len(contacts) > 0:
        for contact in contacts:
            print("Name:", contact.name)
            print("Address:", contact.address)
            print("Telephone:", contact.telephone)
            edit = BTCInput.read_int_ranged(
                "Edit this contact? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            )
            if edit:
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
    else:
        print("This name was not found")


menu = """Tiny Contacts

1. New Contact
2. Find Contact
3. Edit Contact
4. Exit Program

Enter your command: """

while True:
    command = BTCInput.read_int_ranged(prompt=menu, min_value=1, max_value=4)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contacts()
    elif command == 3:
        edit_contacts()
    elif command == 4:
        break
    else:
        raise ValueError("Unexpected command id found: " + str(command))
