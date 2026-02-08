# Exercise 12.1b Roman Numeral Converter
#
# Write a function that converts strings of roman numerals to an integer
#
# This implementation uses a lookup table

import itertools

import BTCInput

thousands = {"": 0, "M": 1000, "MM": 2000, "MMM": 3000}
hundreds = {
    "": 0,
    "C": 100,
    "CC": 200,
    "CCC": 300,
    "CD": 400,
    "D": 500,
    "DC": 600,
    "DCC": 700,
    "DCCC": 800,
    "CM": 900,
}
tens = {
    "": 0,
    "X": 10,
    "XX": 20,
    "XXX": 30,
    "XL": 40,
    "L": 50,
    "LX": 60,
    "LXX": 70,
    "VXXX": 80,
    "XC": 90,
}
ones = {
    "": 0,
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
}


roman_numeral_dictionary = {}

for p in itertools.product(
    thousands.items(), hundreds.items(), tens.items(), ones.items()
):
    key = ""
    value = 0
    for symbol_value_pair in p:
        key += symbol_value_pair[0]
        value += symbol_value_pair[1]
    roman_numeral_dictionary[key] = value

roman_numeral_dictionary.pop("")


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
    try:
        return roman_numeral_dictionary[number_string.upper().strip()]
    except KeyError:
        raise ValueError("{0} is not a valid roman numeral".format(number_string))


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
