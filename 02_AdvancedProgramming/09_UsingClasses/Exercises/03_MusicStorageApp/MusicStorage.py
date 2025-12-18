# Exercise 9.3 Music Storage
#
# A simple music storage app that stores tracks and their length. Provides the
# ability to search based on track length, suggest playlists up to a certain
# size and calculate the length of the current play list

import pickle

import BTCInput


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
        self.name = name
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
    # BTCInput's read_ranged_int doesn't support a single-sided range
    # i.e. (0, inf), so have to handroll the exception handling
    while True:
        length = BTCInput.read_int("Enter the track length in seconds: ")
        if length <= 0:
            print("Track length must be > 0")
        else:
            break
    tracks.append(MusicTrack(name=name, length_in_seconds=length))


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
    global tracks
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        tracks = pickle.load(input_file)


def sort_low_to_high():
    """
    Sorts the music track list by length from shortest to greatest

    Returns
    -------
    None
    """
    print("Sort low to high")
    for sort_pass in range(0, len(tracks)):
        done_swap = False
        for count in range(0, len(tracks) - 1 - sort_pass):
            if tracks[count].length_in_seconds > tracks[count + 1].length_in_seconds:
                temp = tracks[count]
                tracks[count] = tracks[count + 1]
                tracks[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def sort_high_to_low():
    """
    Sorts the music track list by length from greatest to shortest

    Returns
    -------
    None
    """
    print("Sort high to low")
    for sort_pass in range(0, len(tracks)):
        done_swap = False
        for count in range(0, len(tracks) - 1 - sort_pass):
            if tracks[count].length_in_seconds < tracks[count + 1].length_in_seconds:
                temp = tracks[count]
                tracks[count] = tracks[count + 1]
                tracks[count + 1] = temp
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


def display_tracks():
    """
    Displays all the tracks in the track list

    Returns
    -------
    None
    """
    print("Display tracks")
    if len(tracks) > 0:
        for track in tracks:
            display_track(track)
    else:
        print("No tracks found")


def find_tracks_shorter_than_length():
    """
    Finds and returns a list of all tracks with a length
    shorter (or equal to) a user provided maximum length

    Returns
    -------
    List[MusicTrack]
        List of MusicTracks satisfying
        `MusicTrack.length_in_seconds <= maximum length`
        If no MusicTracks are found an empty list is returned
    """
    while True:
        max_length = BTCInput.read_int("Enter the maximum track length (in seconds): ")
        if max_length <= 0:
            print("Track length must be > 0")
        else:
            break
    tracks_shorter_than_max_length = []
    for track in tracks:
        if track.length_in_seconds <= max_length:
            tracks_shorter_than_max_length.append(track)
    return tracks_shorter_than_max_length


def find_tracks_greater_than_length():
    """
    Finds and returns a list of all tracks with a length
    greater (or equal to) a user provided minimum length

    Returns
    -------
    List[MusicTrack]
        List of MusicTracks satisfying
        `MusicTrack.length_in_seconds >= minimum length`
        If no MusicTracks are found an empty list is returned
    """
    while True:
        max_length = BTCInput.read_int("Enter the minimum track length (in seconds): ")
        if max_length <= 0:
            print("Track length must be > 0")
        else:
            break
    tracks_longer_than_min_length = []
    for track in tracks:
        if track.length_in_seconds >= max_length:
            tracks_longer_than_min_length.append(track)
    return tracks_longer_than_min_length


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


def clear_playlist():
    """
    Removes all tracks from the current playlist

    Returns
    -------
    None
    """
    print("Clear playlist")


def display_playlist():
    """
    Displays the contents of the current playlist

    Returns
    -------
    None
    """
    print("Display playlist")


def calculate_playlist_length():
    """
    Calculates and displays the total length of the
    current playlist

    """
    print("Calculate length of playlist")


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


def save_playlist():
    """
    Saves the current playlist as a human readable list
    The user is prompted to give a file name to save the playlist in

    Raises exceptions if the save fails
    """
    print("Save playlist")


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
            sort_high_to_low()
        elif command == 5:
            sort_low_to_high()
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
            display_tracks()
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
6. Suggest Playlist of specified length
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
            display_playlist()
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

run_main_menu()
