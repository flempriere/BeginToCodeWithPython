# Example 6.9 Times Tables Tutor
#
# Uses Times Tables to demonstrate use of a counter
# variable to control a loop

count = 1
times_value = 2
while count < 13:
    result = count * times_value
    print(count, "times", times_value, "equals", result)
    count = count + 1
