# Example 5.1: One Handed Clock
# Uses time to display the hour

import time

current_time = time.localtime()
hour = current_time.tm_hour

print("The hour is", hour)
