# Exercise 7.2 Teletype Fortune Teller
#
# Version of the Fortune Teller Program that uses the teletype_printer function
# to delay the output

import random
import time


def teletype_printer(text, delay=0.25):
    jitter = delay / random.randint(1, 10)
    if random.randint(0, 1):
        delay = delay + jitter
    else:
        delay = delay - jitter

    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print("")


teletype_printer("...", delay=0.5)
# Meeting someone
if random.randint(1, 6) < 4:
    teletype_printer("You will meet a tall, dark stranger")
else:
    teletype_printer("Nobody unexpected will enter your life")

teletype_printer("...", delay=0.5)
# Money
result = random.randint(1, 6)
if result == 1:
    teletype_printer("I see untold riches in your future")
elif result <= 3:
    teletype_printer("A life of comfort is coming")
elif result < 6:
    teletype_printer("You would do well to husband your wealth")
else:
    teletype_printer("I see a future lived on the streets...")

teletype_printer("...", delay=0.5)
# Advice
result = random.randint(1, 6)
if result <= 2:
    teletype_printer("Sometimes the answers to our future, come from the past")
elif result < 6:
    teletype_printer("To define your future, avoid getting hung up on the past")
else:
    teletype_printer("You will soon face a decision that will redefine everything")
