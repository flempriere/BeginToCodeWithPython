# Exercise 6.5 User SelectedTimes Tables Tutor
#
# Version of the times table tutor that allows the user to select the
# times table in the range 2 - 12 they are interested in

count = 1
while True:
    try:
        times_value_text = input(
            "Please enter a times table between 2-12 (inclusive): "
        )
        times_value = int(times_value_text)
        if times_value < 2 or times_value > 12:
            print("Sorry, that is not between 2-12 (inclusive)")
        else:
            break
    except ValueError:
        print("Please enter an integer")

while count < 13:
    result = count * times_value
    print(count, "times", times_value, "equals", result)
    count = count + 1
