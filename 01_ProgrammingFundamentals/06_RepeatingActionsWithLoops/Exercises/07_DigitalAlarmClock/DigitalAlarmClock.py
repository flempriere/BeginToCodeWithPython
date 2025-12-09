# Exercise 6.7: Digital Alarm Clock
#
# Integrates the Alarm Clock Functionality of
# Chapter 5, with the Digital Clock Display of Chapter 6

import time
import snaps

while True:
    current_time = time.localtime()

    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec
    day = current_time.tm_mday
    month = current_time.tm_mon
    year = current_time.tm_year
    is_weekend = current_time.tm_wday >= 5

    # draw the background
    # define day as 6am - 7pm
    if hour >= 6 and hour <= 19:
        snaps.display_image("sun.png")
    else:
        snaps.display_image("moon.png")

    # set up normal time and day clock behaviour
    date_message = "The date is " + str(day) + "/" + str(month) + "/" + str(year)
    time_message = "The time is " + str(hour) + ":" + str(minute) + ":" + str(second)
    message = date_message + "\n" + time_message

    # Play alarm and optionally append a wakeup message
    hour_to_get_up = 7 + is_weekend
    hour_to_sleep = 22
    minute_to_get_up = 30
    minute_to_sleep = 0

    wake_up_message = "TIME TO GET UP!"
    sleep_message = "TIME FOR BED!"

    # case 1: On the alarm
    if hour == hour_to_get_up and minute == minute_to_get_up and second == 0:
        snaps.play_sound("siren.wav")
        message = message + "\n" + wake_up_message
    # Past the alarm
    elif hour == hour_to_get_up and minute >= minute_to_get_up:
        message = message + "\n" + wake_up_message
    # past the alarm but before bed
    elif hour > hour_to_get_up and (
        hour < hour_to_sleep or (hour == hour_to_sleep and minute < minute_to_sleep)
    ):
        message = message + "\n" + wake_up_message
    # time for bed
    else:
        message = message + "\n" + sleep_message

    # display the message and then sleep
    snaps.display_message(message, size=100)
    time.sleep(1)
