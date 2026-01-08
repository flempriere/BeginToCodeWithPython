# Chapter 10: Using Classes to Create Active Objects

- [Notes](#notes)
  - [Create a Time Tracker](#create-a-time-tracker)
    - [Add a Data Attribute to a
      Class](#add-a-data-attribute-to-a-class)
      - [Create a Cohesive Object](#create-a-cohesive-object)
    - [Create Method Attributes for a
      Class](#create-method-attributes-for-a-class)
      - [**Code Analysis**: The `get_hours_worked`
        Method](#code-analysis-the-get_hours_worked-method)
    - [Add Validation to Methods](#add-validation-to-methods)
      - [Create Class Variables](#create-class-variables)
        - [**Code Analysis**: Using class
          variables](#code-analysis-using-class-variables)
      - [Create a Static Method to Validate
        Values](#create-a-static-method-to-validate-values)
        - [**Code Analysis**: Creating Static Validation
          Methods](#code-analysis-creating-static-validation-methods)
      - [Return Status Messages from a Validation
        Method](#return-status-messages-from-a-validation-method)
      - [Raise an Exception to indicate an
        Error](#raise-an-exception-to-indicate-an-error)
      - [**Make Something Happen**: Raising Exceptions from
        Code](#make-something-happen-raising-exceptions-from-code)
      - [Extract an Exception Error
        Message](#extract-an-exception-error-message)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

### Create a Time Tracker

- Program’s tend to evolve in scope over time
  - Sometimes due to scope underestimation
  - Also because customers tend to request new features
- Consider the [Tiny
  Contacts](../09_UsingClasses/Chapter_09.qmd#make-a-tiny-contacts-app)
  - Client now wants to functionality to track the time spent with a
    client
- As usual start with the interface,

``` text
Time Tracker

1. New Contact
2. Find Contact
3. Edit Contact
4. Add Session
5. Exit Program

Enter your command:
```

We want to now storyboard out the new `Add Session` option

``` text
Enter your command: 4
Add Hours
Enter the Contact Name: Rob
Name: Rob Miles
Previous Hours worked: 0
Session Length: 3
Updated hours worked: 3.0
```

We also want to update the `Find Contact` option to include the hours,

``` text
Find Contact
Enter the Contact Name: Rob
Name: Rob Miles
Address: 18 Pussycat Mews, London, NE1 410S
Telephone: 1234 56789
Hours worked: 3.0
```

#### Add a Data Attribute to a Class

- We need to store the hours worked
- Simplest approach is to redefine the `Contact` class
  - Add an `hours_worked` field

``` python
class Contact:
    """
    Contact with a name, address and telephone number.
    Tracks the hours worked with a client

    Parameters
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).

    Attributes
    ----------
    hours_worked : int | float
        Hours worked with a Contact, initialised to 0

    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0
```

- Defaulted to `0` as part of the constructor

  - We might discuss this with the client, it’s possible a contact might
    have some initial consult hours

- From here we can add a new `add_session` function (see the [complete
  updated code](./Examples/01_TimeTracker/TimeTracker.py), in our
  version which supports duplicate names in the search)

  ``` python
    def add_session():
        """
        Prompts the user to add hours worked to contacts matching a search

        Returns
        -------
        None

        See Also
        --------
        find_contacts : returns contacts matching a search name
        """
        print("add session")
        search_name = read_text("Enter the contact name: ")
        contact = find_contact(search_name)
        if contact != None:
            #found a contact
            print("Name: ", contact.name)
            print("Previous hours worked:", contact.hours_worked)
            session_length = BTCInput.read_float_ranged(prompt="Session length: ", min_value=0.5, max_value=3.5)
            contact.hours_worked = contact.hours_worked + session_length
            print("Updated hours worked:", contact.hours_worked)
        else:
            print("This name was not found")
  ```

- Don’t forget we also have to update how we display contacts for the
  `Find Contact` functionality (or in our case the `display_contact`)
  function.

  ``` python
    def display_contact(contact):
        """
        Displays the Contact details for the supplied contact

        Parameters
        ----------
        contact : Contact
            contact to display

        Returns
        -------
        None

        See Also
        --------
        display_contacts : Displays all contacts matching a search name
        """
        print("Name:", contact.name)
        print("Address:", contact.address)
        print("Telephone:", contact.telephone)
        print("Hours worked for this Contact:", contact.hours_worked, "\n")
  ```

- If we create a new `Contact` object then we can see how this looks,

  ``` python
    contact = Contact(name="Alice", address="Bob St", telephone="555")
    display_contact(contact)
    contact.hours_worked = 5.0
    display_contact(contact)
  ```

      Name: Alice
      Address: Bob St
      Telephone: 555
      Hours worked for this Contact: 0

      Name: Alice
      Address: Bob St
      Telephone: 555
      Hours worked for this Contact: 5.0

##### Create a Cohesive Object

- When extending a program you should always look at its design
- Code *rots* as it gets older
  - Gets harder to maintain and understand
- Want to make the design as clear and simple as possible
- Like a builder we want to make houses out of walls, walls out of
  bricks and bricks out of clay
  - i.e. clear progression in scale and responsibility
- A technique for this is called *object-oriented design*
  - Objects are designed to be *cohesive*
  - A cohesive object should contain all the attributes and methods to
    work with its domain
- For the `Contact` object we want it to be responsible for all contact
  information
  - Currently not very cohesive
  - Time Tracker works directly on `Contact` object attributes
- Business logic that applies to a `Contact` is outside the function
  - e.g. in the `add_session` function, we have hardcoded a minimum
    session time of half an hour and a maximum session time of three and
    half hours
  - This is problematic
    1. Because the numbers are just written there as opposed to being
        defined as constants with meaning (they are *magic constants*)
    2. This data validation is external to the data storage object
        itself, the `Contact`
  - We also perform the act of updating the `Contact`’s hours worked,
    outside the `Contact` object

  ``` python
    session_length = BTCInput.read_float_ranged(prompt="Session length: ", min_value=0.5, max_value=3.5)
    contact.hours_worked = contact.hours_worked + session_length
  ```

- The magic constant problem is one issue,
  - If we were to use the `Contact` as a libary object in another
    application, (like a graphical version) then we would have to
    maintain the validation code in two seperate places

> [!TIP]
>
> **Keep Business Rules in Business Objects**
>
> The issue here is we have defined *business rules* (things our
> customer asks the system to do) outside of the *business objects*
> (things created to implement the customer’s system).

- A solution is to make the `Contact` object responsible for validating
  the session length
  - Any application that uses the `Contact` object will naturally use
    its internal validation
  - Only one location to change now

#### Create Method Attributes for a Class

- Any python code can access `hours_worked` in a `Contact`

  - Really only need `hours_worked` to be accessed to,
    1. Display time spent with a contact
    2. Add the length of a session to `hours_worked`

- Python objects can hold method attributes

  - Functions bound to the object

- Let us ask an object to do something

- E.g. the `string` object has the method `upper` (seen in [Chapter
  5](../../01_ProgrammingFundamentals/05_MakingDecisions/Chapter_05.qmd#compare-strings-in-programs))

- Let us define two method attributes for `Contact`

  - Removes the need to directly access the attribute

- Start by defining a method to access the hours worked

``` python
class Contact:
    """
    Contact with a name, address and telephone number.
    Tracks the hours worked with a client

    Parameters
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address
    telephone : str
        Contact phone number (stored as a string)

    Attributes
    ----------
    hours_worked : int | float
        Hours worked with a Contact, initialised to 0

    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.hours_worked = 0

    def get_hours_worked(self):
        """
        Get the hours worked for this contact
        """
        return self.hours_worked
```

##### **Code Analysis**: The `get_hours_worked` Method

*Consider the following questions regarding the* `get_hours_worked`
*function*

1. *What is the parameter* `self` *used to accomplish?*

    - A method is part of an object

    - `self` tells the method which object it is a part of

    - The code sample below shows how the method doesn’t need an
      additional reference to the `Contact` it refers to

      ``` python
        # set up
        rob = Contact("Rob", "A St", "1")
        rob.hours_worked = 1
        jim = Contact("Jim", "B St", "555")
        jim.hours_worked = 2

        # demonstration
        rob_work = rob.get_hours_worked()
        jim_work = jim.get_hours_worked()
        if rob_work > jim_work:
            print("More work for rob")
        else:
            print("More work for jim")
      ```

          More work for jim

2. *Is the* `get_hours_worked` *method stored when we save contact
    information in a file*

    - No, if we use
      [`pickle`](../09_UsingClasses/Chapter_09.qmd#save-contacts-in-a-file-using-pickle)
      to store a contact list, the method attributes are not stored.
      Pickle only stores the data attributes

3. *Can a program still access the* `hours_worked` *attribute of a*
    `Contact` *class*

    - Yes, it can. Using method attributes to get data doesn’t stop a
      program accessing the data directly
    - We simply remove the desire to
    - Later chapters look at techniques for enforcing this more robustly

- We can create a second method to handle adding a session to a
  `Contact`

  ``` python
    # existing class definition
    class Contact:
        def __init__(self, name, address, telephone):
            self.name = name
            self.address = address
            self.telephone = telephone
            self.hours_worked = 0
        def get_hours_worked(self):
            """
            Gets the hours worked for this contact

            Returns
            -------
            int | float
                hours worked for this contact
            """
            return self.hours_worked

        # new method
        def add_session(self, session_length):
            """
            Adds a session (in hours) to the Contacts hours

            Parameters
            ----------
            session_length : int | float
                time spent on session in hours

            Returns
            -------
            None
            """
            self.hours_worked = self.hours_worked + session_length
  ```

- Takes two parameters

  1. `self` - the object the method is attached to
      - Here the `Contact` being updated
  2. `session_length`
      - The length of the session to be added

You can see the above implementation integrated into [our TimeTracker
implementation](./Examples/02_TimeTrackerWithMethods/TimeTrackerWithMethods.py).
Aside from defining these new functions we have to update the file scope
`add_session` function (distinct from the class scope `add_session`
method) and the `display_contact` functions to use the new methods

#### Add Validation to Methods

- Currently `add_session` would allow function calls like,

  ``` python
    rob = Contact("Rob", "A St", "555")
    rob.add_session(-10)
    print(rob.get_hours_worked())
  ```

      -10

- Legal call

  - Makes no logical sense
  - Can’t work negative hours

- At the moment the validation is performed in the global `add_session`
  function

  - Suppose this was maintained by another team
  - They could change it, and break your code

> [!NOTE]
>
> **Think Carefully about Valid Input**
>
> You should think carefully about what is valid input for any function,
> especially when you restrict it. As observed here, a negative number
> of hours doesn’t make sense on the surface. However, it might make
> sense in the case of,
>
> 1. Correcting an overestimated number of hours
> 2. The Client wants to give a client a discounted number of hours

- We want to move the validation inside the `Contact` object
  - Want `add_session` to reject hours that are less than half-an-hour
    or greater than three and a half
- We could add these as variables for each instance of a `Contact`
  - But they’re the same for every instance
  - Would be nice to have a way to define it once for the class

##### Create Class Variables

- A class variable is data not attached to a specific object instance
- Can define the min and max hours as a class variable
  - No longer magic constants
  - Accessible by all `Contact` instances

  ``` python
    class Contact:
        """
        Contact with a name, address and telephone number.
        Tracks the hours worked with a client

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).

        Attributes
        ----------
        hours_worked : int | float
            Hours worked with a Contact, initialised to 0

        min_session_length : Final[int | float]
            minimum length of a billable session

        max_session_length : Final[int | float]
            maximum length of a billable session


        Examples
        --------
        >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
        <Contact ...>
        """

        min_session_length = 0.5
        max_session_length = 3.5

        def __init__(self, name, address, telephone):
            self.name = name
            self.address = address
            self.telephone = telephone
            self.hours_worked = 0

        def get_hours_worked(self):
            """
            Gets the hours worked for this contact

            Returns
            -------
            int | float
                hours worked for this contact
            """
            return self.hours_worked

        # new method
        def add_session(self, session_length):
            """
            Adds a session (in hours) to the Contacts hours

            Parameters
            ----------
            session_length : int | float
                time spent on session in hours

            Returns
            -------
            None
            """
            if session_length < Contact.min_session_length or session_length > Contact.max_session_length:
                return
            self.hours_worked = self.hours_worked + session_length
  ```

- `add_session` now silently rejects invalid `session_length` values
- The idiom of first checking for invalid input and performing a
  `return` if encountered is called an *early return* and is a common
  technique
  - Reduces the need for indentation on the happy path - the error free
    path
- Observe we have to prefix the class variables with the class name as a
  namespace
- The `Final` label in the docstring indicates that the session length
  variables are expected to be constant and should not be modified by a
  consuming program

###### **Code Analysis**: Using class variables

*Build your understanding of class variables by answering the following
questions about their use-cases*

1. *Should I use a class variable to hold the age of a contact?*

    - No. Each contact will have an age, so the age must be a data
      attribute unique to each object instance

2. *Should I use a class variable to hold the maximum age of a
    contact?*

    - Yes, we don’t need to store a copy of this value for every
      `Contact` instance, so it can be a class variable

3. *Should I use a class variable to hold the price per hour that the
    lawyer will charge?*

    - It depends, if the lawyer charges the same for every client then
      it may be reasonable
    - If the lawyer wishes to charge different contacts different rates,
      then we would have to store it as a data attribute
      - In that case we might store the minimum and maximum hourly rate
        as class variables

##### Create a Static Method to Validate Values

- Cohesion generally means objects shouldn’t expose attributes for
  external clients

- Ideally clients interact with a `Contact` via method calls

  - e.g. `get_hours_worked` and `add_session`
  - Eliminates direct dependency on `hours_worked` data attribute

- In the same vein, we don’t want users to directly interact with class
  variables

  - e.g. `max_session_length` and `min_session_length` are used for
    internal validation
  - External client should have no reason to directly modify them

- Could create a method, `validate_session_length`

  - Receive a `session_length` argument
  - Return `True` if valid, else `False`

- Validation information (`max_session_length` and `min_session_length`)
  is held at the class level

  - Would be nice to also have this validation method at the class level
    too

- We can create class level methods through a *Static Method*

  - Static methods can be considered as methods defined on a class
    rather than an object instance

- We can define one as below,

  ``` python
    class Contact:
        """
        Contact with a name, address and telephone number.
        Tracks the hours worked with a client

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).

        Attributes
        ----------
        hours_worked : int | float
            Hours worked with a Contact, initialised to 0

        min_session_length : Final[int | float]
            minimum length of a billable session

        max_session_length : Final[int | float]
            maximum length of a billable session


        Examples
        --------
        >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
        <Contact ...>
        """
        min_session_length = 0.5
        max_session_length = 3.5

        @staticmethod
        def valid_session_length(session_length):
            """
            Check a session length is valid

            Parameters
            ----------
            session_length : int | float
                length of a consult session in hours

            Returns
            -------
            bool
                `True` if the session length is valid else `False`
            """
            if session_length < Contact.min_session_length or session_length > Contact.max_session_length:
                return False
            return True


        def __init__(self, name, address, telephone):
            self.name = name
            self.address = address
            self.telephone = telephone
            self.hours_worked = 0

        def get_hours_worked(self):
            """
            Gets the hours worked for this contact

            Returns
            -------
            int | float
                hours worked for this contact
            """
            return self.hours_worked

        # new method
        def add_session(self, session_length):
            """
            Adds a session (in hours) to the Contacts hours

            Parameters
            ----------
            session_length : int | float
                time spent on session in hours

            Returns
            -------
            None

            See Also
            --------
            Contact.valid_session_length : checks a session length is valid
            """
            if not Contact.valid_session_length(session_length):
                return
            self.hours_worked = self.hours_worked + session_length
  ```

- The `@staticmethod` tag above the definition of `valid_session_length`
  is called a *decorator*

- A decorator *wraps* a function to modify how it works

- Decorators are added by writing `@` followed by the decorator name
  above the function to be wrapped

  - You can wrap a function with multiple decorators

- The `@staticmethod` decorator is a python language built-in

  - Converts a method into a static method
  - Static methods can exist even without an instance of the given class

- Static methods can be called directly from the class e.g.

  ``` python
    print(Contact.valid_session_length(5))
  ```

      False

###### **Code Analysis**: Creating Static Validation Methods

*Input validation is a very common use-case for static methods. Consider
the following questions to understand static validation methods*

1. *Why does the* `valid_session_length` *method not have a* `self`
    *parameter?*

    - `self` refers to a particular object instance
    - static methods are not associated with an instance
      - Associated with the class
      - Thus no `self` to refer to

2. *Why does the* `valid_session_length` *method not print a message to
    the user communicating that the session length is invalid?*

    - `valid_session_length` only has responsibility for checking if a
      session length is valid
    - How to handle an *invalid* session length is the responsibility of
      the caller
      - e.g. a text-based vs graphical interface may want to handle this
        differently
        - e.g. display text vs a window
    - This concept of making a function responsible for one thing is
      called either
      - The *single responsibility principle*,
      - or more generally *seperation of concerns*
    - Here a `Contact` object performs behaviours that modify or capture
      a the state of a clients interactions with a client
      - How the user responds to those states is not its responsibility

3. *What does a decorator do?*

    - A decorator is a function that *wraps* another function
    - They can do some work, call a function then do some clean-up

4. *Can I create my own decorators?*

    - Yes
    - They are beyond the scope of this book though

5. *How do I know when to create a static method in a class?*

    - You want to create behaviour associated with a class, *but*
      - Independent of specific instance of a class

##### Return Status Messages from a Validation Method

- `add_session` prevents invalid session lengths being added to a
  `Contact`
- Currently user has no way of knowing if a session was added
  - Mistakes might be missed
  - Records then lost
- Need to indicate if `add_session` succeeded
- Can do so by returning a *status flag* from `add_session` rather than
  `None`
  - `True` indicates session added
  - `False` indicates session failed

  ``` python
    def add_session(self, session_length):
    """
    Adds a session (in hours) to the Contacts hours

    Parameters
    ----------
    session_length : int | float
        time spent on session in hours

    Returns
    -------
    bool
        `True` if session successfully added, else `False`

    See Also
    --------
    Contact.valid_session_length : checks a session length is valid
    """
    if not Contact.valid_session_length(session_length):
        return False
    self.hours_worked = self.hours_worked + session_length
    return True
  ```

- The calling program can then check the status
  - Behave as appropriate on error

  ``` python
    session_length = BTCInput.read_float(prompt="Session Length: ")
    if contact.add_session(session_length):
        print("Updated hours succeeded", contact.get_hours_worked())
    else:
        print("Add hours failed")
  ```

- The above uses the status
  - On success the new hours are reported
  - On failure, the user is notified of the error
- The full implementation is given in
  [TimeTrackerWithStatusReporting.py](./Examples/05_TimeTrackerWithStatusReporting/TimeTrackerWithStatusReporting.py)
- The problem with status messages is that the user can ignore them,
  e.g. the below variation of the previous example, ignores the return
  value

``` python
   contact.add_session(BTCInput.read_float(prompt="Session Length: "))
   print("Updated hours:", contact.get_hours_worked())
```

- Thus no guarantee that failure will be handled

##### Raise an Exception to indicate an Error

- Exceptions force the caller to deal with them
  - Unhandled exceptions crash the program
- Exceptions are designed for when an error occurs where continuing
  makes no sense
  - e.g. converting strings to numbers

  - meaningless to continue with an unconverted number

  - *Unless* the caller specifies what to do in that case

  - So this causes an exception

    ``` python
      x = int("Rob")
    ```

        ValueError: invalid literal for int() with base 10: 'Rob'
        ---------------------------------------------------------------------------
        ValueError                                Traceback (most recent call last)
        Cell In[28], line 1
        ----> 1 x = int("Rob")

        ValueError: invalid literal for int() with base 10: 'Rob'
- We can make our on code throw exceptions
  - We use the `raise` keyword

  ``` python
    def add_session(self, session_length):
        """
        Adds a session (in hours) to the Contacts hours

        Parameters
        ----------
        session_length : int | float
            time spent on session in hours

        Returns
        -------
        None

        Raises
        ------
        Exception
            Raised if invalid session length passed

        See Also
        --------
        Contact.valid_session_length : checks a session length is valid
        """
        if not Contact.valid_session_length(session_length):
            raise Exception("Invalid Session Length")
        self.hours_worked = self.hours_worked + session_length
  ```

- `Contact`’s `add_session` now raises an `Exception` if the session
  length is invalid
- Exception somewhat like a message
  - Tells the program what went wrong
- `Exception` class provides behaviours for exceptions
  - Takes a string as an initialiser argument
  - string should describe the error
- Once raised, the exception is either,
  1. handled by an `Except` handler inside a `try` block
  2. Stops the program with an error
- The complete integration of the above is given byy
  [TimeTrackerWithException.py](./Examples/06_TimeTrackerWithException/TimeTrackerWithException.py)

##### **Make Something Happen**: Raising Exceptions from Code

*Investigate how exceptions are raised using the sample program [Time
Tracker with
Exception](./Examples/06_TimeTrackerWithException/TimeTrackerWithException.py)*

Start a python interpreter and run the example program above, select
option $1$ on the menu, and enter the following,

    Time Tracker

    1. New Contact
    2. Find Contact
    3. Edit Contact
    4. Add Session
    5. Exit Program

    Enter your command: 1
    Create new contact
    Enter the contact name:  Rob Miles
    Enter the contact address:  18 Pussycat Mews, London, NE1 410S
    Enter the contact phone:  1234 56789

Now add a session lasting 2 hours to the contact using option 4:

    Enter your command:  4
    add session
    Enter the contact name:  Rob Miles
    Name: Rob Miles
    Previous hours worked: 0
    Session Length:  2
    Updated hours worked: 2.0

This should work because $2$ is a valid session length, now repeat but
attempt to add a session length of $4$, which should be invalid,

    Enter your command:  4
    add session
    Enter the contact name:  Rob Miles
    Name: Rob Miles
    Previous hours worked: 2.0
    Session Length:  4

    Exception: Invalid Session Length
    ---------------------------------------------------------------------------
    Exception                                 Traceback (most recent call last)
    Cell In[33], line 3
          1 rob = Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "1234 56789")
          2 add_session(rob, 2)
    ----> 3 add_session(rob, 4)

    Cell In[29], line 24, in add_session(self, session_length)
          2 """
          3 Adds a session (in hours) to the Contacts hours
          4
       (...)     21 Contact.valid_session_length : checks a session length is valid
         22 """
         23 if not Contact.valid_session_length(session_length):
    ---> 24     raise Exception("Invalid Session Length")
         25 self.hours_worked = self.hours_worked + session_length

    Exception: Invalid Session Length

> [!NOTE]
>
> Our implementation will look slightly different to the above (which is
> the book code) because it has additional logic for handling
> duplicates. But follow the steps and the prompts and you should get
> roughly the same process

##### Extract an Exception Error Message

- Now that we can raise exceptions, how do we handle them?
- We’ve seen that we control jumps to an appropriate `except` but what
  if we want to access the message in the exception?
  - We can use the `as` keyword to assign the exception a variable label
  - We modify the user call to the `Contact` object, `add_session` as,
    (see the full implementation as
    [TimeTrackerWithExceptionHandler.py](./Examples/07_TimeTrackerWithExceptionHandler/TimeTrackerWithExceptionHandler.py))

  ``` python
    hours_worked = BTCInput.read_float(prompt="Enter hours spent: ")
    try:
        contact.add_session(hours_worked)
        print("Updated hours succeeded:", contact.get_hours_worked())
    except Exception as e:
        print("Add failed:", e)
  ```

- The main change is rather than just going `except Exception:` we add a
  `as e`
  - Defines a variable `e` that stores the exception
  - `e` exists for the scope of the `except` block
- Passing an exception to `print` prints our the message associated with
  the exception
- A representative use might look like,

<!-- -->

    Enter your command:  4
    add session
    Enter the contact name:  Rob Miles
    Name: Rob Miles
    Previous hours worked: 2.0
    Session Length:  -1
    Add failed: Invalid Session Length

## Summary

## Questions and Answers
