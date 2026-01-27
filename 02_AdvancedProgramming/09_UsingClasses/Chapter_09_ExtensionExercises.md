# Extended Exercises for Chapter 9

- [Make Something Happen: Music Storage
  App](#make-something-happen-music-storage-app)
  - [Storyboarding the Application](#storyboarding-the-application)
  - [Building the User Interface](#building-the-user-interface)
  - [Track Management](#track-management)
    - [The `MusicTrack` Class](#the-musictrack-class)
    - [Adding Tracks to the Database](#adding-tracks-to-the-database)
    - [Searching for Tracks](#searching-for-tracks)
    - [Edit Tracks](#edit-tracks)
    - [Remove Tracks](#remove-tracks)
    - [Adding Sorting Functionality](#adding-sorting-functionality)
    - [Save and Load Tracks via
      `pickle`](#save-and-load-tracks-via-pickle)
  - [Track Search and Display](#track-search-and-display)
    - [Display Tracks](#display-tracks)
    - [Find Tracks by Length](#find-tracks-by-length)
  - [Playlist Management](#playlist-management)
    - [Calculating the Length of a
      Playlist](#calculating-the-length-of-a-playlist)
    - [Saving a Playlist](#saving-a-playlist)
    - [Suggesting a Playlist](#suggesting-a-playlist)
- [Make Something Happen: Recipe Storage
  App](#make-something-happen-recipe-storage-app)
  - [Storyboarding out the design](#storyboarding-out-the-design)
  - [Designing the Recipe Class](#designing-the-recipe-class)
    - [Creating a Recipe from User
      Input](#creating-a-recipe-from-user-input)
  - [Finding Recipes](#finding-recipes)
    - [Listing Recipes](#listing-recipes)
    - [Find Recipes by Name](#find-recipes-by-name)
    - [Finding by Ingredients](#finding-by-ingredients)
  - [Viewing a Recipe](#viewing-a-recipe)
    - [Selecting a Recipe to View](#selecting-a-recipe-to-view)
    - [Viewing a Selected Recipe](#viewing-a-selected-recipe)
  - [Editing and Removing a Recipe](#editing-and-removing-a-recipe)
    - [Remove a Recipe](#remove-a-recipe)
    - [Edit a Recipe](#edit-a-recipe)
  - [Improving the Recipe
    Application](#improving-the-recipe-application)

## Make Something Happen: Music Storage App

*Write a music track storage program that lets you search for tracks
based on the length of the track. The program could suggest tracks that
could be combined to fill an exact amount of time or give the total play
time of a specific playlist.*

*You will have to create a class that can hold track information, store
the information in a list and then create some behaviours that would
search through and process the data*

This is the most complicated application that we have built so far, and
so it is best to both design and implement in stages. We’ll sketch the
process and some of the functions out here, but the full program can be
found [in our
implementation](./Exercises/03_MusicStorageApp/MusicStorage.py). First
storyboard out the high level functionality we want.

### Storyboarding the Application

At the highest level there are two functionalities we need from the
given brief,

``` text
1. Enter Tracks and manage tracks in a database
2. Use these Tracks to build playlists
```

If we focus in on the first item, this is similar to our Tiny Contacts
Program. We also have the feature that we want to be able to search for
tracks based on their length. This leads to the following interface,

``` text
1. Add a Track
2. Edit a Track
3. Remove a Track
4. Sort Tracks by decreasing length
5. Sort Tracks by increasing length
6. Find Tracks by Name
7. Find Tracks shorter than a given length
8. Find Tracks longer than a  given length

Enter a command:
```

Since we want to be able to easily save, load and reconstruct the music
track objects we’ll use `pickle` to implement saving and loading in the
same way as for Tiny Contacts (i.e. on program start and exit)

We can then turn to our playlist interface. At some level this will look
like the interface for adding tracks to the database. With some extra
features such as a convenience function to remove all the tracks in a
playlist. The two functions we were told that we had to add was

1. To be able to get the length of a given playlist, and,
2. To be able to generate a playlist of an exact length given the
    tracks in the database.

It would also be nice for the user to be able to save their playlist. We
want this to be something human readable they could give to a friend, so
we’ll simply output the track names to a text file.

For simplicity we’ll assume that the user can only work on one playlist
at a time.

Our interface would look like,

``` text
1. Add Track to Playlist
2. Remove Track from Playlist
3. Clear Playlist
4. Display Current Playlist
5. Show Runtime of Current Playlist
6. Suggest Playlist of Specified Length
7. Save Current Playlist
```

### Building the User Interface

The most immediate problem is that we have a lot of functionality, that
would probably overwhelm the user. To get around this we will have a
general main menu (as seen below) and sub-menus for

1. Modifying the track database
2. Displaying / Searching the Track database
3. Build Playlists

``` python
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
                save_tracks(file_name)
            except:  # noqa: E722
                print("Tracks failed to save")
            break
        else:
            raise ValueError(
                "Unexpected command id found: " + str(command) + " in main menu"
            )
```

The sub-menu’s look similar (see below). The main menu lets us exit the
program, while the sub-menu’s exit back to the main menu.

``` python
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
```

### Track Management

Let’s work through the sections step by step.

#### The `MusicTrack` Class

First we need to define our Music Track objects. We use a simple class
that stores a name and a track length. We use seconds for the length. We
name the variables `name` and `length_in_seconds` to make them clear.

``` python
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
        Create a new `MusicTrack` instance

        Parameters
        ----------
        name : str
            name of the music track
        length_in_seconds : int
            length of the track in seconds (must be positive)

        Raises
        ------
        ValueError
                Raised if `length_in_seconds` is invalid
        """
        self.name = name
        if length_in_seconds <= 0:
            raise ValueError("Track length must be greater than zero")
        self.length_in_seconds = length_in_seconds
```

One immediate caveat is that a music track should not have a length that
isn’t a positive integer. We enforce this by raising an exception if one
is passed to the constructor.

We would also ideally like to take care of this at the user input level.
It would be pretty frustrating to put in a number as a user then have
the program crash. We would like to enforce that the user can put in any
positive number, unfortunately `BTCInput` doesn’t provide this. We could
simply put an upper bound on the track length, instead we roll our own
input function.

``` python
def read_min_valued_integer(prompt, min_value):
    """
    Displays a prompt and reads in a integer number greater
    than or equal to `min_value`.

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
        integer >= `min_value` entered by the user
    """
    while True:
        result = BTCInput.read_int(prompt)
        if result >= min_value:
            return result
        else:
            print("That number is invalid")
            print("Number must be >", min_value)
```

We make this generic by calling it `read_min_valued_integer` and using a
parameter to define a `min_value`. There is no bound on the `max_value`.
We then use `BTCInput.read_int` and wrap it in the bound checking we
need.

#### Adding Tracks to the Database

We can then define a function `new_track` to add tracks to the database,

``` python
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
```

- Running the above with the input, (represented by red text), generates
  output like,

``` python
print("Enter the track name: \033[31mMerry Christmas Everyone\033[0m")
print("Enter the track length (in seconds): \033[31m220\033[0m")
print(tracks)
print(tracks[0].name)
print(tracks[0].length_in_seconds)
```

    Enter the track name: Merry Christmas Everyone
    Enter the track length (in seconds): 220
    [<__main__.MusicTrack object at 0x7f9824587740>]
    Merry Christmas Everyone
    220

#### Searching for Tracks

Before we go further we need to implement a search by name
functionality. We’ll adopt the following convention

1. A `filter_` function takes a search parameter, and a list of of
    `MusicTrack` objects to search through and returns a list of
    `MusicTrack` objects that meet the conditions
    - By adding the list parameter we can reuse these functions for the
      playlist functionality later
2. A `find_` function, prompts the user for the search parameter, calls
    the corresponding `filter_` and displays the list

The first `filter_` we implement is `filter_by_name` which uses the same
logic as Tiny Contacts (a name is searched using `startswith`). See
below,

``` python
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
```

Running this for the track we just added,

``` python
# looking for a match that exists
results = filter_tracks_by_name("Merry Christmas", tracks)

print(results)
print(results[0].name)
print(results[0].length_in_seconds)

# looking for non existent match
print(filter_tracks_by_name("Missing Track", tracks))
```

    [<__main__.MusicTrack object at 0x7f9824587740>]
    Merry Christmas Everyone
    220
    []

#### Edit Tracks

We can now implement the edit functionality with `edit_tracks`, using
the same pattern we discussed before.

- We find all the matches to a named search
- The user is then prompted if they want to edit each match
- The user can then edit each entry

``` python
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
```

We have to make one change to the pattern of the Tiny Contacts which is
to account for the fact that length is a positive number. To do this we
use `0` rather than `"."` to indicate that the variable should be left
unchanged. An example use might look like,

``` python
print("Edit Music Tracks")
print("Enter track name to edit: \033[31mMerry Christmas Everyone\033[0m")
print("Found 1 matches")
print("Merry Christmas Everyone (220 seconds)")
print("Edit this track? (1 - Yes, 0 - No): \033[31m1\033[0m")
print("Enter new name or . to leave unchanged: \033[31m.\033[0m")
print("Enter new name or 0 to leave unchanged: \033[31m210\033[0m")

print(tracks[0].name)
print(tracks[0].length_in_seconds)
```

    Edit Music Tracks
    Enter track name to edit: Merry Christmas Everyone
    Found 1 matches
    Merry Christmas Everyone (220 seconds)
    Edit this track? (1 - Yes, 0 - No): 1
    Enter new name or . to leave unchanged: .
    Enter new name or 0 to leave unchanged: 210
    Merry Christmas Everyone
    210

#### Remove Tracks

The `remove_track` follows the same pattern, instead of the edit dialog,
we use the `.remove` method on a `list` to remove the matching track,

``` python
    for track in matched_tracks:
        display_track(track)
        if BTCInput.read_int_ranged("Delete this track? (1 - Yes, 0 - No): ", 0, 1):
            tracks.remove(track)
```

#### Adding Sorting Functionality

The next step is to implement sorting functionality. Based on the
description we implement these sorts based on the length of the track.
The ascending order search is then,

``` python
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
```

Let’s add another track `Rockin Little Christmas, 157 seconds`,

``` python
tracks.append(MusicTrack("Rockin Little Christmas", 157))

print("tracks[0]:", tracks[0].name, tracks[0].length_in_seconds)
print("tracks[1]:", tracks[1].name, tracks[1].length_in_seconds)
```

    tracks[0]: Merry Christmas Everyone 210
    tracks[1]: Rockin Little Christmas 157

Then if we run the sort,

``` python
sort_low_to_high(tracks)
print("tracks[0]:", tracks[0].name, tracks[0].length_in_seconds)
print("tracks[1]:", tracks[1].name, tracks[1].length_in_seconds)
```

    Sort low to high
    tracks[0]: Rockin Little Christmas 157
    tracks[1]: Merry Christmas Everyone 210

The descending order search follows the same structure.

#### Save and Load Tracks via `pickle`

The only two track database management functions now are `save` and
`load`, which are done simply via `pickle`.

``` python
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
        string giving the path to the file where the recipes data is stored

    Returns
    -------
    None
        Music Tracks are loaded into the global `tracks` list

    Raises
    ------
    An Exception is raised if the file could not be loaded

    See Also
    --------
    save_tracks : save tracks as a pickled file
    """
    global tracks  # connect to global track list to load into
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        tracks = pickle.load(input_file)
```

`save_tracks` is called on program exit to write out the track database
to a hard-coded database file. Similarly, `load_tracks` will attempt to
read the database file on program start. If it can’t find the database
file then a new blank database is generated

### Track Search and Display

With our track database management up and running the next step is to
look set up how we can display and search for the tracks in the
database. The three functionalities we have to implement are,

``` text
1. Find Tracks (by name)
2. Find Tracks by length (Maximum length)
3. Find Tracks by length (Minimum length)
```

The first one simply wraps the `filter_tracks_by_name` in a user prompt
for a search name and displays the matches. This just leaves us to
implement the display functionality.

#### Display Tracks

We first define a function `display_track` to display a single track,

``` python
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
    print("Name:", track.name, "(", track.length_in_seconds, "seconds )")
```

We can see how it used below,

``` python
display_track(tracks[0])
```

    Name: Rockin Little Christmas ( 157 seconds )

We can then define a higher level function `display_tracks` that
displays an entire list of tracks,

``` python
def display_tracks(tracks):
    """
    Displays all the tracks in the provided list of tracks

    Params
    ------
    list[MusicTrack]
        List of MusicTrack objects to display

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
```

For example, running on our small little example track list,

``` python
display_tracks(tracks)
```

    Name: Rockin Little Christmas ( 157 seconds )
    Name: Merry Christmas Everyone ( 210 seconds )

#### Find Tracks by Length

Let us consider the problem of now finding tracks by a given length. We
want two functions. One where we return all tracks with a length less
than or equal to the provided length, and a second which returns all
with a length greater than or equal to the provided length. Both have
the same logic so we’ll only focus on the first case. As with
`filter_tracks_by_name` we first define a filter function that takes in
a maximum length as a parameter (and a search list) and returns a list
of matches. This looks like,

``` python
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
```

To see how this function works, lets run it on our test list, with three
values, `220` which should catch everything, `200` which should catch
one track, and `100` which should catch nothing.

``` python
print("Filter all the tracks...")
display_tracks(filter_tracks_shorter_than_length(220, tracks))
print("Filter some of the tracks...")
display_tracks(filter_tracks_shorter_than_length(200, tracks))
print("Filter none of the tracks")
display_tracks(filter_tracks_shorter_than_length(100, tracks))
```

    Filter all the tracks...
    Name: Rockin Little Christmas ( 157 seconds )
    Name: Merry Christmas Everyone ( 210 seconds )
    Filter some of the tracks...
    Name: Rockin Little Christmas ( 157 seconds )
    Filter none of the tracks
    No tracks found

We can then define the `find_tracks_shorter_than_length` function, we
prompts the user for the maximum time, passes this time and the tracks
list through to the filter function and displays the results.

``` python
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
```

The case where we instead pass a minimum time is identical

### Playlist Management

For the most part, the playlist management repeats code that has already
been seen before. We’ll only allow the user to work with one playlist at
a time, and store the playlist as a list of `MusicTrack` objects. Recall
that our interface is,

``` text
1. Add Track to Playlist
2. Remove Track from Playlist
3. Clear Playlist
4. Display Current Playlist
5. Show Runtime of Current Playlist
6. Suggest Playlist of Specified Length
7. Save Current Playlist
8. Back to Main Menu
```

Let’s step through each of these and look at what needs new
functionality

1. `add_track_to_playlist` - Uses existing `filter_track_by_name` to
    search for a user prompted track name. User is then prompted to
    optionally add matches to the playlist
2. `remove_tracks_from_playlist` - Identical to `remove_track` but runs
    against the current playlist list
3. `clear_playlist` - We use the list inbuilt method `clear` to clear
    the playlist
4. `display_current_playlist` - Achieved by passing the `playlist` list
    variable to the `display_tracks` function
5. `calculate_playlist_length` - No functionality yet implemented
6. `suggest_playlist_of_given_length` - No functionality yet
    implemented
7. `save_playlist` - Not yet implemented

So as we can see most of the functionality is already implemented. Let’s
focus on the three remaining features, `calculate_playlist_length`,
`suggest_playlist_of_given_length` and `save_playlist`

#### Calculating the Length of a Playlist

Implementing `calculate_playlist_length` is pretty straightforward. We
simply iterate over the tracks in the playlist and sum up their lengths

``` python
def calculate_playlist_length():
    """
    Calculates and displays the total length of the
    current playlist in seconds

    Returns
    -------
    None
    """
    print("Calculate length of playlist")
    total_length = 0
    for track in playlist:
        total_length = total_length + track.length_in_seconds
    print("The playlist is", total_length, "seconds long")
```

For example, if we use a little bit of magic to change our tracks list
to the playlist, we can demonstrate the above function,

``` python
playlist = tracks
calculate_playlist_length()
```

    Calculate length of playlist
    The playlist is 367 seconds long

#### Saving a Playlist

Similarly, `save_playlist` can be implemented pretty easily using what
we’ve seen. We prompt the user for the file that they want to save to,
then write out the names of all of the tracks (one per line) using the
standard `try...except` and `with` construct we’ve seen before

``` python
def save_playlist():
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
```

#### Suggesting a Playlist

Observe that the user always has to choose to save the playlist. This is
because we implement it much more as form of printing out a list of
songs to give to someone else rather than ensuring that a database is
maintained. As a result we provide no behaviour for loading a playlist

The last function we want to implement is the ability to suggest a
playlist of a given length. The original exercise suggests this as being
to create a playlist of an exact length. Doing this requires us to solve
what is called the [Subset Sum
Problem](https://en.wikipedia.org/wiki/Subset_sum_problem) which is in
general very difficult - we are asked to find a subset of the tracks in
the database such that the sum of their lengths matches the target.
Intuitively we should also recognise that given the granularity of song
lengths for many lengths the user might put in, no exact solution
exists.

Our solution to this will be to instead ask the user for an upper bound
on the playlist length. We will then randomly select songs such that the
total length is less than this length. The user is then shown the
proposed playlist and can either accept or reject it. If the reject it
they can then ask the program to generate a new one. Once a playlist is
accepted it can be edited using the other playlist management functions.

Our implementation for this is below,

``` python
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

        while len(candidate_songs) > 0:  # stop when no more eligible songs
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
```

The bulk of the logic however is given by (after getting `target_length`
from the user),

``` python
        candidate_songs = filter_tracks_shorter_than_length(target_length, tracks)

        if len(candidate_songs) == 0:
            print("Could not generate a playlist of that length. Try a longer playlist")
            return

        while len(candidate_songs) > 0:  # stop when no more eligible songs
            # add a random song and update the playlist length
            song_choice = random.choice(candidate_songs)
            suggested_playlist.append(song_choice)
            playlist_length = playlist_length + song_choice.length_in_seconds

            # filter out songs that no longer fit
            candidate_songs = filter_tracks_shorter_than_length(
                target_length - playlist_length, candidate_songs
            )
```

1. We filter the track database to get all the tracks that could fit in
    the allowed playlist time
2. We then randomly pick one of the songs using `random.choice`
    - We add this to our proposed playlist, and add its length to a
      counter tracking the total length
3. We then filter the candidate list again but with the amount of time
    we have yet to use (`target_time - playlist_length`)
4. We repeat steps 2-3 until there are no more candidate songs, this
    gives our final playlist which we can then propose to the user

This sums up the description of the music storage app. The provided code
demonstrates a sample database in
[tracks.pickle](./Exercises/03_MusicStorageApp/tracks.pickle) and a
sample playlist in
[example_playlist.txt](./Exercises/03_MusicStorageApp/example_playlist.txt).
You are encouraged to play around with the code and make sure you
understand what is going on. This program is not super complicated but
it has many components, if you can follow it, you are doing well!

## Make Something Happen: Recipe Storage App

*Make a recipe storage app that stores lists of ingredients and
preparation details. Remember that one of the items in a class could be
a list of strings, which could be the steps performed to prepare the
recipe*

This program will have less individual features than our music storage
program, however the object we’re working on will be complex so it’s
worth also working through this exercise.

### Storyboarding out the design

Let us start by setting out some design specifications,

1. The user should be able to add recipes
2. The user should be able to search for recipes
    - Search for a recipe by name
    - Search for recipes with a given ingredient
3. The user should be able to view a list of ingredients in a recipe
4. The user should be able to view a recipe’s steps
    - All steps displayed at once
    - Displayed step by step
5. The user should be able to edit a given recipe
    - Edit ingredients (including remove them)
    - Edit steps including remove them
6. The user should be able to delete a recipe

### Designing the Recipe Class

From this let’s design our recipe specification. A recipe at it’s most
basic is a list of ingredients and a list of steps. However, if I look
at the recipes that I have at home, quite often ingredients are often
listed both with a quantity and some description of how they should be
prepared. For example a recipe might specify

> 2 spring onions (scallions), finely sliced

We would like to store this extra information. A natural way to do it
would then be to use a dictionary, storing the ingredients as keys, and
the description as the value, i.e.

``` python
ingredients = {"spring onions" : "2, finely sliced"}
```

This also means that the user could quickly get a list of ingredients
for a recipe just by printing the dictionary. We can also easily search
for recipes with a given ingredient by using,

``` python
if ingredient in ingredients
```

**However**, this comes with the downside that the user would need to
specify the exact ingredient to search, i.e. we would have, for the
previous example,

``` python
print("spring onions" in ingredients)
print("Spring Onions" in ingredients)
print("scallions" in ingredients)
```

    True
    False
    False

A user might certainly expect that all these match. The problem is worse
when we consider for example an ingredient like

> small chicken thighs

One user might enter this as (in the dictionary notation),

``` python
ingredients = {"chicken" : "thighs, small"}
```

while another might instead use,

``` python
ingredients = {"chicken thighs" : "small"}
```

If the first user was to search `"chicken"` on a recipe entered by the
second user, they would not find what they expected!

For the purposes of this exercise to get familiarity working with
dictionaries, we’ll simply note these challenges and continue.

The second problem to consider is duplicate keys. In the recipes I read
it is quite common for recipes to be broken down into subcomponents,
each of which may use the same ingredient. This results in an ingredient
being listed multiple times. The way to resolve this is to store the
ingredient description as a *list* of *strings* rather than just one
string. For example if a recipe specified,

> black pepper, to serve black pepper, 1/4 teaspoon ground

The resulting dictionary entry would look like,

``` python
ingredients = {"black pepper" : ["to serve", "1/4 teaspoon ground"]}
```

The next part of the recipe is the steps themselves. This can simply be
treated as an ordered list of strings, so we just store them in a list.
Finally a recipe should have a name. This leaves our `Recipe` object
looking like,

``` python
class Recipe:
    """
    Represent a cooking recipe.

    Attributes
    ----------
    name : str
        Recipe name

    ingredients : dict[str, list[str]]
        Ingredients required for the recipe. Ingredients are stored
        as a dictionary in the format `ingredients[ingredient] = ["description", ...]`

    steps: list[str]
        Ordered list of instructions/steps to prepare the recipe.

    Example
    -------
    >>> Recipe("Omelette", {"eggs" : [2], "milk": ["1 cup"]}, ["Beat eggs", "Add milk", "Cook on pan"])
    """

    def __init__(self, name, ingredients, steps):
        """
        Create a new `Recipe` instance

        Parameters
        ----------
        name : str
            Name of the Recipe
        ingredients : dict[str, list[str]]
            Ingredients required for the recipe. Ingredients are stored
            as a dictionary in the format `ingredients[ingredient] = ["description", ...]`
            e.g. `ingredients["Brown Onion"] = ["1 Medium, diced"]`
        steps : list[str]
            Ordered list of instructions/steps to prepare the recipe.
        """
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
```

#### Creating a Recipe from User Input

We wrap the construction of these objects in a function `add_recipe` to
get input from the user,

``` python
def new_recipe():
    """
    Add a new recipe to the recipe database.

    A recipe consists of a name, dictionary of ingredients and a list of steps
    The user is prompted for the name, ingredients and the steps

    Returns
    -------
    None

    See Also
    --------
    Recipe : Class responsible for storing recipe information
    """
    print("Add New Recipe")
    name = BTCInput.read_text("Enter the recipe name: ")

    print("Enter ingredients")
    ingredients = get_ingredients()
    print("Enter Steps")
    steps = get_steps()
    recipe = Recipe(name, ingredients, steps)
    recipes.append(recipe)
```

This code should look pretty similar to what we’ve seen before except
for the fact that we refer to an unspecified `get_ingredients` and
`get_steps`. These functions both read ingredients or steps one at a
time from the user to construct the appropriate dictionary (or list) for
the `Recipe` object. Both are similar, so we’ll look at the more
complicated `get_ingredients` to understand the idea,

``` python
def get_ingredients():
    """
    Gets a dictionary of ingredients from the user.

    Ingredients are processed
    as key, value pairs of ingredients and descriptions such as their quantity
    or how they are to be prepared.

    Supports duplicates for an ingredient. If a duplicate is detected the
    user will be prompted if they wish to overwrite the existing key, value
    pair, add the description to the pair or ignore the current entry

    Returns
    -------
    dict[str, list[str]]
        Dictionary of Ingredient, description pairs. The dictionary is
        keyed by ingredients and the descriptions are stored as a list
        of strings

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    ingredients = {}
    while True:
        ingredient = BTCInput.read_text("Enter next ingredient or . to stop: ")
        if ingredient == ".":
            break
        if ingredient in ingredients:
            print("That ingredient is already included!")
            duplicate_choice = BTCInput.read_int_ranged(
                "Overwrite (2), append (1) or forget (0)?: ", min_value=0, max_value=2
            )
            if duplicate_choice == 0:
                continue  # ignore this entry and move to the next
            elif duplicate_choice == 1:
                pass  # for append behave normally
            elif duplicate_choice == 2:
                del ingredients[ingredient]  # remove existing entries
            else:
                raise ValueError(
                    "Invalid value "
                    + str(duplicate_choice)
                    + "encountered resolving duplicate ingredient"
                )
        ingredient_description = BTCInput.read_text("Enter quantity and description: ")
        if ingredient in ingredients:
            ingredients[ingredient].append(ingredient_description)
        else:
            ingredients[ingredient] = [ingredient_description]

    return ingredients
```

This code can be broken down as follows,

1. Ask the user for the name of the next ingredient
    - This next bit is a bit tricky, but we check if the ingredient
      already exists in the dictionary, if it does the user can,
      1. Overwrite it
          - Say if they accidentally mis-entered the previous ingredient
            they can use this to correct it
          - We use the `del` keyword to delete the key and the list
            associated with the key `ingredient`
      2. Append it
          - This allows the inclusion of multiple ingredient
            descriptions per ingredient
      3. Forget it
          - Perhaps the user simply accidentally entered an ingredient
            twice, this gives them to option to simply forget this entry
            and move on
2. Ask the user for a description of the ingredient like the quantity
    or how to prepare it
3. To add the ingredient and description we then have to check,
    - If the ingredient doesn’t exist yet, we have to create a new list
      containing the description, this is then assigned to the key
      `ingredient`
    - If the ingredient exists we can simply append to the existing list
4. This repeats until the user provides the `"."` as input, indicating
    they wish to stop
5. The created dictionary is returned

`add_steps` follows the same process, except the processed steps are
simply stored in an ordered list which is returned

### Finding Recipes

Let’s now look at adding search to our recipes. Our specification states
that we should be able to search for recipes by ingredients or by name

#### Listing Recipes

First we need a way to display the recipes returned by a search. Since
recipes can have many steps and ingredients we don’t want to follow the
Tiny Contacts and Music Storage Track approach of printing out all the
contents of the objects, instead we’ll simply print the names of the
recipes.

``` python
def list_recipes(recipes):
    """
    Prints the recipe names in a given list

    Parameters
    ----------
    recipes : list[Recipe]
        list of recipes to display

    Returns
    -------
    None
    """
    print("List Recipes")
    if len(recipes) == 0:
        print("No recipes found")
        return
    for recipe in recipes:
        print("-", recipe.name)
```

We can see this in action if we use the toy demonstration,

``` python
bacon_and_eggs = Recipe(
    name="Bacon and Eggs",
    ingredients={"Bacon": ["2 rashs"], "Eggs": ["1 large"]},
    steps=["Cook bacon", "Cook Eggs"],
)

eggs_on_toast = Recipe(
    name="Eggs on Toast",
    ingredients={"Bread": "2 slices", "Eggs": ["1 large"]},
    steps=["Toast bread", "Cook Eggs"],
)

recipes = [bacon_and_eggs, eggs_on_toast]
list_recipes(recipes)
```

    List Recipes
    - Bacon and Eggs
    - Eggs on Toast

Observe that `list_recipes` takes a list to print. That means we can use
the similar `filter` vs `find` approach as used in [Music
Storage](#track-management) to managing recipe selection

#### Find Recipes by Name

The by name search is similar to what we have already implemented in our
[Tiny
Contacts](./Chapter_09.qmd#use-the-contact-class-in-the-tiny-contacts-program)
and [Music Storage](#track-search-and-display) programs. However,
instead of using `startswith` we’ll use the `find` string method, the
documentation for `find` reads,

``` python
    import pydoc
    pydoc.help("a string".find)
```

    Help on built-in function find:

    find(...) method of builtins.str instance
        S.find(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.

We can see that `find` searches a string for matching substring anywhere
in the string (like `startswith` searches a string for matching
substring at the start)

Importantly, it also returns `-1` if there no match. This means that we
can use `find` to see if a recipe name contains the user provided search
string. So we define our filter function as,

``` python
def filter_recipe_by_name(search_name):
    """
    Finds and returns recipes whose name contains a search name

    Parameters
    ----------
    search_name : str
        name to search for, search is conducted as a substring search

    Returns
    -------
    list[Recipe]
        list of recipes whose name contains `search_name` as a substring
    """
    results = []
    search_name = search_name.strip().lower()
    for recipe in recipes:
        if recipe.name.strip().lower().find(search_name) != -1:
            results.append(recipe)
    return results
```

We use the standard normalisation of `strip().lower()` then call `find`
and check the return value is not `-1` to determine if we have a match

> [!NOTE]
>
> Remember our convention is a `filter_` function takes a search
> parameter and returns a list of matches while a `find_` prompts the
> user for the search parameter and displays / prints the matches

We can see the outcome of running, `filter_by_name` for a couple of
inputs on our `recipes` list,

``` python
print("Looking for toast...")
list_recipes(filter_recipe_by_name("toast"))
print("Looking for eggs")
list_recipes(filter_recipe_by_name("egg"))
print("Looking for milk")
list_recipes(filter_recipe_by_name("milk"))
```

    Looking for toast...
    List Recipes
    - Eggs on Toast
    Looking for eggs
    List Recipes
    - Bacon and Eggs
    - Eggs on Toast
    Looking for milk
    List Recipes
    No recipes found

The corresponding `find_by_name` function then looks very simple,

``` python
def find_recipe_by_name():
    """
    Prints all recipes matching a user-specified search

    Returns
    -------
    None
        Matches are printed to standard output

    See Also
    --------
    filter_recipe_by_name : returns a list containing recipes which match a name
    find_recipe_by_ingredient : find recipes containing a user-prompted ingredient
    """
    print("Find Recipe by Name")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe name: "))
    list_recipes(results)
```

#### Finding by Ingredients

Matching for ingredients looks very similar to the search method
proposed for the dictionary based [Tiny
Contacts](./Chapter_09.qmd#use-a-dictionary-to-store-contacts), combined
with our filter and find technique. The filter function,

``` python
def filter_recipe_by_ingredient(search_ingredient):
    """
    Find and return a list of all recipes which contain a given ingredient

    Parameters
    ----------
    search_ingredient : str
        ingredient to search for

    Returns
    -------
    list[Recipe]
        list of Recipes containing `search_ingredient`

    Warnings
    --------
    search matching is exact on `search_ingredient`, for example if a recipe
    had the ingredient dictionary,

    `{"Bread" : ["sliced"], "chicken thighs" : ["large"]}`

    1. `filter_recipes_by_ingredient("Bread")` would match
    2. `filter_recipes_by_ingredient("bread")` would not match
    3. `filter_recipes_by_ingredient("chicken")` would not match
    """
    results = []
    for recipe in recipes:
        if search_ingredient in recipe.ingredients:
            results.append(recipe)
    return results
```

Which we can see would have the following results,

``` python
print("Searching by ingredient: Eggs")
list_recipes(filter_recipe_by_ingredient("Eggs"))
print("Searching by ingredient: eggs")
list_recipes(filter_recipe_by_ingredient("eggs"))
print("Searching by ingredients: Bacon")
list_recipes(filter_recipe_by_ingredient("Bacon"))
print("Searching by ingredients: Milk")
list_recipes(filter_recipe_by_ingredient("milk"))
```

    Searching by ingredient: Eggs
    List Recipes
    - Bacon and Eggs
    - Eggs on Toast
    Searching by ingredient: eggs
    List Recipes
    No recipes found
    Searching by ingredients: Bacon
    List Recipes
    - Bacon and Eggs
    Searching by ingredients: Milk
    List Recipes
    No recipes found

We can see that as discussed the dictionary key search is vulnerable to
how the user chooses to input their ingredient. We could get around
simple differences like `eggs` and `Eggs` by simply normalising the keys
when they’re entered however if the user was to instead search `egg`
this would still break. Even worse would be if they searched `scallion`
instead of `spring onion` which would break even if we used a method
like `find`

As you should be able to see, the general search and find problem is
difficult!

### Viewing a Recipe

We now have a way to find recipes so we can start looking at how to view
them. As mentioned in printing out a recipe, they may have too much
information to simply print them out. We have three specifications to
implement

1. Display a recipe’s ingredients
    - This might be useful if we are simply trying to write a shopping
      list
2. Display a recipe’s steps
    - This might useful if we want to read through an entire recipe
3. Display recipe step by step
    - This would be useful when working through a recipe, the user would
      then be able to step through each recipe as they completed it

#### Selecting a Recipe to View

We will implement recipe viewing using a similar technique to the Music
Track program. If the user selects to view a recipe, we will first
perform a name based search, then the user can decide to view any
matches. If they do they will be taken to a new menu, which looks like,

``` text
Current Recipe: "Recipe currently selected to view"
View Recipe
1. View Ingredients
2. View Steps
3. View Step by Step
4. Return to Main Menu
```

The implementation of this first part looks like,

``` python
def view_recipes():
    """
    Provide a prompt for the user to select a recipe to view

    Reports the number of successful matches. For each match
    (if any) the user is then prompted if they wish to view
    the recipe in which case they are taken to the view
    recipe menu

    See Also
    --------
    `run_view_recipe_menu` - provides options for viewing a specific recipe
    """
    print("View Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to view: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe: ", recipe.name)
        command = BTCInput.read_int_ranged(
            "View this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 1:
            run_view_recipe_menu(recipe)
```

Observe that we defer the viewing functionality to the
`run_view_recipe_menu` function which accepts a `Recipe` object as a
parameter.

#### Viewing a Selected Recipe

To implement each of these features, lets work through them step by step

1. List ingredients
    - We could simply output the dictionary, but that won’t format
      nicely
    - Instead loop over the dictionary and print each ingredient then
      the list of descriptions with each ingredient getting its own line
2. List Steps
    - Again simply printing the list would not format nicely
    - We print the steps as a bullet-pointed list using by printing each
      list entry on a new line prepended by `-`
3. List Step by Step
    - For this we can follow the same procedure as above, **but**
    - Before the next iteration of the loop over the step list, we
      prompt the user to continue
    - For usability we’ll allow the user quit stepping through at any
      point using `q`

Finally after selecting any option, the function loops back to the start
allowing the user to chose another view option until they choose to quit
back to the main menu.

``` python
def run_view_recipe_menu(recipe):
    """
    Provides a looping menu interface allowing the user
    to view the details of a specific recipe

    View Options are

    1. List ingredients
        - Shows all the ingredients in a recipe
    2. View All Steps
        - Shows all the steps in a recipe
    3. Step through Recipe
        - Allows the user to interactively step through a recipe
        one step at a time

    Parameters
    ----------
    recipe : Recipe
        recipe to view

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    header = "Current Recipe: " + recipe.name + "\n"
    view_recipe_menu = (
        header
        + """View Recipe
1. List Ingredients
2. View All Steps
3. Step through Recipe
4. Return to Main Menu

Enter your command: """
    )
    while True:
        command = BTCInput.read_int_ranged(
            prompt=view_recipe_menu, min_value=1, max_value=4
        )
        if command == 1:
            print("Ingredients")
            for ingredient in recipe.ingredients:
                print(ingredient, "-", recipe.ingredients[ingredient])
        if command == 2:
            print("View all Steps")
            for step in recipe.steps:
                print("-", step)
        if command == 3:
            print(
                "Step through Recipe"
            )  # waits for user confirmation before printing next step
            for step in recipe.steps:
                print("-", step)
                go_to_next = BTCInput.read_text("Next step? (Q - Quit): ")
                if go_to_next.strip().upper() == "Q":
                    return
        if command == 4:
            break
```

A sample pipeline for above might look like,

    View Recipe
    Enter recipe to view:  Bacon
    Found 1 matches
    Recipe: Bacon and Eggs
    View this recipe? (1 - Yes, 0 - No): 1
    Current Recipe: Bacon and Eggs
    View Recipe
    1. List Ingredients
    2. View All Steps
    3. Step through Recipe
    4. Return to Main Menu

    Enter your command: 1

    Bacon - 2 rashs
    Eggs - 1 large

### Editing and Removing a Recipe

#### Remove a Recipe

The last features to implement are the processes of editing and removing
a recipe. Remove can be implemented simply enough, we use
`find_recipes_by_name` to get a list of matching recipes from the user,
then simply prompt them to see if the want to remove each one

``` python
def remove_recipe():
    """
    Remove a recipe from the database

    Prompts the user to select a recipe to match.
    Reports the number of successful matches. For each match
    (if any) the user is prompted if they want to remove the recipe

    Returns
    -------
    None

    See Also
    --------
    filter_recipe_by_name : gives a list of recipes matching a name
    """
    print("Remove Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to remove: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe:", recipe.name)
        command = BTCInput.read_int_ranged(
            "View this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 1:
            recipes.remove(recipe)
```

#### Edit a Recipe

For editing we also go with a simple implementation similar to what
we’ve already used for Tiny Contacts and the Music Track Storage App.
Here the user will search for a track to edit, then after confirming
they want to edit it, we prompt them for a new name, new ingredient
dictionary or new list of steps.

``` python
def edit_recipe():
    """
    Provides a prompt to the user to select a recipe to edit

    Reports the number of successful matches. For each match
    (if any) the user is prompted if they want to edit the recipe
    in which case they are provided the options to edit the name,
    ingredients or steps

    Returns
    -------
    None

    Warnings
    --------

    Edits are performed in-place and live, they cannot be rolled back

    See Also
    --------
    filter_recipe_by_name : gives a list of recipes matching a name
    """
    print("Edit Recipe")
    results = filter_recipe_by_name(BTCInput.read_text("Enter recipe to edit: "))
    if len(results) == 0:
        print("No recipe found matching that name")
    else:
        print("Found", len(results), "matches")
    for recipe in results:
        print("Recipe:", recipe.name)
        command = BTCInput.read_int_ranged(
            "Edit this recipe? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if command == 0:
            continue
        new_name = BTCInput.read_text("Enter new name or . to leave unchanged: ")
        if new_name != ".":
            recipe.name = new_name
        should_edit_ingredients = BTCInput.read_int_ranged(
            "Edit ingredients? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if should_edit_ingredients:
            recipe.ingredients = get_ingredients()
        should_edit_steps = BTCInput.read_int_ranged(
            "Edit steps? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        )
        if should_edit_steps:
            recipe.steps = get_steps()
```

This implementation perhaps isn’t the greatest, for example it might be
annoying to have to renter every step if you just want to fix a typo in
one step, or to have to renter every ingredient if you want to add a new
one. However for now this will do for a first pass

### Improving the Recipe Application

As we’ve hinted, there are plenty of ways that the recipe app could be
completed. However as it stands now, I’m pretty happy with it as a
something that’s gone through an initial design and a refactor. if
you’re interested you might like to try improve the following features

1. Improve the ingredient search to be more forgiving in how it matches
2. Improve the edit functionality
    - Allow the ingredient dictionary to be edited such that,
      1. An individual key can be edited
      2. An individual key can be removed
      3. An individual key can be added, (including as a duplicate)
    - Allow the steps list to be edited such that,
      1. An individual step can be edited
      2. An individual step can be removed
      3. An individual step can be added
