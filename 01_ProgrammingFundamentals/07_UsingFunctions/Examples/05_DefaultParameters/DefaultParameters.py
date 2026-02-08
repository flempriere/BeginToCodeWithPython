# Example 7.5: Default Parameters
#
# Demonstrates default arguments by capturing the single
# argument times table code in the two parameter version


def print_times_table(times_value, limit=12):
    count = 1
    while count < limit + 1:
        result = times_value * count
        print(count, "times", times_value, "equals", result)
        count = count + 1


print_times_table(times_value=7)
