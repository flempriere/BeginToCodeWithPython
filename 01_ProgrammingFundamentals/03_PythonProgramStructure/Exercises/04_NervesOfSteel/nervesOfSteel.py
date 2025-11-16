# Nerves of Steel
# Implements the Nerves of Steel Party Game
# Players stand
# Generates a random time interval
# All players standing after the time interval expires lose
# Last to sit down before the interval expires wins

import snaps

import random
import time

snaps.display_message("Players Stand")
time.sleep(random.randint(5, 20))
snaps.display_message("Last to sit down wins", color=(0, 255, 0))

time.sleep(5)  # so program doesn't immediately end
