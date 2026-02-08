# Example 9.10: Pirate Treasure Dictionary
#
# Implementation of the Pirates Treasure map that uses a
# dictionary rather than a tuple to provide contextual
# key-value pairs


def get_treasure_location():
    """
    Get the location of the treasure

    Returns
    -------
    dict
        Dictionary containing the location of the treasure, containing
        the following keys

        `"start"` : str

            landmark to start at

        `"n"` : int

            number of paces to walk north relative to the
            start

        `"e"` : int

            number of paces to walk east relative to the
            start
    """
    return {"start": "The old oak tree", "n": 20, "e": 30}


location = get_treasure_location()
print(
    "Start at",
    location["start"],
    "walk",
    location["n"],
    "paces north, and",
    location["e"],
    "paces east",
)
