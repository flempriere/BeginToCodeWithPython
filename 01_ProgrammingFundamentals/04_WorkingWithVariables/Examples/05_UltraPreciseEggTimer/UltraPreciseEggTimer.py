# Example 4.5
# Ultra-Precise Egg Timer
#
# A version of the Configurable Egg Timer using floating point for the input time

import time

time_text = input("Enter the cooking time in seconds: ")
time_float = float(time_text)

print("Put the egg in boiling water now")
input("Press enter to continue once the egg is in...")

time.sleep(time_float)

print("Take the egg out now")
