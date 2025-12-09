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
    - [Exceptions and Number Reading](#exceptions-and-number-reading)
      - [Example: Handling Exceptions in
        Loops](#example-handling-exceptions-in-loops)
    - [Handling Multiple Exceptions](#handling-multiple-exceptions)
  - [`break` out of Loops](#break-out-of-loops)
  - [Return to the top of a loop with
    `continue`](#return-to-the-top-of-a-loop-with-continue)
  - [Count a Repeating Loop](#count-a-repeating-loop)
    - [Example: CounterIntelligence](#example-counterintelligence)
    - [Exercise: Allow the User to Select the Times
      Value](#exercise-allow-the-user-to-select-the-times-value)
  - [The `for` Loop Construction](#the-for-loop-construction)
    - [Example: Loops, `break` and
      `continue`](#example-loops-break-and-continue)
    - [Exercise: Make a Times Table
      Quiz](#exercise-make-a-times-table-quiz)
  - [Make a Digital Clock using
    Snaps](#make-a-digital-clock-using-snaps)
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
ride_number is valid. (The full code is in
[LoopingRideSelector.py](./Exercises/01_LoopingRideSelector/LoopingRideSelector.py))

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

This is a straightforward exercise (see
[Countdown.py](./Exercises/02_Countdown/Countdown.py)), we set up our
counter value to $10$ and use the appropriate loop expression (here
`time_left >= 0`) to ensure that $0$ is included in the countdown.

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

The complete code is given in
[RideNumberValidation.py](./Exercises/03_RideNumberValidation/RideNumberValidation.py)

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

The full code is given in
[AgeValidation.py](./Exercises/04_AgeValidation/AgeValidation.py)

### Detect Invalid Number Entry using Exceptions

- **Problem:** We can easily write a loop that checks if a value is
  invalid but **how** do we deal with the *type* being invalid?
  - e.g. in the ride selector how do we deal with the user typing in a
    word rather than a number?
  - Consider the snippet below, emulating the ride selector given a
    string input, we get an error, *before* we even get a chance to
    validate the value

  ``` python
    ride_number_text = "three"
    ride_number = int(ride_number_text)
  ```

      ValueError: invalid literal for int() with base 10: 'three'
      ---------------------------------------------------------------------------
      ValueError                                Traceback (most recent call last)
      Cell In[21], line 2
            1 ride_number_text = "three"
      ----> 2 ride_number = int(ride_number_text)

      ValueError: invalid literal for int() with base 10: 'three'

  - This occurs because `int` requires it’s input to be convertable to a
    number
    - Unfortunately this does not extend to human-language written
      versions of a number
    - In this case `int` *throws* an error, it is better to end the
      program than continue in an erroneous state
  - In general, when a program encounters an error state, it should aim
    to fail fast, rather than continue and generate unexpected outcomes
- *Exceptions* are a mechanism by which elements of a program can inform
  other parts about errors that have occured
  - *Exceptions* combine a description of *what* the error that occured
    was, with *where* the error occured
  - In the example above e.g. we are told that we got a `ValueError`
  - i.e. an invalid value was found, we are given the additional detail
    “invalid literal for int() with base 10: ‘three’”
  - In plain english, the program did not know how to convert ‘three’ to
    an integer
  - We are also told *where*, in this case the second line, in the
    function `int`
- To recover from an exception we have to *handle* it, i.e. do something
  - The first step is to *catch* the exception
  - We wrap code that might *throw* an exception in a `try... except`
    block

  ``` python
  # Example 6.3: Catching Exceptions
  #
  # Demonstrates how to catch and handle
  # an exception

    try:
        ride_number_text = input("Please enter a ride number: ")
        ride_number = int(ride_number_text) #statement that might raise exception
        print("You have entered", ride_number)
    except ValueError: # Start of an exception handler
        print("Invalid number") # Performed if exception raised
  ```

- We wrap the code that may throw an exception in a `try`
- We then use `except` to define statements we want to run if an
  exception is thrown
  - If an exception is thrown, control immediately jumps to the `except`
    block
  - e.g. In the above example if `int` throws a `ValueError` then the
    line `print("You have entered", ride_number)` won’t run
    - Instead `print("Invalid number")` runs
- As observed `except` is followed by the exception type we want to
  catch (in this case `ValueError`)
- The full example is given in
  [CatchingExceptions](./Examples/03_CatchingExceptions/CatchingExceptions.py)

``` mermaid
block-beta
    columns 4
    space
    title["Breakdown of a Try-Except Block"]:2
    space

    block:Try:2
    columns 1
        try["try"]
        tryDescr["(start of the try construction)"]
    end

    block:TryColon
    columns 1
        Trycolon[":"]
        TryColonDescr["colon"]
    end

    block:TrySuite
    columns 1
        Trysuite["Statements"]
        TrysuiteDescr[("statements to execute normally")]
    end



classDef BG stroke:transparent, fill:transparent
class title BG
class try BG
class tryDescr BG
class Trycolon BG
class TryColonDescr BG
class Trysuite BG
class TrysuiteDescr BG

    block:ExceptOne
    columns 1
        exceptOne["except"]
        exceptOneDescr["(start of an exception construction)"]
    end

    block:ExceptNameOne
    columns 1
        exceptOneName["Name"]
        exceptOneNameDescr["(exception name)"]
    end

    block:ExceptOneColon
    columns 1
        exceptOneColon[":"]
        exceptOneColonDescr["colon"]
    end

    block:ExceptOneStatements
    columns 1
        exceptOneStatements["statements"]
        exceptOneStatementsDescr[("statements to execute if exception caught")]
    end

class exceptOne BG
class exceptOneDescr BG
class exceptOneName BG
class exceptOneNameDescr BG
class exceptOneColon BG
class exceptOneColonDescr BG
class exceptOneStatements BG
class exceptOneStatementsDescr BG

    block:ExceptTwo
    columns 1
        exceptTwo["except"]
        exceptTwoDescr["(start of an exception construction)"]
    end

    block:ExceptNameTwo
    columns 1
        exceptTwoName["Name"]
        exceptTwoNameDescr["(exception name)"]
    end

    block:ExceptTwoColon
    columns 1
        exceptTwoColon[":"]
        exceptTwoColonDescr["colon"]
    end

    block:ExceptTwoStatements
    columns 1
        exceptTwoStatements["statements"]
        exceptTwoStatementsDescr[("statements to execute if exception caught")]
    end

class exceptTwo BG
class exceptTwoDescr BG
class exceptTwoName BG
class exceptTwoNameDescr BG
class exceptTwoColon BG
class exceptTwoColonDescr BG
class exceptTwoStatements BG
class exceptTwoStatementsDescr BG
```

- As demonstrated above a `try...except` block may contain multiple
  `except` statements designed to handle different exception types

#### Exceptions and Number Reading

- We’ve seen how to use loops to handle invalid values
- We’ve seen how to use exceptions to handle invalid types
- Now let’s put that together to write a loop to handle exceptions

##### Example: Handling Exceptions in Loops

*We want to make a program that will perform a* `while` *construction as
long as the user keeps typing in text that cannot be converted into a
number. Look at the example code below, (see
[HandlingInvalidText.py](./Examples/04_HandlingInvalidText/HandlingInvalidText.py))
and answer the questions*

``` python
# Example 6.4: Handling Invalid Text
#
# Combines loops and exception handling to prompt a user
# for a valid number and repeat until a number is provided

ride_number_valid = False  # create and set a flag to False
while not ride_number_valid:  # repeats while flag is False
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)  # can throw a ValueError
        ride_number_valid = True  # successfully read a number
    except ValueError:  # catch the ValueError
        print("Invalid number. Please enter a number in digits")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)
```

1. *What is the purpose of the variable,* `ride_number_valid`*?*
    - It is a *flag*
    - Tracks the state of a program, in this case a valid number been
      read
    - Starts `False` once successfully received an `int` flips to `True`
2. *How many times would you expect the* `while` *construction to loop
    when the program is used?*
    - Ideally we would expect it to run once
      - i.e. The user enters a number straight away
    - In the next best case we would expect it run twice
      - The user experiences an error, reads the message and corrects
        their input the next time
3. *Why don’t we have to test* `ride_number_valid` *at line* $10$*, to
    make sure that the ride number is valid?*
    - The while loop stops when it’s condition is `False`
    - This corresponds to `ride_number_valid = True`
    - So we know that once we leave the loop `ride_number_valid`
      **must** be `True`

#### Handling Multiple Exceptions

- Sometimes there a multiple exception types we wish to handle
- e.g. a `KeyboardInterrupt` allows a user to issue an exception which
  could stop a program
  - If the user is interacting with somebody else’s external facing
    program, we might not want them to be able to do this
- *Simultaneously* we might need to ensure that the user inputs valid
  data like numbers
- We can just add an additional `except` block
  - When an exception is thrown, the appropriate handler takes control
- The improved exception handling code is given in
  [HandlingInvalidTextMultipleExceptions](./Examples/05_HandlingInvalidTextMultipleExceptions/HandlingInvalidTextMultipleExceptions.py)

``` python
# Example 6.5: Improved Handling Invalid Text
#
# Extends Example 6.4 by preventing the user from issuing a
# keyboard interrupt to stop the program

ride_number_valid = False  # create and set a flag to False
while not ride_number_valid:  # repeats while flag is False
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)  # can throw a ValueError
        ride_number_valid = True  # successfully read a number
    except ValueError:  # catch the ValueError
        print("Invalid number. Please enter a number in digits")
    except KeyboardInterrupt:  # catches the interrupt
        print("You do not have permission to interupt this program")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)  # type: ignore
```

> [!IMPORTANT]
>
> **Plan for Failure**
>
> When writing a program you should always be thinking about how it
> could fail and the appropriate response. Any point that asks for user
> input is a major potential point of failure and should be handled
> correctly.
>
> You should never catch exceptions to hide errors. You *could* all
> statements in a `try...except` block, but then you can’t identify any
> errors that occur.

### `break` out of Loops

- `break` statements allow you to exit a loop from inside
- As soon as a `break` is encountered control immediately jumps to the
  next statement after the loop
- The example code is given in
  [UsingBreakToExitLoops.py](./Examples/06_UsingBreakToExitLoops/UsingBreakToExitLoops.py)

``` python
# Example 6.6 Using Break to Exit Loops
#
# Demonstrates using a break statement to exit
# a while loop from inside the loop

while True:  # use break rather than a condition to exit
    try:
        ride_number_text = input("Please enter the ride number you want: ")
        ride_number = int(ride_number_text)
        break
    except ValueError:
        print("Invalid number text. Please enter digits")
    except KeyboardInterrupt:
        print("You do not have permission to interupt this program")
# Once outside the loop we have a valid number
print("You have selected ride", ride_number)  # type: ignore
```

- The above follows the previous example, but uses `break` rather than a
  flag to control the loop
- `break` statements can be paired with conditionals like `if`, as
  demonstrated in
  [EarlyExitLoop.py](./Examples/07_EarlyExitLoop/EarlyExitLoop.py)

``` python
# Example 6.7 Loop with condition ending early
#
# Demonstrates the pairing of break and conditional
# statements to end a program early

count = 0
while count < 5:
    print("Inside Loop")
    count = count + 1
    if count == 3:
        break
print("Outside loop")
```

    Inside Loop
    Inside Loop
    Inside Loop
    Outside loop

> [!TIP]
>
> **Don’t use too many** `break` **statements**
>
> A loop can theoretically only use many `break` statements to control
> flow. However `break` statements make it harder to reason about the
> flow of a loop. Sometimes they are the cleanest way to do something,
> but often they just make the code less readable.
>
> In general prefer to use conditions to control loops, they are easier
> to reason about the state at the end of the loop

### Return to the top of a loop with `continue`

- `continue` causes control to immediately jump to the start of the next
  loop iteration
- For example consider the Ride Selector example. If a ride is
  temporarily down we might push a patch to skip any selection of the
  ride, e.g. [IgnoreRide.py](./Examples/08_IgnoreRide/IgnoreRide.py)
  given below

``` python
while True:
    ride_number_text = input("Please enter the ride number you want: ")
    ride_number = int(ride_number_text)
    if ride_number == 3:
        print("sorry, this ride is unavailable")
        continue
    print("you have selected ride number: ", ride_number)
```

> [!NOTE]
>
> **You wont use** `continue` **as often as you use** `break`
>
> `break` can be useful in quite a few use cases. `continue` tends to be
> much more niche and isn’t used often

### Count a Repeating Loop

- You can use a variable to make a loop repeat a specified number of
  times, e.g. in the below [Times Tables
  Program](./Examples/09_TimesTablesTutor/TimesTablesTutor.py)

``` python
# Example 6.9 Times Tables Tutor
#
# Uses Times Tables to demonstrate use of a counter
# variable to control a loop

count = 1
times_value = 2
while count < 13:
    result = count * times_value
    print(count, "times", times_value, "equals", result)
    count = count + 1
```

    1 times 2 equals 2
    2 times 2 equals 4
    3 times 2 equals 6
    4 times 2 equals 8
    5 times 2 equals 10
    6 times 2 equals 12
    7 times 2 equals 14
    8 times 2 equals 16
    9 times 2 equals 18
    10 times 2 equals 20
    11 times 2 equals 22
    12 times 2 equals 24

- The combination of `while count < 13` and `count = count + 1` means
  that after $12$ loop iterations the loop condition evaluates `False`
  and the loop ends

#### Example: CounterIntelligence

- *Consider the previous [example](#count-a-repeating-loop) and answer
  the following questions*

1. *What statement would you change if you wanted to generate the times
    table for three instead of two?*
    - *We would change* `times_value`
2. *Which statement would you change if you wanted to generate up to
    the* $24$ *times table?*
    - We would change the loop condition to `count < 25`
3. *What would happen to the program if we changed the line*
    `count = count + 1` *to* `count = count - 1`
    - *The loop would produce negative times tables, and never stop
      since* `count` *will be decreased every iteration and thus is
      always less than* $13$

#### Exercise: Allow the User to Select the Times Value

*Write a version of the [previous example](#count-a-repeating-loop) that
asks the user for the value of the times table they want. Add validation
so that the user must enter a number between* $2$ *and* $12$ *inclusive*

- Our solution (given in
  [UserSelectedTimesTableTutor.py](./Exercises/05_UserSelectedTimesTableTutor.py/UserSelectedTimesTableTutor.py))
  prompts the user to enter a number between $2$ - $12$ inclusive, and
  then validates that the input is in the range. A `try`, `except` block
  is used to catch any invalid input type, and the whole thing is
  wrapped in a `while True` block that only ends once a valid integer in
  the range $2$ - $12$ is received through the use of a `break`
  statement.
- The actual times tables code is then identical

``` python
# Exercise 6.5 User SelectedTimes Tables Tutor
#
# Version of the times table tutor that allows the user to select the
# times table in the range 2 - 12 they are interested in

count = 1
while True:
    try:
        times_value_text = input(
            "Please enter a times table between 2-12 (inclusive): "
        )
        times_value = int(times_value_text)
        if times_value < 2 or times_value > 12:
            print("Sorry, that is not between 2-12 (inclusive)")
        else:
            break
    except ValueError:
        print("Please enter an integer")

while count < 13:
    result = count * times_value
    print(count, "times", times_value, "equals", result)
    count = count + 1
```

### The `for` Loop Construction

- `For` loops operate similar to `while` loops, but are designed for
  when the number of iterations are known

``` mermaid
block-beta
    columns 6
    space
    space
    title["Breakdown of a For"]:2
    space
    space

    block:Input
    columns 1
        while["for"]
        whileDescr["(start of the for construction)"]
    end

    block:MiddleOne
    columns 1
        condition["variable"]
        conditionName["function name"]
        conditionDescr["(variable controlled in the for)"]
    end

    block:In
    columns 1
        in["in"]
    end

    block:Items
    columns 1
        items["items"]
        itemsDescr["(items to work through)"]
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
class conditionName BG
class conditionDescr BG
class colon BG
class colonDescr BG
class while BG
class whileDescr BG
class items BG
class itemsDescr BG
class suite BG
class suiteDescr BG
class in BG
```

- `for` loops over a collection of items, acting on each item in turn
- Each iteration acts on next item in the collection
- An example of a collection is a tuple, e.g.
  - `names = ('Rob', 'Mary', 'David', 'Jenny', 'Chris', 'Imogen')`
  - `names` is a tuple (denoted by the `()` containing the above names)
  - We’ll discuss Tuples in more detail in Chapter 8
- We can pair the above tuple with a `for` loop e.g.

``` python
# Example 6.10 Name Printer
#
# Prints a collection of names
names = ('Rob', 'Mary', 'David', 'Jenny', 'Chris', 'Imogen')
for name in names:
    print(name)
```

    Rob
    Mary
    David
    Jenny
    Chris
    Imogen

- `range` is a python function for generating a collection of numbers
  - syntax is `range(start, stop)` where `start` is included, but `stop`
    is excluded
  - e.g. We could rewrite ours times table program as using range (see
    \[RangeBasedTimeTables.py\])

``` python
# Example 6.11 Range Based Times Tables
#
# Demonstrates Python's range function using a for
# loop to generate a times table

times_value = 2
for count in range(1, 13):
    result = count * times_value
    print(count, "times", times_value, "equals", result)
```

    1 times 2 equals 2
    2 times 2 equals 4
    3 times 2 equals 6
    4 times 2 equals 8
    5 times 2 equals 10
    6 times 2 equals 12
    7 times 2 equals 14
    8 times 2 equals 16
    9 times 2 equals 18
    10 times 2 equals 20
    11 times 2 equals 22
    12 times 2 equals 24

- `break` and `continue` also work with `for` loops
  - `continue` causes the loop to proceed to the next item in the
    collection

#### Example: Loops, `break` and `continue`

*Look at the following simple programs, and answer the corresponding
questions about* `break` *and* `continue`

1. *What would the following code print?*

    ``` python
     for count in range(1, 13):
         if count == 5:
             break
         print(count)
     print('Finished')
    ```

        1
        2
        3
        4
        Finished

    - *It would print* `1`, `2`, `3`, `4` *then* `"finished"` *since
      when* `count` *is* $5$ *the loop breaks* **before** *the print
      statement and then the print outside the loop is called*

2. *What would the following code print?*

    ``` python
     for count in range(1, 13):
         if count == 5:
             continue
         print(count)
     print('Finished')
    ```

        1
        2
        3
        4
        6
        7
        8
        9
        10
        11
        12
        Finished

    - *This program is similar to the above, except it would print* `1`
      *through to* `12` *but skip* `5`*, before printing* `"Finished"`*.
      This is because the* `continue` *causes the loop iteration for*
      `count = 5` *to skip the print statement in the loop and go to the
      next loop iteration*

3. *What would the following code print?*

    ``` python
     for count in range(1, 13):
         count = 13
         print(count)
     print('Finished')
    ```

        13
        13
        13
        13
        13
        13
        13
        13
        13
        13
        13
        13
        Finished

    - *This will print* $13$ *twelve times, because each time* `count`
      *starts a loop iteration it is set to the next value in the*
      `range(1, 13)`
      - *Then inside the loop* `count` *is set to* `13` *and that value
        is printed*
    - *Of course* `"Finished"` *is printed after the loop is down*

4. *Would the following program run forever?*

    ``` python
     while True:
         break
     print('Finished')
    ```

        Finished

    - *No, it will immediately end because* `break` *exits the loop*

5. *Would the following program print the message “Looping”?*

    ``` python
     while True:
         continue
         print('Looping')
    ```

    - *No, the loop will hit the* `continue` *keyword and the go back to
      the start*
    - *This happens forever*

6. *What would the following program do? Is it legal?*

    ``` python
     for letter in 'hello world':
         print(letter)
    ```

        h
        e
        l
        l
        o

        w
        o
        r
        l
        d

    - *Strings are collections of letters*
    - *The above program works, it loops over and prints each letter in
      the string*

#### Exercise: Make a Times Table Quiz

*Reverse the behaviour of the times-table program so that rather than
printing out the times-table your program insteads asks questions like,*
“What is $6$ times $4$?” *The user could enter their answer, and the
program could compare it with the correct answer and keep score of how
many correct answers are given. You could use a loop to make the program
produce* $12$ *“times-table” questions, and you could use random numbers
so that the quiz is different every time*

Our solution given in
[TimesTableQuiz.py](./Exercises/06_TimesTableQuiz/TimesTableQuiz.py) is
relatively complete. We use first print a header message, then we set up
a variable to track the number of correct answers total and a second
variable to track the number of questions to ask. We then go into our
`for` loop, looping over `range(0, NumberOfQuestions)`, this makes the
loop run `NumberOfQuestions` times.

The actual quiz then proceeds, we randomly generate the two numbers, the
`times_value` from the range `[2, 12]` and the `count` from the range
`[1, 12]`. We then calculate the correct answer, and prompt the user for
an answer, using the standard `ValueError` exception handling. If the
user’s answer is correct we congratulate them and increment the score,
else we tell them what the correct answer is. After they’ve answered all
the questions we give them the final score

``` python
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
```

### Make a Digital Clock using Snaps

## Summary

## Questions and Answers
