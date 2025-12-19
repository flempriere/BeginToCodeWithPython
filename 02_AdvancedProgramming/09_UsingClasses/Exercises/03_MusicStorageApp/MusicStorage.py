# Exercise 9.3 Music Storage
#
# A simple music storage app that stores tracks and their length. Provides the
# ability to search based on track length, suggest playlists up to a certain
# size and calculate the length of the current play list

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

    Params
    ------
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
        length of the track in seconds (must be positive)

    Raises
    ------
    ValueError
        Raised if length_in_seconds is non-positive

    Examples
    --------
    >>> MusicTrack("Merry Christmas Everyone", 220)
    <MusicTrack ...>
    """

    def __init__(self, name, length_in_seconds):
        self.name = name
        if length_in_seconds <= 0:
            raise ValueError("Track length must be greater than zero")
        self.length_in_seconds = length_in_seconds


def new_track():
    """
    Creates and adds a new track to the track storage program

    Returns
    -------
    None
    """
    print("Add a new track")
    name = BTCInput.read_text("Enter the track name: ")
    length = read_min_valued_integer(
        "Enter the track length (in seconds): ", min_value=1
    )
    tracks.append(MusicTrack(name=name, length_in_seconds=length))


def filter_tracks_by_name(search_name, tracks_to_search):
    """
    Filters tracks from the list tracks_to_search with a name
    containing search_name as a prefix

    Params
    ------

    search_name : str
        name to search for (search uses prefix matching)

    tracks_to_search : list[MusicTrack]
        list of music tracks to search through

    Returns
    -------
    list[MusicTrack]
        list of contacts matching the name. If no matches
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
    Reads in a name to search for and then allows the user to edit
    the details of the Music Track

    If there a no matching Music Tracks the function will indicate
    that the name was not found. If multiple matches are found, the
    user will have the option to edit each of them

    Returns
    -------
    None
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
    Saves the music tracks to the given file name
    Music tracksare stored in binary as a pickled file
    Exceptions will be raised if the save fails

    Params
    ------
    file_name : str
        string giving the path to the file to store the contacts data in

    Returns
    -------
    None
    """
    print("Save music tracks")
    with open(file_name, "wb") as out_file:
        pickle.dump(tracks, out_file)


def load_tracks(file_name):
    """
    Loads the music tracks from the given file name
    Music Tracks are stored in binary as a pickled file
    Exceptions will be raised if the load fails

    Params
    ------
    file_name : str
        string giving the path to the file where the contacts data is stored

    Returns
    -------
    None
        Music Tracks are loaded into the global tracks list
    """
    global tracks  # connect to global track list to load into
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        tracks = pickle.load(input_file)


def sort_low_to_high(tracks_to_sort):
    """
    Sorts the music track list given by tracks_to_sort
    by length from shortest to greatest

    Params
    ------
    tracks_to_sort : list[MusicTrack]
        list of tracks to sort
    Returns
    -------
    None
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
    Sorts the music track list given by tracks_to_sort
    by length from greatest to shortest

    Params
    ------
    tracks_to_sort : list[MusicTrack]

    Returns
    -------
    None
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
    Displays the name and length (in seconds) of the MusicTrack track

    Params
    ------
    track : MusicTrack
        track to display

    Returns
    -------
    None
    """
    print("Name:", track.name, "(", track.length_in_seconds, "seconds )")


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
    """
    if len(tracks) > 0:
        for track in tracks:
            display_track(track)
    else:
        print("No tracks found")


def find_tracks_by_name():
    """
    Finds and displays a list of tracks matching a
    user provided track name. If the user provides
    an empty string all tracks are displayed

    Returns
    -------
    None
    """
    print("Find Tracks by Name")
    search_name = BTCInput.read_text("Enter track name (Press enter to display all): ")
    matched_tracks = filter_tracks_by_name(search_name, tracks)
    display_tracks(matched_tracks)


def filter_tracks_shorter_than_length(max_length, tracks_to_filter):
    """
    Finds and returns a list of all tracks with a length
    shorter (or equal to) max_length in the provided tracks_to_filter

    Params
    ------
    max_length : int
        maximum (inclusive) length of tracks to include in
        the filtered result

    tracks_to_filter : list[MusicTrack]
        list of tracks to filter

    Returns
    -------
    list[MusicTrack]
        List of MusicTracks satisfying
        `MusicTrack.length_in_seconds <= maximum length`
        If no MusicTracks are found an empty list is returned
    """
    tracks_shorter_than_max_length = []
    for track in tracks_to_filter:
        if track.length_in_seconds <= max_length:
            tracks_shorter_than_max_length.append(track)
    return tracks_shorter_than_max_length


def filter_tracks_greater_than_length(min_length, tracks_to_filter):
    """
    Finds and returns a list of all tracks with a length
    greater (or equal to) min_length in the provided tracks_to_filter

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
        `MusicTrack.length_in_seconds <= maximum length`
        If no MusicTracks are found an empty list is returned
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
    """
    min_length = read_min_valued_integer(
        "Enter the minimum track length (in seconds): ", min_value=1
    )
    display_tracks(filter_tracks_greater_than_length(min_length, tracks))


def add_track_to_playlist():
    """
    Prompts the user for a the start of a track name, then
    finds all tracks that have a name starting with the
    provided substring. For each match, the user is then
    given the option of adding the track to the current
    playlist

    Returns
    -------
    None
        Accepted tracks are added to the global playlist
    """
    print("Add track to playlist")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track name to add: "), tracks
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Add this track? (1 - Yes, 0 - No): ", 0, 1):
            playlist.append(track)


def remove_tracks_from_playlist():
    """
    Prompts the user for a the start of a track name, then
    finds all tracks that have a name starting with the
    provided substring in the current playlist. For each
    match, the user is then given the option of removing
    the track from the current playlist

    Returns
    -------
    None
        Removed tracks are deleted from the global playlist
    """
    print("Remove tracks from playlist")
    matched_tracks = filter_tracks_by_name(
        BTCInput.read_text("Enter track to remove: "), playlist
    )
    print("Found", len(matched_tracks), "matches")

    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Remove this track? (1 - Yes, 0 - No): ", 0, 1):
            playlist.remove(track)


def clear_playlist():
    """
    Removes all tracks from the current playlist

    Returns
    -------
    None
    """
    print("Clear playlist")
    playlist.clear()


def calculate_playlist_length():
    """
    Calculates and displays the total length of the
    current playlist

    """
    print("Calculate length of playlist")
    total_length = 0
    for track in playlist:
        total_length = total_length + track.length_in_seconds
    print("The playlist is", total_length, "seconds long")


def suggest_playlist_of_given_length():
    """
    Asks the user for a maximum playlist length, and
    the suggests a playlist by combining tracks randomly
    such that the suggested playlist is no greater than
    the max length

    The user has the option to review the proposed list
    and either accept, reject or regenerate the list
    """
    print("Suggest playlist of given length")
    global playlist

    target_length = read_min_valued_integer(
        "Enter maximum playlist length: ", min_value=1
    )

    while True:
        suggested_playlist = []
        playlist_length = 0
        # find tracks that could fit in the playlist
        candidate_songs = filter_tracks_shorter_than_length(target_length, tracks)

        if len(candidate_songs) == 0:
            print("Could not generate a playlist of that length. Try a longer playlist")
            return

        while len(candidate_songs) > 0:  # stop when no more eligable songs
            # add a random song and update the playlist length
            song_choice = random.choice(candidate_songs)
            suggested_playlist.append(song_choice)
            playlist_length = playlist_length + song_choice.length_in_seconds

            # filter out songs that no longer fit
            candidate_songs = filter_tracks_shorter_than_length(
                target_length - playlist_length, candidate_songs
            )
        print("Generated a playlist...")
        # let the user review the playlist
        display_tracks(suggested_playlist)
        if BTCInput.read_int_ranged(
            "Accept this playlist? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        ):
            playlist = suggested_playlist
            return
        else:
            if BTCInput.read_int_ranged(
                "Generate again? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            ):
                continue
            return


def save_playlist():
    """
    Saves the current playlist as a human readable list
    The user is prompted to give a file name to save the playlist in

    Raises exceptions if the save fails
    """
    print("Save playlist")
    if len(playlist) == 0:
        print("No playlist to save")
        return

    file_name = BTCInput.read_text("Enter file to save playlist to: ")
    try:
        with open(file_name, "w") as output_file:
            for track in playlist:
                output_file.write(track.name + "\n")
    except:  # noqa: E722
        print("Failed to save playlist")


def run_track_menu():
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
    playlist_management_menu = """Playlist Management

1. Add Track to Playlist
2. Remove Track from Playlist
3. Clear Playlist
4. Display Current Playlist
5. Show Runtime of Current Playlist
6. Suggest Playlist of Specified Length
7. Save Current Playlist
8. Back to Main Menu

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            prompt=playlist_management_menu, min_value=1, max_value=8
        )
        if command == 1:
            add_track_to_playlist()
        elif command == 2:
            remove_tracks_from_playlist()
        elif command == 3:
            clear_playlist()
        elif command == 4:
            display_tracks(playlist)
        elif command == 5:
            calculate_playlist_length()
        elif command == 6:
            suggest_playlist_of_given_length()
        elif command == 7:
            save_playlist()
        elif command == 8:
            break
        else:
            raise ValueError(
                "Invalid command id "
                + str(command)
                + " found in playlist management sub-menu"
            )


def run_main_menu():
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
                save_tracks(file_name)
            except:  # noqa: E722
                print("Tracks failed to save")
            break
        else:
            raise ValueError(
                "Unexpected command id found: " + str(command) + " in main menu"
            )


file_name = "tracks.pickle"

try:
    load_tracks(file_name)
except:  # noqa: E722
    print("Tracks file not found")
    tracks = []

playlist = []

run_main_menu()
