# Exercise 10.1 Playlist Storage
#
# Improves the Music Storage App by allowing the user to manage multiple
# playlists

import pickle
import random

import BTCInput


def read_min_valued_integer(prompt, min_value):
    """
    Displays a prompt and reads in a integer number greater
    than or equal to min_value.

    Keyboard interrupts (CTRL+C) are ignored
    Invalid numbers are rejected
    returns a number containing the value input by the user

    Parameters
    ----------
    prompt : str
        string to display to the user before the enter the number

    min_value : int
        minimum value (inclusive) to accept from the user

    Returns
    -------
    int
        integer > 0 entered by the user
    """
    while True:
        result = BTCInput.read_int(prompt)
        if result >= min_value:
            return result
        else:
            print("That number is invalid")
            print("Number must be >", min_value)


class MusicTrack:
    """
    Music Track with a name and a length (in seconds)

    Attributes
    ----------
    name : str
        name of the music track
    length_in_seconds : int
        length of the track in seconds

    Examples
    --------
    >>> MusicTrack("Merry Christmas Everyone", 220)
    <MusicTrack ...>
    """

    def __init__(self, name, length_in_seconds):
        """
        Create a new MusicTrack instance

        Parameters
        ----------
        name : str
            name of the music track
        length_in_seconds : int
            length of the track in seconds (must be positive)

        Raises
        ------
        ValueError
                Raised if length_in_seconds is invalid
        """
        self.name = name
        if length_in_seconds <= 0:
            raise ValueError("Track length must be greater than zero")
        self.length_in_seconds = length_in_seconds

    def __str__(self):
        template = "{0} ({1} s)"
        return template.format(self.name, self.length_in_seconds)


def new_track():
    """
    Creates and adds a new track to the track storage program

    Returns
    -------
    None

    See Also
    --------
    MusicTrack : class for storing music track information
    """
    print("Add a new track")
    name = BTCInput.read_text("Enter the track name: ")
    length = read_min_valued_integer(
        "Enter the track length (in seconds): ", min_value=1
    )
    tracks.append(MusicTrack(name=name, length_in_seconds=length))


def filter_tracks_by_name(search_name, tracks_to_search):
    """
    Finds tracks matching a search name

    Filters tracks from the list `tracks_to_search` with a name
    containing `search_name` as a prefix

    Parameters
    ----------
    search_name : str
        name to search for (search uses prefix matching)

    tracks_to_search : list[MusicTrack]
        list of music tracks to search through

    Returns
    -------
    list[MusicTrack]
        list of tracks matching the name. If no matches
        exist the list is empty
    """
    search_name = search_name.strip().lower()  # normalise the search name
    results = []
    for track in tracks_to_search:
        name = track.name.strip().lower()  # normalise track word
        if name.startswith(search_name):
            results.append(track)
    return results


def edit_tracks():
    """
    Edits a user selected track

    Reads in a name to search for and then allows the user to edit
    the details of the Music Track

    If there a no matching Music Tracks the function will indicate
    that the name was not found. If multiple matches are found, the
    user will have the option to edit each of them

    Returns
    -------
    None

    See Also
    --------
    filter_tracks_by_name : filters a list of tracks by a search name
    """
    print("Edit Music Tracks")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track name to edit: "), tracks
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged(
            "Edit this track? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        ):
            new_name = BTCInput.read_text("Enter new name or . to leave unchanged: ")
            if new_name != ".":
                track.name = new_name
            new_length_in_seconds = read_min_valued_integer(
                "Enter new length (in seconds) or 0 to leave unchanged: ", min_value=0
            )
            if new_length_in_seconds != 0:
                track.length_in_seconds = new_length_in_seconds


def remove_tracks():
    """
    Removes a user selected track

    Reads in a name to search for and then allows the user to delete
    the details of the Music Track

    If there a no matching Music Tracks the function will indicate
    that the name was not found. If multiple matches are found, the
    user will have the option to delete each of them

    Returns
    -------
    None
    """
    print("Delete Music Tracks")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track name to remove: "), tracks
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Delete this track? (1 - Yes, 0 - No): ", 0, 1):
            tracks.remove(track)


def save_tracks(file_name):
    """
    Saves the music tracks to the given file

    Music tracks are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file to store the track data in

    Returns
    -------
    None

    Raises
    ------
    An Exception is raised if the file could not be saved

    See Also
    --------
    load_tracks : load music tracks from a pickled file
    """
    print("Save music tracks")
    with open(file_name, "wb") as out_file:
        pickle.dump(tracks, out_file)


def load_tracks(file_name):
    """
    Loads the music tracks from the given file

    Music Tracks are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the tracks data is stored

    Returns
    -------
    None
        Music Tracks are loaded into the global tracks list

    Raises
    ------
    An Exception is raised if the file could not be loaded

    See Also
    --------
    save_tracks : save tracks as a pickled file
    """
    global tracks  # connect to global track list to load into
    print("Load tracks")
    with open(file_name, "rb") as input_file:
        tracks = pickle.load(input_file)


def sort_low_to_high(tracks_to_sort):
    """
    Sorts tracks by increasing track length

    Sorts the music track list given by `tracks_to_sort`
    by length from shortest to greatest

    Parameters
    ----------
    tracks_to_sort : list[MusicTrack]
        list of tracks to sort
    Returns
    -------
    None

    See Also
    --------
    sort_high_to_low : sort tracks by decreasing track length
    """
    print("Sort low to high")
    for sort_pass in range(0, len(tracks)):
        done_swap = False
        for count in range(0, len(tracks) - 1 - sort_pass):
            if (
                tracks_to_sort[count].length_in_seconds
                > tracks_to_sort[count + 1].length_in_seconds
            ):
                temp = tracks_to_sort[count]
                tracks_to_sort[count] = tracks_to_sort[count + 1]
                tracks_to_sort[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def sort_high_to_low(tracks_to_sort):
    """
    Sorts tracks by decreasing track length

    Sorts the music track list given by `tracks_to_sort`
    by length from greatest to shortest

    Params
    ------
    tracks_to_sort : list[MusicTrack]

    Returns
    -------
    None

    See Also
    --------
    sort_low_to_high : sort tracks by increasing track length
    """
    print("Sort high to low")
    for sort_pass in range(0, len(tracks)):
        done_swap = False
        for count in range(0, len(tracks) - 1 - sort_pass):
            if (
                tracks_to_sort[count].length_in_seconds
                < tracks_to_sort[count + 1].length_in_seconds
            ):
                temp = tracks_to_sort[count]
                tracks_to_sort[count] = tracks_to_sort[count + 1]
                tracks_to_sort[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def display_track(track):
    """
    Displays the name and length (in seconds) of a track

    Params
    ------
    track : MusicTrack
        track to display

    Returns
    -------
    None

    See Also
    --------
    display_tracks : display all tracks in a list
    """
    print(track)


def display_tracks(tracks):
    """
    Displays all the tracks in the provided list of tracks

    Params
    ------
    list[MusicTrack]
        List of MusicTrack objcts to display

    Returns
    -------
    None

    See Also
    --------
    display_track : display a single track
    """
    if len(tracks) > 0:
        for track in tracks:
            display_track(track)
    else:
        print("No tracks found")


def find_tracks_by_name():
    """
    Displays all tracks matching a user-prompted name

    Finds and displays a list of tracks matching a
    user provided track name. If the user provides
    an empty string all tracks are displayed

    Returns
    -------
    None

    See Also
    --------
    filter_tracks_by_name : filters a list of tracks by a search name
    """
    print("Find Tracks by Name")
    search_name = BTCInput.read_text("Enter track name (Press enter to display all): ")
    matched_tracks = filter_tracks_by_name(search_name, tracks)
    display_tracks(matched_tracks)


def filter_tracks_shorter_than_length(max_length, tracks_to_filter):
    """
    Filter a list of tracks to those shorter than a target length

    Finds and returns a list of all tracks with a length
    shorter (or equal to) `max_length` in the provided `tracks_to_filter`

    Parameters
    ----------
    max_length : int
        maximum (inclusive) length of tracks to include in
        the filtered result

    tracks_to_filter : list[MusicTrack]
        list of tracks to filter

    Returns
    -------
    list[MusicTrack]
        List of MusicTracks satisfying
        `MusicTrack.length_in_seconds <= maximum length`.
        If no MusicTracks are found an empty list is returned

    See Also
    --------
    filter_tracks_greater_than_length : filters out tracks shorter than a given length
    """
    tracks_shorter_than_max_length = []
    for track in tracks_to_filter:
        if track.length_in_seconds <= max_length:
            tracks_shorter_than_max_length.append(track)
    return tracks_shorter_than_max_length


def filter_tracks_greater_than_length(min_length, tracks_to_filter):
    """
    Filter a list of tracks to those greater than a target length

    Finds and returns a list of all tracks with a length
    greater (or equal to) `min_length` in the provided `tracks_to_filter`

    Params
    ------
    min_length : int
        minimum (inclusive) length of tracks to include in
        the filtered result

    tracks_to_filter : list[MusicTrack]
        list of tracks to filter

    Returns
    -------
    list[MusicTrack]
        List of MusicTracks satisfying
        `MusicTrack.length_in_seconds <= maximum length`.
        If no MusicTracks are found an empty list is returned

    See Also
    --------
    filter_tracks_shorter_than_length : filters out tracks greater than a given length
    """
    tracks_greater_than_min_length = []
    for track in tracks_to_filter:
        if track.length_in_seconds >= min_length:
            tracks_greater_than_min_length.append(track)
    return tracks_greater_than_min_length


def find_tracks_shorter_than_length():
    """
    Finds and displays all tracks shorter (or equal to) a user prompted
    maximum length

    Returns
    -------
    None

    See Also
    --------
    filter_tracks_shorter_than_length : filters out tracks greater than a given length
    """
    max_length = read_min_valued_integer(
        "Enter the maximum track length (in seconds): ", min_value=1
    )
    display_tracks(filter_tracks_shorter_than_length(max_length, tracks))


def find_tracks_greater_than_length():
    """
    Finds and displays all tracks greater (or equal to) a user prompted
    minimum length

    Returns
    -------
    None

    See Also
    --------
    filter_tracks_greater_than_length : filters out tracks shorter than a given length
    """
    min_length = read_min_valued_integer(
        "Enter the minimum track length (in seconds): ", min_value=1
    )
    display_tracks(filter_tracks_greater_than_length(min_length, tracks))


class Playlist:
    """
    A class representing a music playlist with a name and list of tracks

    Tracks and records the length of the playlist
    """

    def __init__(self, name, tracks=[]):
        """
        Create a new Playlist instance

        Parameters
        ----------
        name : str
            name to associate with the playlist
        tracks : list, optional
            list of songs in the playlist, by default []
        """
        self.name = name
        self.tracks = tracks
        self.__runtime = 0
        for song in self.tracks:
            self.__runtime += song.length_in_seconds

    def __str__(self):
        template = """Playlist: {0}
Total Length: {1} s
Songs:
{2}"""
        return template.format(self.name, self.runtime, self.track_report)

    @property
    def runtime(self):
        """
        runtime : int
            total run time of the playlist in seconds
        """
        return self.__runtime

    @property
    def track_report(self):
        """
        track_report : str
            string representation of tracks in the playlist, giving each track
            on its own line
        """
        song_strings = map(str, self.tracks)
        return "\n".join(song_strings)

    def add_track(self, track):
        """
        Add a new track to the playlist

        Updates the playlist length

        Parameters
        ----------
        track : MusicTrack
            track to add to the playlist

        Returns
        -------
        None

        See Also
        --------
        Playlist.remove_track : removes a track from a playlist
        """
        # first update runtime so a non-track objects causes an error
        self.__runtime += track.length_in_seconds
        self.tracks.append(track)

    def remove_track(self, track):
        """
        Remove a track from the playlist

        Parameters
        ----------
        track : MusicTrack
            track to remove from the playlist

        See Also
        --------
        Playlist.add_track : add a track to a playlist
        Playlist.clear_tracks : remove all tracks from a playlist
        """
        try:
            self.tracks.remove(track)
            self.__runtime -= track.length_in_seconds
        except ValueError:
            print("Could not find track:", track.name, "in the playlist")

    def clear_tracks(self):
        """
        Remove all tracks from a playlist

        Runtime is set to 0
        """
        self.tracks.clear()
        self.__runtime = 0


def valid_playlist_name(name):
    """
    Verifies that a playlist name is valid

    Playlist names must be unique

    Parameters
    ----------
    name : str
        proposed name for a playlist

    Returns
    -------
    bool
        `True` if playlist name is valid else, `False`
    """
    if name == "None":
        return False
    for playlist in playlists:
        if name == playlist.name:
            return False
    return True


def create_playlist(tracks=[]):
    """
    Create a new playlist and make it the active playlist

    Prompts the user for a new name for the playlist, and ensures its valid
    then constructs a playlist and sets it as the current active playlist

    Parameters
    ----------
    tracks : list, optional
        tracks to assign to the playlist, by default []

    See Also
    --------
    valid_playlist_name : validates a playlist name
    Playlist : class used to represent a playlist
    """
    print("Create a new playlist")
    global current_playlist

    new_playlist_name = BTCInput.read_text("Enter the playlist name: ")
    while not valid_playlist_name(new_playlist_name):
        print("That playlist name is already in use")
        new_playlist_name = BTCInput.read_text("Enter the playlist name: ")

    new_playlist = Playlist(new_playlist_name, tracks)
    current_playlist = new_playlist
    playlists.append(new_playlist)


def select_playlist():
    """
    Select an existing playlist to be the current playlist

    Prompts the user for a search name then returns all playlists
    that match that string. The user will be displayed each playlist
    in turn and asked if they want to make that the current playlist

    Notes
    -----
    Passing the empty string can be used to display all playlists
    """
    print("Select a playlist")
    global current_playlist

    search_name = BTCInput.read_text("Enter playlist name (enter to see ): ")

    matched_playlists = []

    for playlist in playlists:
        if playlist.name.strip().lower().startswith(search_name.strip().lower()):
            matched_playlists.append(playlist)

    if len(matched_playlists) > 0:
        print("Found {0} matches".format(len(matched_playlists)))
        for playlist in matched_playlists:
            display_playlist(playlist)
            select = BTCInput.read_int_ranged(
                "Select this playlist? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            )
            if select:
                current_playlist = playlist
                return
    else:
        print("No playlists found matching that name")


def display_playlist(playlist, name_only=True):
    """
    Display a playlist

    Can optionally list all the tracks or just the name and length

    Parameters
    ----------
    playlist : Playlist
        playlist to display
    name_only : bool, optional
        only dispaly the playlists name and runtime, by default `True`

    Returns
    -------
    None
    """
    if name_only:
        print("{0} ({1} s)".format(playlist.name, playlist.runtime))
    else:
        print(playlist)


def add_track_to_playlist():
    """
    Adds a track from the track database to the current playlist

    Prompts the user for a the start of a track name, then
    finds all tracks that have a name starting with the
    provided substring. For each match, the user is then
    given the option of adding the track to the current
    playlist

    Returns
    -------
    None
        Accepted tracks are added to the current playlist

    See Also
    --------
    filter_tracks_by_name : filters a list of tracks by a search name
    """
    print("Add track to playlist")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track name to add: "), tracks
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Add this track? (1 - Yes, 0 - No): ", 0, 1):
            current_playlist.add_track(track)


def remove_tracks_from_playlist():
    """
    Removes a track from the currrent playlist

    Prompts the user for a the start of a track name, then
    finds all tracks that have a name starting with the
    provided substring in the current playlist. For each
    match, the user is then given the option of removing
    the track from the current playlist

    Returns
    -------
    None

    See Also
    --------
    filter_tracks_by_name : filters a list of tracks by a search name
    """
    print("Remove tracks from playlist")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track to remove: "), current_playlist.tracks
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Remove this track? (1 - Yes, 0 - No): ", 0, 1):
            current_playlist.remove_track(track)


def clear_playlist():
    """
    Removes all tracks from the current playlist

    Returns
    -------
    None
    """
    print("Clear playlist")
    current_playlist.clear_tracks()


def calculate_playlist_length():
    """
    Calculates and displays the total length of the
    current playlist in seconds

    Returns
    -------
    None
    """
    print("Calculate length of playlist")
    print("The playlist is", current_playlist.runtime, "seconds long")


def suggest_playlist_of_given_length():
    """
    Suggests a playlist of length less than or equal to
    a user prompted length

    Asks the user for a maximum playlist length, and
    then suggests a playlist by combining tracks randomly
    such that the suggested playlist is no greater than
    the length

    The user has the option to review the proposed list
    and either accept, reject or regenerate the list

    Returns
    -------
    None
    """
    print("Suggest playlist of given length")
    global current_playlist

    target_length = read_min_valued_integer(
        "Enter maximum playlist length: ", min_value=1
    )

    while True:
        suggested_tracks = []
        suggested_tracks_total_length = 0
        # find tracks that could fit in the playlist
        candidate_songs = filter_tracks_shorter_than_length(target_length, tracks)

        if len(candidate_songs) == 0:
            print("Could not generate a playlist of that length. Try a longer playlist")
            return

        while len(candidate_songs) > 0:  # stop when no more eligable songs
            # add a random song and update the playlist length
            song_choice = random.choice(candidate_songs)
            suggested_tracks.append(song_choice)
            suggested_tracks_total_length = (
                suggested_tracks_total_length + song_choice.length_in_seconds
            )

            # filter out songs that no longer fit
            candidate_songs = filter_tracks_shorter_than_length(
                target_length - suggested_tracks_total_length, candidate_songs
            )
        print("Generated a playlist...")
        # let the user review the playlist
        display_tracks(suggested_tracks)
        if BTCInput.read_int_ranged(
            "Accept this playlist? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        ):
            create_playlist(suggested_tracks)
            return
        else:
            if BTCInput.read_int_ranged(
                "Generate again? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            ):
                continue
            return


def export_playlist():
    """
    Saves the current playlist as a human readable list

    The user is prompted to give a file name to save the playlist in

    Returns
    -------
    None

    Raises
    ------
    Exceptions are raised if the save fails
    """
    print("Save playlist")
    if len(current_playlist.tracks) == 0:
        print("No playlist to save")
        return

    file_name = BTCInput.read_text("Enter file to save playlist to: ")
    try:
        with open(file_name, "w") as output_file:
            output_file.write(str(current_playlist))
    except:  # noqa: E722
        print("Failed to save playlist")


def save_playlists(file_name):
    """
    Saves the playlists to the given file

    Playlists are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file to store the playlist data in

    Returns
    -------
    None

    Raises
    ------
    An Exception is raised if the file could not be saved

    See Also
    --------
    load_playlists : load playlists from a pickled file
    """
    print("Save playlists")
    with open(file_name, "wb") as out_file:
        pickle.dump(playlists, out_file)


def load_playlists(file_name):
    """
    Loads the playlists from the given file

    Playlists are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the playlists data is stored

    Returns
    -------
    None
        Playlists are loaded into the global playlists list

    Raises
    ------
    An Exception is raised if the file could not be loaded

    See Also
    --------
    save_playlists : save playlists as a pickled file
    """
    global playlists  # connect to global track list to load into
    print("Load playlists")
    with open(file_name, "rb") as input_file:
        playlists = pickle.load(input_file)


def run_track_menu():
    """
    Provides a looping track management menu to the user

    The user has the option to
    1. Add a Track
    2. Edit a Track
    3. Remove a Track
    4. Sort the Track List in Order of Decreasing Length
    5. Sort the Track list in ORder of Increasing Length
    6. Return to the Main Menu

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    track_menu = """Track Management

1. Add Track
2. Edit Track
3. Remove Track
4. Sort Tracks by decreasing length
5. Sort Tracks by increasing length
6. Back to Main Menu

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(prompt=track_menu, min_value=1, max_value=6)
        if command == 1:
            new_track()
        elif command == 2:
            edit_tracks()
        elif command == 3:
            remove_tracks()
        elif command == 4:
            sort_high_to_low(tracks)
        elif command == 5:
            sort_low_to_high(tracks)
        elif command == 6:
            break
        else:
            raise ValueError(
                "Invalid command id "
                + str(command)
                + " found in track management sub-menu"
            )


def run_display_track_menu():
    """
    Provides the user with a looping menu to display tracks

    The user has the option to
    1. Display tracks matching a name
    2. Display tracks less than (or equal to) a given max length
    3. Display tracks greater than (or equal to) a given min length
    4. Return to the Main Menu

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    display_track_menu = """Find and Display Tracks

1. Find Tracks by Name
2. Find Tracks by length (Maximum length)
3. Find Tracks by length (Minimum length)
4. Back to Main Menu

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            prompt=display_track_menu, min_value=1, max_value=4
        )
        if command == 1:
            find_tracks_by_name()
        elif command == 2:
            find_tracks_shorter_than_length()
        elif command == 3:
            find_tracks_greater_than_length()
        elif command == 4:
            break
        else:
            raise ValueError(
                "Invalid command id "
                + str(command)
                + " found in track display sub-menu"
            )


def run_playlist_management_menu():
    """
    Provides the user with a looping playlist menu

    1. Create a new playlist
    2. Select playlist
    3. Get a suggested playlist of a target length
    4. Add a track to the playlist
    5. Remove a track from the playlist
    6. Clear the playlist
    7. Display the playlist
    8. Show the runtime of the playlist
    9. Export the current playlist
    10. Return to the main menu

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    playlist_management_menu = """Playlist Management
Current playlist is {0}

1. Create a new playlist
2. Select playlist
3. Get a suggested playlist of a target length
4. Add a track to the playlist
5. Remove a track from the playlist
6. Clear the playlist
7. Display the playlist
8. Show the runtime of the playlist
9. Export the current playlist
10. Return to the main menu

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            prompt=playlist_management_menu.format(current_playlist.name),
            min_value=1,
            max_value=10,
        )
        if command == 1:
            create_playlist()
        elif command == 2:
            select_playlist()
        elif command == 3:
            suggest_playlist_of_given_length()
        elif command == 10:
            break
        elif current_playlist.name == "None":
            print("There is no active playlist. Please select or create one")
            continue
        elif command == 4:
            add_track_to_playlist()
        elif command == 5:
            remove_tracks_from_playlist()
        elif command == 6:
            clear_playlist()
        elif command == 7:
            display_playlist(current_playlist, name_only=False)
        elif command == 8:
            calculate_playlist_length()
        elif command == 9:
            export_playlist()
        else:
            raise ValueError(
                "Invalid command id "
                + str(command)
                + " found in playlist management sub-menu"
            )


def run_main_menu():
    """Provides the user with a looping main menu

    The user has the option to,
    1. Manage Tracks
    2. Find and Display Tracks
    3. Manage a Playlist
    4. Exit the program

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered

    """
    main_menu = """Music Storage

1. Track Management
2. Find and Display Tracks
3. Playlist Management
4. Exit Program

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(prompt=main_menu, min_value=1, max_value=4)
        if command == 1:
            run_track_menu()
        elif command == 2:
            run_display_track_menu()
        elif command == 3:
            run_playlist_management_menu()
        elif command == 4:
            try:
                save_tracks(tracks_file_name)
                save_playlists(playlists_file_name)
            except:  # noqa: E722
                print("Error while trying to save tracks and playlists")
            break
        else:
            raise ValueError(
                "Unexpected command id found: " + str(command) + " in main menu"
            )


tracks_file_name = "tracks.pickle"
playlists_file_name = "playlists.pickle"

try:
    load_tracks(tracks_file_name)
except:  # noqa: E722
    print("Tracks file not found")
    tracks = []

try:
    load_playlists(playlists_file_name)
except:  # noqa: E722
    print("Playlist file not found")
    playlists = []

# null object
no_playlist = Playlist(name="None")
current_playlist = no_playlist

run_main_menu()
