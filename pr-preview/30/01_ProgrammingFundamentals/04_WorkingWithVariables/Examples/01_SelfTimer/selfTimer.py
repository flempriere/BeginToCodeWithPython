# Example 4.1: Self Timer
#
# Extends the Nerves of Steel Game from Chapter 3, by adding a skill element
# with the players being informed of how long they have to stand for

import random
import time

print("Welcome to Self Timer")
print()  # just prints a newline
print("Everybody stand up")
print("Stay standing until you think the time has ended")
print("Then sit down")
print("Anyone still standing when the time expires loses")
print("The last person to sit down before the time ended will win")

stand_time = random.randint(5, 20)  # generate the time to stand for

print("Stay standing for", stand_time, "seconds.")  # display standing time
time.sleep(stand_time)  # sleep for the standing time
print("****TIMES UP, LAST TO SIT WINS!****")
