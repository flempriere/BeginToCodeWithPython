# Example 6.11 Range Based Times Tables
#
# Demonstrates Python's range function using a for
# loop to generate a times table

times_value = 2
for count in range(1, 13):
    result = count * times_value
    print(count, "times", times_value, "equals", result)
