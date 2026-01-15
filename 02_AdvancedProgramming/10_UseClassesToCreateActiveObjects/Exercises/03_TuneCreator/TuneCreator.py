# Exercise 10.3 Tune Creator
#
# A simple tune editing application

import pickle
import time

import BTCInput
import snaps


class Note:
    """
    Musical note with a playback duration.

    Class Attributes
    ----------------
    min_note_id : int
        minimum valid note id
    max_note_id : int
        maximum valid note id
    """

    min_note_id = 0
    max_note_id = 12

    @staticmethod
    def valid_note(note):
        """
        Checks if a note id is valid

        Parameters
        ----------
        note : int
            id of the note to validate

        Returns
        -------
        bool
            `True` if note is valid, else `False`
        """
        if note < 0 or note > 12:
            return False
        return True

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
        if not Note.valid_note(note):
            raise ValueError(
                "invalid note {0} passed. note must be between {1} and {2}".format(
                    note, Note.min_note_id, Note.max_note_id
                )
            )
        self.__note = note
        self.__duration = duration

    @property
    def duration(self):
        """
        duration : str
            time in seconds the note is played for
        """
        return self.__duration

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


class Tune:
    """
    Represents a tune consisting of a sequence of notes of a specified duration

    Attributes
    ----------
    name : str
        name of the tune
    """

    def __init__(self, name):
        """
        Create a new `Tune` instance

        Parameters
        ----------
        name : str
            name of the tune
        """
        self.name = name
        self.__notes = []
        self.__length = 0

    def __str__(self):
        notes_string = ""
        for idx, note in enumerate(map(str, self.__notes)):
            notes_string = notes_string + str(idx) + ": " + note + "\n"

        template = """name: {0}
duration: {1}
notes:
{2}
"""
        return template.format(self.name, self.__length, notes_string)

    @property
    def length(self):
        """
        length : int | float
            total length of the tune in seconds
        """
        return self.__length

    @property
    def number_of_notes(self):
        """
        number_of_notes : int
            number of notes in the tune
        """
        return len(self.__notes)

    def play(self):
        """
        Plays the tune

        Returns
        -------
        None
        """
        for note in self.__notes:
            note.play()

    def add_note(self, note, index=None):
        """
        Add a new note to the tune

        Adds a new note to the tune, if the index is specified
        the note is inserted at that index, else the note is appended

        Parameters
        ----------
        note : Note
            note to add to the tune
        index : int | None, optional
            index to insert the note at, if `None`, the Note is appended,
            by default `None`

        Returns
        -------
        None

        See Also
        --------
        Tune.remove_note : remove a note at a given index from a `Tune`
        """
        if index is not None:
            self.__notes.insert(index, note)
        else:
            self.__notes.append(note)
        self.__length += note.duration

    def remove_note(self, index):
        """
        Remove a note from the tune

        Parameters
        ----------
        index : int
            index of the note to remove

        Returns
        -------
        Note
            the removed Note

        See Also
        --------
        Tune.add_note : insert or append a new note to a `Tune` instance
        Tune.clear_tune : remove all notes in a `Tune` instance
        """
        try:
            note = self.__notes.pop(index)
            self.__length -= note.duration
            return note
        except IndexError:
            print("Failed to remove the {0}-th note".format(index + 1))

    def clear_tune(self):
        """
        Clear all notes from the tune

        Returns
        -------
        None

        See Also
        --------
        Tune.remove_note : remove a note at a given index from a `Tune`
        """
        self.__notes.clear()
        self.__length = 0


# Edit Menu Functions
def rename_tune():
    """
    Rename the current tune to a user prompted string

    Returns
    -------
    None
    """
    print("Rename current tune")
    new_name = prompt_valid_name("Enter new name (or . to leave unchanged): ")
    if new_name != ".":
        current_tune.name = new_name


def get_new_note_from_user():
    """
    Prompts the user for a new Note

    The user is prompted for the note and duration, and the input validated
    to ensure that a valid Note object is created

    Returns
    -------
    Note
        `Note` object containing the user specified note id and duration
    """

    note_prompt = "Enter note ({0} - {1}): ".format(Note.min_note_id, Note.max_note_id)
    note = BTCInput.read_int_ranged(
        prompt=note_prompt, min_value=Note.min_note_id, max_value=Note.max_note_id
    )

    min_note_length = 0.1
    max_note_length = 1
    duration_prompt = "Enter duration ({0} - {1}): ".format(
        min_note_length, max_note_length
    )
    duration = BTCInput.read_float_ranged(
        duration_prompt, min_value=min_note_length, max_value=max_note_length
    )

    return Note(note, duration)


def add_note_to_tune():
    """
    Adds a note to the current tune

    Prompts the user to specify a new note as well as an index of
    where to insert the note in the tune (`-1` indicating append). The created
    note is then added to the current tune at the indicated index (or appended)

    Returns
    -------
    None
    """
    print("Add note to current tune")
    new_note = get_new_note_from_user()
    if current_tune.number_of_notes == 0:
        current_tune.add_note(new_note)
        print("Added note:", new_note)
        return

    insert_prompt = "Enter index to add note (0 - {0}) or -1 to append: ".format(
        current_tune.number_of_notes - 1
    )
    insertion_idx = BTCInput.read_int_ranged(
        insert_prompt, -1, current_tune.number_of_notes - 1
    )
    if insertion_idx == -1:
        insertion_idx = None
    current_tune.add_note(new_note, insertion_idx)
    print("Added note:", new_note)


def edit_note():
    """
    Modifies an existing note in the current tune

    Prompts the user for the index of the existing note to overwrite and
    then the details of the new note

    Returns
    -------
    None
    """
    print("Edit note in current tune")
    if current_tune.number_of_notes == 0:
        print("There are no notes in the current tune to edit")
        return

    edit_prompt = "Enter index of note to edit (0 - {0}): ".format(
        current_tune.number_of_notes - 1
    )
    insertion_idx = BTCInput.read_int_ranged(
        edit_prompt, 0, current_tune.number_of_notes - 1
    )
    old_note = current_tune.remove_note(insertion_idx)

    if insertion_idx == current_tune.number_of_notes:
        insertion_idx = None  # we removed the last index, so now need to append

    new_note = get_new_note_from_user()
    current_tune.add_note(new_note, insertion_idx)
    print("Note successfully edited")
    print("Note was:", old_note)
    print("Note now:", new_note)


def remove_note():
    """
    Remove the note at a user prompted index from the current tune

    Returns
    -------
    None
    """
    print("Remove note from current tune")
    remove_prompt = "Enter index of note to remove (0 - {0}): ".format(
        current_tune.number_of_notes - 1
    )
    remove_idx = BTCInput.read_int_ranged(
        remove_prompt, 0, current_tune.number_of_notes - 1
    )
    current_tune.remove_note(remove_idx)


# Main Menu Functions
def valid_tune_name(name):
    """
    Verifies that a tune name is available

    Tune names must be unique

    Parameters
    ----------
    name : str
        proposed name for a tune

    Returns
    -------
    bool
        `True` if tune name is valid else, `False`
    """
    if name == "None":
        return False
    for tune in tunes:
        if name == tune.name:
            return False
    return True


def prompt_valid_name(prompt):
    """
    Prompts the user for a valid tune name

    Loops until a valid name is provided

    Parameters
    ----------
    prompt : str
        prompt to display to the user

    Returns
    -------
    str
        string containing a valid tune name
    """
    tune_name = BTCInput.read_text(prompt)
    while not valid_tune_name(tune_name):
        print("That tune name is already in use")
        tune_name = BTCInput.read_text(prompt)

    return tune_name


def new_tune():
    """
    Create a new tune and make it the active tune

    Prompts the user for a new name for the tune, and ensures its valid
    then constructs a Tune and sets it as the current active tune

    Returns
    -------
    None

    See Also
    --------
    valid_tune_name : validates a tune name
    Tune : class used to represent a tune
    """
    print("New tune")
    global current_tune
    new_tune_name = prompt_valid_name("Enter the tune name: ")
    new_tune = Tune(new_tune_name)
    current_tune = new_tune
    tunes.append(new_tune)


def filter_tunes_by_name(search_name):
    """
    Finds tunes matching a search name

    Tunes are matched if their name is prefixed by the search name
    after normalisation (striping whitespace and lowercasing)

    Parameters
    ----------
    search_name : str
        name to search for (search uses prefix matching)

    Returns
    -------
    list[Tune]
        list of tunes matching the name. If no matches
        exist the list is empty

    """
    search_name = search_name.strip().lower()
    print(search_name)
    matched_tunes = []
    for tune in tunes:
        tune_name = tune.name.strip().lower()
        if tune_name.startswith(search_name):
            matched_tunes.append(tune)
    return matched_tunes


def list_tunes():
    """
    List all tunes matching a user-specified search string

    Returns
    -------
    None

    See Also
    --------
    filter_tunes_by_name : handles searching for tunes by name
    """
    print("List tunes")
    search_name = BTCInput.read_text("Tune names to search (press enter for all): ")
    matched_tunes = filter_tunes_by_name(search_name)
    if len(matched_tunes) == 0:
        print("No matches found")
        return
    print("Found {0} matches".format(len(matched_tunes)))
    for tune in matched_tunes:
        print("- {0} ({1:.2f} s)".format(tune.name, tune.length))


def select_tune():
    """
    Select a tune from tunes matching a user-specified search string

    Returns
    -------
    None

    See Also
    --------
    filter_tunes_by_name : handles searching for tunes by name
    """
    print("Select tune")
    search_name = BTCInput.read_text("Enter name of tune to select: ")
    matched_tunes = filter_tunes_by_name(search_name)
    if len(matched_tunes) == 0:
        print("No matches found")
        return
    print("Found {0} matches".format(len(matched_tunes)))
    for tune in matched_tunes:
        select = BTCInput.read_int_ranged(
            "Tune: {0}, select this tune? (1 - Yes, 0 - No): ".format(tune.name),
            min_value=0,
            max_value=1,
        )
        if select:
            global current_tune
            current_tune = tune
            break


def delete_tune():
    """
    Optionally delete tunes matching a user-specified search string

    Returns
    -------
    None

    See Also
    --------
    filter_tunes_by_name : handles searching for tunes by name
    """
    print("Delete tune")
    search_name = BTCInput.read_text("Enter name of tune to select: ")
    matched_tunes = filter_tunes_by_name(search_name)
    if len(matched_tunes) == 0:
        print("No matches found")
        return
    print("Found {0} matches".format(len(matched_tunes)))
    for tune in tunes:
        select = BTCInput.read_int_ranged(
            "Tune: {0}, delete this tune? (1 - Yes, 0 - No): ".format(tune.name),
            min_value=0,
            max_value=1,
        )
        if select:
            global current_tune
            if tune == current_tune:
                current_tune = no_tune
            tunes.remove(tune)


def save_tunes(file_name):
    """
    Saves the tunes to the given file

    Tunes are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file to store the tune data in

    Returns
    -------
    None

    Raises
    ------
    An Exception is raised if the file could not be saved

    See Also
    --------
    load_tunes : load tunes from a pickled file
    """
    print("Save tunes")
    with open(file_name, "wb") as out_file:
        pickle.dump(tunes, out_file)


def load_tunes(file_name):
    """
    Loads the tunes from the given file

    Tunes are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the tunes data is stored

    Returns
    -------
    None
        Tunes are loaded into the global `tunes` list

    Raises
    ------
    An Exception is raised if the file could not be loaded

    See Also
    --------
    save_tunes : save playlists as a pickled file
    """
    global tunes  # connect to global track list to load into
    print("Load tunes")
    with open(file_name, "rb") as input_file:
        tunes = pickle.load(input_file)


def run_edit_menu():
    first_option_id = 1
    last_option_id = 8

    edit_tune_menu_template = """Editing Tune
Current Tune: {0}
1. Rename Tune
2. Display Tune
3. Play Tune
4. New Note
5. Edit Note
6. Remove Note
7. Clear Tune
8. Finish Editing

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            edit_tune_menu_template.format(current_tune.name),
            min_value=first_option_id,
            max_value=last_option_id,
        )

        if command == 1:
            rename_tune()
        elif command == 2:
            print(current_tune)
        elif command == 3:
            print("Playing", current_tune.name)
            current_tune.play()
        elif command == 4:
            add_note_to_tune()
        elif command == 5:
            edit_note()
        elif command == 6:
            if current_tune.number_of_notes == 0:
                print("No notes to remove")
                continue
            remove_note()
        elif command == 7:
            print("Cleared", current_tune.name)
            current_tune.clear_tune()
        elif command == 8:
            break
        else:
            raise ValueError(
                "Unexpected command id: {0} found in Edit Menu".format(command)
            )


def run_main_menu():
    first_option_id = 1
    last_option_id = 7

    main_menu_template = """Tune Editor
Current Tune: {0}

1. New Tune
2. List Tunes
3. Select Tune
4. Play Tune
5. Edit Tune
6. Delete Tune
7. Exit program

Enter your command: """

    while True:
        command = BTCInput.read_int_ranged(
            main_menu_template.format(current_tune.name),
            min_value=first_option_id,
            max_value=last_option_id,
        )
        if command == 1:
            new_tune()
        elif command == 2:
            list_tunes()
        elif command == 3:
            select_tune()
        elif command == 7:
            try:
                save_tunes(tune_file_name)
            except:  # noqa: E722
                print("Failed to save tunes")
            break
        elif current_tune.name == "None":
            print("No tune currently selected")
            continue
        elif command == 4:
            current_tune.play()
        elif command == 5:
            run_edit_menu()
        elif command == 6:
            delete_tune()
        else:
            raise ValueError(
                "Unexpected command id: {0} found in Main Menu".format(command)
            )


tune_file_name = "tunes.pickle"
try:
    load_tunes(tune_file_name)
except:  # noqa: E722
    print("Tunes file not found")
    tunes = []
no_tune = Tune("None")
current_tune = no_tune

run_main_menu()
