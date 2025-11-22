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
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

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
        Cell In[143], line 1
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

</div>

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

    The hour is: 15

*Run the program, it should print out the current hour*

##### Exercise: Improved Clock

*Improve the previous
[example](./Chapter_05.qmd#example-one-handed-clock) to produce a more
fully featured clock that reports the time, and date when run*

We can use the table above to grab
the correct attributes. We then simply need to format the attribute as
nessecary. The final
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
    The time is 15 : 38 : 49

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

## Summary

## Questions and Answers
