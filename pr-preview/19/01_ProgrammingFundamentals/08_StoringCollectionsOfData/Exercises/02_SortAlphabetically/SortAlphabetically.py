# Exercise 8.2 Sort Alphabetically
#
# A version of the Party Guests program that prints the guests out in
# alphabetical order

import BTCInput

guests = []


def sort_alphabetical():
    """
    Sorts a list alphabetically

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(guests)):
        done_swap = False
        for count in range(0, len(guests) - 1 - sort_pass):
            if guests[count] > guests[count + 1]:
                temp = guests[count]
                guests[count] = guests[count + 1]
                guests[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


number_of_guests = BTCInput.read_int_ranged(
    "Enter the number of guests (5-15): ", 5, 15
)

for count in range(1, number_of_guests + 1):
    prompt = "Enter the name of guest " + str(count) + ": "
    guests.append(BTCInput.read_text(prompt))

# sort
sort_alphabetical()

# print a heading
print("\nGuests attending:")
count = 1
for guest in guests:
    print("- ", guest)
    count = count + 1
