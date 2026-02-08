# Example 8.7 Bubble Sort Multiple Pass
#
# Implements a complete working version of bubble sort

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def sort_high_to_low():
    """
    Print out a sales list from highest to lowest

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(sales)):
        for count in range(0, len(sales) - 1):
            if sales[count] < sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp


print("Input list:", sales)

sort_high_to_low()

print("Output list:", sales)
