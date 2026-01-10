# Example 10.15.1 Play Notes
#
# Demonstrates using snaps to play notes

import time

import snaps

for note in range(0, 13):
    snaps.play_note(note)
    time.sleep(0.5)
input("Press enter to continue...")
