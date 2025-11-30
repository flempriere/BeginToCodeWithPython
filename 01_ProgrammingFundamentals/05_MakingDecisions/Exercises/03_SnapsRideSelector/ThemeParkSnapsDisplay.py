# Exercise 5.3: Snaps Ride Selector
# Reimplments the entirety of the Theme Park Ride Selector using
# a snaps interface, and adds some audio ques to warn the user
# when they are ineligable for ride

import time
import snaps


snaps.display_image("themepark.png")

prompt = """Welcome to our Theme Park
      These are the available ride:

      1. Scenic River Cruise
      2. Carnival Carousel
      3. Jungle Adventure Water Splash
      4. Downhill Mountain Run
      5. The Regurgitator

      Select your ride: """

ride_number_text = snaps.get_string(prompt, vert="bottom", max_line_length=3)
confirm = "Ride " + ride_number_text

snaps.display_message(confirm)
time.sleep(2)  # gives user time to read the output

ride_number = int(ride_number_text)

if ride_number == 1:
    msg = confirm + "\nScenic River Cruise\n\nThere are no age limits for this ride"
    snaps.display_message(msg, size=100)
else:  # need to get the age of the user
    age_text = snaps.get_string(
        "Please enter your age: ", vert="bottom", max_line_length=3
    )
    age = int(age_text)

    if ride_number == 2:
        msg = confirm + "\nCarnival Cruise"
        if age >= 3:
            msg = msg + "\n\nYou can go on the ride"
            snaps.display_message(msg, size=100)
        else:
            snaps.play_sound("siren.wav")
            msg = msg + "\n\nSorry, you are too young"
            snaps.display_message(msg, size=100)
    if ride_number == 3:
        msg = confirm + "\nJungle Adventure Water Splash"
        if age >= 6:
            msg = msg + "\n\nYou can go on the ride"
            snaps.display_message(msg, size=100)
        else:
            msg = msg + "\n\nSorry, you are too young"
            snaps.play_sound("siren.wav")
            snaps.display_message(msg, size=100)
    if ride_number == 4:
        msg = confirm + "\nDownhill Mountain Run"
        if age >= 12:
            msg = msg + "\n\nYou can go on the ride"
            snaps.display_message(msg, size=100)
        else:
            msg = msg + "\n\nSorry, you are too young"
            snaps.play_sound("siren.wav")
            snaps.display_message(msg, size=100)
    if ride_number == 5:
        msg = confirm + "\nThe Regurgitator"
        if age >= 12:
            # first check age not too lowe
            if age > 70:
                # Age is too old
                msg = msg + "\n\nSorry, you are too old"
                snaps.play_sound("siren.wav")
                snaps.display_message(msg, size=100)
            else:
                msg = msg + "\n\nYou can go on the ride"
                snaps.display_message(msg, size=100)
        else:
            msg = msg + "\n\nSorry, you are too young"
            snaps.display_message(msg, size=100)
time.sleep(5)
