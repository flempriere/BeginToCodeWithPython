# Example 7.7: Get Value
#
# Demonstrates function returns through a program
# that receives and validates an integer


def get_value(prompt, value_min, value_max):
    while True:
        number_text = input(prompt)
        try:
            number = int(number_text)
        except ValueError:
            print("Invalid number text. Please enter digits.")
            continue
        if number < value_min:
            print("Value too small")
            print("The minimum value is", value_min)
            continue
        elif number > value_max:
            print("Value too large")
            print("The maximum value is", value_max)
            continue
        return number


ride_number = get_value(
    prompt="Please enter the ride number you want: ", value_min=1, value_max=5
)

print("You have selected ride: ", ride_number)
