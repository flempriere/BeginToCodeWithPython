# Example 6.12: Digital Clock
#
# Uses a combination of loops and snaps to create a digital clock

import time
import snaps

while True:
    current_time = time.localtime()
    hour_string = str(current_time.tm_hour)
    minute_string = str(current_time.tm_min)
    second_string = str(current_time.tm_sec)

    time_string = hour_string + ":" + minute_string + ":" + second_string
    snaps.display_message(time_string)
    time.sleep(1)
