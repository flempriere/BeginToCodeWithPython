# Example 8.19 Load Sales
#
# Implements the Load Sales function

sales = []


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
    input_file = open(file_path, "r")
    for line in input_file:
        line = line.strip()
        sales.append(int(line))
    input_file.close()


load_sales("test_input.txt")
print(sales)
