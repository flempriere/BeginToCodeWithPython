# Exercise 5.4 Weather Helper
#
# Simple Weather Program that reminds the user about
# the weather conditions, with helpful text and
# pictures

import time

import snaps

temp = snaps.get_weather_temp(latitude=47.61, longitude=-122.33)
conditions = snaps.get_weather_desciption(latitude=47.61, longitude=-122.33)

if temp is None or conditions is None:
    msg = "Could not retrieve Weather..."
else:
    msg = "The temperature is: " + str(temp)
    if temp < 40:
        msg = msg + "\n\nWear a coat - it is cold out there"
        snaps.display_image("snowflake.png")
    elif temp > 70:
        msg = msg + "\n\nRemember to wear sunscreen"
        snaps.display_image("sun.png")
    msg = msg + "\n\nThe weather is " + conditions

snaps.display_message(msg, size=100, color="red")
time.sleep(5)
