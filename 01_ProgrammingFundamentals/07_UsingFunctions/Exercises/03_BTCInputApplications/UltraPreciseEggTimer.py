# Exercise 7.2.2 Ultra-Precise Egg Timer
#
# Implementation of Ultra-Precise Egg Timer using BTCInput

import time

import BTCInput

egg_time = BTCInput.read_float("Enter the cooking time in seconds: ")

print("Put the egg in boiling water now")
input("Press enter to continue once the egg is in...")

time.sleep(egg_time)

print("Take the egg out now")
print("Take the egg out now")
