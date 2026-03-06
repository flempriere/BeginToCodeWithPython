# Exercise 7.2.3: Pizza Order Calculator
#
# Implementation of Pizza Order Calculator that uses BTCInput

import BTCInput

students_int = BTCInput.read_int("How many students are attending? ")

pizza_count = int(students_int / 1.5) + 1  # perform division int -> float
print("You will need", pizza_count, "pizzas")
