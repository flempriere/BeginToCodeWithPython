# Example 8.22 Day Name If
#
# Uses a if, elif, else construction to convert an integer
# to a string representation of the day of the week

import time

current_time = time.localtime()
day_number = current_time.tm_wday

if day_number == 0:
    day_name = "Monday"
elif day_number == 1:
    day_name = "Tuesday"
elif day_number == 2:
    day_name = "Wednesday"
elif day_number == 3:
    day_name = "Thursday"
elif day_number == 4:
    day_name = "Friday"
elif day_number == 5:
    day_name = "Saturday"
elif day_number == 6:
    day_name = "Sunday"
else:
    raise ValueError("Unexpected day_number " + str(day_number) + " encountered")

print(day_name)
