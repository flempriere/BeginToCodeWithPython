# Example 8.20 Using with to Access Files
#
# Rewrites read_sales and load_sales to use the with functionality
# implemented in python

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def save_sales(file_path):
    """
    Saves the contents of the sales list to a file

    Parameters
    ----------

    file_path : str
        string giving the file path to save to

    Returns
    -------
    None

    Raises
    ------
    FileException
        Raised if the save fails

    See Also
    --------
    load_sales : load sales from a given file
    """
    print("Save the sales in:", file_path)
    try:
        with open(file_path, "w") as output_file:
            for sale in sales:
                output_file.write(str(sale) + "\n")
    except:  # noqa: E722
        print("Something went wrong with the file")


def load_sales(file_path):
    """
    loads the contents of a file into the sales list

    Parameters
    ----------

    file_path : str
        string giving the file path to load from

    Returns
    -------
    None

    Raises
    ------
    FileException
        Raised if the load fails

    See Also
    --------
    save_sales : save sales to a file
    """
    print("Load the sales in:", file_path)
    sales.clear()
    try:
        with open(file_path, "r") as input_file:
            for line in input_file:
                line = line.strip()
                sales.append(int(line))
    except:  # noqa: E722
        print("Something went wrong with the file")


print("Sales before save and load:", sales)
save_sales("test.txt")
load_sales("test.txt")
print("Sales after save and load:", sales)
