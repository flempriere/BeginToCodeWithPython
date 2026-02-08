# Example 8.18 File Read
#
# Demonstrates the use of file_object.read to read
# the contents of a file in one go

input_file = open("test.txt", "r")
total_file = input_file.read()
print(total_file)
input_file.close()
