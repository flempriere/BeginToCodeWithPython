# Exercise 6.1 Looping Ride Selector
#
# Wraps the Ride Selector Program in a while
# loop to allow the user to look at multiple rides

run_program = True

while run_program:
    print("""Welcome to our Theme Park
        These are the available ride:

        1. Scenic River Cruise
        2. Carnival Carousel
        3. Jungle Adventure Water Splash
        4. Downhill Mountain Run
        5. The Regurgitator
        Any other number to quit...
        """)

    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)

    if ride_number < 1 or ride_number > 5:
        run_program = False
    elif ride_number == 1:
        print("You have selected Scenic River Cruise")
        print("There are no age limits for this ride")
    else:  # need to get the age of the user
        age_text = input("Please enter your age: ")
        age = int(age_text)

        if ride_number == 2:
            print("You have selected the Carnival Carousel")
            if age >= 3:
                print("You can go on the ride")
            else:
                print("Sorry, you are too young")
        if ride_number == 3:
            print("You have selected Jungle Adventure Water Splash")
            if age >= 6:
                print("You can go on the ride")
            else:
                print("Sorry, you are too young")
        if ride_number == 4:
            print("You have selected Downhill Mountain Run")
            if age >= 12:
                print("You can go on the ride")
            else:
                print("Sorry, you are too young")
        if ride_number == 5:
            print("You have selected The Regurgitator")
            if age >= 12:
                # first check age not too lowe
                if age > 70:
                    # Age is too old
                    print("Sorry, you are too old")
                else:
                    # In the valid range
                    print("You can go on the ride")
            else:
                # Age is too young
                print("Sorry, you are too young")
