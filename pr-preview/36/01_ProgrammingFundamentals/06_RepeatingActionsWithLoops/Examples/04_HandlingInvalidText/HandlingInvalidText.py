# Example 6.4: Handling Invalid Text
#
# Combines loops and exception handling to prompt a user
# for a valid number and repeat until a number is provided

ride_number_valid = False  # create and set a flag to False
while not ride_number_valid:  # repeats while flag is False
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)  # can throw a ValueError
        ride_number_valid = True  # successfully read a number
    except ValueError:  # catch the ValueError
        print("Invalid number. Please enter a number in digits")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)  # type: ignore
