# Exercise 8.2 File Output
#
# A simple program to demonstrate opening and writing to a file

output_file = open("test.txt", "w")
output_file.write("line 1\n")
output_file.write("line 2\n")
output_file.close()
