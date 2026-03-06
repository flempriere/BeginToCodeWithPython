# Example 7.8 Local Variables
#
# Demonstrates the local namespaces of functions


def func_2():
    i = 99  # noqa: F841


def func_1():
    i = 0
    func_2()
    print("The value of i is: ", i)


func_1()
