# Example 8.20 Using with to Access Files
#
# Rewrites read_sales and load_sales to use the with functionality
# implemented in python

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def save_sales(file_path):
    """
    Saves the contents of the sales list in the file given by file_path

    Parameters
    ----------

    file_path : str
        string giving the file path to save to

    Raises
    ------
    FileException
        Raised if the save fails

    Returns
    -------
    None
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
    loads the contents of the file given by file_path into the sales list

    Parameters
    ----------

    file_path : str
        string giving the file path to load from

    Raises
    ------
    FileException
        Raised if the load fails

    Returns
    -------
    None
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
