# Example 5.11: Snaps get_string function
#
# Demonstrates using the get_string function
# in snaps to get user input via a graphical
# interface

import time

import snaps

name = snaps.get_string("Enter your name: ")
snaps.display_message("Hello " + name)

time.sleep(5)
