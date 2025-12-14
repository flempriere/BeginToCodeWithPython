# Example 8.24 Day Name Tuple
#
# Reimplements the Day Name lookup table with a tuple
# and demonstrates the immutability of the data structure

import time

current_time = time.localtime()
day_number = current_time.tm_wday

day_names = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

day_name = day_names[day_number]

print("Today is", day_name)

print("Attempting to change the lookup table...")

day_names[day_number] = "Splatterday"  # type: ignore
print("Today is", day_names[day_number])
