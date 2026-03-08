# Example 8.25 Pirates Treasure
#
# Demonstrates returning a tuple from a function, and tuple-unpacking
# to access its arguments


def get_treasure_location():
    """
    Gets the location of the treasure

    Returns
    -------
    str
        Name of a landmark to start at
    int
        Number of paces north
    int
        Number of paces east
    """

    return ("The old oak tree", 20, 30)


landmark, north, east = get_treasure_location()
print("Start at", landmark, "walk", north, "paces north and", east, "paces east")
