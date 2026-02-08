# Example 8.17 File Input
#
# Demonstrates reading input from a file

input_file = open("test.txt", "r")
for line in input_file:
    print(line)
input_file.close()
