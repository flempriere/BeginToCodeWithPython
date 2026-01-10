# Exercise 4.1.2: Pizza Order Calculator
#
# A basic pizza order calculator based on the heuristic that 1 pizza = 1.5 people fed
# Converts the rseult to an integer using int on pizza_count then adding one
# has the disadvantage it will tend to overestimate the number of pizzas needed

students_int = int(
    input("How many students are attending? ")
)  # read in string, convert to int and store
pizza_count = int(students_int / 1.5) + 1  # perform division int -> float
print("You will need", pizza_count, "pizzas")
