# Example 6.7 Loop with condition ending early
#
# Demonstrates the pairing of break and conditional
# statements to end a program early

count = 0
while count < 5:
    print("Inside Loop")
    count = count + 1
    if count == 3:
        break
print("Outside loop")
