# Exercise 12.1a Roman Numeral Converter
#
# Write a function that converts strings of roman numerals to an integer
# This initial implementation uses an active parser that reads the string
# validating and converting to roman numerals as we go
import BTCInput


class RomanNumeral:
    """
    Lightweight class representing a roman numeral

    Attributes
    ----------
    symbol : str
        latin character symbolising the roman numeral
    value : int
        numeric value of a roman numeral
    precedes : set[str]
        set of strings representing other roman numerals this numeral may precede
    """

    def __init__(self, symbol, value, precedes):
        """
        Create a new `RomanNumeral` Instance

        Parameters
        ----------
        symbol : str
            latin character symbolising the roman numeral
        value : int
            numeric value of a roman numeral
        repetition_limit : int
            maximum number of times the same numeral can be repeated
        precedes : set[str]
            set of strings representing other roman numerals this numeral may precede
        """
        self.symbol = symbol
        self.value = value
        self.precedes = precedes

    def may_precede(self, roman_numeral):
        """
        Checks if this numeral may precede another

        Parameters
        ----------
        roman_numeral : str
            character representing roman numeral to check if we can precede

        Returns
        -------
        `True` if `self` may precede `roman_numeral` else, `False`
        """
        return roman_numeral in self.precedes


def roman_numeral_converter(number_string):
    """
    Convert a number written in roman numerals to an int

    The string must be a valid roman numeral in `standard format`__

    Parameters
    ----------
    number_string : str
        A valid roman numeral expression

    Returns
    -------
    int
        Result of converting the roman numeral to an int

    Raises
    ------
    ValueError
        Raised if `number_string` is not a valid roman numeral

    .. _standard format: https://en.wikipedia.org/wiki/Roman_numerals#Standard_form
    """
    roman_numerals = {
        "I": RomanNumeral("I", 1, {"I", "V", "X"}),
        "V": RomanNumeral("V", 5, {"I"}),
        "X": RomanNumeral("X", 10, {"I", "X", "L", "C"}),
        "L": RomanNumeral("L", 50, {"I", "V", "X"}),
        "C": RomanNumeral("C", 100, {"I", "V", "X", "L", "C", "M"}),
        "D": RomanNumeral("D", 500, {"C", "L", "X", "V", "I"}),
        "M": RomanNumeral("M", 1000, {"I", "V", "X", "L", "C", "D", "M"}),
    }

    def get_roman_numeral(numeral):
        """
        Returns the `RomanNumeral` corresponding to the provided string

        Parameters
        ----------
        numeral : str
            character representing a roman numeral digit

        Returns
        -------
        RomanNumeral
            object describing the corresponding roman numeral

        Raises
        ------
        ValueError
            The provided character is not a valid roman numeral digit

        """
        try:
            return roman_numerals[numeral]
        except KeyError:
            raise ValueError(numeral, "is not a valid character for a roman numeral")

    total = 0
    previous = None
    n_reps = 0
    number_string = number_string.upper().strip()
    max_repeats = 3

    for i, ch in enumerate(number_string):
        # get the roman numeral associated with the next character
        numeral = get_roman_numeral(ch)
        if numeral.value == previous:
            # check that we haven't repeated this numeral too many times
            n_reps += 1
            if n_reps > max_repeats:
                raise ValueError(
                    ch,
                    "repeated {0} times, maximum is {1}".format(n_reps, max_repeats),
                )
        else:
            n_reps = 1
        if i + 1 == len(number_string):  # reached the end and stop
            return total + numeral.value
        else:
            next_numeral = get_roman_numeral(number_string[i + 1])

            if not numeral.may_precede(next_numeral.symbol):
                raise ValueError(
                    "Invalid roman numeral: {0} may not precede {1}".format(
                        numeral.symbol, next_numeral.symbol
                    )
                )
            # if next is larger perform subtraction if valid
            if next_numeral.value > numeral.value:
                if n_reps > 1:
                    raise ValueError(
                        "Invalid roman numeral: cannot repeat digits for subtraction"
                    )
                else:
                    total -= numeral.value
            else:
                total += numeral.value
        previous = numeral.value
    return total


# Tests

print("I: Expected: 1, Received: {0}".format(roman_numeral_converter("I")))
print("V: Expected: 5, Received: {0}".format(roman_numeral_converter("V")))
print("X: Expected: 10, Received: {0}".format(roman_numeral_converter("X")))
print("L: Expected: 50, Received: {0}".format(roman_numeral_converter("L")))
print("C: Expected: 100, Received: {0}".format(roman_numeral_converter("C")))
print("D: Expected: 500, Received: {0}".format(roman_numeral_converter("D")))
print("M: Expected: 1000, Received: {0}".format(roman_numeral_converter("M")))

## Now Test basic repetition rules

print("II: Expected: 2, Received: {0}".format(roman_numeral_converter("II")))
print("III: Expected: 3, Received: {0}".format(roman_numeral_converter("III")))
try:
    print(
        "IIII: Expected: Invalid Number, Received: {0}".format(
            roman_numeral_converter("IIII")
        )
    )
    print("Test failed, no exception thrown")
except ValueError as e:
    print(e)
    print("Test passed exception encountered")

try:
    print(
        "VV: Expected: Invalid Number, Received: {0}".format(
            roman_numeral_converter("VV")
        )
    )
    print("Test failed, no exception thrown")
except ValueError as e:
    print(e)
    print("Test passed exception encountered")

print("IV: Expected: 4, Received: {0}".format(roman_numeral_converter("IV")))

try:
    print(
        "IIV: Expected: Invalid Number: Received: {0}".format(
            roman_numeral_converter("IIV")
        )
    )
    print("Test failed, no exception thrown")
except ValueError as e:
    print(e)
    print("Test passed, exception encountered")


# Testing a complex expression

print(
    "MMMDCXCVIII: Expected: 3698, Result: {0}".format(
        roman_numeral_converter("MMMDCXCVIII")
    )
)

## Test precedence rules
try:
    print(
        "VX: Expected: Invalid Number, Received: {0}".format(
            roman_numeral_converter("VX")
        )
    )
    print("Test failed, no exception thrown")
except ValueError as e:
    print(e)
    print("Test passed exception encountered")

try:
    print(
        "IM: Expected: Invalid Number, Received: {0}".format(
            roman_numeral_converter("IM")
        )
    )
    print("Test failed, no exception thrown")
except ValueError as e:
    print(e)
    print("Test passed exception encountered")

print(BTCInput.read_number("Enter a standard roman numeral: ", roman_numeral_converter))
