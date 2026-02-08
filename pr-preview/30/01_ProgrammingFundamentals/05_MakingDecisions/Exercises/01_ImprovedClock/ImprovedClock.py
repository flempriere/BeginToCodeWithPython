# Exercise 5.1: Improved Clock
#
# An improved clock that displays the date and time when run

import time

current_datetime = time.localtime()

day = current_datetime.tm_mday
month = current_datetime.tm_mon
year = current_datetime.tm_year
print("The date is", day, "/", month, "/", year)

seconds = current_datetime.tm_sec
minutes = current_datetime.tm_min
hours = current_datetime.tm_hour
print("The time is", hours, ":", minutes, ":", seconds)
