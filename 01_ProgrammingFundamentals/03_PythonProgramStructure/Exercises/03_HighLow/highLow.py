# High-Low
# Implements the High-Low Party game
# Generates a random number in the interval [1, 10]
# Sleeps for a period of time
# Shows another number
# Players are asked to guess if this second number will be higher or lower

import snaps
import random
import time

snaps.display_message("The first number is...")
time.sleep(5)  # sleep so people can read the first message
snaps.display_message(random.randint(1, 10))
time.sleep(3)  # leave time to read the number
snaps.display_message("Will the next be higher or lower?")

# sleep for 20 seconds total, with a message to raise the tension with 5s left
time.sleep(15)
snaps.display_message("The second number is...")
time.sleep(5)

snaps.display_message(random.randint(1, 10))
time.sleep(10)  # leave time for the players to read
