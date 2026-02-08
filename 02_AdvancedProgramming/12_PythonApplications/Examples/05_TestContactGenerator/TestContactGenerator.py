# Example 12.5 Test Contact Generator
#
# Demonstrates using yield to generate test Contacts for the
# time tracker application


class Contact:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0

    @staticmethod
    def create_test_contacts():
        phone_number = 1000000
        hours_worked = 0
        for first_name in ("Rob", "Mary", "Jenny", "Davis", "Chris", "Imogen"):
            for second_name in ("Miles", "Brown"):
                full_name = first_name + " " + second_name
                address = full_name + "'s house"
                telephone = str(phone_number)
                contact = Contact(full_name, address, telephone)
                contact.hours_worked = hours_worked
                hours_worked = hours_worked + 1
                yield contact


for contact in Contact.create_test_contacts():
    print(contact.name)

contacts = list(Contact.create_test_contacts())

for contact in contacts:
    print(
        """{0}
Address: {1}
Telephone: {2}
Hours worked: {3}
""".format(contact.name, contact.address, contact.telephone, contact.hours_worked)
    )
