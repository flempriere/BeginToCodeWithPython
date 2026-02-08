# Example 12.6 Demonstrates functions with arbitrary arguments


def add_function(*values):
    total = 0
    for value in values:
        total += value
    return total


print(add_function())
print(add_function(1))
print(add_function(1, 2))
print(add_function(1, 2, 3))

numbers = (1, 2, 3, 4, 5)

print(add_function(*numbers))

print(sum(numbers))
