# Example 7.10 Shadowing Global Variables
#
# Demonstrates local variables shadowing a
# global variable

cheese = 99


def func():
    cheese = 100
    print("Local cheese is:", cheese)


func()
print("Global cheese is:", cheese)
