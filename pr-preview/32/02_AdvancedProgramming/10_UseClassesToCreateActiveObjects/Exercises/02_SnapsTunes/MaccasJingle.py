# Exercise 10.2.1 Maccas Jingle
#
# Uses the Note playback program to play the Maccas jingle

import time

import snaps


class Note:
    """
    Musical note with a playback duration.
    """

    def __init__(self, note, duration):
        """
        Create a `Note` instance

        Parameters
        ----------
        note : int
            id of the note to play
        duration : int | float
            duration of the note
        """
        self.__note = note
        self.__duration = duration

    def __str__(self):
        template = "Note: {0} Duration: {1}"
        return template.format(self.__note, self.__duration)

    def play(self):
        """
        play the note

        plays the note then pauses for the specified duration
        """
        snaps.play_note(self.__note)
        time.sleep(self.__duration)


tune = [
    Note(note=7, duration=0.3),
    Note(note=11, duration=0.3),
    Note(note=2, duration=0.3),
    Note(note=5, duration=0.3),
    Note(note=7, duration=0.5),
]

for note in tune:
    note.play()

tune_strings = map(str, tune)
print("\n".join(tune_strings))
