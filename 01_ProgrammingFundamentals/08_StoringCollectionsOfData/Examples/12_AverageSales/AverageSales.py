# Example 8.12 Average Sales
#
# Calculate the Average Sales

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


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


print("Input list:", sales)

average_sales()
