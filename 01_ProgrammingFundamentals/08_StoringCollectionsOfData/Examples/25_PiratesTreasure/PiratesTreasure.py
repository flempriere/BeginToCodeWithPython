# Example 8.25 Pirates Treasure
#
# Demonstrates returning a tuple from a function, and tuple-unpacking
# to access its arguments


def get_treasure_location():
    """
    Gets the location of the treasure

    Returns
    -------
    tuple(str, int, int)

    [0] is a string naming the landmark to start
    [1] is the number of paces north
    [2] is the number of paces east
    """

    return ("The old oak tree", 20, 30)


landmark, north, east = get_treasure_location()
print("Start at", landmark, "walk", north, "paces north and", east, "paces east")
