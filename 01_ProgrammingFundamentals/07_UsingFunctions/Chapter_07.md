# Chapter 7: Using Functions to Simplify Programs

- [Notes](#notes)
  - [What makes a Function?](#what-makes-a-function)
    - [Example: Investigating
      Functions](#example-investigating-functions)
    - [Exercise: Program Pathfinder](#exercise-program-pathfinder)
    - [Structure of a Function
      Definition](#structure-of-a-function-definition)
    - [Give Information to Functions using
      Parameters](#give-information-to-functions-using-parameters)
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

#### Example: Investigating Functions

*Use a python interpreter to work through the following questions to
understand python functions*

*Enter the following program into the interpreter*

``` python
def greeter():
     print("Hello")
```

1. *Why did the interpreter not print* `"Hello"`*?*

    - *Because the* `print` *statement is stored as part of the*
      `greeter` *function*

2. *How do I tell Python that I’ve finished entering the* `greeter`
    *function?*

    - *The same way you close a loop or an* `if` *statement, by
      deindenting and adding an empty line*

3. *How do I make a call to the* `greeter` *function?*

    ``` python
     greeter()
    ```

        Hello

    - *The same way you call any other function. Write the function name
      and a parenthesised list of parameters. In this case the list is
      empty. Once called the function runs all the statements contained
      in its definition.*

*Now consider the following code snippet*

``` python
x = greeter
x()
```

    Hello

*Observe that we can treat functions like variables. We can assign them
to other **labels/variables** in this case* `x` *is set to the value of*
`greeter`*. We can then call* `x` *as if it where* `greeter`

*The ability to treat functions as variables is a powerful feature we
will explore more in Chapter 12*

#### Exercise: Program Pathfinder

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

    ``` bash
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
        Cell In[42], line 4
              1 def m1():
              2     m1()
        ----> 4 m1()

        Cell In[42], line 2, in m1()
              1 def m1():
        ----> 2     m1()

        Cell In[42], line 2, in m1()
              1 def m1():
        ----> 2     m1()

            [... skipping similar frames: m1 at line 2 (2975 times)]

        Cell In[42], line 2, in m1()
              1 def m1():
        ----> 2     m1()

        RecursionError: maximum recursion depth exceeded

    - The code generates a `RecursionError`!
      - A function that calls itself is called a rescursive function
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
    *display* **a** menu
- Then parameters in a parenthese-enclosed, comma-delimited list
  - No space between name and left parenthesis
  - Parameters feed extra information for the function to work on
  - Parameter list can be empty (as we’ve seen)
- Then colon
- Followed by indented set of statements associated with the function
  - Called the *function body*

#### Give Information to Functions using Parameters

- Functions can receive data to work on through parameters

## Summary

## Questions and Answers
