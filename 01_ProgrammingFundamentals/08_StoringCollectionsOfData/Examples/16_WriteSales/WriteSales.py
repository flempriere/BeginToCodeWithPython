# Example 8.16 Write Sales
#
# Implements the Write Sales function

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
    """
    print("Save the sales in: ", file_path)
    output_file = open(file_path, "w")
    for sale in sales:
        output_file.write(str(sale) + "\n")
    output_file.close()


save_sales("test_output.txt")
