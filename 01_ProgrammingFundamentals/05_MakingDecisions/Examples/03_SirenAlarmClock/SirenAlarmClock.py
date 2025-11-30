# Example 5.3: Siren Alarm Clock
# Improves the Simple Alarm Clock to also play a sound

import time

import snaps

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    snaps.display_message("TIME TO GET UP")
    snaps.play_sound("siren.wav")
    # pause the program to give time for the sound to play
    time.sleep(10)
