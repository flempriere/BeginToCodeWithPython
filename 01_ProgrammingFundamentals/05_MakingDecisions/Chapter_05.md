# Chapter 5: Making Decisions

- [Notes](#notes)
  - [Boolean Data](#boolean-data)
    - [Create Boolean Values](#create-boolean-values)
    - [Example: Working with Boolean
      Values](#example-working-with-boolean-values)
    - [Boolean Expressions](#boolean-expressions)
      - [Example: One-Handed Clock](#example-one-handed-clock)
      - [Exercise: Improved Clock](#exercise-improved-clock)
    - [Comparing Values](#comparing-values)
      - [Comparison Operators](#comparison-operators)
        - [Example: Examining Comparison
          Operators](#example-examining-comparison-operators)
    - [Boolean Operations](#boolean-operations)
      - [Example: Examining Boolean
        Operators](#example-examining-boolean-operators)
  - [The `if` Construct](#the-if-construct)
    - [Example: Simple Alarm Clock](#example-simple-alarm-clock)
    - [Conditions in Python](#conditions-in-python)
    - [Combine Python Statements into a
      Suite](#combine-python-statements-into-a-suite)
      - [Example: Siren Alarm Clock](#example-siren-alarm-clock)
      - [Example: Time Display Alarm
        Clock](#example-time-display-alarm-clock)
    - [Structure of an `if` Statement](#structure-of-an-if-statement)
      - [Example: Layout of Conditional
        Statements](#example-layout-of-conditional-statements)
    - [Add an `else` to an `if`
      Construction](#add-an-else-to-an-if-construction)
      - [Example: Simple Alarm Clock with
        Else](#example-simple-alarm-clock-with-else)
      - [Example: If Constructions](#example-if-constructions)
    - [Compare Strings in Programs](#compare-strings-in-programs)
      - [Example: Broken Greeter](#example-broken-greeter)
      - [Example: Methods and Functions](#example-methods-and-functions)
    - [Nesting `if` Conditions](#nesting-if-conditions)
      - [Example: Protected Greeter](#example-protected-greeter)
    - [Working with Logic](#working-with-logic)
      - [Exercise: Make an Advanced Alarm
        Clock](#exercise-make-an-advanced-alarm-clock)
  - [Use Decisions to make an
    Application](#use-decisions-to-make-an-application)
    - [Design the User Interface](#design-the-user-interface)
    - [Implement the User Interface](#implement-the-user-interface)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

> [!CAUTION]
>
> A number of the code examples in this use the file *siren.wav*, this
> can be found in the corresponding chapter in the samples submodule.
> For space reasons we haven’t uploaded it to the github

### Boolean Data

- Boolean values are a type that is used to distinguish between values
  that are *True* or *False*
- For example, we could use an `int` to count the number of hairs on a
  person’s head, but a `bool` to indicate if they are bald

#### Create Boolean Values

- Simply declare a variable with a value of `True` or `False`
  - Python will infer the type
- For example, to declare a true valued boolean,

``` python
it_is_time_to_get_up = True
```

- we can then set the value to `false`,

``` python
it_is_time_to_get_up = False
```

- Note that `True` and `False` are python keywords, and are
  case-sensitive, e.g. true and false will not work as expected

#### Example: Working with Boolean Values

*Open up the python interpreter and work through the following questions
to understand booleans*

1. \*What do you think would happen if you printed the contents of a
    boolean value?

    ``` python
    it_is_time_to_get_up = True
    print(it_is_time_to_get_up)
    ```

        True

    - *Python will try to print out something meaningful, for a boolean
      this is either* `True` *or* `False`

2. *What do you think would happen if you gave the word* **True** to
    the `input` function?

    ``` bash
    x = input("True or False: ")
    True or False: True
    ```

    - `input` returns it’s input as a string, so in this case `x` will
      not be a `bool` but rather a `string` with the value `'True'`

3. *Is there a python function called* `bool` *that will convert things
    into Boolean, just like there are* `int` *and* `float` *functions?*

    - *Yes there is, consistent behaviour with bool. Consider the
      following examples*

    ``` python
    print(bool(1))
    print(bool(0))
    print(bool(0.0))
    print(bool(0.1))
    print(bool(''))
    print(bool('Hello'))
    ```

        True
        False
        False
        True
        False
        True

    - *We can see that non-zero numbers evaluate* `True` *while zero,
      evaluates as* `False`. *Similarly the empty string evaluates*
      `False` *while a non-empty string evaluates as* `True`

4. *What happens if a program combines* `bool` *values with other
    values?*

    - *We should already expect that if we try to mix incompatible data
      that an error should be generated*

    ``` python
     'Hello' + True
    ```

        TypeError: can only concatenate str (not "bool") to str
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[148], line 1
        ----> 1 'Hello' + True

        TypeError: can only concatenate str (not "bool") to str

    - *We can see that we cannot concatenate a boolean value to a
      string*
    - *The behaviour can be a little less intuitive with numbers
      though*,

    ``` python
    1 + True
    ```

        2

    - `True` *is implicitly converted to the integer value* $1$

    ``` python
    1 + False
    ```

        1

    - *Similarly,* `False` *is implicitly converted to the intger value*
      $0$
    - *We can see that numeric operations on bool thus have well-allowed
      behaviour but we cannot do the same with textual data*

#### Boolean Expressions

- Normally we don’t declare a boolean with `True` or `False` explicitly
  but instead as the result of evaluating an expression
  - Some expressions evaluate to `True` or `False` which naturally suits
    being stored in a boolean
- Consider a simple alarm clock,
  - We can get the time through the `time` library we’ve seen
    [before](../03_PythonProgramStructure/Chapter_03.qmd#the-time-library)

    ``` python
    import time

    current_time = time.localtime()

    hour = current_time.tm_hour
    ```

  - `time.localtime` returns an object containing information about the
    current time.

    - This different blocks of information are called *attributes*,
      below is a list of the attributes contained in the object returned
      by `localtime`

| **Attribute** | **Value** |
|----|----|
| tm_year | Year (for example, 2017) |
| tm_mon | Month (in the range 1 … 12, 1 represents January) |
| tm_mday | Day in the Month (in the range 1 … month length) |
| tm_hour | Hour in the Day (in the range 0 … 23) |
| tm_min | Minute in the Hour ( in the range 0 … 59) |
| tm_sec | Seconds in the Minute ( in the range 0 … 59) |
| tm_wday | Day of the Week (in the range 0 … 6 with Monday as 0) |
| tm_yday | Day in the Year (in the range 0 … 364 or 365 depending on if the year is a leap year) |

- An example of a `localtime` object might look like,

| **Attribute** | **Value** |
|---------------|-----------|
| tm_year       | 2017      |
| tm_mon        | 7         |
| tm_mday       | 19        |
| tm_hour       | 11        |
| tm_min        | 40        |
| tm_sec        | 30        |
| tm_wday       | 2         |
| tm_yday       | 200       |

##### Example: One-Handed Clock

*Lets make a clock that displays only the hour value, using `localtime`.
These* **one-handed clocks** *are supposed promote a more relaxed
attitude. Create a new program
([OneHandedClock.py](./Examples/01_OneHandedClock/OneHandedClock.py))
and copy the below text.*

``` python
# Example 5.1: One Handed Clock
# Uses time to display the hour

import time

current_time = time.localtime()
hour = current_time.tm_hour

print("The hour is:", hour)
```

    The hour is: 20

*Run the program, it should print out the current hour*

##### Exercise: Improved Clock

*Improve the previous
[example](./Chapter_05.qmd#example-one-handed-clock) to produce a more
fully featured clock that reports the time, and date when run*

We can use the table above to grab the correct attributes. We then
simply need to format the attribute as nessecary. The final
[program](./Exercises/01_ImprovedClock/ImprovedClock.py) is given below

``` python
# Exercise 5.1: Improved Clock
# An improved clock that displays the date and time when run

import time

current_datetime = time.localtime()

day = current_datetime.tm_mday
month = current_datetime.tm_mon
year = current_datetime.tm_year
print("The date is", day, "/", month, "/", year)

seconds = current_datetime.tm_sec
minutes = current_datetime.tm_min
hours = current_datetime.tm_hour
print("The time is", hours, ":", minutes, ":", seconds)
```

    The date is 22 / 11 / 2025
    The time is 20 : 10 : 49

#### Comparing Values

- We’ve seen expressions as being made of operators and operands
- One type of operator is a *comparison* operator
  - Returns a value that is `True` or `False`, e.g.

``` mermaid
block-beta
    columns 3
    space
    title["Breakdown of an Example Comparison Expression"]
    space

    block:Input
    columns 1
        operand1["hour"]
        operand1Word["Operand"]
        operand1descr["(thing to work on)"]
    end

    block:Middle
    columns 1
        operator[">"]
        operatorWord["Operator"]
        operatorDescr["(thing to do)"]
    end

    block:Output
    columns 1
        operand2["6"]
        operand2Word["Operand"]
        operand2descr["(thing to work on)"]
    end

classDef BG stroke:transparent, fill:transparent
class title BG
class operand2Word BG
class operand2descr BG
class operand1Word BG
class operand1descr BG
class operatorWord BG
class operatorDescr BG
```

##### Comparison Operators

- Below is a table of the common comparison operators

| **Operator** | **Name** | **Effect** |
|----|----|----|
| $>$ | Greater than | `True` if the left argument is greater than the right, else `False` |
| $<$ | Less than | `True` if the left argument less than the right, else `False` |
| $>=$ | Greater than or Equal | As for Greater than but also `True` if the left argument equals the right |
| $<=$ | Less than or Equal | As for Less than but also `True` if the left argument equals the right |
| $==$ | Equals | `True` if the left argument equals the right argument, else `False` |
| $!=$ | Not Equals | `True` if the left argument **does not equal** the right argument, else `False` |

- A program can use a comparison operator to set a boolean variable,
  e.g. the below code fragment which sets the boolean variable
  `it_is_time_to_get_up` to `True` if the variable `hour` is greater
  than $6$ else sets it to `False`

``` python
it_is_time_to_get_up = hour > 6
```

###### Example: Examining Comparison Operators

*Use the python interpreter to work through the following questions in
order to understand Comparison Operators*

1. *How does the equality operator work?*
    - *The equality operator evaluates to* `True` *if the two operands
      hold the same value*

    ``` python
    1 == 1
    ```

        True

    - *The equality operator can be used to compare strings and bools*

    ``` python
     'Rob' == 'Rob'
    ```

        True

    ``` python
     True == True
    ```

        True
2. *How do I remember which relational operator to use?*
    - *Practice, patience and muscle memory*
3. *Can we apply relational operators between other types of
    expressions?*
    - *Yes. For example, the* $>$ *and* $<$ *operators when used to
      compare strings will use an alphabetic ordering*, e.g.

      ``` python
      'Alice' < 'Brian'
      ```

          True

> [!WARNING]
>
> In [Chapter
> 4](../04_WorkingWithVariables/Chapter_04.qmd#real-numbers-and-floating-point)
> we noted that floating points only approximate a specific real-value.
> These approximations can cause issues when using comparison operators,
> e.g.
>
> ``` python
> x = 0.3
> y = 0.1 + 0.2
> x == y
> ```
>
>     False
>
> - The variables `x` and `y` should both notionally store $0.3$, but
>   the equality shows they are unequal. This is because the addition of
>   $0.1$ and $0.2$ actually leads to `y` storing the slightly
>   inaccurate $0.3000...4$
> - If comparing floating-point numbers for equality, the best approach
>   is to check that the values are appropriately close

- Python provides the `type` function, `type(x)` returns the type of the
  variable `x`, especially useful for investigating the type of values
  returned by library functions you’ve never seen before

#### Boolean Operations

- What if we want to combine boolean expressions to create a new boolean
  expression
- e.g. An alarm might want to go off when the hour is after $7$ *and*
  the minute is after $30$
- Python provides *logic* operators for combining boolean expressions

##### Example: Examining Boolean Operators

*Use the python interpreter to answer the following questions and
investigate boolean operators*

1. *What does the following expression evaluate too?*

    ``` python
    not True
    ```

        False

    - `not` *inverts the value of a boolean, so* `True` *is converted
      to* `False`

2. *How about this expression?*

    ``` python
    True and True
    ```

        True

    - `and` *is* `True` *iff both arguments are* `True` *as is the case
      above, so the result is* `True`

3. *How about this expression?*

    ``` python
    True and False
    ```

        False

    - *Since one of the arguments is* `False` `and` *will evaluate to*
      `False`

4. *How about this expression?*

    ``` python
    True or False
    ```

        True

    - *Since one of the arguments is `True` `or`*will evaluate to\*
      `True`

5. *So far, the examples have only used boolean values. What happens if
    we mix boolean and numeric values?*

    ``` python
    True and 1
    ```

        1

    - *Recall that python can convert numeric expressions to boolean
      ones, this implicitly happens to the* $1$ *in the above. So we
      would expect* `and` *to return* `True`*. However ,instead* $1$ *is
      returned. This is due to some odd python behaviour*
      - *Python sees* `True` *-\> result of* `and` *implied by second
        argument*

        - *So simply returns the second argument, since the*
          **truthfulness** *of* $1$*, is equivalent to the original
          expression*

      - *If we flip the arguments, we should see this more clearly*

        ``` python
        1 and True
        ```

            True

        - *This time the above expressions should return* `True`

      - *The same behaviour will also occur with* `or`

        ``` python
        1 or False
        ```

            1

        - *Here the* `or` *operator short-circuits on* $1$, *so returns*
          $1$

        ``` python
        0 or True
        ```

            True

        - *Here the* `or` *evaluates the first argument as false, so
          cannot short-circuit, the second argument is returned, i.e*
          `True`

- Let us now use `and` to try construct an expression that will
  correctly evaluate when the time is after $7:30$, naively we might
  expect,

``` python
it_is_time_to_get_up = hour > 6 and minute > 29
```

- We can use a truth table to check,

| **Hour** | **Minute** | **Desired** | **Output** |
|----------|------------|-------------|------------|
| 6        | 0          | False       | False      |
| 7        | 29         | False       | False      |
| 7        | 30         | True        | True       |
| 8        | 0          | True        | False      |

- We can see in the last case the result is not what we want!
  - `hour > 7` is true, but `minute > 29` is false, so we need to be
    more precise,

``` python
it_is_time_to_get_up = (hour > 7) or (hour == 7 and minute > 29)
```

- We use brackets to make the expression more readable
- Here we use short-circuiting, if the the hour is greater than $7$ we
  don’t need to check the minutes value

> [!WARNING]
>
> When working with boolean operations you should always check that the
> logic matches what you expect!

### The `if` Construct

- Suppose we want a program to tell me if it’s time to get out of bed
- Need the ability to run code `if` a boolean condition is met
  - Can do so using the aptly named `if` operator

#### Example: Simple Alarm Clock

- *Create a new python program
  ([SimpleAlarmClock.py](./Examples/02_SimpleAlarmClock/SimpleAlarmClock.py))
  with the following contents*

``` python
# Example 5.2: Simple Alarm Clock
# Demonstrates `if` using a simple alarm clock

import time

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_sec

it_is_time_to_get_up = (hour > 7) or (hour == 7 and minute > 29)

if it_is_time_to_get_up:
    print("IT IS TIME TO GET UP")
```

    IT IS TIME TO GET UP

- *The program should print* `IT IS TIME TO GET UP` *only if the time is
  after* $7:30$

- The `if` construct starts with the word `if`, following by a boolean
  value called the `condition`, then a `:`

- Any statements we want to execute *if* the `if` is `True` are then
  written below the `if` and *indented* one level

#### Conditions in Python

- Condition is a term for the expression that controls which branch of
  the `if` is executed
- If the condition evaluates `True` the indented branch is run
- If the condition evluates `False` the indented branch is skipped
- We could simply the above code by including the check directly in the
  `if` rather than an intermediate variable

``` python
if (hour > 7) or (hour == 7 and minutes > 29):
    print("IT IS TIME TO GET UP")
```

    IT IS TIME TO GET UP

#### Combine Python Statements into a Suite

- What if we want multiple statements to run after an `if` statement
- We just write them as a sequence of indented statements

##### Example: Siren Alarm Clock

*Let us improve the previous [example](#example-simple-alarm-clock) to
also play a sound if it’s time to get up. Create a program
([SirenAlarmClock.py](./Examples/03_SirenAlarmClock/SirenAlarmClock.py))
with the contents below*

``` python
# Example 5.3: Siren Alarm Clock
# Improves the Simple Alarm Clock to also play a sound
import time

import snaps

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    snaps.display_message("TIME TO GET UP")
    snaps.play_sound("siren.wav")
    # pause the program to give time for the sound to play
    time.sleep(10)
```

*This program now runs three statements in the* `if`

1. *First a message is displayed*
2. *Second a sound is played*
3. *Third the program sleeps so the sound has time to play*

- If we want something to run regardless of the `if` condition, we write
  it either before or after the `if` statement

##### Example: Time Display Alarm Clock

*Add to the simple Alarm Clock, by making it so the program will always
print the current time regardless of if the alarm goes off. Create a new
program
([AlarmClockWithTimeDisplay.py](./Examples/04_AlarmClockWithTimeDisplay/AlarmClockWithTimeDisplay.py)).
Enter the following contents,*

``` python
# Example 5.4: Alarm Clock with Time Display
# A variant of Alarm Clock to also always display the time

import time

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    print("TIME TO GET UP")
    print("RISE AND SHINE")
    print("THE EARLY BIRD GETS THE WORM")
print("The time is", hour, ":", minute)
```

    TIME TO GET UP
    RISE AND SHINE
    THE EARLY BIRD GETS THE WORM
    The time is 20 : 10

- *The program above will always print the current time, regardless of
  if the alarm block is run*

> [!CAUTION]
>
> **Indented Text can cause Big Problems**
>
> As seen above, python uses indentation for control flow, this has the
> advantage in that it follows normal code style practices, but has some
> pitfalls
>
> 1. If the indention is wrong the program won’t run
>
>     - i.e. if one line is indented four spaces, and the next three an
>       error will be thrown
>
>       ``` python
>       import time
>       current_time = time.localtime()
>       hour = current_time.tm_hour
>       minutes = current_time.tm_min
>
>       if (hour > 7) or (hour == 7 and minute > 29):
>         print("IT IS TIME TO GET UP")
>             print("The early bird gets the worm...")
>       ```
>
>           IndentationError: unexpected indent (1845908205.py, line 8)
>             Cell In[169], line 8
>               print("The early bird gets the worm...")
>               ^
>           IndentationError: unexpected indent
>
> 2. A more insidious error, occurs if one mixes tabs and spaces in the
>     indentation, since the code may appear to be fine until it
>     attempts to run
>
>     ``` python
>      import time
>      current_time = time.localtime()
>      hour = current_time.tm_hour
>      minutes = current_time.tm_min
>
>      if (hour > 7) or (hour == 7 and minute > 29):
>          print("IT IS TIME TO GET UP")
>          print("The early bird gets the worm...")
>     ```
>
>         IT IS TIME TO GET UP
>         The early bird gets the worm...
>
>     - Most programmers and even text editors will automatically
>       convert one style of indentation to the other (commonly tabs to
>       spaces, but sometimes spaces to tabs) to avoid this issue
>       - In the above code, my editor converted the second line which
>         was indented with spaces to a tab to match the previous line

#### Structure of an `if` Statement

- Formally, an `if` has a structure like

``` mermaid
block-beta
    columns 4
    space
    title["Breakdown of an if statement"]:2
    space

    block:Input
    columns 1
        if["if"]
        ifDescr["(start of the if construction)"]
    end

    block:Condition
    columns 1
        condition["condition"]
        conditionDescr["(value that is true or false)"]
    end

    block:Colon
    columns 1
        colon[":"]
        colonDescr["colon"]
    end

    block:Suite
    columns 1
        suite["suite"]
        suiteDescr["statements"]
    end

classDef BG stroke:transparent, fill:transparent
class title BG
class condition BG
class conditionDescr BG
class colon BG
class colonDescr BG
class suite BG
class suiteDescr BG
class if BG
class ifDescr BG
```

- There are two ways to write the *suite*
  1. A set of indented statements on the lines proceeding the `if`

  2. A set of statements on the same line as the `if` each seperated by
      a semicolon (`;`) e.g.

      ``` python
       if (hour > 6): print('IT IS TIME TO GET UP'); print('THE EARLY BIRD GETS THE WORM')
      ```

> [!WARNING]
>
> You can’t combine inline `if` statements, with indented `if`
> statements, e.g.
>
> ``` python
>     import time
>     current_time = time.localtime()
>     hour = current_time.tm_hour
>     minutes = current_time.tm_min
>
>     if (hour > 7) or (hour == 7 and minute > 29): print("IT IS TIME TO GET UP"); print("RISE AND SHINE")
>         print("The early bird gets the worm...")
> ```
>
>     IndentationError: unexpected indent (1682748311.py, line 7)
>       Cell In[171], line 7
>         print("The early bird gets the worm...")
>         ^
>     IndentationError: unexpected indent

##### Example: Layout of Conditional Statements

*Use the python interpreter to answer the following questions to
understand conditional statements*

1. *Can we work with conditional statements using the python shell?*
    - *Yes you can, type the following into the shell,*

    ``` python
    if True:
    ```

    - *The shell may display* `...` *instead of* `>>>` *or, omit* `>>>`
      *and indent*

      - *In the first case we can indent ourselves to write the suite*
      - *In the second we simply write the suite*

    - *Once done writing the* `if` *suite, simply deindent*

    - *Try write the following in the shell, and verify the output*

      ``` python
        if True:
            print('True')
            print('Still True')
      ```

          True
          Still True
2. *How many spaces must you indent a suite of Python statements
    controlled by an* `if` *statement?*
    - *There is no approved value, but it must be consistent, i.e. if
      the first indentation is four, then all future indentations must
      also be four*
      - *Common choices are 4, 8 or 2*

#### Add an `else` to an `if` Construction

- Sometimes we want conditional behaviour on both the `True` and `False`
  branches
- `else` is a keyword that lets us add behaviour that executes when an
  `if` evaluates as `False`

##### Example: Simple Alarm Clock with Else

*Modify the [Simple Alarm Clock](#example-simple-alarm-clock) to now
print a message telling us to go back to bed if it before our alarm
should go off. Write a new program
([SimpleAlarmClockWithElse.py](./Examples/05_SimpleAlarmClockWithElse/SimpleAlarmClockWithElse.py))
with the following contents,*

``` python
# Example 5.5: Simple Alarm Clock
# Variant of the Simple Alarm Clock
# that modifies the output depending on if its time to get up

import time

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min

if (hour > 7) or (hour == 7 and minute > 29):
    print("IT IS TIME TO GET UP")
else:
    print("Go back to bed")
```

    IT IS TIME TO GET UP

- *Observe that only one line of the paired `if-else` statements is
  printed*

##### Example: If Constructions

*Work through the following questions to understand `if` constructions*

1. *Must an* `if` *construction have an* `else` *part?*
    - **No***,we saw when first working with* `if` *that we could
      exclude the* `else` *in that case no additional code runs if the*
      `if` *evaluates* `False`
2. *What happens if a condition is never* `True`*?*
    - *It simply never executes*

#### Compare Strings in Programs

- The `if` statement can be used to compare strings, as seen with the
  [comparison operators](#comparison-operators)

##### Example: Broken Greeter

*The following program uses the equality operator and an `if` statement
to greet a person if their name matches. What is a potential issue with
this [program](./Examples/06_BrokenGreeter/BrokenGreeter.py)?*

``` python
# Example 5.6: Broken Greeter
# A Greeter program using string matching
# Identify the issues with this program

name = input("Enter your name: ")

if name == "Rob":
    print("Hello, Oh great one")
```

*The equality operator checks against the string* `"Rob"` *exactly,
i.e. it is case sensitive, if we write* `"ROB"`*, or* `"rob"` *or some
variation thereof, the statement will not match.*

*We can fix this by using the string method* `upper`*, this converts all
forms of the word* `"rob"` *to* `"ROB"` *which we can reliably check
against. The new
[program](./Examples/07_UppercaseGreeter/UppercaseGreeter.py) looks
like*

``` python
# Example 5.7: Uppercase Greeter
# A Greeter program using string matching
# Fixes the issues with Example 5.6 by using
# str.upper()

name = input("Enter your name: ")

if name.upper() == "ROB":
    print("Hello, Oh great one")
```

- *We could also use the string method `lower` to compare against an all
  lowercase word*

##### Example: Methods and Functions

*Consider the following questions to learn about methods and functions*

1. *How do `lower()` and `upper()` work?*
    - *Python types are objects that provide* **methods**.
    - *Methods are called like functions*
2. *Why do we have to write `lower()` and not `lower`?*
    - *Leave the parentheses off, and see what happens*

      ``` python
        name = 'Rob'
        name.upper
      ```

          <function str.upper()>

    - *We are instead returned a description of the method itself*
3. *What’s the difference between functions and methods?*
    - *They are used the same way, but they differ in where they are
      created*
    - *Functions are not associated any specific object*
    - *Methods are bound as attributes of objects*

#### Nesting `if` Conditions

- You can nest conditions, e.g. if you want to perform sequential checks

##### Example: Protected Greeter

*Let us demonstrate nested `if` through a greeter which requires a
follow on code word to confirm the identity of the user. Create a
program ([CodedGreeter.py](./Examples/08_CodedGreeter/CodedGreeter.py))
with the following contents*

``` python
# Example 5.8: Coded Greeter
# Asks the user for a follow on code to confirm their ID
# before the program greets them

name = input("Enter your name: ")

if name.upper() == "ROB":
    code = input("Enter the codeword: ")
    if code == "secret":
        print("Hello, Oh great one")
    else:
        print("Begone. Imposter")
```

- *Play around with the above code to see what happens for various input
  combinations. You should see if the first input is not a variant of
  `"rob"` the second prompt never occurs and the program ends. Adjust
  the above by writing a new program
  ([CodedGreeterWithOuterElse.py](./Examples/09_CodedGreeterWithOuterElse/CodedGreeterWithOuterElse.py))*

#### Working with Logic

##### Exercise: Make an Advanced Alarm Clock

*Improve the [Alarm Clock](#example-time-display-alarm-clock). Make the
alarm display the date as well as the time, and let the user sleep in on
the weekends.*

Our implementation is given below,

``` python
# Exercise 4.2: Advanced Alarm Clock
# An Advanced Alarm Combining the Behaviour
# of most increments of the alarm clock
# and allowing you to sleep in on weekends

import time
import snaps

current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
day = current_time.tm_mday
month = current_time.tm_mon
is_weekend = current_time.tm_wday >= 5

date_message = "The date is " + str(day) + "/" + str(month)
time_message = "The time is " + str(hour) + ":" + str(minute)

msg = ""
up_hour = 7 + is_weekend  # get to sleep in an extra hour on weekends

if (hour > up_hour) or (hour == up_hour and minute > 29):
    msg = msg + "TIME TO GET UP"
    snaps.play_sound("siren.wav")
else:
    msg = msg + "Go back to bed!"
msg = msg + "\n" + date_message + "\n" + time_message
snaps.display_message(msg, size=50)
time.sleep(10)  # leave time for the sound and to read
```

Most of the text simply exists to correctly create the final message we
will display on the screen. The most important parts are,
`is_weekend = current_time.tm_wday >= 5` which uses the fact that
Saturday and Sunday have the value $5$ and $6$ in the
`current_time.tm_wday` attribute (A number representing the day in the
week) to set a boolean flag. We then use the fact that `True` acts
numerically as one, and `False` acts numerically as zero to let us sleep
in an hour on the weekend using `up_hour = 7 + is_weekend` which is $8$
on weekends and $7$ on weekdays.

We then run through the code as we have for most of the alarm clock
cases, using an `else` clause to ensure we always have a message for the
user, and appending the date and time message to this output.

Lastly we pass the method to `snaps` for display

### Use Decisions to make an Application

- In this next section we’ll write our first semi-sophisticated program

> **Scenario:**
>
> A local theme park wants you to write a program that will let users
> check if they meet the age requirements to go on a ride. They provide
> the following table covering the current rides
>
> | **Ride**                      | **Restrictions**                       |
> |-------------------------------|----------------------------------------|
> | Scenic River Cruise           | None                                   |
> | Carnival Carousel             | At least 3 years old                   |
> | Jungle Adventure Water Splash | At least 6 years old                   |
> | Downhill Mountain Run         | At least 12 years old                  |
> | The Regurgitator              | At least 12 years old and less than 70 |

#### Design the User Interface

- We will use a simple text interface

``` text
Welcome to our Theme Park

These are the available rides

1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator

Please enter the ride you want: 1
You have selected the Scenic River Cruise
There are no age limits for this ride
```

> [!IMPORTANT]
>
> **Design the User Interface with the Customer**
>
> The UI can be the most important and most difficult part of design
> because it can be very subjective. Ultimately the Customer is the one
> paying and so they should be involved in the UI design throughout!

#### Implement the User Interface

- We have a UI design, now we need to implement it
- Our code starts as below,

``` python
# Example 5.10: Ride Selector Start
# The basic shell of the Ride Selector UI

print("""Welcome to our Theme Park
      These are the available ride:

      1. Scenic River Cruise
      2. Carnival Carousel
      3. Jungle Adventure Water Splash
      4. Downhill Mountain Run
      5. The Regurgitator
      """)

ride_number_text = input("Please enter the ride number you want: ")
ride_number = int(ride_number_text)

if ride_number == 1:
    print("You have selected Scenic River Cruise")
    print("There are no age limits for this ride")
```

- We first print out our Menu, using a triple-delimited string so we can
  multiline it
- Then we implement the menu using a series of `if` statements.
  - For the first case (Scenci River Cruise) we don’t need the user’s
    age so we can output the result immediately
- For other rides the user needs to supply their age, so we continue,

``` python
else:  # need to get the age of the user
    age_text = input("Please enter your age: ")
    age = int(age_text)

    if ride_number == 2:
        print("You have selected the Carnival Carousel")
        if age >= 3:
            print("You can go on the ride")
        else:
            print("Sorry, you are too young")
    if ride_number == 3:
        print("You have selected Jungle Adventure Water Splash")
        if age >= 6:
            print("You can go on the ride")
        else:
            print("Sorry, you are too young")
```

- We have to get the age using another input pair
- We then use nested `if` statements, with each case checking against
  the ride’s age restriction

> [!TIP]
>
> You may have noticed that the above statement appears to have a bunch
> of duplicated code. The rough structure is,
>
> ``` text
> select ride
> if age of user is greater than or equal to the rides min age
>     Inform the user they can go on the ride
> else:
>     Inform the user they cannot go on the ride
> ```
>
> Programmers typically don’t like to repeat themselves as it increases
> the number of ways a program can go wrong. So ideally we would like a
> way were we could write something like the above *once* and have the
> appropriate checks be carried out, and the message printed without
> having to write it out for every case. We’ll look at some ways to do
> this later in the book.

## Summary

## Questions and Answers
