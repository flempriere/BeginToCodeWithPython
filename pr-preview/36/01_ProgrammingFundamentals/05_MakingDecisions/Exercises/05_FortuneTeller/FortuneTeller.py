# Exercise 5.5 Fortune Teller Program
#
# A simple program that uses random numbers to generate a sequence of
# fortunes for the user

import random

# Meeting someone
if random.randint(1, 6) < 4:
    print("You will meet a tall, dark stranger")
else:
    print("Nobody unexpected will enter your life")

# Money
result = random.randint(1, 6)
if result == 1:
    print("I see untold riches in your future")
elif result <= 3:
    print("A life of comfort is coming")
elif result < 6:
    print("You would do well to husband your wealth")
else:
    print("I see a future lived on the streets...")

# Advice
result = random.randint(1, 6)
if result <= 2:
    print("Sometimes the answers to our future, come from the past")
elif result < 6:
    print("To define your future, avoid getting hung up on the past")
else:
    print("You will soon face a decision that will redefine everything")
