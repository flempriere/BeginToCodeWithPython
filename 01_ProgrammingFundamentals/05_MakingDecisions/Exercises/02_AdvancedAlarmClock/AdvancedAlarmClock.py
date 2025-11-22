# Exercise 4.2: Advanced Alarm Clock
# An Advanced Alarm Combining the Behaviour
# of most increments of the alarm clock
# and allowing you to sleep in on weekends

import time
import snaps

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
day = current_time.tm_mday
month = current_time.tm_mon
is_weekend = current_time.tm_wday >= 5

date_message = "The date is " + str(day) + "/" + str(month)
time_message = "The time is " + str(hour) + ":" + str(minute)

msg = ""
up_hour = 7 + is_weekend  # get to sleep in an extra hour on weekends

if (hour > up_hour) or (hour == up_hour and minute > 29):
    msg = msg + "TIME TO GET UP"
    snaps.play_sound("siren.wav")
else:
    msg = msg + "Go back to bed!"
msg = msg + "\n" + date_message + "\n" + time_message
snaps.display_message(msg, size=50)
time.sleep(10)  # leave time for the sound and to read
