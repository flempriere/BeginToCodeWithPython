# Example 7.4: Two Parameter Times Table
#
# Demonstrates a multi-parameter function through a variable
# length times table program


def print_times_table(times_value, limit):
    count = 1
    while count < limit + 1:
        result = times_value * count
        print(count, "times", times_value, "equals", result)
        count = count + 1


# call by positional arguments
print_times_table(6, 5)

# call by keyword arguments
print_times_table(times_value=12, limit=7)
