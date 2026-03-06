# Example 12.3 Robot Dancer
#
# Demonstrates creating collections of function references

import time


def forward():
    print("Robot moving forward")
    time.sleep(1)


def back():
    print("Robot moving backwards")
    time.sleep(1)


def left():
    print("Robot moving left")
    time.sleep(1)


def right():
    print("robot moving right")
    time.sleep(1)


dance_moves = [forward, back, left, right]

print("Dance starting")
for move in dance_moves:
    move()
print("Dance over")
