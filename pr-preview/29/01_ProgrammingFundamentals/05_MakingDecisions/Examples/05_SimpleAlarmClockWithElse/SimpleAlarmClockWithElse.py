# Example 5.5: Simple Alarm Clock
#
# Variant of the Simple Alarm Clock
# that modifies the output depending on if its time to get up

import time

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    print("IT IS TIME TO GET UP")
else:
    print("Go back to bed")
