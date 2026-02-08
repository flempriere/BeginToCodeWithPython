# Example 8.8 Efficient Bubble Sort
#
# A bubble sort implementation incorporating efficiency savings to the number
# of comparisons and passes through the list

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
        done_swap = False
        for count in range(0, len(sales) - 1 - sort_pass):
            if sales[count] < sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


print("Input list:", sales)

sort_high_to_low()

print("Output list:", sales)
