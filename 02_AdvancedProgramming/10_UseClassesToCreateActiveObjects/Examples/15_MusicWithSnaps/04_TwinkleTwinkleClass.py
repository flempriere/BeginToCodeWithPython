# Example 10.15.4 Twinkle Twinkle with Classes
#
# Modifies the data driven tuple implementation by definining a lightweight
# Note class

import time

import snaps


class Note:
    """
    Musical note with a playback duration.
    """

    def __init__(self, note, duration):
        """
        Create a Note instance

        Parameters
        ----------
        note : int
            id of the note to play
        duration : int | float
            duration of the note
        """
        self.__note = note
        self.__duration = duration

    def play(self):
        """
        play the note

        plays the note then pauses for the specified duration
        """
        snaps.play_note(self.__note)
        time.sleep(self.__duration)


tune = [
    Note(note=0, duration=0.4),
    Note(note=0, duration=0.4),
    Note(note=7, duration=0.4),
    Note(note=7, duration=0.4),
    Note(note=9, duration=0.4),
    Note(note=9, duration=0.4),
    Note(note=7, duration=0.8),
    Note(note=5, duration=0.4),
    Note(note=5, duration=0.4),
    Note(note=4, duration=0.4),
    Note(note=4, duration=0.4),
    Note(note=2, duration=0.4),
    Note(note=2, duration=0.4),
    Note(note=0, duration=0.8),
]

for note in tune:
    note.play()
