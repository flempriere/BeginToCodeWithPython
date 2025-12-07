# Exercise 6.6: Times Table Quiz
#
# Generates a times table quiz

import random

print("===Times table Quiz===")
score = 0
NumberOfQuestions = 12

for question in range(0, NumberOfQuestions):
    times_value = random.randint(2, 12)
    count = random.randint(1, 12)
    correct_answer = times_value * count
    while True:
        try:
            answer_text = input(
                "What is " + str(count) + " x " + str(times_value) + ": "
            )
            answer = int(answer_text)
            break
        except ValueError:
            print("Please enter an integer")
    if answer == correct_answer:
        score = score + 1
        print("Corect!")
    else:
        print("Sorry that's wrong!")
        print("The correct answer is", correct_answer, "you gave", answer)

print("You got", score, "/", NumberOfQuestions, "correct")
