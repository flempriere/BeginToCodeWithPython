# Chapter 6: Repeating Actions with Loops

- [Notes](#notes)
  - [The `while` construction](#the-while-construction)
    - [Example: Investigating the `while`
      construction](#example-investigating-the-while-construction)
    - [Exercise: Create a Looping Selection
      Program](#exercise-create-a-looping-selection-program)
    - [Exercise: Create a Looping Countdown
      Program](#exercise-create-a-looping-countdown-program)
    - [Handling Invalid User Entry](#handling-invalid-user-entry)
      - [Make a Loop to Validate Input](#make-a-loop-to-validate-input)
        - [Exercise: Add Ride Number Validation to the Theme Park Ride
          Selector](#exercise-add-ride-number-validation-to-the-theme-park-ride-selector)
        - [Example: When good loops go
          bad](#example-when-good-loops-go-bad)
        - [Exercise: Add Validation to the Theme Park Age
          Input](#exercise-add-validation-to-the-theme-park-age-input)
    - [Detect Invalid Number Entry using
      Exceptions](#detect-invalid-number-entry-using-exceptions)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### The `while` construction

- `while` allows a program to repeat blocks of statements
- structure is similar to an `if`

``` mermaid
block-beta
    columns 4
    space
    title["Breakdown of a While"]:2
    space

    block:Input
    columns 1
        while["while"]
        whileDescr["(start of the while construction)"]
    end

    block:MiddleOne
    columns 1
        condition["condition"]
        conditionDescr["(value that is True or False)"]
    end

    block:MiddleTwo
    columns 1
        colon[":"]
        colonDescr["Colon"]
    end

    block:Suite
    columns 1
        suite["Statement block"]
        suiteDescr["(statements)"]
    end

classDef BG stroke:transparent, fill:transparent
class title BG
class condition BG
class conditionDescr BG
class colon BG
class colonDescr BG
class while BG
class whileDescr BG
class suite BG
class suiteDescr BG
```

- if the condition evaluates `True` then the block of statements is run
  - After the statements are run, control returns to the start of the
    `while` loop
  - If the condition is *still* `True` then the loop runs again

#### Example: Investigating the `while` construction

*Use the python interpreter to run the following to understand the*
`while` *loop*

1. *Can we use a boolean value to control a* `while` *construction?*

    - *Yes, for example the block of statements in the* `while` *here
      shouldn’t run*

    ``` python
     while False:
         print("Loop")
     print("Outside the Loop")
    ```

        Outside the Loop

2. *Can a loop go on forever?*

    - *Yes, an control expression for a* `while` *that always evaluates*
      `True` *will cause the loop to run infinitely*

    ``` python
     while True:
         print("Loop")
     print("Outside the Loop")
    ```

    - *The above should only print* `"Loop"` *when executed*
    - *If you accidently do this you may need to use `CTRL+C`, `CRTL+Z`
      or an interrupt execution feature of your live environment to stop
      the execution*

3. *Will the following program ever print out the message,*
    `"Outside loop"`*?*

    ``` python
     while True:
         print("Inside Loop")
     print("Outside Loop")
    ```

    - *No, the above is a quintessential infinite loop*

4. *Will the following program ever print out the message,*
    `"Inside Loop"`*? How about* `"Outside loop"`*?*

    ``` python
     while False:
         print("Inside Loop")
     print("Outside Loop")
    ```

        Outside Loop

    - *The* `while` *never executes the statements inside so*
      `"Inside Loop"` *is never printed, but* `"Outside Loop"` *is.*

5. *What will the following program print?*

    ``` python
     flag = True
     while flag:
         print("Inside Loop")
         flag = False
     print("Outside Loop")
    ```

        Inside Loop
        Outside Loop

    - *When we first enter the loop* `flag` *is* `True` *so the loop
      executes and* `"Inside Loop"` *is printed*, `flag` *is then set*
      `False` *so on the next iteration of the loop, the loop doesn’t
      execute. We move to the next statement outside of the loop and
      print out* `"Outside Loop"`
    - *The pattern of using a control variable that is updated in the
      loop body in a* `while` *loop is very common*

6. *What will the following program print?*

    ``` python
     flag = True
     while flag:
         print("Inside Loop")
         Flag = False
     print("Outside Loop")
    ```

    - *This looks similar to the previous, but note the typo, we refer
      to* `Flag` **not** `flag` *inside the loop, which defines a*
      **new** *variable, instead of modifying the loop control. We thus
      get an infinite series of* `"Inside Loop"` *being printed.*

7. *What will the following program print?*

    ``` python
     count = 0
     while count < 5:
         print("Inside Loop")
         count = count + 1
     print("Outside Loop")
    ```

        Inside Loop
        Inside Loop
        Inside Loop
        Inside Loop
        Inside Loop
        Outside Loop

    - `count` *is initially set to* $0$*, at each iteration we print*
      `"Inside Loop"` *and increase the value of* `count` *by* $1$*. The
      loop stops once* `count` *reaches* $5$ *This means that*
      `"Inside Loop"` *should be printed* $5$ *times, followed by*
      `"Outside Loop"`

#### Exercise: Create a Looping Selection Program

*Use a* `while` *loop, to make a theme park selector that runs
continously. All you need to do is put all of the statements that
implement the theme park behaviour into a* `while True` *construction*

For usability our program won’t loop endlessly. We’ll say that any
number that it is not a valid ride number is code for quitting the
program. The relevant changes to the [Ride
Selector](../05_MakingDecisions/Chapter_05.qmd#use-decisions-to-make-an-application)
are then,

``` python
run_program = True

while run_program:
    print("""Welcome to our Theme Park
        These are the available ride:

        1. Scenic River Cruise
        2. Carnival Carousel
        3. Jungle Adventure Water Splash
        4. Downhill Mountain Run
        5. The Regurgitator
        Any other number to quit...
        """)

    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)

    if ride_number < 1 or ride_number > 5:
        run_program = False
    elif ride_number == 1:
```

Observe that first we wrap all of the code in a `while` loop, and
introduce a boolean flag `run_program` initially set to `True` to flag
if the program continues to run at each loop iteration. When a user
enters a number we first check if it corresponds to a ride number and if
not, we set the program to quit on the next loop iteration by setting
`run_program` to `False`. We now change the original
`if ride_number == 1` to and `elif` so it is only checked if we know the
ride_number is valid

#### Exercise: Create a Looping Countdown Program

*One of the examples [in the above question
set](#example-investigating-the-while-construction) involved a
count***up** *to* $5$*. Implement a program that counts down from* $10$
*to* $0$ *over* $10$ *seconds*

``` python
# Exercise 6.2: Countdown
# Performs a 10-second countdown

import time

time_left = 10

while time_left >= 0:
    print(time_left)
    time_left = time_left - 1
    time.sleep(1)
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0

This is a straightforward exercise, we set up our counter value to $10$
and use the appropriate loop expression (here `time_left >= 0`) to
ensure that $0$ is included in the countdown.

In the loop we print the current value of `time_left`, then *decrement*
time_left by $1$, and sleep for the required time. Observe that after
the program prints $0$, `time_left` becomes $-1$ and the next iteration
of the loop won’t run.

#### Handling Invalid User Entry

- Ride Selector doesn’t account for invalid user entry
  - Blindly assumes a number outside the range $1$ to $5$ represents
    quitting the program
- Ideally we would like to have a distinct number that represents
  quitting and a way to *capture and handle* any invalid inputs

> [!TIP]
>
> **Great Programmers Think Defensively**
>
> Defensive programming is a programming technique in which a programmer
> attempts to *defend* their code against possible errors that might
> occur in a code e.g. receiving a word when expecting a number
>
> It is good practice to think about, typically a user expects a
> computer to do something reasonable even when provided unreasonable
> input.
>
> Data validation does have the downside in that it can make programs
> significantly bigger, and in compiled languages knowing that data is
> valid can make them much faster. A good skill is learning the correct
> layers or boundaries of a program to perform the defensive data
> validation so the core can run without concern

- Ignoring the question of quitting for now, data validation for the
  ride selector might look like,

  ``` python
    if ride_number < 1 or ride_number > 5:
        print('Invalid ride number')
  ```

##### Make a Loop to Validate Input

- Above acknowledges the error, but if we want to use this in our loop
  control we will need to use `while`

  ``` python
    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)

    while ride_number < 1 or ride_number > 5:
        print("There is no ride with that number")
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)
    print("You have selected ride number: ", ride_number)
  ```

  - `while` means program repeats until it receives valid input
  - Observe the downside
    - We have to repeat the code asking for the ride number and
      converting to an integer
    - Some languages have a `do ... while` statement which performs its
      test *after* executing the loop body for the first time
      - Would allow us to write the above as one construct

###### Exercise: Add Ride Number Validation to the Theme Park Ride Selector

*Add ride number validation to the Looping Ride Selector implementation.
Remember that the* `while` *construction must be added after the*
`ride_number` *value has been read by the program*

We can basically add the validation in immediately after the first
attempt to read the ride number from the user. We also have to adjust
the code to now use $0$ as the explicit value for quitting rather than
inferring any non-ride-number as a quit value. The main changes are,

``` python
while run_program:
    print("""Welcome to our Theme Park
        These are the available ride:

        1. Scenic River Cruise
        2. Carnival Carousel
        3. Jungle Adventure Water Splash
        4. Downhill Mountain Run
        5. The Regurgitator
        Press 0 to quit the program
        """)

    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)

    while ride_number < 0 or ride_number > 5:
        print("There is no ride with that number")
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)

    if ride_number == 0:
        run_program = False
```

###### Example: When good loops go bad

*When creating composite conditions for loops, making sure the logic is
correct is incredibly important. Examine the following program to
understand more complicated loop control*

``` python
age_text = input("Please enter your age: ")
age = int(age_text)
while age < 1 and age > 95:
    #repeat this code while the age is invalid
    print("This age is not valid")
    age_text = input("Please enter your age: ")
    age = int(age_text)
#when we are here, we have a valid age value
print("Thank you for entering your age")
```

1. *What is the fault in this program?*
    - *The condition* `age < 1 and age > 95` *requires* `age` *to be
      both* **less than** $1$ **and** **greater than** $95$*, this is
      impossible, so the loop never runs*
2. *What will the fault cause the program to do?*
    - *Since the loop body can never run, every entered age will be
      considered valid*
3. *How do you fix this?*
    - *The desired logic is that* `age` *should be between* $1$ and $95$
      *inclusive. This logic is captured by the* `or` *operator. The
      corrected expression is*

      ``` python
        while age < 1 or age > 95
      ```

> [!IMPORTANT]
>
> **Always test failure behaviours along with successful ones**
>
> It’s very important when testing software to test both the successful
> path (the so-called “happy path”) and any possible error states.
>
> A good programmer proactively looks for potential points of failure,
> writes code to handle the errors and importantly checks that the code
> to handle the errors does what it’s supposed to do
>
> A good heuristic for starting to do this with simple programs is
> called boundary-value testing. Boundaries are the points between
> different expected behaviours. For example with the ride selector, we
> expect different behaviour for numbers $< 1$ or $> 5$ to those in the
> range $1$ to $5$. So a good set of tests might be $0$, $1$, $2$, $4$,
> $5$, $6$. i.e. we test either side of the boundary, and on the
> boundary

###### Exercise: Add Validation to the Theme Park Age Input

*Add age validation to the Ride Selection Program. The theme park owner
has told you that the minimum age for anyone going on a ride at the
theme park is* $1$ *year, and the maximum age is* $95$*. Use these
values in your program*

Observe that in this case if the user provides an age outside the
accepted range, we don’t want to prompt them to put in a new age, since
this could legitimately be their age. Instead we want to tell them
regardless of the ride they chose they can’t ride. In this case we
should use an `if` style validation technique

The change is applied at our age reading section of the program, we use
an `if...elif...else` construct to tell the user they are either too
young, too old, or to continue on to the standard ride selection code

``` python
age_text = input("Please enter your age: ")
age = int(age_text)
if age < 1:
    print("You are too young to go on any rides")
elif age > 95:
    print("You are too old to go on any rides")
else:
    #continue on to normal ride selection code...
```

#### Detect Invalid Number Entry using Exceptions

## Summary

## Questions and Answers
