# reimplements the Egg Timer Exercise using the snaps library
# to add a visual and audio component
# By Felix Lempriere

import snaps
import time

snaps.display_image("egg_timer_background.png")
snaps.display_message(
    "Drop the egg in boiling water", color=(255, 0, 0), vert="top", size=100
)
time.sleep(270)
snaps.display_message(
    "Nearly cooked, get your spoon ready!", color=(0, 0, 255), size=100
)
time.sleep(30)
snaps.play_sound("ding.wav")
snaps.display_message(
    "Egg cooked, remove now.", color=(0, 255, 0), vert="bottom", size=100
)
time.sleep(30)
