# Example 12.4 Lambda Functions
#
# Demonstrates the creation and use of lambda functions

numbers = [2, 3, 4, 5, 6, 7, 8]


# using the function based method


def increment(x):
    return x + 1


new_numbers_fn = map(increment, numbers)
print("Increment list: ", list(new_numbers_fn))

# using the lambda based method

new_numbers_lambda = map(lambda x: x + 1, numbers)
print("Increment list: ", list(new_numbers_lambda))
