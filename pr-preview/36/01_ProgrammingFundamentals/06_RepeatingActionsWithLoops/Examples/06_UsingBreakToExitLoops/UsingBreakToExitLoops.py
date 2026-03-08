# Example 6.6 Using Break to Exit Loops
#
# Demonstrates using a break statement to exit
# a while loop from inside the loop

while True:  # use break rather than a condition to exit
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)
        break
    except ValueError:
        print("Invalid number text. Please enter digits")
    except KeyboardInterrupt:
        print("You do not have permission to interrupt this program")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)  # type: ignore
