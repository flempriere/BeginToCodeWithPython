# Example 7.14 Investigate the Debugger
#
# A sample code for practising with the debugger


def increment_function(input_value):
    """
    Increments the input value by one

    Parameters
    ----------
    input_value : int | float
        value to increment

    Returns
    -------
    int | float
        `input_value` + 1
    """
    result = input_value + 1
    return result


x = 99
y = increment_function(x)
print("The answer is:", y)
