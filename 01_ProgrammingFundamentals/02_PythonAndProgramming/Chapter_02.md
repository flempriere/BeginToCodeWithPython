# Chapter 2: Python and Programming

- [Notes](#notes)
  - [What makes a Programmer?](#what-makes-a-programmer)
    - [Programming and Problems](#programming-and-problems)
    - [Programmers and People](#programmers-and-people)
  - [Computers as Data Processors](#computers-as-data-processors)
    - [Machines, Computers and Us](#machines-computers-and-us)
    - [Programs as Data Processors](#programs-as-data-processors)
    - [Python as a Data Processor](#python-as-a-data-processor)
      - [Example: Playing with the
        Shell](#example-playing-with-the-shell)
      - [Exercise: Python Expressions](#exercise-python-expressions)
    - [Python as a Scripting Language](#python-as-a-scripting-language)
  - [Data and Information](#data-and-information)
    - [Data Processing in Python](#data-processing-in-python)
      - [Example: Work with Text in
        Python](#example-work-with-text-in-python)
      - [Exercise: Break the rules with
        Python](#exercise-break-the-rules-with-python)
    - [Text and Numbers as Data Types](#text-and-numbers-as-data-types)
  - [Working with Python Functions](#working-with-python-functions)
    - [The `ord` function](#the-ord-function)
      - [Example: Investigate Text Representation using
        `ord`](#example-investigate-text-representation-using-ord)
    - [The `chr` function](#the-chr-function)
      - [Example: Convert Numbers to text using
        `chr`](#example-convert-numbers-to-text-using-chr)
    - [Investigate data storage using
      `bin`](#investigate-data-storage-using-bin)
      - [Exercise: Discover Binary
        Representation](#exercise-discover-binary-representation)
- [Summary](#summary)
- [Question and Answers](#question-and-answers)

## Notes

### What makes a Programmer?

- The ability to solve a program yourself
- Convert that solution into something the computer understands

#### Programming and Problems

- Programming is problem solving
- A key part of programming is properly defining the problem and scope
  - In real projects this may take the form of a *functional design
    specification*
- A well defined problem is easy to reason about

> [!TIP]
>
> **Specifications must always exist**
>
> One should never write a program without getting a solid specification
> first. Defining a specification is essential even(or perhaps
> especially) when I do a job for a friend

- Modern design techniques emphasise *prototyping*
  - The use of successive versions to solicit customer feedback

#### Programmers and People

- The best programmers are also good communicators
- Effective communication extends to writing
  - Helps write code that more clearly articulates your point

> [!TIP]
>
> **Communication leads to the most interesting work**
>
> Interesting tasks go to developers who are good communicators. They
> can articulate their ideas and liase with customers

### Computers as Data Processors

#### Machines, Computers and Us

- Computers automate instructions
  - They follow given instructions
  - Convert input data into output data
- Computers are typically unware of the veracity of their data
  - No inate ability to question, or *error recover*

``` mermaid
block-beta
    columns 3
    space
    title["Examples of Typical Data-Processing Applications"]
    space

    block:Input
    columns 1
        Inputs
        radio["Radio Signals and Touchpad"]
        car["Temperature, Pressures, Throttle"]
        game["Gamepad"]
    end

    block:Middle
    columns 1
        space
        phone["Mobile Phone"]
        carMiddle["Car"]
        console["Console"]
    end

    block:Output
    columns 1
        Outputs
        phoneOut["Sound, Pictures"]
        carOut["Fuel Injector, Ignition timings"]
        consoleOut["Gameplay"]
    end

    radio-->phone
    phone-->phoneOut
    car-->carMiddle
    carMiddle-->carOut
    game-->console
    console-->consoleOut

classDef BG stroke:transparent, fill:transparent
class title BG
class Inputs BG
class Outputs BG
```

> [!NOTE]
>
> **Software might be a matter of life or death**
>
> Seemingly innocent programs can have real consequences. E.g. a program
> that calculates drug dosages may be used by a doctor.
> [Therac-25](https://en.wikipedia.org/wiki/Therac-25) is the classic
> example.

#### Programs as Data Processors

``` mermaid
---
title: Computers as Data Processors
config:
  flowchart:
    htmlLabels: false
---
flowchart LR

input(("Input"))
computer["Computer"]
output(("Output"))

input-->computer
computer-->output
```

- As discussed computers can be seen as data transformers
- We can view this as similar to following a recipe

``` mermaid
---
title: Recipes as Programs
config:
  flowchart:
    htmlLabels: false
---
flowchart LR

flour(("Flour"))
sugar(("Sugar"))
milk(("Milk"))
eggs(("Eggs"))

human["Human following
     recipe"]

cake(("Cake"))

flour-->human
sugar-->human
milk-->human
eggs-->human

human-->cake
```

#### Python as a Data Processor

- Python is effectively one of the ways we can make a computer do things

``` mermaid
---
title: Python as a Data Processor
config:
  flowchart:
    htmlLabels: false
---
flowchart LR

input(("Python
        Commands"))
computer["Python Command Shell"]
output(("Results"))

input-->computer
computer-->output
```

- Commands are the *input* which are processed by the
  `python command shell` (*the computer*) and turned into results
  (*output*)

##### Example: Playing with the Shell

- *Start up a python interpreter and run the following*
  1. `hello`

      ``` python
      hello
      ```

          NameError: name 'hello' is not defined
          ---------------------------------------------------------------------------
          NameError                                 Traceback (most recent call last)
          Cell In[1], line 1
          ----> 1 hello

          NameError: name 'hello' is not defined

      - *The interpreter doesn’t recognise the arbitrary word* `hello`
        *and produces an error message*

  2. `2` - `2`

      ``` python
      2
      ```

          2

      - *The interpreter echoes a number back out!*

  3. `2 + 2`

      ``` python
      2 + 2
      ```

          4

  - *The interpreter **evaluates** and **echoes** out the arithmetic!*
- `2 + 2` in the previous example is a representation of an *expression*
- Python can be seen as an *expression* evaluator. An expression
  consists of *operators* that act on *operands* to produce new output
- We can break down the `2+2` example from the previous example to

``` mermaid
block-beta
    columns 3
    space
    title["Breakdown of a Simple Expression"]
    space

    block:Input
    columns 1
        operand1["2"]
        operand1Word["Operand"]
        operand1descr["(thing to work on)"]
    end

    block:Middle
    columns 1
        operator["+"]
        operatorWord["Operator"]
        operatorDescr["(thing to do)"]
    end

    block:Output
    columns 1
        operand2["2"]
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

> [!WARNING]
>
> As seen in the previous example, when invalid code is entered into the
> shell, an error message occurs. The same happens for an incomplete
> expression. e.g. the following is a shell sequence,
>
> ``` python
> 2+
> ```
>
>     SyntaxError: invalid syntax (4209523232.py, line 1)
>       Cell In[4], line 1
>         2+
>           ^
>     SyntaxError: invalid syntax

##### Exercise: Python Expressions

1. *What do you think would happen if you tried to evaluate `2+3*4`?*

We would expect `14` from the basic mathematical order of operations.
Plugging this into the shell,

``` python
2 + 3 * 4
```

    14

2.  *What do you think would happen if you tried to evaluate `(2+3)*4`?*

We would expect `20` from the basic mathematical order of operations.
Plugging this into the shell,

``` python
(2 + 3) * 4
```

    20

3.  *What do you think would happen if you tried to evaluate `(2+3*4`?*

We might expect a syntax error, instead the interpreter, simply goes to
a new line, and waits for us to enter the matching parenthesis. One such
sequence in the shell might be,

``` python
(2 + 3 * 4
)
```

    14

These notes use a slightly different version of a python interpreter
called a [Jupyter Notebook](https://jupyter.org/) to render the inline
code. In Jupyter Notebooks code is written in cells and executed cell-by
cell. This means that the interpreter can’t *wait* for the user to
provide the missing input, so instead we get the slightly different
error message below,

``` python
(2 + 3 * 4
```

    SyntaxError: incomplete input (4019191811.py, line 1)
      Cell In[8], line 1
        (2 + 3 * 4
                  ^
    SyntaxError: incomplete input

4.  *What do you think would happen if you tried to evaluate `)2+3*4`?*

If we see a right parenthesis before a left parenthesis there is no way
to retroactively go back and fix the missing left, like in the previous
case where the shell simply waited for us to add the parenthesis. So
here we would expect a syntax error.

``` python
)2+3*4
```

    SyntaxError: unmatched ')' (1306523100.py, line 1)
      Cell In[9], line 1
        )2+3*4
        ^
    SyntaxError: unmatched ')'

#### Python as a Scripting Language

- We can use the interpreter like this to work line by line because
  python is a “scripting” language
  - i.e. The program reads a line and then *interprets* the output

> [!NOTE]
>
> **Not all languages are scripting languages**
>
> Not all languages are scripting languages. Some are converted to
> low-level hardware instructions. This is called *compilation*, and in
> place of an interpreter it requires a *compiler* to convert the code.
> Compiled programs are typically faster, since they can be *optimised*

### Data and Information

- Computers fundamentally represent data as $0$ or $1$ in binary
  - We build up layers of abstract that let us handle concepts like
    *numbers*, *characters* and *strings* of text
- **Data** can be regarded as the *stored values* representing
  *information*
- **Information** is thus the interpretation of data, to mean
  *something*

#### Data Processing in Python

- Python scripts thus can be considered data processors
  - The script is interpreted and converted to output

##### Example: Work with Text in Python

*Start up the python interpreter and run the following*

1. `'hello'`

    ``` python
     'hello'
    ```

        'hello'

    - Like before with $2$ the word is echoed.

2. \`‘hello’ + ’ world’

    ``` python
     'hello' + 'world'
    ```

        'helloworld'

    - “Adding” two words performs a string concatenation
    - Observe we explicitly have to include the space character in one
      of the strings
    - A cool observation is that `+` changes it’s behaviour in response
      to what it’s arguments are

##### Exercise: Break the rules with Python

1. *What do you think would happen if missed the closing quote of a
    string you were typing?*

    - We would expect it, to either hang waiting for the closing quote
      like with the missing left parenthesis, or a syntax error like a
      right quote. We find,

    ``` python
    'hello
    ```

        SyntaxError: unterminated string literal (detected at line 1) (628875690.py, line 1)
          Cell In[12], line 1
            'hello
            ^
        SyntaxError: unterminated string literal (detected at line 1)

    - EOL stands for “End of Line”
    - Operands like strings and numbers can’t span multiple lines
    - A string literal is just a string there in the code

2. *What do you think would happen if you tried to subtract one string
    from another?*

    - While addition of strings can be easily seen as concatenation,
      there is no meaningful equivalent for substraction.
    - We could think of it as substring removal, but that has a lot of
      nuance that is hard to capture in a single symbol. We expect an
      error.

    ``` python
     'hello' - ' world'
    ```

        TypeError: unsupported operand type(s) for -: 'str' and 'str'
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[13], line 1
        ----> 1 'hello' - ' world'

        TypeError: unsupported operand type(s) for -: 'str' and 'str'

    - TypeError: unsupported operand type(s) for -: ‘str’ and ‘str’
    - The error message is somewhat obtuse but simply means that for the
      operand (-) we can’t subtract a string from another string

3. *What do you think would happen if you tried to add a number to a
    string?*

    - This one can vary. There a two valid interpretations,
      - You can’t add a number to a word
      - Treat the number as word, and concatenate it
    - Most languages, use the former choice and so we make the
      assumption that python does too

    ``` python
     'hello' + 2
    ```

        TypeError: can only concatenate str (not "int") to str
        ---------------------------------------------------------------------------
        TypeError                                 Traceback (most recent call last)
        Cell In[14], line 1
        ----> 1 'hello' + 2

        TypeError: can only concatenate str (not "int") to str

    - The result is as expected, the error tells we can only concatenate
      a string to another string

4. What do you think would happen if you tried to multiply a string by
    a number?

    - Again there are two interpretations,
      - You can’t multiply a word by a number
      - You can consider `word * 3` as adding word three lots of `word`,
        where adding is string concatenation
    - Lets see what choice python uses,

    ``` python
     'hello' * 3
    ```

        'hellohellohello'

    - The moral? Python tries to do something sensible when it can

#### Text and Numbers as Data Types

- Python seperates numerical data (e.g. `2`) from text data (e.g. `'2'`)
  - Numerics and text are stored differently
- Behaviour of operators depends on the data types fed into them as
  operands

### Working with Python Functions

- A *function* is behaviour with a distinct name
  - e.g. “Move left” is name for a distinct behaviour
- Python comes bundled with a number of *built-in* functions

> [!IMPORTANT]
>
> **Functions are a critical part of programming languages**
>
> Learning a new language often involves learning the functions it
> natively supports.

#### The `ord` function

- `ord` is a short name for *ordinal value*
  - Built-in function, mean’s *“give me the number representing this
    character”*

  - Let’s examine the use,

    ``` python
    ord('W')
    ```

        87

##### Example: Investigate Text Representation using `ord`

*Start up a python interpreter, and run the following,*

1. `ord('W')`

    ``` python
     ord('W')
    ```

        87

    - *This matches our first example*

2. `ord(W)`

    ``` python
     ord(W)
    ```

        NameError: name 'W' is not defined
        ---------------------------------------------------------------------------
        NameError                                 Traceback (most recent call last)
        Cell In[18], line 1
        ----> 1 ord(W)

        NameError: name 'W' is not defined

    - *Here we get an error*
    - `ord` *is quite pedantic, requiring it’s argument to be a single
      character string*

- Observe a function is called with the structure (using `ord` as an
  example),

``` mermaid
block-beta
    columns 4
    space
    title["Function Call Structure"]:2
    space

    block:name
    columns 1
        ord["ord"]
        functionName["function name"]
        fndescr["(thing we want done)"]
    end

    block:leftParenthesis
    columns 1
        leftP["("]
        leftPname["Parenthesis"]
        space
    end

    block:argumentblock
    columns 1
        argument["'W'"]
        argumentName["argument"]
        argumentDescr["(thing to give function)"]
    end

    block:rightParenthesis
    columns 1
        rightP[")"]
        rightPname["Parenthesis"]
        space
    end


classDef BG stroke:transparent, fill:transparent
class title BG
class ord BG
class functionName BG
class fndescr BG
class leftP BG
class leftPname BG
class argument BG
class argumentName BG
class argumentDescr BG
class rightP BG
class rightPname BG
```

#### The `chr` function

- The `chr` function is the counterpart to `ord`
  - Converts numbers to text

  ``` python
    chr(87)
  ```

      'W'

##### Example: Convert Numbers to text using `chr`

*Start up a python interpreter, and run the following,*

1. `chr(87)`

    ``` python
     chr(87)
    ```

        'W'

    - *Exactly what we saw before, and what we would expect from* `ord`

2. `chr(88)`

    ``` python
     chr(88)
    ```

        'X'

    - *Observe that there is some logical progression.*
    - *X comes after W in the alphabet, and does so in numerical
      representation*

- International standards govern text representation
  - However, older languages, software or hardware that predates these
    standards may not follow them

#### Investigate data storage using `bin`

- As mentioned before, computers store data in binary
- Each $0$ or $1$ is called a *bit*, a byte is typically a collection of
  $8$ bits, and the smallest addressable unit of memory
- Bytes can be grouped together to represent larger blocks of data
- `bin` converts a number to a string containing it’s binary
  representation

``` python
bin(87)
```

    '0b1010111'

- The prefix `0b` indicates that the remaining suffix is the binary
  representation of a number

##### Exercise: Discover Binary Representation

*Answer the following questions about binary representations*

1. *What does the binary value of* $0$ *look like?*
    - Would expect this to also be $0$

    ``` python
     bin(0)
    ```

        '0b0'
2. *What does the binary value of* $1$ *look like?*
    - Would also expect this to be $1$

    ``` python
     bin(1)
    ```

        '0b1'
3. *What does the binary value of* $2$ *look like?*
    - In binary, digits are in columns of powers of $2$ i.e. $1$ like
      before is viewed as $1 \times 2^{0}$
    - $2$ can be viewed as $1 \times 2^{1} + 0 \times 2^{0}$, so we
      would expect the representation to be $10$

    ``` python
     bin(2)
    ```

        '0b10'
4. *What do you think the binary value of* $11$ *means?*
    - If we consider the above discussion, we expect this to be decimal
      $3$

    ``` python
     3
    ```

        3
5. *How does the binary value* $86$ *differ from the binary value of*
    $87$*?*
    - Lets look at `87` first.

    ``` python
     bin(87)
    ```

        '0b1010111'

    - $86$ differs by one, so we would expect $86$ to be $1010110$

    ``` python
     bin(86)
    ```

        '0b1010110'

## Summary

- Computers view data as binary
- Computers process input data into output data
- Humans intepret data as *information*
- Computers do not naturally understand meaningful or nonsense input or
  output
- A program is the process of telling a computer how to convert input
  data into output data
  - Programming languages are a way to write these programs that the
    computer understands
- Python is one such language
  - It can also be viewed as a program that takes language statements,
    and then converts them to orders for the computer to carry out
- Programmers create sequences of instructions to describe the task a
  computer needs to carry out
  - Good code means knowing what the code needs to do
  - Formal requirements solicitation and communication skills are key
    for programmers

## Question and Answers

1. *Would a computer “know” that its stupid for someone to have an age
    of* $-20$*?*
    - No. As far as the computer is concerned, the age valueis just a
      pattern of bits that represents a number. If we want a computer to
      reject negative ages, we must actually build that understanding
      into the program
2. *If the output from a program is settings for the fuel-injection
    system on a car, is the output data or information?*
    - As soon as something starts acting on data, it becomes
      information. A human being is not doing anything with these
      values, but they will cause the speed of the engine to change,
      which might affect humans, so this makes the output information
      rather than data by the authors opinion
3. *Is the computer stupid because it can’t understand English?*
    - No, english can be a quite ambiguous languge. The legal profession
      is an example of somewhere were debate over the semantics of
      language is tricky
4. *If I don’t know how to solve a problem, can I write a program to do
    it?*
    - No, you need to understand the solution before you can write it
      and make sure that it does exactly what you want it to do
5. *Is it sensible to assume the customer measures everything in
    inches?*
    - It’s never sensible to assume anything about a project. Every
      assumption increases the chance of a potential disaster
6. *If the program does the wrong thing, is it my fault or the
    customer’s fault?*

| **Specification?** | **Program?** | **Whose Fault?** |
|--------------------|--------------|------------------|
| Right              | Wrong        | Programmer       |
| Wrong              | Right        | Customer         |
| Wrong              | Wrong        | Everyone         |
