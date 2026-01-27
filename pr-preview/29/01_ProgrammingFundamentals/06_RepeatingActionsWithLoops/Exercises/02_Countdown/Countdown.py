# Exercise 6.2: Countdown
#
# Performs a 10-second countdown

import time

time_left = 10

while time_left >= 0:
    print(time_left)
    time_left = time_left - 1
    time.sleep(1)
