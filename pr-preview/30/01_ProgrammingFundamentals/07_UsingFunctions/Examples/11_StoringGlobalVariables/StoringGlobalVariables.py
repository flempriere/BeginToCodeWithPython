# Example 7.11 Storing Global Variables
#
# Demonstrates storing a global variables in a
# variable in a function. Also shows updating a global
# variable

cheese = 99


def func():
    global cheese  # use the global variable
    print("Global cheese is:", cheese)
    cheese = 100


func()
print("Global cheese is:", cheese)
