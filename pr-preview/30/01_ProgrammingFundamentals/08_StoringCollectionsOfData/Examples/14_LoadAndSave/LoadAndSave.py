# Example 8.14 Load and Save
#
# Implementation of the Sales Program with stub functionality implemented for
# Loading and Saving from a file

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

    See Also
    --------
    sort_low_to_high : sorts from lowest to highest
    """
    for sort_pass in range(0, len(sales)):
        done_swap = False
        for count in range(0, len(sales) - 1 - sort_pass):
            if sales[count] < sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def sort_low_to_high():
    """
    Print out a sales list from lowest to highest

    Returns
    -------
    None

    See Also
    --------
    sort_high_to_low : sorts from highest to lowest
    """
    for sort_pass in range(0, len(sales)):
        done_swap = False
        for count in range(0, len(sales) - 1 - sort_pass):
            if sales[count] > sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def highest_and_lowest():
    """
    Print out the highest and lowest elements of a sales list

    Returns
    -------
    None
    """
    highest = sales[0]
    lowest = sales[0]

    for sales_value in sales:
        if sales_value > highest:
            highest = sales_value
        elif sales_value < lowest:
            lowest = sales_value
    print("The highest is:", highest)
    print("The lowest is", lowest)


def total_sales():
    """
    Print out the total sales of a sales list

    Returns
    -------
    None
    """
    total = 0
    for sales_value in sales:
        total = total + sales_value
    print("Total sales are:", total)


def average_sales():
    """
    Print out the average sales of a sales list

    Returns
    -------
    None
    """
    total = 0
    for sales_value in sales:
        total = total + sales_value
    average_sales = total / len(sales)
    print("Average sales are:", average_sales)


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
    load_sales : load sales from a sales list file
    """
    print("Save the sales in:", file_path)


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
    save_sales : save the sales list into a file
    """
    print("Load the sales in:", file_path)


# Get initial sales list
read_sales(10)


menu = """
Ice Cream Sales

0. Quit the Program
1. Print the Sales
2. Sort High to Low
3. Sort Low to High
4. Highest and Lowest
5. Total Sales
6. Average Sales
7. Enter Figures
8. Save Sales
9. Load Sales

Enter your command: """

while True:
    command = BTCInput.read_int_ranged(menu, 0, 9)
    if command == 0:
        break
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
    elif command == 8:
        file_to_save_to = BTCInput.read_text("Enter file to save to: ")
        save_sales(file_to_save_to)
    elif command == 9:
        file_to_load_from = BTCInput.read_text("Enter file to load: ")
        load_sales(file_to_load_from)
    else:
        raise ValueError("Unexpected value " + str(command) + " found")
