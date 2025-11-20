# Example 4.6: Pizza Order Calculator
# A basic pizza order calculator based on the heuristic that 1 pizza = 1.5 people fed
# Converts the rseult to an integer using int when calculating pizza_count
# has the disadvantage it will tend to underestimate the number of pizzas needed

students_int = int(
    input("How many students are attending? ")
)  # read in string, convert to int and store
pizza_count = int(students_int / 1.5)  # perform division int -> float
print("You will need", pizza_count, "pizzas")
