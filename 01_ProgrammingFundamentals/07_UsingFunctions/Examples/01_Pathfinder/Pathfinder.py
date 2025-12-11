# Example 7.1: Pathfinder
#
# Sample Program to demonstrate function flow


def m2():
    print("the")


def m3():
    print("sat on")
    m2()


def m1():
    m2()
    print("cat")
    m3()
    print("mat")


m1()
