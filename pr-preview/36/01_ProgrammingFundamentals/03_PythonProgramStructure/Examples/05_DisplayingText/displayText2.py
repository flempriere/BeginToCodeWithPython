# Example 3.5.2 Displaying Text via Snaps
#
# Extends the previous example by demonstrating
# adding color, size, text position

import time

import snaps

snaps.display_message(
    "This is smaller text in green on the top left",
    color=(0, 255, 0),
    size=50,
    horiz="left",
    vert="top",
)
time.sleep(5)  # add a sleep for 5 seconds so the window doesn't autoclose
