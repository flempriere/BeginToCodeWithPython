# Example 12.2 Invalid Function References


def func_1():
    print("Hello from func_1")


x = func_1
x(99)
