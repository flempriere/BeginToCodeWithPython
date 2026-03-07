# Example 8.10 Highest and Lowest
#
# Function that finds the highest and lowest value in a collection

# Example 8.9 Bubble Sort Low to High
#
# Implementation of Bubble Sort that sorts from low to high

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


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


print("Input list:", sales)

highest_and_lowest()
