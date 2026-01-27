# Example 7.2: Times Tables
#
# Demonstrates function parameters through a
# Times Table function that takes in an argument to
# determine which times table is printed


def print_times_table(times_value):
    count = 1
    while count < 13:
        result = count * times_value
        print(count, "times", times_value, "equals", result)
        count = count + 1


print_times_table(6)
