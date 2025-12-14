# Example 8.11 Total Sales
#
# Calculate the Total Sales

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


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


print("Input list:", sales)

total_sales()
