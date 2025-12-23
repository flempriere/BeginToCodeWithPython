# Example 4.3: Configurable Egg Timer
#
# Reads in a user specified time to set the timer for

import time

time_text = input("Enter the cooking time in seconds: ")
time_int = int(time_text)

print("Put the egg in boiling water now")
input("Press enter to continue once the egg is in...")

time.sleep(time_int)

print("Take the egg out now")
