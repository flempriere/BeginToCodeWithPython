# Example 7.13 BTCInput
# A collection of functions for reading validated input
# from the user


def read_text(prompt="Please enter some text: "):
    """
    Displays a prompt and reads in a string of text.
    Keyboard Interrupts are ignored

    Parameters
    ----------
    prompt : str
        Prompt the user sees before entering text

    Returns
    -------
    str
        String containing the string input by the user
    """
    while True:
        try:
            result = input(prompt)
            break  # stop loop if no exception
        except KeyboardInterrupt:
            print("Please enter text")
    return result


name = read_text("Please enter your name: ")
print("Your name is", name)


def read_float(prompt):
    """
    Displays a prompt and reads in a number

    Keyboard interrupts are ignored
    Invalid numbers are rejected

    Parameters
    ----------
    prompt : str
        Prompt the user sees before giving input

    Returns
    -------
    float
        The input value

    See Also
    --------
    read_float_ranged : reads a float resticted to a closed interval
    """
    while True:
        try:
            number_text = read_text(prompt)
            result = float(number_text)
            break
        except ValueError:
            print("Please enter a number")
    return result


def read_float_ranged(prompt, min_value, max_value):
    """
    Displays a prompt and reads in a number between
    min_value and max_value (inclusive)

    Keyboard interrupts are ignored
    Invalid numbers or out of range numbers are rejected

    Parameters
    ----------
    min_value: float
        minimum value (inclusive)
    max_value: float
        maximum value (inclusive)

    Returns
    -------
    float
        value input by user in the range [min_value, max_value]

    Raises
    ------
    Exception
        If min_value > max_value

    See Also
    --------
    read_float : reads an unbounded float
    """
    if min_value > max_value:
        raise Exception("Min value is greater than max value")
    while True:
        result = read_float(prompt)
        if result < min_value:
            print("That number is too low")
            print("The minimum value is", min_value)
            continue
        elif result > max_value:
            print("That value is too large")
            print("The maximum value is", max_value)
            continue
        break  # if here have a valid number
    return result
