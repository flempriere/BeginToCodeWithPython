# Example 6.5: Improved Handling Invalid Text
#
# Extends Example 6.4 by preventing the user from issuing a
# keyboard interrupt to stop the program

ride_number_valid = False  # create and set a flag to False
while not ride_number_valid:  # repeats while flag is False
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)  # can throw a ValueError
        ride_number_valid = True  # successfully read a number
    except ValueError:  # catch the ValueError
        print("Invalid number. Please enter a number in digits")
    except KeyboardInterrupt:  # catches the interrupt
        print("You do not have permission to interrupt this program")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)  # type: ignore
