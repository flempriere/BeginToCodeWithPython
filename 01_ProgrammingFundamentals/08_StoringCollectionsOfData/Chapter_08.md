# Chapter 8: Storing Collections of Data

- [Notes](#notes)
  - [Lists and Tracking Sales](#lists-and-tracking-sales)
    - [Limitations of Individual
      Variables](#limitations-of-individual-variables)
    - [Lists in Python](#lists-in-python)
      - [Example: Creating a List](#example-creating-a-list)
    - [Read in a List](#read-in-a-list)
      - [Example: Investigate a List Reading
        Loop](#example-investigate-a-list-reading-loop)
    - [Display a `list` using a `for`
      Loop](#display-a-list-using-a-for-loop)
      - [Exercise: Read the Names of Guests for a
        Party](#exercise-read-the-names-of-guests-for-a-party)
  - [Refactor Programs into
    Functions](#refactor-programs-into-functions)
    - [Example: Functions in the Sales Analysis
      Program](#example-functions-in-the-sales-analysis-program)
    - [Create Placeholder Functions](#create-placeholder-functions)
    - [Create a User Menu](#create-a-user-menu)
      - [Use the `elif` keyword to simplify
        conditions](#use-the-elif-keyword-to-simplify-conditions)
  - [Sort Using Bubble Sort](#sort-using-bubble-sort)
    - [Initialise a list with Test
      Data](#initialise-a-list-with-test-data)
    - [Sort a List from High to Low](#sort-a-list-from-high-to-low)
      - [Example: Work through a List using a
        Loop](#example-work-through-a-list-using-a-loop)
      - [Example: Improving Performance](#example-improving-performance)
      - [Exercise: Sort Alphabetically](#exercise-sort-alphabetically)
    - [Sort a List from Low to High](#sort-a-list-from-low-to-high)
    - [Find the Highest and Lowest Sales
      Values](#find-the-highest-and-lowest-sales-values)
    - [Evaluates Total and Average
      Sales](#evaluates-total-and-average-sales)
    - [Complete the Program](#complete-the-program)
  - [Store Data in a File](#store-data-in-a-file)
    - [Write into a File](#write-into-a-file)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### Lists and Tracking Sales

- Consider the following vignette
- The owner of an ice-cream stand wants a program to track sales
  - There are ten stands, each selling multiple items
  - The program should take sales data as input and then provide the
    following views on the data
    - Sorted from lowest to highest
    - Sorted from highest to lowest
    - Show just the highest and the lowest
    - Show the total number of sales
    - Show the average number of sales

> [!IMPORTANT]
>
> **Getting the specification right: Storyboarding**
>
> Agreeing on the specification with your client is important. A
> technique is called storyboarding, best done by sitting down with a
> paper and pen (or a whiteboard)
>
> A storyboard shows how the program should flow in response to various
> user inputs. E.g. depicting the menus the user might use, with a
> storyboard for each menu choice. The storyboard should also show how
> the program will work
>
> For bigger programs you can break different components out into their
> own storyboards, much in the same way we built up functions.
> Storyboards depict what needs to happen, but not how to do it.

- Given the spec for the ice cream stand we can now outline the program

  1. Store the sales data in variables
  2. Implement a way to sort the data
  3. A way to print the output
  4. Store the data globally and pass it to functions to handle the
      work

- We can construct the prototype interface, similar to the [Ride
  Selector
  Program](../05_MakingDecisions/Chapter_05.qmd#use-decisions-to-make-an-application)

  ``` shell
    Ice-Cream Sales

    1: Print the Sales
    2: Sort Low to High
    3: Sort High to Low
    4: Highest and Lowest
    5: Total Sales
    6: Average Sales
    7: Enter Figures

    Enter your command: 3
  ```

#### Limitations of Individual Variables

- We first need to store the sales
  - For ten stores, we could theoretically use ten variables, one for
    each store

  - But this method becomes clunky when we want to start analysing the
    variables

  - E.g. the following code
    ([FindingLargestSales.py](./Examples/01_FindingLargestSales/FindingLargestSales.py)),
    only handles finding if the first stand is the one with the greatest
    sales

    ``` python
      # Example 8.1 Finding the Largest Sales
      #
      # Checks if sales1 has the largest sales. Demonstrates the difficulty of using
      # individual named variables to deal with aggregate data

      import BTCInput

      sales1 = BTCInput.read_int("Enter the sales for stand 1: ")
      sales2 = BTCInput.read_int("Enter the sales for stand 2: ")
      sales3 = BTCInput.read_int("Enter the sales for stand 3: ")
      sales4 = BTCInput.read_int("Enter the sales for stand 4: ")
      sales5 = BTCInput.read_int("Enter the sales for stand 5: ")
      sales6 = BTCInput.read_int("Enter the sales for stand 6: ")
      sales7 = BTCInput.read_int("Enter the sales for stand 7: ")
      sales8 = BTCInput.read_int("Enter the sales for stand 8: ")
      sales9 = BTCInput.read_int("Enter the sales for stand 9: ")
      sales10 = BTCInput.read_int("Enter the sales for stand 10: ")

      if (
          sales1 > sales2
          and sales1 > sales3
          and sales1 > sales4
          and sales1 > sales5
          and sales1 > sales6
          and sales1 > sales7
          and sales1 > sales8
          and sales1 > sales9
          and sales1 > sales10
      ):
          print("Stand 1 had the best sales")
    ```

  - Problem: We would have to repeat the code each time for each
    individual sales variable

  - If we add more stands, we have add another named variable and
    another big `if` statement

    - **AND** modify all the previous `if` statements
- Clearly this approach is not very maintainable

#### Lists in Python

- A collection is a *composite* type
  - It stores multiple elements of another type
- We’ve already (briefly) seen one type of collection the *tuple*
- The most common form of collection is the `list`
  - What it sounds like, a list of items

##### Example: Creating a List

*Open a python interpreter and work through the following steps to learn
about* `list`

1. *A list is created using brackets around the contents* `[]`*, e.g.*

    ``` python
     sales = []
    ```

    - *The above defines* `sales` *as an empty list*

2. *Items can be appended to a* `list` *using the* `append` *function*

    ``` python
     sales.append(99)
     sales
    ```

        [99]

    - *As we can see from above* `sales` *now contains the value* `99`

3. *Calling append again, adds the new item to the end of the list*

    ``` python
     sales.append(100)
     sales
    ```

        [99, 100]

4. *Observe from above you can see the contents of a list, by simply
    typing the variable name in the interpreter*

    - *In scripts we can also use the explicit* `print` *call*

      ``` python
        print(sales)
      ```

          [99, 100]

5. *You can access individual items of the list, using the **indexing**
    operator* `[]`

    ``` python
     sales[0]
    ```

        99

    - *Syntax is* `list_name[index]` *where* `index` *is an integer
      giving the index of the item*
    - *Python lists are zero-indexed. i.e. the first value is stored at
      index* $0$

6. *The indexing operator can be used to change the value of an item at
    a given index*

    ``` python
     sales[1] = 101
     sales
    ```

        [99, 101]

    - *The above changes the value of the second item in* `sales` *to*
      $101$

- **Note:** *Whenever we use the indexing operator the index must exist!
  For example if we tried to view the (non-existent) third item, we
  would get an error*

  ``` python
    sales[2]
  ```

      IndexError: list index out of range
      ---------------------------------------------------------------------------
      IndexError                                Traceback (most recent call last)
      Cell In[23], line 1
      ----> 1 sales[2]

      IndexError: list index out of range

  - *Observe the error type is an* `IndexError`
  - *Thus something we can catch and handle*

1. *A single list can store values of different types, and can replace
    items with new items of a different type*

    ``` python
     sales.append("Rob")
     sales[0] = "Python"
     sales
    ```

        ['Python', 101, 'Rob']

    - *The above appends a new string* `"Rob"`*, converts* `sales[0]`
      *from an int to the string* `"Python"` *and leaves the number*
      $101$ *in* `sales[1]` *untouched*
    - *Overall list thus mixes string and integer types*

> [!WARNING]
>
> **Avoid Mixing Types in Lists**
>
> *Just because you **can** mix types in lists, doesn’t mean you
> **should.** Typically lists and list processing is much easier when a
> list stores all items of the same type*

#### Read in a List

- You can use loops to populate a list (see
  [ReadAndDisplay.py](./Examples/02_ReadAndDisplay/ReadAndDisplay.py))

  ``` python
    # Example 8.2.1 Read and Display
    #
    # Demonstrates using a loop to populate a list

    import BTCInput

    # create an empty list to populate
    sales = []

    for count in range(1, 11):
        prompt = "Enter the sales for stand " + str(count) + ": "
        sales.append(BTCInput.read_int(prompt))

    print(sales)
  ```

##### Example: Investigate a List Reading Loop

*Examine the code given above and consider the following questions to
understand how the list is processed*

1. *What is the purpose of the* `count` *variable?*
    - `count` *tracks the value of the current index in the loop. This
      is used to print the id for the sales stand we are collecting the
      data from*
2. *Why does the range of* `count` *go from* $1$ *to* $11$*?*
    - *The* `range` *function returns a collection with the start
      included but the stop excluded. Since we have stores* $1$
      *through* $10$*, we want the range to go from* $1$ *to* $11$ *so
      the generated numbers are* $1$ *through to* $10$
3. *Which item in the list would hold the sales for stand number*
    $1$*?*
    - *The first item in the list, or the zeroth indexed, i.e.*
      `sales[0]`
4. *What part of the code would have to be changed if we instead had*
    $100$ *stands?*
    - *We simply change* `range(1,11)` *through to* `range(1,101)`

    - *The program below
      ([ReadAndDisplay2.py](./Examples/02_ReadAndDisplay/ReadAndDisplay2.py))
      is a variant in which the user specifies the number of stands*

      ``` python
        # Example 8.2.2 Read and Display 2
        #
        # Improved version of Read and Display which allows the user to specify
        # the number of stands

        import BTCInput

        # create an empty list to populate
        sales = []

        number_of_stands = BTCInput.read_int("Enter the number of stands: ")
        for count in range(1, number_of_stands + 1):
            prompt = "Enter the sales for stand " + str(count) + ": "
            sales.append(BTCInput.read_int(prompt))

        print(sales)
      ```

    - *The above is more flexible, but as a result it is more
      complicated, the trade off between flexibility and ease of use is
      one that should be considered with the input of the users*
5. *If I got one sales value wrong, would it be possible to edit the
    list to put in a corrected version?*
    - *This is not implemented in the current program, but we have
      already seen that you can reassign the value of list at a given
      index, so we could implement this in a more complete program*

#### Display a `list` using a `for` Loop

- We’ve already seen that `print` has a default way of displaying a list

- We can use a `for` loop for if we want custom printing for each item

  ``` python
    # Example 8.3 Read and Display Loop
    #
    # Uses a for loop to provide custom list printing

    import BTCInput

    sales = []

    for count in range(1, 11):
        prompt = "Enter the sales for stand " + str(count) + ": "
        sales.append(BTCInput.read_int(prompt))

    # print a heading
    print("Sales Figures")
    count = 1
    for sales_value in sales:
        print("Sales for stand", count, "are", sales_value)
        count = count + 1
  ```

##### Exercise: Read the Names of Guests for a Party

*Lists can hold any type of data that you need to store, including
strings. You can change the ice-cream sales program to read and store
the names of guests for a party or an event you’re planning. Make a
modified version of the sales program that reads in some guest names and
then displays them. Make your program handle between* $5$ *and* $15$
*guests*

- We basically just copy the previous program with the following changes
  - `sales` $\rightarrow$ `guests`
  - `sales_value` $\rightarrow$ `guest`
  - We change the prompts to appropriately refer to guests rather than
    sales
- The two main changes are
  1. We add an initial prompt for the number of guests
      - We use `BTCInput.read_int_ranged` to ensure the value is from
        $5$ to $15$
  2. We use `BTCInput.read_text` instead of `BTCInput.read_int` to get
      the guest names

``` python
    # Exercise 8.1 Party Guests
    #
    # A program that receives and then prints a list of party guests
    # Works for between 5 and 15 guests

    import BTCInput

    guests = []
    number_of_guests = BTCInput.read_int_ranged(
        "Enter the number of guests (5-15): ", 5, 15
    )

    for count in range(1, number_of_guests + 1):
        prompt = "Enter the name of guest " + str(count) + ": "
        guests.append(BTCInput.read_text(prompt))

    # print a heading
    print("\nGuests attending:")
    count = 1
    for guest in guests:
        print("- ", guest)
        count = count + 1
```

### Refactor Programs into Functions

- The previous examples build up our program as one long chain of events

  - There are two distinct responsibilities occuring
    1. First we *read* in the data
    2. Second we *display* the data
  - These are natural candidates to be converted into functions

- The program locks us into one way of processing data

  - What happens if we want to read in a second set of data?
  - What if we want to print the data multiple times?

- *Refactoring* is the process of modifying existing code

  - Specifically changing how *factors* interact

- *Refactoring* avoids the problem of overcomplicating the design at the
  start of the process

  - Instead we write the program the most simple way we can
  - Then once a structure emerges, or we need to add functionality we
    can *refactor* the design

- Let us factor out the two key components identified above into a new
  implementation ([Functions.py](./Examples/04_Functions/Functions.py))

  ``` python
    # Example 8.4 Functions
    #
    # Demonstrates refactoring a program into component functions

    import BTCInput

    sales = []


    def read_sales(number_of_sales):
        """
        Reads in the sales values and stores them in the sales list

        Parameters
        ----------
        number_of_sales : int
            Number of Stores to record sales values for

        Returns
        -------
        None
            Results are read into the sales list
        """
        sales.clear()  # remove existing sales values
        for count in range(1, number_of_sales + 1):
            prompt = "Enter the sales for stand " + str(count) + ": "
            sales.append(BTCInput.read_int(prompt))


    def print_sales():
        """
        Prints the sales figures on the screen with a heading. Each figure is
        numbered in sequence
        """
        print("Sales Figures")
        count = 1
        for sales_value in sales:
            print("Sales for stand", count, "are", sales_value)
            count = count + 1


    read_sales(10)
    print_sales()
  ```

#### Example: Functions in the Sales Analysis Program

*Our sales analysis program now consists of two functions,* `read_sales`
*and* `print_sales`

1. *What does the parameter for the* `read_sales` *function do?*
    - *We hinted at in the previous section that we might want to
      account for the potential for the number of stands to change in a
      future implementation. To support this behaviour* `read_sales`
      *reads in the number of sales value that it should reads*
2. *What does* `clear` *do?*
    - *We want to start with a fresh list every time we read the sales
      values.* `clear` *is a method on* `list` *that clears its
      contents*
3. *Why don’t we need to tell the* `print_sales` *function how many
    sales figures to print?*
    - *The* `for` *loop goes through the contents of the* `sales` *list.
      Which tracks its own size. In some languages like C, containers do
      not naturally track their sizes and we would need to specify them*
4. *Why didn’t we have to write* `global sales` *in the* `read_sales`
    *function?*
    - *Python variable names are references to memory*
    - *These are distinct from the **objects** that live in that memory*
    - *Assignments change what object a reference (variable) refers to*
      - e.g. `sales=[]`
    - *However, calling methods on a variable, is not changing the
      reference e.g.* `sales.append(99)` *(They change the object
      contents)*
      - *So we don’t need to use global because by calling methods its
        clear what reference we’re using*

#### Create Placeholder Functions

- A development technique called *stubs* is where we write placeholder
  functions before we can provide a complete implementation for a given
  behaviour
- The placeholders are sometimes called *stub* functions e.g. the two
  below

``` python
def sort_high_to_low():
    """
    Print out a sales list from highest to lowest
    """
    pass

def sort_low_to_high():
    """
    Print out a sales list from lowest to highest
    """
    pass
```

- Placeholders let us model the flow of program before we have all the
  behaviours specified
  - Obviously does not model the complete program since the functions
    are incomplete
- `pass` is a keyword for a statement that does nothing
  - It is effectively a placeholder statement

#### Create a User Menu

- At the start of the Chapter we defined a user interface
  - By using the previous discussion on stubbing, and our initial
    functions we can implement this menu (see the full implementation in
    [FunctionsAndMenu.py](./Examples/05_FunctionsAndMenu/FunctionsAndMenu.py))

  ``` python
    menu = """
    Ice Cream Sales

    1. Print the Sales
    2. Sort High to Low
    3. Sort Low to High
    4. Highest and Lowest
    5. Total Sales
    6. Average Sales
    7. Enter Figures

    Enter your command: """

    command = BTCInput.read_int_ranged(menu, 1, 7)

    if command == 1:
        print_sales()
    elif command == 2:
        sort_high_to_low()
    elif command == 3:
        sort_low_to_high()
    elif command == 4:
        highest_and_lowest()
    elif command == 5:
        total_sales()
    elif command == 6:
        average_sales()
    elif command == 7:
        read_sales(10)
    else:
        raise ValueError("Unexpected value " + str(command) + " found")
  ```

- We use stub functions for the unimplemented behaviour
- **Note** The `else` condition should never trip, because of the
  behaviour in `read_int_ranged`
  - However we add it as the `else` clause so that if for some reason
    someone accidently edits the code, or if `read_int_ranged` was some
    upstream dependency we can’t control and the behaviour breaks we can
    catch any unexpected input

##### Use the `elif` keyword to simplify conditions

- In many of the examples and exercises I’ve used `elif` to simplify
  cases where we would otherwise have a bunch of nested `if...else`
  conditions.
- `elif` is short for `else if` and is effectively a *next* condition to
  check if the first `if` (or all preceding `elif`) statement is `False`
  - All `elif` conditions must come before the `else`

### Sort Using Bubble Sort

- Sorting is a common task for computing programs
- It can be time-intensive
- There are often multiple ways that we may wish to sort things, e.g.
  - Alphabetically vs Numerically
  - Increasing vs Decreasing
  - Case-sensitive vs Case-insensitive
- Traditional sorts are down, one item (or pair of items) at a time
- Algorithms, are a sequence of steps that solve a problem
  - *Sorting Algorithms* are algorithms that sort collections
  - Programming is really the *implementation* of an algorithm
- *Bubble Sort* is a simple sorting algorithm
  - Easy to follow and understand
  - Not scalable to larger data sets

#### Initialise a list with Test Data

- Often when implementing an algorithm we want to use a fixed set of
  *test data*
  - i.e. Data for which we can easily know the desired final state or
    output
  - Allows us to check our algorithm is not incorrect
- We can define a `list` in python with some contents,

``` python
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
```

#### Sort a List from High to Low

``` mermaid
block-beta
    columns 6

    classDef BG stroke:transparent, fill:transparent

    index["Index"]:1
    class index BG

    block:Indices:5
    columns 10
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
    end

    value["Value"]:1
    class value BG

    block:Values:5
    columns 10
        50
        54_1["54"]
        29
        33
        22
        100
        45
        54_2["54"]
        89
        75
    end

```

- The above shows how the test data looks in a python list
- For a highest to lowest sort we want the largest value to be in index
  $0$ and the lowest in index $9$
- The basic idea of *Bubble sort* is to compare neighbouring values, if
  the right value is larger we want to swap them so the larger value is
  on the left
  - Thus closer to the top of the list

> [!IMPORTANT]
>
> **Swap two values in a variable**
>
> The following code to swap two variables is broken,
>
> ``` python
> if sales[0] < sales[1]:
>     # the two items are in the wrong order and must be swapped
>     sales[0] = sales[1]
>     sales[1] = sales[0]
> ```
>
> Why? Lets work through what happens
>
> 1. `sales[0]` is set to the value of `sales[1]`
> 2. `sales[1]` is set to the *current* value of `sales[0]`
> 3. *But*, `sales[0]` has already been set to `sales[1]`
>     - So `sales[1]` is set to the same value it already has
>
> The net result is that we only copy `sales[1]` to `sales[0]`
>
> The correct implementation is given below,
>
> ``` python
> if sales[0] < sales[1]:
>     temp = sales[0]
>     sales[0] = sales[1]
>     sales[1] = temp
> ```
>
> `temp` is used to store the value of `sales[0]` before it was
> overwritten

Obviously, we don’t want to write the code with explicit reference to
indices. However we can write this generically with a `for` loop as
below

``` python
for count in range(0, len(sales) - 1):
    if sales[count] < sales[count - 1]:
        temp = sales[count]
        sales[count] = sales[count + 1]
        sales[count + 1] = temp
```

##### Example: Work through a List using a Loop

*The above code uses some new python features. Work through the
following questions to understand what’s going on*

1. *Why have you used a* `for` *loop, rather than a* `while` *loop?*
    - *We could use either, the* `for` *loop is slightly smaller since
      we don’t have to manually increment* `count`*. Additionally*
      `range` *technically returns what is called a **generator**, this
      is more memory efficient, as rather than creating a full list of
      numbers in memory, it just returns the next number each time the*
      `for` *loop requests it*
2. *What does the* `len` *function do on line* $1$*?*
    - `len` *returns the length of a collection, i.e. the number of
      items in the collection. This lets you write code that is
      insensitive to the size of the collection being worked with. This
      means our sorting code could work on any length list*
3. *Why is the limit of* `count` *the length of the list minus 1?*
    - *This is because bubble sort compares the current item to the item
      to its right, i.e. at the **next** index. If the range goes to the
      last index, then program will try an access an element one past
      the end of the list which doesn’t exist. This will cause an error.
      e.g.*

    ``` python
     a_list = [1,2]
     for count in range(0, len(a_list)):
         if a_list[count] < a_list[count + 1]:
             temp = a_list[count]
             a_list[count] = a_list[count + 1]
             a_list[count + 1] = temp
    ```

        IndexError: list index out of range
        ---------------------------------------------------------------------------
        IndexError                                Traceback (most recent call last)
        Cell In[25], line 3
              1 a_list = [1,2]
              2 for count in range(0, len(a_list)):
        ----> 3     if a_list[count] < a_list[count + 1]:
              4         temp = a_list[count]
              5         a_list[count] = a_list[count + 1]

        IndexError: list index out of range

- The [complete
  implementation](./Examples/06_BubbleSortFirstPass/BubbleSortFirstPass.py)
  of the above discussion below performs *one* pass through the list

``` python
# Example 8.6 Bubble Sort First Pass
#
# Implements the first pass of bubble sort and shows the impact on the list

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def sort_high_to_low():
    """
    Print out a sales list from highest to lowest

    Returns
    -------
    None
    """

    for count in range(0, len(sales) - 1):
        if sales[count] < sales[count + 1]:
            temp = sales[count]
            sales[count] = sales[count + 1]
            sales[count + 1] = temp


print("Input list:", sales)

sort_high_to_low()

print("Output list:", sales)
```

    Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
    Output list: [54, 50, 33, 29, 100, 45, 54, 89, 75, 22]

after which the test data looks like this

``` mermaid
block-beta
    columns 6

    classDef BG stroke:transparent, fill:transparent

    index["Index"]:1
    class index BG

    block:Indices:5
    columns 10
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
    end

    value["Value"]:1
    class value BG

    block:Values:5
    columns 10
        54_1["54"]
        50
        33
        29
        100
        45
        54_2["54"]
        89
        75
        22
    end
```

- Notice that the list has been partially sorted
  - Also notice that the *smallest* value $22$ has been moved to the
    correct index (the end)
  - The high numbers effectively bubble left past *one* of the values
    smaller than them
- Since we can see that after sorting the *smallest* value has been
  moved to the end we expect on the second loop through the *second
  smallest* value will have been moved to the correct spot
  - So we want to loop through `len(sales)` times
- The working bubble sort implemention is then,

``` python
# Example 8.7 Bubble Sort Multiple Pass
#
# Implements a complete working version of bubble sort

# test data
sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


def sort_high_to_low():
    """
    Print out a sales list from highest to lowest

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(sales)):
        for count in range(0, len(sales) - 1):
            if sales[count] < sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp


print("Input list:", sales)

sort_high_to_low()

print("Output list:", sales)
```

    Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
    Output list: [100, 89, 75, 54, 54, 50, 45, 33, 29, 22]

##### Example: Improving Performance

*As seen above, the sorting program now works correctly. Once you have a
working implementation its worth investigating if there are changes you
can make to improve the efficiency. Work through the following questions
to get the idea*

1. *Is the program making more comparisons than necessary?*
    - *Yes, as we mentioned before, after one pass the smallest item
      will always be at the end of the collection*

    - *This means we don’t need to check any swaps against it any more
      for the inner loop*

    - *After each pass the size of this sorted section increases by at
      least one*

    - *An implementation taking this into account is,*

      ``` python
        for sort_pass in range(0, len(sales)):
            for count in range(0, len(sales) - 1 - sort_pass):
                if sales[count] < sales[count + 1]:
                    temp = sales[count]
                    sales[count] = sales[count + 1]
                    sales[count + 1] = temp
      ```

2. *Is the program performing more passes through the list than
    nessecary?*
    - *Probably, unless the largest value is at the end of the list all
      values should be **bubbled** to their correct spot by then*

    - *We can stop doing additional passes if we work out the list is
      already sorted*

    - *How?* we use a flag to track if any swaps occur in a pass. If
      none do then the list is already sorted and we can stop\*

      ``` python
        # Example 8.8 Efficient Bubble Sort
        #
        # A bubble sort implementation incorporating efficiency savings to the number
        # of comparisons and passes through the list

        # test data
        sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


        def sort_high_to_low():
            """
            Print out a sales list from highest to lowest

            Returns
            -------
            None
            """
            for sort_pass in range(0, len(sales)):
                done_swap = False
                for count in range(0, len(sales) - 1 - sort_pass):
                    if sales[count] < sales[count + 1]:
                        temp = sales[count]
                        sales[count] = sales[count + 1]
                        sales[count + 1] = temp
                        done_swap = True
                if not done_swap:
                    break

        print("Input list:", sales)

        sort_high_to_low()

        print("Output list:", sales)
      ```

          Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
          Output list: [100, 89, 75, 54, 54, 50, 45, 33, 29, 22]

##### Exercise: Sort Alphabetically

*Bubble sort works for strings as well as integers. We saw that in
[Chapter 5](../05_MakingDecisions/Chapter_05.qmd#comparison-operators)
the python relational operators also work for strings. See if you can
modify the [Party Guest
Program](#exercise-read-the-names-of-guests-for-a-party) to display the
names in alphabetical order*

We can basically just reuse our sort code, but renamed for the guest
program.

``` python
def sort_alphabetical():
    """
    Sorts a list alphabetically

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(guests)):
        done_swap = False
        for count in range(0, len(guests) - 1 - sort_pass):
            if guests[count] > guests[count + 1]:
                temp = guests[count]
                guests[count] = guests[count + 1]
                guests[count + 1] = temp
                done_swap = True
        if not done_swap:
            break
```

There is a second modification above, which is changing the sign of the
relational operator, e.g.

``` python
guests[count] < guests[count + 1]
```

has been changed to,

``` python
guests[count] > guests[count + 1]
```

This is because as written the program tries to put the *smallest*
strings last, but for strings where the relational operator is
alphabetically ordered this puts strings starting with *a* for example,
after those starting with *z* etc. So we need to swap the sign so that
the list is printed *a, b, … , z* etc.

Why don’t we have to make more modifications? Well the code as written
only requires that the items being sorted are stored in a collection,
and that the items in the list can be compared with a relational
operator. Both of these properties are satisfied by a collection of
strings so the code effectively works out of the box

The complete code, including the integration with reading and printing
the guest list is given in
[SortAlphabetically.py](./Exercises/02_SortAlphabetically/SortAlphabetically.py)

#### Sort a List from Low to High

- To flip the direction of the sort, we just need the condition that
  determines what is out of order or not
  - We do this by changing $<$ to $>$, i.e.

    ``` python
      # Example 8.9 Bubble Sort Low to High
      #
      # Implementation of Bubble Sort that sorts from low to high

      # test data
      sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


      def sort_low_to_high():
          """
          Print out a sales list from highest to lowest

          Returns
          -------
          None
          """
          for sort_pass in range(0, len(sales)):
              done_swap = False
              for count in range(0, len(sales) - 1 - sort_pass):
                  if sales[count] > sales[count + 1]:
                      temp = sales[count]
                      sales[count] = sales[count + 1]
                      sales[count + 1] = temp
                      done_swap = True
              if not done_swap:
                  break


      print("Input list:", sales)

      sort_low_to_high()

      print("Output list:", sales)
    ```

        Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
        Output list: [22, 29, 33, 45, 50, 54, 54, 75, 89, 100]
- The code above is given in
  [BubbleSortLowToHigh.py](./Examples/09_BubbleSortLowToHigh/BubbleSortLowToHigh.py)

#### Find the Highest and Lowest Sales Values

- In comparison to sorting, *finding* a value is much easier

- The basic outline for finding the highest is,

  ``` text
    for values in collection
        if(new value > highest seen so far)
            highest = new value
  ```

- We can write the code for the highest and lowest in python then as,

  ``` python
    highest = sales[0]
    for sales_value in sales:
        if sales_value > highest:
            highest = sales_value

    lowest = sales[0]
    for sales_value in sales:
        if sales_value < lowest:
            lowest = sales_value
  ```

- If we want to find both at the same time, then we can combine the code
  above, which means we only have to do one pass through the collection

  ``` python
    # Example 8.10 Highest and Lowest
    #
    # Function that finds the highest and lowest value in a collection

    # Example 8.9 Bubble Sort Low to High
    #
    # Implementation of Bubble Sort that sorts from low to high

    # test data
    sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


    def highest_and_lowest():
        """
        Print out the highest and lowest elements of a sales list

        Returns
        -------
        None
        """
        highest = sales[0]
        lowest = sales[0]

        for sales_value in sales:
            if sales_value > highest:
                highest = sales_value
            elif sales_value < lowest:
                lowest = sales_value
        print("The highest is:", highest)
        print("The lowest is", lowest)


    print("Input list:", sales)

    highest_and_lowest()
  ```

      Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
      The highest is: 100
      The lowest is 22

  - The code above is given in
    [HighestAndLowest.py](./Examples/10_FindHighestAndLowest/HighestAndLowest.py)

#### Evaluates Total and Average Sales

- To evaluate the total we have to sum the contents of a list, simple
  using the `for` loops we’ve looked at, (implementation in
  [TotalSales.py](./Examples/11_TotalSales/TotalSales.py))

  ``` python
    # Example 8.11 Total Sales
    #
    # Calculate the Total Sales

    # test data
    sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


    def total_sales():
        """
        Print out the total sales of a sales list

        Returns
        -------
        None
        """
        total = 0
        for sales_value in sales:
            total = total + sales_value
        print("Total sales are:", total)


    print("Input list:", sales)

    total_sales()
  ```

      Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
      Total sales are: 551

- It is a simple extra step to them calculate the average, (divide the
  total by the number of elements in the collection)

  ``` python
    # Example 8.12 Average Sales
    #
    # Calculate the Average Sales

    # test data
    sales = [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]


    def total_sales():
        """
        Print out the total sales of a sales list

        Returns
        -------
        None
        """
        total = 0
        for sales_value in sales:
            total = total + sales_value
        average_sales = total / len(sales)
        print("Average sales are:", average_sales)


    print("Input list:", sales)

    total_sales()
  ```

      Input list: [50, 54, 29, 33, 22, 100, 45, 54, 89, 75]
      Average sales are: 55.1

#### Complete the Program

- The previous Exercises have given us all the parts, now we want to put
  it together
- The crux of our program should be a loop around [the
  menu](#create-a-user-menu) through which the user selects different
  functions
- We first however need to read in the data from the user
- For useability we should add the ability to quit the program
- The [final program](./Examples/13_CompleteProgram/CompleteProgram.py)
  implements this

``` python
# Example 8.13 Complete Program
#
# A Complete implementation of the Sales Program combining all the individual
# programs that we have implemented

import BTCInput

sales = []


def read_sales(number_of_sales):
    """
    Reads in the sales values and stores them in the sales list

    Parameters
    ----------
    number_of_sales : int
        Number of Stores to record sales values for

    Returns
    -------
    None
        Results are read into the sales list
    """
    sales.clear()  # remove existing sales values
    for count in range(1, number_of_sales + 1):
        prompt = "Enter the sales for stand " + str(count) + ": "
        sales.append(BTCInput.read_int(prompt))


def print_sales():
    """
    Prints the sales figures on the screen with a heading. Each figure is
    numbered in sequence

    Returns
    -------
    None
    """
    print("Sales Figures")
    count = 1
    for sales_value in sales:
        print("Sales for stand", count, "are", sales_value)
        count = count + 1


def sort_high_to_low():
    """
    Print out a sales list from highest to lowest

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(sales)):
        done_swap = False
        for count in range(0, len(sales) - 1 - sort_pass):
            if sales[count] < sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def sort_low_to_high():
    """
    Print out a sales list from lowest to highest

    Returns
    -------
    None
    """
    for sort_pass in range(0, len(sales)):
        done_swap = False
        for count in range(0, len(sales) - 1 - sort_pass):
            if sales[count] > sales[count + 1]:
                temp = sales[count]
                sales[count] = sales[count + 1]
                sales[count + 1] = temp
                done_swap = True
        if not done_swap:
            break


def highest_and_lowest():
    """
    Print out the highest and lowest elements of a sales list

    Returns
    -------
    None
    """
    highest = sales[0]
    lowest = sales[0]

    for sales_value in sales:
        if sales_value > highest:
            highest = sales_value
        elif sales_value < lowest:
            lowest = sales_value
    print("The highest is:", highest)
    print("The lowest is", lowest)


def total_sales():
    """
    Print out the total sales of a sales list

    Returns
    -------
    None
    """
    total = 0
    for sales_value in sales:
        total = total + sales_value
    print("Total sales are:", total)


def average_sales():
    """
    Print out the average sales of a sales list

    Returns
    -------
    None
    """
    total = 0
    for sales_value in sales:
        total = total + sales_value
    average_sales = total / len(sales)
    print("Average sales are:", average_sales)


# Get initial sales list
read_sales(10)


menu = """
Ice Cream Sales

0. Quit the Program
1. Print the Sales
2. Sort High to Low
3. Sort Low to High
4. Highest and Lowest
5. Total Sales
6. Average Sales
7. Enter Figures

Enter your command: """

while True:
    command = BTCInput.read_int_ranged(menu, 0, 7)
    if command == 0:
        break
    if command == 1:
        print_sales()
    elif command == 2:
        sort_high_to_low()
    elif command == 3:
        sort_low_to_high()
    elif command == 4:
        highest_and_lowest()
    elif command == 5:
        total_sales()
    elif command == 6:
        average_sales()
    elif command == 7:
        read_sales(10)
    else:
        raise ValueError("Unexpected value " + str(command) + " found")
```

> [!WARNING]
>
> Playing around with the program you might notice one thing. The stands
> are numbered in the order that they are printed. This works great for
> printing the original list out, but once we start sorting these
> numbers don’t match their original value. This is fine if we only care
> about the sales figures, but if we want to maintain a relationship
> between a stand and its sales this is something that would have to be
> modified.
>
> This is something you would discuss with the client

### Store Data in a File

- A natural extension to the program would be the ability to read or
  store the sales data to a file

- Files allow for persisting the data between sessions

- To do this we’ll add two new options, `8. Save Sales` and
  `9. Load Sales`

- Let us start by stubbing out our functions (the complete integration
  is found in
  [LoadAndSave.py](./Examples/14_LoadAndSave/LoadAndSave.py)),

  ``` python
    def save_sales(file_path):
        """
        Saves the contents of the sales list in the file given by file_path

        Parameters
        ----------

        file_path : str
            string giving the file path to save to

        Raises
        ------
        FileException
            Raised if the save fails

        Returns
        -------
        None
        """
        print("Save the sales in:", file_path)


    def load_sales(file_path):
        """
        loads the contents of the file given by file_path into the sales list

        Parameters
        ----------

        file_path : str
            string giving the file path to load from

        Raises
        ------
        FileException
            Raised if the load fails

        Returns
        -------
        None
        """
        print("Load the sales in:", file_path)
  ```

- We also add a basic integration to the user menu, where we use
  `BTCInput.read_text` to get a file name, then call the function

  ``` python
      elif command == 7:
        read_sales(10)
    elif command == 8:
        file_to_save_to = BTCInput.read_text("Enter file to save to: ")
        save_sales(file_to_save_to)
    elif command == 9:
        file_to_load_from = BTCInput.read_text("Enter file to load: ")
        load_sales(file_to_load_from)
    else:
        raise ValueError("Unexpected value " + str(command) + " found")
  ```

#### Write into a File

- When interacting with a file, python represents it as a memory object

  - Technically representing the connection

- `open` creates a connection to a file, the below, opens a file,
  `test.txt`, in write mode `w` and stores it in the variable
  `output_file`

  ``` python
    output_file = open('test.txt', 'w')
  ```

  - The two arguments are called the `file_path` and the `mode`
    - `file_path` is the file you want to open
    - `mode` is what you want to do with it

## Summary

## Questions and Answers
