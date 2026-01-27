# Example 7.3: Safe Times Tables
#
# A version of Times Tables that uses isinstance
# to ensure that argument is an integer


def print_times_table(times_value):
    if not isinstance(times_value, int):
        raise Exception("print_times_table requires an integer argument")
    count = 1
    while count < 13:
        result = count * times_value
        print(count, "times", times_value, "equals", result)
        count = count + 1


print_times_table("six")
