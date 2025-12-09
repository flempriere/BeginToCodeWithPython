# Example 6.3: Catching Exceptions
#
# Demonstrates how to catch and handle
# an exception

try:
    ride_number_text = input("Please enter a ride number: ")
    ride_number = int(ride_number_text)
    print("You have entered", ride_number)
except ValueError:
    print("Invalid number")
