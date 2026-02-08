# Example 8.23 Day Name List
#
# Uses a lookup table to correctly print the day

import time

current_time = time.localtime()
day_number = current_time.tm_wday

day_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

day_name = day_names[day_number]

print("Today is", day_name)
