# Exercise 8.3 Guest List with Save
#
# A version of the Party Guests program that prints the guests out in
# alphabetical order and then prompts the user to save the list

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


def save(file_path):
    """
    Saves the guest list to a file

    Parameters
    ----------

    file_path : str
        string giving the file path to save to

    Returns
    -------
    None

    Raises
    ------
    FileException
        Raised if the save fails
    """
    print("Save the guest list in:", file_path)
    try:
        with open(file_path, "w") as output_file:
            for guest in guests:
                output_file.write(str(guest) + "\n")
    except:  # noqa: E722
        print("Something went wrong with the file")


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

user_wants_to_save = BTCInput.read_int_ranged(
    "Would you like save the list? (1 for yes, 0 for no): ", min_value=0, max_value=1
)

if user_wants_to_save:
    save_file_name = BTCInput.read_text("Enter file name to save as: ")
    save(save_file_name)
