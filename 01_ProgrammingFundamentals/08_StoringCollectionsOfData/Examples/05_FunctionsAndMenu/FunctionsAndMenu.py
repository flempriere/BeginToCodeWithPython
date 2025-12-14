# Example 8.5 Functions and Menu
#
# Uses placeholder functions and stubs to implement the user menu
# for the sales program

import BTCInput

# global sales list
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
    Prints the sales figures on the screen with a heading. Each figure is
    numbered in sequence

    Returns
    -------
    None
    """
    print("Sales Figures")
    count = 1
    for sales_value in sales:
        print("Sales for stand", count, "are", sales_value)
        count = count + 1


def sort_high_to_low():
    """
    Print out a sales list from highest to lowest

    Returns
    -------
    None
    """
    pass


def sort_low_to_high():
    """
    Print out a sales list from lowest to highest

    Returns
    -------
    None
    """
    pass


def highest_and_lowest():
    """
    Print out the highest and lowest elements of a sales list

    Returns
    -------
    None
    """
    pass


def total_sales():
    """
    Print out the total sales of a sales list

    Returns
    -------
    None
    """
    pass


def average_sales():
    """
    Print out the average sales of a sales list

    Returns
    -------
    None
    """
    pass


menu = """
Ice Cream Sales

1. Print the Sales
2. Sort High to Low
3. Sort Low to High
4. Highest and Lowest
5. Total Sales
6. Average Sales
7. Enter Figures

Enter your command: """

command = BTCInput.read_int_ranged(menu, 1, 7)

if command == 1:
    print_sales()
elif command == 2:
    sort_high_to_low()
elif command == 3:
    sort_low_to_high()
elif command == 4:
    highest_and_lowest()
elif command == 5:
    total_sales()
elif command == 6:
    average_sales()
elif command == 7:
    read_sales(10)
else:
    raise ValueError("Unexpected value " + str(command) + " found")
