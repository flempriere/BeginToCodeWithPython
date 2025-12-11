# Exercise 7.1: Teletype Printer
#
# Emulates the slow speed of a teletype printer
# by using a for loop and time to slowly loop over
# an input string

import time
import random


def teletype_printer(text, delay=0.5):
    jitter = delay / random.randint(1, 10)
    if random.randint(0, 1):
        delay = delay + jitter
    else:
        delay = delay - jitter

    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print("")


teletype_printer("hello")
