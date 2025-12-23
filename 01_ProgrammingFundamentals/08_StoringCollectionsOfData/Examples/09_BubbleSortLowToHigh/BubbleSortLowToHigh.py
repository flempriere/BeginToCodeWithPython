# Example 8.9 Bubble Sort Low to High
#
# Implementation of Bubble Sort that sorts from low to high

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def sort_low_to_high():
    """
    Print out a sales list from lowest to highest

    Returns
    -------
    None
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


print("Input list:", sales)

sort_low_to_high()

print("Output list:", sales)
