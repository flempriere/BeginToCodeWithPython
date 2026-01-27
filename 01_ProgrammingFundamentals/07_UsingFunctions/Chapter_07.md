# Chapter 7: Using Functions to Simplify Programs

- [Notes](#notes)
  - [What makes a Function?](#what-makes-a-function)
    - [Make Something Happen: Investigating
      Functions](#make-something-happen-investigating-functions)
    - [Code Analysis: Program
      Pathfinder](#code-analysis-program-pathfinder)
    - [Structure of a Function
      Definition](#structure-of-a-function-definition)
    - [Give Information to Functions using
      Parameters](#give-information-to-functions-using-parameters)
      - [Arguments and Parameters](#arguments-and-parameters)
        - [Code Analysis: Argument and
          Parameters](#code-analysis-argument-and-parameters)
      - [Multiple Parameters in a
        Function](#multiple-parameters-in-a-function)
      - [Positional and Keyword
        Arguments](#positional-and-keyword-arguments)
      - [Default Parameter Values](#default-parameter-values)
      - [Code Analysis: Parameters as
        Values](#code-analysis-parameters-as-values)
      - [Make Something Happen: Creating a Teletype
        Printer](#make-something-happen-creating-a-teletype-printer)
      - [Make Something Happen: Teletype Fortune
        Teller](#make-something-happen-teletype-fortune-teller)
    - [Return Values from Function
      Calls](#return-values-from-function-calls)
      - [Code Analysis: Functions and
        `return`](#code-analysis-functions-and-return)
    - [Local Variables in Python
      Functions](#local-variables-in-python-functions)
    - [Global Variables in Python
      Programs](#global-variables-in-python-programs)
  - [Build Reusable Functions](#build-reusable-functions)
    - [Create a Text Input Function](#create-a-text-input-function)
      - [Code Analysis: Investigate the `read_text`
        function](#code-analysis-investigate-the-read_text-function)
    - [Add Help Information to
      Functions](#add-help-information-to-functions)
      - [Use Pydoc](#use-pydoc)
    - [Create a Number Input Function](#create-a-number-input-function)
    - [Code Analysis: Investigating the `read_float_ranged`
      Function](#code-analysis-investigating-the-read_float_ranged-function)
    - [Convert our Functions into a Python
      Module](#convert-our-functions-into-a-python-module)
      - [Make Something Happen: Add `BTCInput` to your Existing
        Programs](#make-something-happen-add-btcinput-to-your-existing-programs)
  - [Using a Debugger](#using-a-debugger)
    - [Make Something Happen: Investigate Programmers with a
      Debugger](#make-something-happen-investigate-programmers-with-a-debugger)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### What makes a Function?

- A function is a named chunk of code
  - Can be thought of as like a variable containing code rather than a
    value
  - Consider the simple function

  ``` python
    def greeter():
        print("Hello")
  ```

  - Print’s the message `"Hello"`
  - Called by the function name, then parentheses, e.g.

  ``` python
    greeter()
  ```

      Hello

  - functions must be defined *before* they can be called

#### Make Something Happen: Investigating Functions

*Use a python interpreter to work through the following questions to
understand python functions*

*Enter the following program into the interpreter*

``` python
def greeter():
     print("Hello")
```

1. *Why did the interpreter not print* `"Hello"`*?*

    - Because the `print` statement is stored as part of the `greeter`
      function

2. *How do I tell Python that I’ve finished entering the* `greeter`
    *function?*

    - The same way you close a loop or an `if` statement, by
      de-indenting and adding an empty line

3. *How do I make a call to the* `greeter` *function?*

    ``` python
     greeter()
    ```

        Hello

    - The same way you call any other function. Write the function name
      and a parenthesised list of parameters. In this case the list is
      empty. Once called the function runs all the statements contained
      in its definition.

*Now consider the following code snippet*

``` python
x = greeter
x()
```

    Hello

Observe that we can treat functions like variables. We can assign them
to other *labels/variables* in this case `x` is set to the value of
`greeter`. We can then call `x` as if it where `greeter`

The ability to treat functions as variables is a powerful feature we
will explore more in Chapter 12

#### Code Analysis: Program Pathfinder

*Examine the following code block and and answer the following questions
to understand how functions work. (You can run the code at
[Pathfinder.py](./Examples/01_Pathfinder/Pathfinder.py))*

``` python
# Example 7.1: Pathfinder
#
# Sample Program to demonstrate function flow


def m2():
    print("the")


def m3():
    print("sat on")
    m2()


def m1():
    m2()
    print("cat")
    m3()
    print("mat")


m1()
```

    the
    cat
    sat on
    the
    mat

1. *What will the program display when it runs?*

    - Step through the program one statement at a time
    - First `m1` is called
      - `m1` calls `m2`
        - `m2` prints `"the"`
        - `m2` ends and control returns to `m1`
      - `m1`’s next statement prints `"cat"`
      - `m1`’s next statement calls `m3`
        - `m3` prints `"sat on"`
        - `m3` calls `m2`
          - `m2` prints `"the"`
          - `m2` ends and control returns to `m3`
        - `m3` ends and control returns to `m1`
      - `m1` prints `"mat"`
      - `m1` and thus the program ends
    - The final output is thus:

    ``` text
     the
     cat
     sat on
     the
     mat
    ```

2. *What happens if a function calls itself? For example what if* `m1`
    *called* `m1`

    - Let’s try changing `m1` to the following,

      ``` python
        def m1():
            m1()

        m1()
      ```

          RecursionError: maximum recursion depth exceeded
          ---------------------------------------------------------------------------
          RecursionError                            Traceback (most recent call last)
          Cell In[6], line 4
                1 def m1():
                2     m1()
          ----> 4 m1()

          Cell In[6], line 2, in m1()
                1 def m1():
          ----> 2     m1()

          Cell In[6], line 2, in m1()
                1 def m1():
          ----> 2     m1()

              [... skipping similar frames: m1 at line 2 (2975 times)]

          Cell In[6], line 2, in m1()
                1 def m1():
          ----> 2     m1()

          RecursionError: maximum recursion depth exceeded

    - The code generates a `RecursionError`!

      - A function that calls itself is called a recursive function
      - Like an infinite loop infinite recursion occurs when a function
        calls itself with no condition to stop
      - Eventually the computer cannot allocate more memory to track the
        function calls
        - This can be dangerous so Python prematurely limits the “depth”
          of recursive calls a function can make

    - Formally with recursion:

      - Each time a function is called Python stores the return address
        (where the code goes back to) on the “stack”
        - The stack is special memory responsible for managing the
          program
        - When a function finishes the program grabs the return of the
          stack and looks at the address to to determine where to run
      - Calling and exiting functions thus grows and shrinks the stack
        - Up to a limit defined by Python at which point a recursion
          error occurs

    - Recursive functions are a powerful and elegant technique in many
      cases

      - However, often it is better to use simple loop structures
      - Recursion more of interest for theory

#### Structure of a Function Definition

``` mermaid
block-beta
    columns 7

    classDef BG stroke:transparent, fill:transparent


    space
    space
    title["Breakdown of a Function Definition"]:3
    space
    space

    class title BG

    block:Def
    columns 1
        def["def"]
        defDescr["(start of function definition)"]
    end

    class def BG
    class defDescr BG


    block:Name
    columns 1
        name["name"]
        nameDescr["(name of the function)"]
    end

    class name BG
    class nameDescr BG

    block:LeftP
    columns 1
        leftP["("]
        leftPDescr[" "]
    end

    class leftP BG
    class leftPDescr BG

    block:Parameters
    columns 1
        parameters["parameters"]
        parametersDescr["(items to feed into the function)"]
    end

    class parameters BG
    class parametersDescr BG

    block:RightP
    columns 1
        rightP[")"]
        rightPDescr[" "]
    end

    class rightP BG
    class rightPDescr BG

    block:Colon
    columns 1
        colon[":"]
        colonDescr["colon"]
    end

    class colon BG
    class colonDescr BG

    block:Suite
    columns 1
        suite["Statement block"]
        suiteDescr["(statements)"]
    end

    class suite BG
    class suiteDescr BG
```

- `def` tells python we’re defining a function
  - As opposed to calling an existing one
- space then name of the function
  - Same naming rules as for variables
  - functions *do* things, i.e. the are naturally associated with verbs
    - Unlike variables with *are* things i.e. nouns
  - e.g. `display_menu` names a function which takes the *action* to
    *display* a menu
- Then parameters in a parentheses-enclosed, comma-delimited list
  - No space between name and left parenthesis
  - Parameters feed extra information for the function to work on
  - Parameter list can be empty (as we’ve seen)
- Then colon
- Followed by indented set of statements associated with the function
  - Called the *function body*

#### Give Information to Functions using Parameters

- Functions can receive data to work on through parameters

- E.g. we can parameterise our times table code

  ``` python
    def print_times_table(times_value):
        count = 1
        while count <  13:
            result = count * times_value
            print(count, 'times', times_value, 'equals', result)
            count = count + 1
  ```

- We can then call with different `times_value` to print the respective
  times table

``` python
    print_times_table(5)
    print_times_table(99)
```

    1 times 5 equals 5
    2 times 5 equals 10
    3 times 5 equals 15
    4 times 5 equals 20
    5 times 5 equals 25
    6 times 5 equals 30
    7 times 5 equals 35
    8 times 5 equals 40
    9 times 5 equals 45
    10 times 5 equals 50
    11 times 5 equals 55
    12 times 5 equals 60
    1 times 99 equals 99
    2 times 99 equals 198
    3 times 99 equals 297
    4 times 99 equals 396
    5 times 99 equals 495
    6 times 99 equals 594
    7 times 99 equals 693
    8 times 99 equals 792
    9 times 99 equals 891
    10 times 99 equals 990
    11 times 99 equals 1089
    12 times 99 equals 1188

##### Arguments and Parameters

- A *parameter* is the name assigned to a value passed to a function
- An *argument* is the specific value passed when a function is called
- e.g. in the above `print_times_table` function:
  - The *parameter* is `times_value`
  - But a specific *argument* is $5$ or $99$
- Consider it as the phrase “we call the function passing the arguments
  to the parameters”

###### Code Analysis: Argument and Parameters

*Find out more about arguments and parameters by answering the following
questions*

1. *What would the [following
    program](./Examples/02_TimesTable/TimesTables.py) do?*

    ``` python
     # Example 7.2: Times Tables
     #
     # Demonstrates function parameters through a
     # Times Table function that takes in an argument to
     # determine which times table is printed

     def print_times_table(times_value):
         count = 1
         while count < 13:
             result = count * times_value
             print(count, "times", times_value, "equals", result)
             count = count + 1

     print_times_table(6)
    ```

        1 times 6 equals 6
        2 times 6 equals 12
        3 times 6 equals 18
        4 times 6 equals 24
        5 times 6 equals 30
        6 times 6 equals 36
        7 times 6 equals 42
        8 times 6 equals 48
        9 times 6 equals 54
        10 times 6 equals 60
        11 times 6 equals 66
        12 times 6 equals 72

    - The above should print out the times table for $6$

2. *What would happen if we changed the call of the*
    `print_times_table` *function to the one below that has a string as
    the argument? Would the program fail?*

    ``` python
     print_times_table("six")
    ```

        1 times six equals six
        2 times six equals sixsix
        3 times six equals sixsixsix
        4 times six equals sixsixsixsix
        5 times six equals sixsixsixsixsix
        6 times six equals sixsixsixsixsixsix
        7 times six equals sixsixsixsixsixsixsix
        8 times six equals sixsixsixsixsixsixsixsix
        9 times six equals sixsixsixsixsixsixsixsixsix
        10 times six equals sixsixsixsixsixsixsixsixsixsix
        11 times six equals sixsixsixsixsixsixsixsixsixsixsix
        12 times six equals sixsixsixsixsixsixsixsixsixsixsixsix

    - Recall that multiplication between strings and numbers is defined
      in python as the repeated concatenation of the string with itself
    - The above thus prints a triangle of increasingly concatenated
      `"six"`
    - This behaviour while *semantically* correct by the python language
      is not *logically* correct. Really we would expect an error to
      occur

3. *How do we make the `print_times_table` function work with integer
    parameters only?*

    - First: is it a problem?
      - If this function is wrapped in a higher level function that does
        the error handling we can probably forget it
    - Second: If it is a problem, what is the way to fix it?
      1. Print a warning message?
      2. Stop the program?
      3. Handle the error locally? (within the function)
    - In this case let’s throw an error if the type is not an integer
      - The `isinstance` function lets you type check an item
      - Accepts two arguments, item to test, and the type to match
      - Returns `True` if item is that type else `False`

    ``` python
     # Example 7.3: Safe Times Tables
     #
     # A version of Times Tables that uses isinstance
     # to ensure that argument is an integer


     def print_times_table(times_value):
         if not isinstance(times_value, int):
             raise Exception("print_times_table requires an integer argument")
         count = 1
         while count < 13:
             result = count * times_value
             print(count, "times", times_value, "equals", result)
             count = count + 1


     print_times_table("six")
    ```

        Exception: print_times_table requires an integer argument
        ---------------------------------------------------------------------------
        Exception                                 Traceback (most recent call last)
        Cell In[11], line 17
             13         print(count, "times", times_value, "equals", result)
             14         count = count + 1
        ---> 17 print_times_table("six")

        Cell In[11], line 9, in print_times_table(times_value)
              7 def print_times_table(times_value):
              8     if not isinstance(times_value, int):
        ----> 9         raise Exception("print_times_table requires an integer argument")
             10     count = 1
             11     while count < 13:

        Exception: print_times_table requires an integer argument

    - [SafeTimesTable.py](./Examples/03_SafeTimesTable/SafeTimesTables.py)
      shown above demonstrates using `isinstance` to raise an exception
    - `Exception` can be thought of as an object that holds the error
      description
      - string argument describes the error
    - `raise` creates and throws it

##### Multiple Parameters in a Function

- functions can have multiple parameters
  - e.g. what if we want to adjust the length of the times table

  ``` python
    # Example 7.4: Two Parameter Times Table
    #
    # Demonstrates a multi-parameter function through a variable
    # length times table program


    def print_times_table(times_value, limit):
        count = 1
        while count < limit + 1:
            result = times_value * count
            print(count, "times", times_value, "equals", result)
            count = count + 1
  ```

  - The above uses `times_value` to control which times table is
    printed, and `limit` controls the length
    - The full code is given in
      [TwoParameterTimesTable.py](./Examples/04_TwoParameterTimesTable/TwoParameterTimesTable.py)
  - An example call is then,

  ``` python
    print_times_table(6,5)
  ```

      1 times 6 equals 6
      2 times 6 equals 12
      3 times 6 equals 18
      4 times 6 equals 24
      5 times 6 equals 30

  - The above prints the first $5$ entries of the $6$ times tables

##### Positional and Keyword Arguments

- Consider the call,

  ``` python
    print_times_table(12, 7)
  ```

      1 times 12 equals 12
      2 times 12 equals 24
      3 times 12 equals 36
      4 times 12 equals 48
      5 times 12 equals 60
      6 times 12 equals 72
      7 times 12 equals 84

- The above, to the unfamiliar user makes it unclear if its a $12$ times
  table of length $7$ or a times table for $7$ of length $12$

  - This is because the arguments are passed as *positional* parameters
    - i.e. order the arguments go in, controls which parameter they are
      assigned too

- You can also pass arguments to functions by specifying the parameter
  name, e.g.

  ``` python
    print_times_table(times_value=12, limit=7)
  ```

      1 times 12 equals 12
      2 times 12 equals 24
      3 times 12 equals 36
      4 times 12 equals 48
      5 times 12 equals 60
      6 times 12 equals 72
      7 times 12 equals 84

  - This is called *keyword* arguments, because we specify the arguments
    associated parameter by its name

> [!WARNING]
>
> **Don’t mix positional and keyword arguments**
>
> Python lets you mix positional and keyword arguments in a call to a
> function. This can make it hard to work out what is assigned to what.
> You should either use all *positional* arguments (when obvious) or all
> *keyword* arguments
>
> Beware that *positional* arguments **must** precede all *keyword*
> arguments

##### Default Parameter Values

- Our original implementation of `print_times_table` assumed the length
  was $12$

- The second version allowed us to specify the length, but no longer
  assumes that it is $12$

- *Default* parameters let us combine both behaviours

  ``` python
    # Example 7.5: Default Parameters
    #
    # Demonstrates default arguments by capturing the single
    # argument times table code in the two parameter version


    def print_times_table(times_value, limit=12):
        count = 1
        while count < 13:
            result = times_value * count
            print(count, "times", times_value, "equals", result)
            count = count + 1
  ```

  - If an argument is not provided to a parameter with a default
    argument, the default is used, e.g. the below call implicitly uses
    `limit = 12`

    ``` python
      print_times_table(times_value=7)
    ```

        1 times 7 equals 7
        2 times 7 equals 14
        3 times 7 equals 21
        4 times 7 equals 28
        5 times 7 equals 35
        6 times 7 equals 42
        7 times 7 equals 49
        8 times 7 equals 56
        9 times 7 equals 63
        10 times 7 equals 70
        11 times 7 equals 77
        12 times 7 equals 84

- Most modern python editors and tooling can read function definitions,
  and highlight and default arguments

> [!TIP]
>
> **Why use named arguments and default parameters?**
>
> Named arguments and default parameters help make functions clearer in
> intent. Reduce the possibility of getting arguments confused or mixed
> up. Makes it easy to define “standard” behaviour for a function

##### Code Analysis: Parameters as Values

*What does it mean when we pass the value of an argument to a function
parameter? Consider the following program*

``` python
# Example 7.6 Parameters as Values
#
# Demonstrates how python handles passing values to a function


def what_would_I_do(input_value):
    input_value = 99  # noqa: F841


test = 0
what_would_I_do(test)
print("The value of test is", test)
```

    The value of test is 0

*The function accepts a single value and sets it to* $99$*. We then call
the function with the value of* `test` *which has been set to* $0$*. We
then print the value of* `test` *after the function call*

*Answer the following question,*

1. *What would this program print when it runs?*

    - The program follows this sequence
      1. `test` is set to $0$
      2. `what_would_I_do` is called, being passed the value of `test`
          which is $0$
      3. In `what_would_I_do`, `input_value` is initially set to $0$
      4. `input_value` is set to $99$
      5. `what_would_I_do` then ends
      6. The value of `test` is printed
    - The main observation here is that the *value* of `test` is passed
      to the function *not* `test` itself
      - `test` is unchanged outside the function

##### Make Something Happen: Creating a Teletype Printer

*Write a function* `teletype_print` *that slowly writes out an input
string. Use a* `for` *loop to loop over the contents of the string and
the `time` library to delay the output. Use a default argument with a
value of* $0.1$ *to control the print speed. Use the random library to
add a random amount of noise to the specified delay*

The final function is given in the example
[TeletypePrinter.py](./Exercises/01_TeletypePrinter/TeletypePrinter.py),
but we’ll work through the code in parts

- We first import the modules we need

``` python
# Exercise 7.1: Teletype Printer
#
# Emulates the slow speed of a teletype printer
# by using a for loop and time to slowly loop over
# an input string

import random
import time
```

- We then define our function signature, `text` is left as something
  that must be supplied while `delay` is given a default value of $0.5$
  (purely to make the delay more obvious than the $0.1$ suggested in the
  original book)
- We then add a *jitter* to the delay from $1/10$ through to the full
  size of the delay, by generating a random number
  - We then randomly generate a $0$ or a $1$ and use that to determine
    if the jitter is added or removed from the delay

``` python
def teletype_printer(text, delay=0.5):
    jitter = delay / random.randint(1, 10)
    if random.randint(0, 1):
        delay = delay + jitter
    else:
        delay = delay - jitter
```

- We then loop over the string, printing each character
  - We have to override the `print` default arguments
    - `end` determines what is printed after each call to `print`, we
      set `end` to the empty string so that all the characters are
      printed on the same line
    - Setting `flush` to `False` ensures the interpreter prints each
      character as it is called rather than waiting for the end of a
      line
- After the loop we now have to print an empty line to get the new line

``` python
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print("")
```

- Lastly we demonstrate the function being called with it’s default
  values on the word `"hello"`

``` python
teletype_printer("hello")
```

    hello

##### Make Something Happen: Teletype Fortune Teller

*Use the function you wrote for a teletype output to add some style to
the [Fortune Teller
Program](../05_MakingDecisions/Chapter_05.qmd#make-something-happen-fortune-teller)*

Our solution is given in
[TeletypeFortuneTeller.py](./Exercises/02_TeletypeFortuneTeller/TeletypeFortuneTeller.py)
and repeated below

``` python
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
```

We basically copy across the `teletype_printer` function from the
[previous exercise](#make-something-happen-creating-a-teletype-printer)
and replace the previous `print` statements with the new function. For
fun we change the default delay to a lower number so the prints occur
faster but between advice add a new

``` python
teletype_printer("...", delay=0.5)
```

call, with a longer delay that makes it look like the fortune teller is
thinking between each piece of advice

#### Return Values from Function Calls

- Functions can return values, e.g.

``` python
name = input('Enter your name please: ')
```

- Here `name` is assigned the *value* returned by the function `input`
- Functions return values via the `return` keyword, e.g. the function
  below, returns the value $1$

``` python
def return_one():
    return 1

return_one()
```

    1

##### Code Analysis: Functions and `return`

*Take a look look at the* `return` *in the following function and the
attached program to answer the following questions*

``` python
def get_value(prompt, value_min, value_max):
    return 1
    return 2

ride_number = get_value(prompt="Please enter the ride you want:", value_min=1, value_max=5)
print("You have selected ride", ride_number)
```

    You have selected ride 1

1. *What would the above program print?*

    - The function returns at the first `return` which in this case is
      $1$, so the returned value is $1$
    - The second `return` is never reached

2. *What would the program below print? Would it run correctly?*

    ``` python
     def get_value(prompt, value_min, value_max):
         return

     ride_number = get_value(prompt="Please enter the ride number you want:", value_min=1, value_max=5)
     print("You have selected ride:", ride_number)
    ```

        You have selected ride: None

    - `return` ends the function without returning a value
    - A distinct value `None` is returned
      - Represents the lack of a usable value
    - `None` is also returned when a function ends without hitting a
      `return` statement

3. *Can a function contain multiple* `return` *statements?*

    - Yes! We already saw this with the first question
    - A program exits from a function as soon as it reaches a `return`

- The program below gives a generic function that asks the user for an
  integer with a client specified `prompt` between a range of
  `value_min` and `value_max` (inclusive)

``` python
# Example 7.7: Get Value
#
# Demonstrates function returns through a program
# that receives and validates an integer


def get_value(prompt, value_min, value_max):
    while True:
        number_text = input(prompt)
        try:
            number = int(number_text)
        except ValueError:
            print("Invalid number text. Please enter digits.")
            continue
        if number < value_min:
            print("Value too small")
            print("The minimum value is", value_min)
            continue
        elif number > value_max:
            print("Value too large")
            print("The maximum value is", value_max)
            continue
        return number

#Example usage
ride_number = get_value(
    prompt="Please enter the ride number you want: ", value_min=1, value_max=5
)

print("You have selected ride: ", ride_number)
```

- An example interaction might proceed as follows

<!-- -->

    Please enter the ride number you want:  6
    Value too large
    The maximum value is 5
    Please enter the ride number you want:  3
    You have selected ride: 3

> [!TIP]
>
> **Designing Functions**
>
> Thinking about how to break a program down into functions is an
> important part of the design process. Functions are typically defined
> first in terms of their behaviour and then their header (i.e. name,
> parameters and return values).
>
> Function reduce the amount of repeated code that needs to be written.
> Don’t start by creating too many functions but when you find yourself
> repeating yourself, it’s a good sign to start writing a function
>
> 1. Any changes can now be made in one place - the function
> 2. Functions provide testable components for a larger piece of
>     software
>     - They are effectively mini-programs
>     - Tests run the function for some input and check the output
>       against some expected output
>     - Tests are typically written alongside the code itself, and mean
>       that as the code is developed and modified we can ensure it
>       still works

#### Local Variables in Python Functions

- Functions have what is called a *local namespace*
  - If we declare a variable `i` in one function we can declare another
    variable `i` in a second function,
    e.g. ([LocalVariables.py](./Examples/08_LocalVariables/LocalVariables.py))

``` python
    # Example 7.8 Local Variables
    #
    # Demonstrates the local namespaces of functions


    def func_2():
        i = 99  # noqa: F841


    def func_1():
        i = 0
        func_2()
        print("The value of i is: ", i)


    func_1()
```

    The value of i is:  0

- Here `func_1` sets its version of `i` to $0$, the calls `func_2` which
  defines its own version of `i` to $99$
- When we return to `func_1` we are dealing with `func_1`’s version of
  `i` which still has the value $0$

#### Global Variables in Python Programs

- Any variable declared outside a function is a *global* variable
- Can be implicitly accessed by any function
  - See the program
    ([GlobalVariables.py](./Examples/09_GlobalVariables/GlobalVariables.py))
    below

  ``` python
    # Example 7.9 Global Variables
    #
    # Demonstrates using global variables in functions

    cheese = 99


    def func():
        print("Global cheese is:", cheese)


    func()
  ```

      Global cheese is: 99
- If we define a new variable inside a function, with the same name as a
  global variable the global variable is hidden or *shadowed*
  - See the program
    ([ShadowingGlobalVariables.py](./Examples/10_ShadowingGlobalVariables/ShadowingGlobalVariables.py))

  ``` python
    # Example 7.10 Shadowing Global Variables
    #
    # Demonstrates local variables shadowing a
    # global variable

    cheese = 99


    def func():
        cheese = 100
        print("Local cheese is:", cheese)


    func()
    print("Global cheese is:", cheese)
  ```

      Local cheese is: 100
      Global cheese is: 99

  - We can see in the above that inside `func` we can’t see the value of
    the global `cheese`
- But what if we want to update a global variable inside a function?
  - Can use the `global` keyword to connect the variable in a function
    to the global counterpart, see
    [StoringGlobalVariables.py](./Examples/11_StoringGlobalVariables/StoringGlobalVariables.py)

  ``` python
    # Example 7.11 Storing Global Variables
    #
    # Demonstrates storing a global variables in a
    # variable in a function. Also shows updating a global
    # variable

    cheese = 99


    def func():
        global cheese  # use the global variable
        print("Global cheese is:", cheese)
        cheese = 100


    func()
    print("Global cheese is:", cheese)
  ```

      Global cheese is: 99
      Global cheese is: 100
- Observe in the above program we first connect `func` to the global
  variable `cheese`
  - The `print` shows that `func`’s `cheese` has the same value as the
    global `cheese`
- We then change the value of `cheese` in `func` and can see that this
  is propagated back to the global context
- The use of the `global` keyword makes it clear when we are intending
  to use global variables
  - However shadowing can cause confusion

> [!WARNING]
>
> **Use global data with care**
>
> Global data, while useful can make programs hard to debug. Global
> variables connect all the functions that rely on them. Changes (and by
> extension error) can propagate through to all the functions that
> depend on the variable. You should therefore limit and be clear when
> you use global variables

### Build Reusable Functions

- It is useful to write functions to capture common, reusable
  functionality
- For example: Collecting valid user data

#### Create a Text Input Function

- The simplest case, is getting a string from the user
  - Simply want to prevent the user interrupting the program
  - Also useful to provide a generic standard prompt if the user doesn’t
    want to provide one every time, i.e. default argument
- Start by defining the function header

``` python
read_text(prompt="Please enter some text: ")
```

- The implementation is then pretty similar to what we’ve developed
  before, (the full example in
  [InputFunctions.py](./Examples/12_InputFunctions/InputFunctions.py)
  contains some additional lines of code to demonstrate the use of the
  function)

``` python
# Read Text
#
# A simple function for getting validated strings from a user


def read_text(prompt="Please enter some text: "):
    while True:
        try:
            result = input(prompt)
            break  # stop loop if no exception
        except KeyboardInterrupt:
            print("Please enter text")
    return result
```

##### Code Analysis: Investigate the `read_text` function

*Use the [`read_text`](./Chapter_07.qmd#create-a-text-input-function)
function to answer the following questions*

1. *What is the* `result` *variable used to accomplish?*

    - Local variable storing the user input to be returned

2. *What stops the function from repeating continuously?*

    - The `break` statement ends the loop one a string has been entered
    - Once the loop finishes the rest of the function is linear and will
      end

3. *Why does the text reading loop repeat after the exception has been
    handled?*

    - The function reaches the end of the loop block (look at the
      indentation of the `return`)
    - The loop condition is `while True` so unless stopped by the
      `break` which requires the program to successfully read a string,
      the loop will run again

#### Add Help Information to Functions

- Python has a convention for adding comments that describe a function
- These can be automatically read and displayed by Python tooling
  - Enables automatic documentation generation
- A string literal immediately after the function header but before any
  other code is interpreted as a functions *docstring*, e.g.

``` python
def read_line(prompt):
    'Displays a prompt and reads in a string of text'
```

- The above is single-line comment that provides a simple description of
  the function
- The alternate below, is a multi-line comment which can provide more
  detail,

``` python
def read_text(prompt="Please enter some text: "):
    """
    Displays a prompt and reads in a string of text.
    Keyboard Interrupts are ignored

    prompt: str
        prompt the user sees before entering text

    return: str
        returns a string containing the string input by the user
    """
```

- Note the use of triple quotes to write a string over multiple lines
- Here we describe the function, it’s parameters and the return in
  detail
  - Our descriptions of parameters and returns explain both what they
    mean, and also the expected type

> [!TIP]
>
> **Use a standard docstring convention**
>
> There are a number of standard formats used for docstrings. Two common
> ones being
> [google](https://google.github.io/styleguide/pyguide.html#s3.8.1-comments-in-doc-strings)
> and
> [numpy](https://numpydoc.readthedocs.io/en/latest/format.html#method-docstrings)
>
> The advantage of using a common format is that it means that not only
> can we generate and display information about functions in code (see
> below for information about [pydoc](#use-pydoc)) but that there exists
> many tools for converting these standard formats into reference
> documentation that can be hosted or shared (e.g. on a website.)
>
> You could of course define your own format, but then you might need to
> roll your own tooling if you ever wanted to publish your own reference
> documentation.
>
> In these notes and the included code snippets we have generally stuck
> to using the **numpy** convention

##### Use Pydoc

- The pydoc library is designed to read function docstrings
  - For example if we use it on the standard library function `print`

  ``` python
    import pydoc

    pydoc.help(print)
  ```

      Help on built-in function print in module builtins:

      print(*args, sep=' ', end='\n', file=None, flush=False)
          Prints the values to a stream, or to sys.stdout by default.

          sep
            string inserted between values, default a space.
          end
            string appended after the last value, default a newline.
          file
            a file-like object (stream); defaults to the current sys.stdout.
          flush
            whether to forcibly flush the stream.

> [!TIP]
>
> **Form a habit of documenting your code**
>
> Nowadays, programmers try to package the documentation with the code
> writing process. Sometimes this extends to the concept of
> documentation-as-code. Whenever you write a function, you should get
> into the habit of writing documentation.

#### Create a Number Input Function

- The next function in our set of input functions is one to handle
  receiving a numbers
  - More specifically floating point numbers
- We can break this down into steps
  1. First we get a valid string from the user
      - We can reuse `read_text`
  2. We check that it’s a valid number
      - Wrap the extra functionality

``` python
def read_float(prompt):
    """
    Displays a prompt and reads in a number

    Keyboard interrupts are ignored
    Invalid numbers are rejected

    Parameters
    ----------
    prompt : str
        Prompt the user sees before giving input

    Returns
    -------
    float
        The input value

    See Also
    --------
    read_float_ranged : reads a float restricted to a closed interval
    """
    while True:
        try:
            number_text = read_text(prompt)
            result = float(number_text)
            break
        except ValueError:
            print("Please enter a number")
    return result
```

- An example usage is (mirrored in
  [InputFunctions.py](./Examples/12_InputFunctions/InputFunctions.py))

``` python
age = read_float("Please enter your age: ")
print(age)
```

- Which the user might see as,

``` python
print("Please enter your age: \033[31m 32.7 \033[0m")
print(32.7)
```

    Please enter your age:  32.7
    32.7

- We can then create a specialised version of `read_float` that uses it
  as a component to get a float restricted to a user specified range

``` python
def read_float_ranged(prompt, min_value, max_value):
    """
    Displays a prompt and reads in a number between
    min_value and max_value (inclusive)

    Keyboard interrupts are ignored
    Invalid numbers or out of range numbers are rejected

    min_value: float minimum value (inclusive)
    max_value: float maximum value (inclusive)

    return: float
    value input by user in the range [min_value, max_value]
    """
    while True:
        result = read_float(prompt)
        if result < min_value:
            print("That number is too low")
            print("The minimum value is", min_value)
            continue
        elif result > max_value:
            print("That value is too large")
            print("The maximum value is", max_value)
            continue
        break  # if here have a valid number
    return result
```

- Like with the `read_float` we use a previous function (here
  `read_float`) to capture existing error-handling and input handling
  code
  - Then add in the extra functionality
  - Example usage (again seen in the complete file
    [InputFunctions.py](./Examples/12_InputFunctions/InputFunctions.py))

  ``` python
    age = read_float_ranged("Please enter your age", min_value=5, max_value=90)
    print(age)
  ```

- Observe how we have used each function as a reusable component in the
  *next* **more** specific function
  - We can do this because we cleanly define the responsibilities of
    each function

#### Code Analysis: Investigating the `read_float_ranged` Function

*Let’s examine the final function* `read_float_ranged` *in more detail
to capture all the things we’ve built up. Answer the following
questions*

1. *Why doesn’t this function have code to capture exceptions?*

    - No, The two exception types we care about `KeyboardInterrupt` and
      `ValueError` are handled by `read_text` (via `read_float`) and
      `read_float` respectively

2. *Will chaining these functions together slow down the program?*

    - There would probably be some slow down, since each time we have to
      call a function there is some setup and tear-down
    - However, the slow down would be minuscule
    - The improved readability and compartmentalisation has advantages
      in readability and maintainability for the user
      - This practice of building higher-level functions out of smaller
        “lower level” functions is very common

3. *What would happen if a programmer reversed the minimum and maximum
    values?*

    - The program would not work, it would require a number that is
      greater than what it thinks is the `min` (actually `max`) and less
      than what it thinks is the `max` (actually the `min`). These are
      incompatible conditions and the program would never be able to
      exit the function (or interrupt it)
    - There are three options
      1. Fix the program so it swaps `min` and `max` if they are
          reversed

      2. Documents that it’s not expected to work and leaves it to the
          user to ensure that the case doesn’t arise.

      3. Raises an exception for the caller to handle. (Our
          implementation in
          [InputFunctions.py](./Examples/12_InputFunctions/InputFunctions.py))
          uses the former technique

          ``` python
           if min_value > max_value:
               raise Exception("Min value is greater than max value")
          ```

          - It is good etiquette to document exceptions raised in the
            function documentation

#### Convert our Functions into a Python Module

- Ideally we want to write our functions once and be able to reuse them
  - The most basic way would be to simply copy them into a new file each
    time we need them
- A more complete method is to write our own *module*
  - We create a file [BTCInput.py](./Examples/13_BTCInput/BTCInput.py)

  - So long as we include this file in the same directory as our new
    project we can include the functions the same way we would use
    `time` or `random` via

    ``` python
      import BTCInput
    ```

  - We then call the functions as for any other module e.g.

    ``` python
      age = BTCInput.read_float_ranged("Enter your age: ", min_value=5, max_value=90)
    ```

- If we want to avoid having to write the module name every time we call
  a function we can use the `from` keyword
  - Allows us to import specific components into the global namespace
  - Alternatively can import all components of a module using `*`
    - Typically avoid this, it carries a high risk of name clashes
      between functions defined in different modules

``` python
#option 1: import function
from BTCInput import read_float_ranged
age = read_float_ranged("Enter your age: ", min_value=5, max_value=90)

#option 2: import all
from BTCInput import *
age = read_float_ranged("Enter your age: ", min_value=5, max_value=90)
```

##### Make Something Happen: Add `BTCInput` to your Existing Programs

*Rewrite the following programs to use* `BTCInput` *for input*

1. *[Greeter](../04_WorkingWithVariables/Chapter_04.qmd#make-something-happen-use-input-to-make-a-greeter-program)*
2. *[Ultra Precise Egg
    Timer](../04_WorkingWithVariables/Chapter_04.qmd#example-ultra-precise-egg-timer)*
3. *[Pizza Order
    Calculator](../04_WorkingWithVariables/Chapter_04.qmd#make-something-happen-calculating-a-pizza-order)*
4. *[Fahrenheit To
    Celsius](../04_WorkingWithVariables/Chapter_04.qmd#make-something-happen-converting-between-fahrenheit-and-centigrade)*
5. *[Ride
    Selector](../05_MakingDecisions/Chapter_05.qmd#use-decisions-to-make-an-application)*
6. *[User-Selected Times
    Table](../06_RepeatingActionsWithLoops/Chapter_06.qmd#make-something-happen-allow-the-user-to-select-the-times-value)*

> [!NOTE]
>
> We’ve linked to where each of these programs are first referenced, but
> we’ll generally try to update the most comprehensive version of the
> respective program. We use the version of `BTCInput.py` included in
> Chapter 8 of the original code (see samples in the repo) since it
> offers a more complete set of validation functions based on the
> discussion above.
>
> To correctly setup `BTCInput.py` ensure the variable
> `DEBUG_MODE = FALSE`

1. [Greeter](./Exercises/03_BTCInputApplications/Greeter.py)

    - This change is straight forward, we replace `input` with
      `read_text`

    ``` python
     # Exercise 7.2.1: Greeter
     # An implementation of Greeter than uses BTCInput for validation

     import BTCInput

     name = BTCInput.read_text("Enter your name please: ")
     print("Hello", name)
    ```

2. [Ultra Precise Egg
    Timer](./Exercises/03_BTCInputApplications/UltraPreciseEggTimer.py)

    - We can combine the original code that reads in the egg boiling
      time and the float conversion to one call to the `BTCInput`
      function `read_float`. Note that we don’t change the second input
      which just asks the user to press enter, since really we’re
      looking for any input from the user

    ``` python
     # Exercise 7.2.2 Ultra-Precise Egg Timer
     #
     # Implementation of Ultra-Precise Egg Timer using BTCInput

     import time
     import BTCInput

     egg_time = BTCInput.read_float("Enter the cooking time in seconds: ")

     print("Put the egg in boiling water now")
     input("Press enter to continue once the egg is in...")

     time.sleep(egg_time)

     print("Take the egg out now")
    ```

3. [Pizza Order
    Calculator](./Exercises/03_BTCInputApplications/PizzaOrderCalculator.py)

    - Again we simply replace the `int(input())` structure with the
      BTCInput equivalent, `BTCInput.read_int`

    ``` python
     # Exercise 7.2.3: Pizza Order Calculator
     #
     # Implementation of Pizza Order Calculator that uses BTCInput

     import BTCInput

     students_int = BTCInput.read_int("How many students are attending? ")

     pizza_count = int(students_int / 1.5) + 1  # perform division int -> float
     print("You will need", pizza_count, "pizzas")
    ```

4. [Fahrenheit To
    Celsius](./Exercises/03_BTCInputApplications/FahrenheitToCelsius.py)

    - Again a simple replacement, here `float(input(...))` becomes
      `BTCInput.read_float()`

    ``` python
     # Exercise 7.2.4: Fahrenheit to Celsius
     #
     # Version of Fahrenheit to Celsius that uses BTCInput

     import BTCInput

     temperature_fahrenheit = BTCInput.read_float("Enter a temperature in Fahrenheit: ")
     temperature_centigrade = (temperature_fahrenheit - 32) / 1.8
     print("The temperature is", temperature_centigrade, "degrees Celsius")
    ```

5. [Ride Selector](./Exercises/03_BTCInputApplications/RideSelector.py)

    - The implementation is based on the [Full input validated version
      of Ride
      Selector](../06_RepeatingActionsWithLoops/Chapter_06.qmd#make-something-happen-add-validation-to-the-theme-park-age-input)
      in Chapter 6

    - There are two important changes, first to ensure the user selects
      a valid theme park ride option, we use `BTCInput.read_int_ranged`

      ``` python
        ride_number = BTCInput.read_int_ranged(
            "Please enter the ride number you want: ", 0, 5
        )
      ```

    - *Remember that* $0$ *is a number we’ve chosen to represent
      quitting the program*

    - Second the ensure the user adds an age, here even though we have a
      valid age range, this is for being able to ride

      - We still want to accept those ages, *and then* inform the user
        of the issue
      - So here we use `BTCInput.read_int` (note un-ranged)

      ``` python
        age = BTCInput.read_int("Please enter your age: ")
      ```

6. [User Selected Times
    Tables](./Exercises/03_BTCInputApplications/TimesTables.py)

    - Here we can remove all the validation code we wrote and simply
      replace it with the `BTCInput.read_int_ranged` call

    - This highlights the advantage of functions, the final program is
      much cleaner and easier to read

      ``` python
        # Exercise 7.2.6 Tables Tables
        #
        # Variant of the User Selected Times Tables Tutor that uses BTCInput for
        # validation

        import BTCInput

        count = 1
        times_value = BTCInput.read_int("Please enter a times table between 2-12 (inclusive): ")

        while count < 13:
            result = count * times_value
            print(count, "times", times_value, "equals", result)
            count = count + 1
      ```

### Using a Debugger

- Most python development environments support a *debugger*
- A *debugger* is a program designed to help you identify (and solve)
  *bugs* or problems in your program
- This section will introduce concepts of a debugger
  - The book discusses the specifics of using the debugger packaged in
    IDLE
  - The notes here discuss generics
- A *debugger* runs code like normal, but supports extra tools and
  techniques for interrogating the internal state of a program
- A *breakpoint* causes the program being run in the debugger to pause
  when it reaches the line where the break occurs.
  - breakpoints allow the programmer to halt the program at a desired
    point (typically close to where a problem occurs) and inspect
    variable contents

> [!NOTE]
>
> **Breakpoints vs** `break`
>
> A *breakpoint* is different to the `break` keyword
>
> - `break` is used to immediately escape a loop structure in a running
>   program
> - A *breakpoint* is used to pause the execution of a program at a
>   specific point when it is being debugged

#### Make Something Happen: Investigate Programmers with a Debugger

*Use the following example, found in*
[InvestigateTheDebugger.py](./Examples/14_InvestigateTheDebugger/InvestigateTheDebugger.py)
*as the basis to learn the debugger*

``` python
# Example 7.14 Investigate the Debugger
#
# A sample code for practising with the debugger


def increment_function(input_value):
    result = input_value + 1
    return result


x = 99
y = increment_function(x)
print("The answer is:", y)
```

*Using your debugger, set a breakpoint on the line* `x = 99`

- In *VSCode* for my setup with the python extensions I simply click on
  the line, left of the line number, a red circle appears indicating a
  breakpoint
  - To clear the breakpoint just click on it again
- Then run your program using the debugger
  - In *VSCode* I simply go to the *Run and Debug* tab, and click the
    *Run and Debug* button
    - I then select from a dropdown menu, *python debugger* followed by
      *debug the current file*
  - The code starts running then stops at the breakpoint
  - On the left a panel shows the *call stack*
    - The call stack shows the sequence of function calls we are in
  - Above a panel shows the contents of variables
    - Broken up into a tab for
      - Local variables
      - Global variables
      - There are also tabs for special and function variables which can
        be ignored for now
  - A control panel shows at the top of the program, the options are as
    follows,
    - **Go** continues running the program
    - **Step Over** goes to the next line in the program
      - If the line the program is on is a function, the program will
        calculate the results of the function and then go to the line
        after the program
    - **Step In** goes to the next line in the program, if the program
      is on a function, the debugger will step into the function and go
      through it line by line
      - This includes opening any files where a function is defined in
        another file
    - **Step Out** completes the current function and goes to the line
      after it
    - **Restart** restarts the program
    - **Stop** immediately stops the program
- Use the step function to watch how python flows through this program,
  observe the call stack and the variable values when you step into
  `increment_function`
  - Observe what happens when you step into `print`
    - Depending on the debugger it may or may not step into the `print`
      function
    - Use **Step Out** to leave `print`
    - Use **Step Out** again, the program should end

## Summary

- Functions allow us to reuse blocks of code
- Functions consist of a header describing the function and the code
  - Header supplies function and parameter names (including their
    default values if specified)
- Functions are called with arguments passed to the parameters
- Parameters are value copied objects the function can work on
  - This means changes are local to the function
- Functions can return a value via the `return` function
- `None` is returned when a function finishes without an explicit return
  value
- Variables defined in a function are local to that function
  - Cannot be accessed outside the function
- Variables declared outside any function are called global variables
  - Can be read by functions
  - Can be modified by functions via the `global` keyword
- Local variables can shadow global variables if they share the same
  name
- A function can contain a string as the first statement
  - This is called the *docstring* and documents the behaviour of the
    function
- Functions can be imported into another python file that has access to
  the file they are defined in

## Questions and Answers

1. *Does using functions in programs slow down the program?*
    - Not noticeably. The slight cost of setting up and tearing down
      functions is minimal
2. *Can I use functions to spread work around a group of programmers?*
    - Yes, packaging functions into modules is a very common way for
      programmers to share code including functions
    - Alternatively when building programs together, programmers may
      define the function headers together, and then each can work on
      implementing different functions separately
3. *How do I come up with names for my functions?*
    - Functions should typically be *verbs* that describe what action
      they do, e.g. `read_string` reads a string. Where reasonable also
      try to indicate what it returns
4. *Can functions in libraries use global variables?*
    - Global variables are those declared at file scope
    - Library files can contain global variables
    - They can be used by the functions in those files
    - But they cannot be shared across files
5. *Should I put all my functions in modules/libraries?*
    - Probably not *all* of your functions
    - Good for common utility functions that have quite broad use cases
    - A common pattern in larger applications is to split functions into
      files that group together natural sets of logic
