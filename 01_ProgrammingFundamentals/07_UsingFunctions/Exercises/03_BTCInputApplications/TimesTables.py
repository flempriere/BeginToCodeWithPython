# Exercise 7.2.6 Tables Tables
#
# Variant of the User Selected Times Tables Tutor that uses BTCInput for
# validation

import BTCInput

count = 1
times_value = BTCInput.read_int("Please enter a times table between 2-12 (inclusive): ")

while count < 13:
    result = count * times_value
    print(count, "times", times_value, "equals", result)
    count = count + 1
