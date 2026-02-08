# Example 10.15.3 Twinkle Twinkle with Tuples
#
# Converts play notes to a data-driven program using tuples to specify notes
# and how long to pause after

import time

import snaps

tune = [
    (0, 0.4),
    (0, 0.4),
    (7, 0.4),
    (7, 0.4),
    (9, 0.4),
    (9, 0.4),
    (7, 0.8),
    (5, 0.4),
    (5, 0.4),
    (4, 0.4),
    (4, 0.4),
    (2, 0.4),
    (2, 0.4),
    (0, 0.8),
]

for note in tune:
    note_id, sleep_time = note
    snaps.play_note(note_id)
    time.sleep(sleep_time)
