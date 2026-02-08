# Example 7.6 Parameters as Values
#
# Demonstrates how python handles passing values to a function


def what_would_I_do(input_value):
    input_value = 99  # noqa: F841


test = 0
what_would_I_do(test)
print("The value of test is", test)
