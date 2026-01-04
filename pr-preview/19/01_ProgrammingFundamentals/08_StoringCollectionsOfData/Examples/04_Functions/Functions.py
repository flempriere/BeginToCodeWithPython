# Example 8.4 Functions
#
# Demonstrates refactoring a program into component functions

import BTCInput

sales = []


def read_sales(number_of_sales):
    """
    Reads in the sales values and stores them in the sales list

    Parameters
    ----------
    number_of_sales : int
        Number of Stores to record sales values for

    Returns
    -------
    None
        Results are read into the sales list
    """
    sales.clear()  # remove existing sales values
    for count in range(1, number_of_sales + 1):
        prompt = "Enter the sales for stand " + str(count) + ": "
        sales.append(BTCInput.read_int(prompt))


def print_sales():
    """
    Prints the sales figures on the screen with a heading.

    Each figure is numbered in sequence

    Returns
    -------
    None
    """
    print("Sales Figures")
    count = 1
    for sales_value in sales:
        print("Sales for stand", count, "are", sales_value)
        count = count + 1


read_sales(10)
print_sales()
