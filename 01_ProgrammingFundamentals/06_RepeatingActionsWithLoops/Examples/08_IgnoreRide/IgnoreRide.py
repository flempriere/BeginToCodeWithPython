# Example 6.8: Ignore Ride
#
# Demonstrates the use of continue to move
# to the next loop iteration, skipping remaining
# loop logic

while True:
    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)
    if ride_number == 3:
        print("sorry, this ride is unavailable")
        continue
    print("you have selected ride number: ", ride_number)
