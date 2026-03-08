# Exercise 8.1 Party Guests
#
# A program that receives and then prints a list of party guests
# Works for between 5 and 15 guests

import BTCInput

guests = []
number_of_guests = BTCInput.read_int_ranged(
    "Enter the number of guests (5-15): ", 5, 15
)

for count in range(1, number_of_guests + 1):
    prompt = "Enter the name of guest " + str(count) + ": "
    guests.append(BTCInput.read_text(prompt))

# print a heading
print("\nGuests attending:")
count = 1
for guest in guests:
    print("- ", guest)
    count = count + 1
