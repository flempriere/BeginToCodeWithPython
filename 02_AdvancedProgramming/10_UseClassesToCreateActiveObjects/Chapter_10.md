# Chapter 10: Using Classes to Create Active Objects

- [Notes](#notes)
  - [Create a Time Tracker](#create-a-time-tracker)
    - [Add a Data Attribute to a
      Class](#add-a-data-attribute-to-a-class)
      - [Create a Cohesive Object](#create-a-cohesive-object)
    - [Create Method Attributes for a
      Class](#create-method-attributes-for-a-class)
      - [Code Analysis: The `get_hours_worked`
        Method](#code-analysis-the-get_hours_worked-method)
    - [Add Validation to Methods](#add-validation-to-methods)
      - [Create Class Variables](#create-class-variables)
        - [Code Analysis: Using class
          variables](#code-analysis-using-class-variables)
      - [Create a Static Method to Validate
        Values](#create-a-static-method-to-validate-values)
        - [Code Analysis: Creating Static Validation
          Methods](#code-analysis-creating-static-validation-methods)
      - [Return Status Messages from a Validation
        Method](#return-status-messages-from-a-validation-method)
      - [Raise an Exception to indicate an
        Error](#raise-an-exception-to-indicate-an-error)
      - [Make Something Happen: Raising Exceptions from
        Code](#make-something-happen-raising-exceptions-from-code)
      - [Extract an Exception Error
        Message](#extract-an-exception-error-message)
      - [Make Something Happen: Catching
        Exceptions](#make-something-happen-catching-exceptions)
      - [Code Analysis: Raising and Dealing with
        Exceptions](#code-analysis-raising-and-dealing-with-exceptions)
    - [Protect a Data Attribute against
      Damage](#protect-a-data-attribute-against-damage)
      - [Make Something Happen: Protecting Data Attributes in a
        Class](#make-something-happen-protecting-data-attributes-in-a-class)
    - [Protected Methods](#protected-methods)
  - [Create Class Properties](#create-class-properties)
    - [Code Analysis: Properties in
      Classes](#code-analysis-properties-in-classes)
    - [Make Something Happen: Investigating
      Properties](#make-something-happen-investigating-properties)
  - [Evolve Class Design](#evolve-class-design)
    - [Code Analysis: Managing the Billing
      Amount](#code-analysis-managing-the-billing-amount)
    - [Manage Class Versions](#manage-class-versions)
      - [Add a version attribute to a
        class](#add-a-version-attribute-to-a-class)
      - [Check Version Numbers](#check-version-numbers)
      - [Upgrade a Class](#upgrade-a-class)
      - [Make Something Happen: Explore Version
        Management](#make-something-happen-explore-version-management)
    - [The `__str__` Method in a Class](#the-__str__-method-in-a-class)
      - [Python String Formatting](#python-string-formatting)
      - [Make Something Happen: Adventures with String
        Formatting](#make-something-happen-adventures-with-string-formatting)
  - [Session Tracking in Time
    Tracker](#session-tracking-in-time-tracker)
    - [Code Analysis: Creating a Session
      Class](#code-analysis-creating-a-session-class)
    - [The Python `map` Function](#the-python-map-function)
      - [Make Something Happen: Investigating the `map` Function and
        Iteration](#make-something-happen-investigating-the-map-function-and-iteration)
    - [The Python `join` Method](#the-python-join-method)
      - [Make Something Happen: Investigating the `join`
        Function](#make-something-happen-investigating-the-join-function)
    - [Exercise: Playlist Storage App](#exercise-playlist-storage-app)
  - [Make Music with Snaps](#make-music-with-snaps)
    - [Code Analysis: The `Note` Class](#code-analysis-the-note-class)
    - [Make Something Happen: Make Your Own
      Music](#make-something-happen-make-your-own-music)
    - [Exercise: Simple Tune Creator](#exercise-simple-tune-creator)
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

    Attributes
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).
    hours_worked : int | float
        Hours worked with a Contact, initialised to 0

    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """

    def __init__(self, name, address, telephone):
        """
        Create a new Contact instance

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        """
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

    Attributes
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).
    hours_worked : int | float
        Hours worked with a Contact, initialised to 0

    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """

    def __init__(self, name, address, telephone):
        """
        Create a new Contact instance

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        """
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

##### Code Analysis: The `get_hours_worked` Method

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

        Attributes
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        hours_worked : int | float
            Hours worked with a Contact, initialised to 0

        Class Attributes
        ----------------
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
            """
            Create a new Contact instance

            Parameters
            ----------
            name : str
                Contact Name
            address : str
                Contact's postal or street address.
            telephone : str
                Contact phone number (stored as a string).
            """
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

###### Code Analysis: Using class variables

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

        Attributes
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        hours_worked : int | float
            Hours worked with a Contact, initialised to 0

        Class Attributes
        ----------------
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
            if (
                session_length < Contact.min_session_length
                or session_length > Contact.max_session_length
            ):
                return False
            return True

        def __init__(self, name, address, telephone):
            """
            Create a new Contact instance

            Parameters
            ----------
            name : str
                Contact Name
            address : str
                Contact's postal or street address.
            telephone : str
                Contact phone number (stored as a string).
            """
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

###### Code Analysis: Creating Static Validation Methods

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
        Cell In[11], line 1
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

##### Make Something Happen: Raising Exceptions from Code

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
    Cell In[16], line 3
          1 rob = Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "1234 56789")
          2 add_session(rob, 2)
    ----> 3 add_session(rob, 4)

    Cell In[12], line 24, in add_session(self, session_length)
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

##### Make Something Happen: Catching Exceptions

*Repeat the steps in the [previous
example](#make-something-happen-raising-exceptions-from-code) but this
time use the new code in [Time Tracker with Exceptionn
Handler](./Examples/07_TimeTrackerWithExceptionHandler/TimeTrackerWithExceptionHandler.py).
You should find the program runs and the errors are captured without
causing a crash*

##### Code Analysis: Raising and Dealing with Exceptions

*Consider the following questions about dealing with exceptions*

1. *Why does this version of the program not check the result returned
    by* `add_session`*?*

    - This implementation of `add_session` returns `None`
    - Instead an exception is raised to indicate a failure state
    - There is therefore nothing to check

2. *Isn’t raising an exception and stopping the program when something
    goes wrong a bit harsh?*

    - Depends on your philosophy
    - Generally you want to avoid *silent errors*
    - i.e. errors that are undetected by the user
    - Exceptions force the user to handle the error rather than silently
      ignore it
    - If the user wants to avoid exception handling, they can explicitly
      use `validate_session_length`

3. *Can a method be resumed once it has raised an exception?*

    - No
    - Exceptions immediately terminate the normal control flow
    - The user can always call the function again

4. *Why would you want to create your own types of exceptions?*

    - Allows any errors returned to be descriptive to your specific code
    - e.g. if your program relies on a specific file being loaded you
      might want a more descriptive error message than the standard
      `FileException` provides
    - Error management and reporting should be decided early in a
      program

5. *Should I always use exceptions to indicate something has gone
    wrong?*

    - Depends
      - You may not care about handling all types of errors
    - Exceptions ensure errors are dealt with
      - User can customise the error handling in response to exception
      - e.g. for a text-based vs GUI interface

6. *Why have we made* `add_session` *work like this? The program worked
    before we made this change*

    - Technically correct
      - Old code used the error status to validate code
    - Arguably cleaner with the new error handling
      - Knowledge about the `Contact` class has been centralised in the
        `Contact` class itself
      - No need to have external variables storing information about
        valid session length or doing the validation
    - Typically a good idea to put all knowledge about a classes
      behaviour in the class itself

#### Protect a Data Attribute against Damage

- Client no longer needs to directly interact with `hours_worked`
- However, client can still modify `hours_worked`
  - Programmer could accidently change the value
  - Could also intentionally change it to break the code
- Ideally we want to prevent it being directly modified

> [!WARNING]
>
> **Python protects against mistakes, not attacks**
>
> Python provides features to help protect data attributes against
> accidental modifications. However, they don’t stop a programmer who
> intentionally (and perhaps maliciously) decides they want to modify
> the data attributes.
>
> There is no mechanism in the python language to prevent another
> progrmmer adding code that changes `hours_worked` in the `Contact`
> object

- By convention, python dictates that an attribute name starting with
  `_` should not be used outside the class
  - Also referred to as being *internal* to the class

  - e.g. `_hours_worked` means that the variable should not be touched

    ``` python
      def get_hours_worked(self):
          """
          Gets the hours worked for this contact

          Returns
          -------
          int | float
              hours worked for this contact
          """
          return self._hours_worked
    ```

- Above we provide a `get_hours_worked` method to get the value of
  `_hours_worked`
  - `_` indicates not to modify `hours_worked` itself
- No actual protection for `_hours_worked`
  - Could still be ignored by a programmer
- Can get greater security through, *name-mangling*
  - starting a varible name with double underscores `__`
- *name-mangling* makes it harder to access and modify the variable

##### Make Something Happen: Protecting Data Attributes in a Class

*Follow the following steps to examine how to make a python class
secure. Open a python interpreter and enter the statements below*

``` python
    class Secret:
        def __init__(self):
            self._secret = 99
            self.__top_secret = 100
```

The above creates a class `Secret` which has two attributes, `_secret`
and `__top_secret`

*Create an instance of the* `Secret` *class*

``` python
    x = Secret()
```

The above creates a new instance of a `Secret` class and stores it with
the variable `x`.

*Try to access the* `_secret` *attribute on* `x`

``` python
    x._secret
```

    99

Even though we said that `_` indicates we should not access the data
attribute, we can see that nothing stops us from doing so

*Now try to access the* `__top_secret` *attribute*

``` python
    x.__top_secret
```

    AttributeError: 'Secret' object has no attribute '__top_secret'
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    Cell In[21], line 1
    ----> 1 x.__top_secret

    AttributeError: 'Secret' object has no attribute '__top_secret'

This time we get an `AttributeError` which suggests that there is no
`__top_secret` attribute associated with the `Secret` class

*However, Python has performed some “name-mangling” to the name*
`__top_secret`*. Inside the* `Secret` *class we can refer to*
`__top_secret`*. Outside the class, the variable name is prepended with
the class name (and an underscore). So we can still access it, as the
below proves*

``` python
    x._Secret__top_secret
```

    100

Name-mangling thus secures us against accidental attribute use, however
any one who knows the name mangling scheme and our attributes can still
modify the data attribute if they want to

There are programs that check against this kind of bad code behaviour.
One example is [pylint](https://www.pylint.org/)

#### Protected Methods

- Our current methods for the `Contact` class are all intended to be
  used by clients
  - Referred to as *public* methods
- We might also want to protect methods in a class
- Can use `_` prefix to indicate that it should not be used
- Or `__` prefix to name mangle

> [!TIP]
>
> **Writing secure code is all about workflow**
>
> Making a secure program is all about establishing a workflow to
> generate quality code. For example, using prototypes to make sure that
> a customer agrees with the direction of a program early in the
> development
>
> The next step is to sensible design and tools like pylint to make sure
> we’re writing good quality code.

### Create Class Properties

- We’ve talked about protecting `hours_spent` for our `Contact`
- We should add more business logic to ensure that name, address and
  telephone items are sensible
  - As a purely toy example, lets say they must each be $4$ characters
    long
- Realistically they would be discussed and confirmed with the customer

``` python
class Contact:

    __min_text_length = 4

    @staticmethod
    def valid_text(text):
        """
        Validates text to be stored in the contact storage

        Parameters
        ----------
        text : str
            text string to store

        Returns
        -------
        bool
            `True` if the text is valid, else `False`
        """

        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True
```

- Above mirrors `valid_session_length`
- Called to validate text to be stored in a `Contact`
- We could then name mangle `name`, `address`, `telephone`
- Supply methods to get and set these attributes
  - e.g. `set_name` and `get_name` for example
- Python has a built-in way for providing read and write access to
  protected data
- This is called a *Property*
  - Properties preserve simple access, while allowing us to implement
    validation

#### Code Analysis: Properties in Classes

``` python
class Contact:
    __min_text_length = 4

    @staticmethod
    def valid_text(text):
        """
        Validates text to be stored in the contact storage

        Valid input must be have a length greater than or
        equal to Contact.__min_text_length

        Parameters
        ----------
        text : str
            text string to store

        Returns
        -------
        bool
            `True` if the text is valid, else `False`
        """
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property  # decorator makes name a property
    def name(self):  # name of property function to get the name
        """
        name : str
            Contact Name

        Raises
        ------
        Exception
            raised if new name is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__name  # return private attribute containing the name

    @name.setter  # decorator to identify the setter for name
    def name(self, name):
        if not Contact.validate_text(name):
            raise Exception("Invalid name")
        self.__name = name
```

*The code above shows how to implement a property for* `name` *in the*
`Contact` *class. The property implements validation and rejects invalid
names. Work through the following questions to understand properties*

1. *How does the value being set in the property get into the*
    `setter`*?*

    - `setter` is called with two parameters
    - `self` refers to the object on which the `setter` is being called
    - The second is the proposed value to set the property to
      - Here it is setting the `name` attribute

2. *How does the program know which* `setter` *method to call for a
    particular property?*

    - The `setter` decorator has the format `property.setter`
      - Associates a `setter` to a property

3. *Must the* `setter` *method raise an exception if the value is being
    set is not valid?*

    - No
    - `setter` could ignore invalid values, or assign a default
    - Exceptions allow us to inform the user that the set has failed
      - And also forces the user to deal with the error

4. *Do we need to perform the same validation for all properties in a
    class?*

    - No
    - We could test that telephone is purely numeric (for example)
      - This is not a good idea for real telephone numbers
    - We could ensure address matches a certain structure for a valid
      address

5. *Must a property have a* `setter`*?*

    - No
    - Properties without a `setter` are *read-only*
    - They cannot be modified
    - We could use this to remove the `get_hours_worked` method
      - Use a property instead

#### Make Something Happen: Investigating Properties

*Investigate how properties work. Open up the python interpreter and
enter the statements below*

``` python
class Prop:
    @property
    def x(self):
        print("got property x")
        return self.__x
    @x.setter
    def x(self, x):
        print("set property x:", x)
        self.__x = x
```

This creates a new class `Prop` with a property `x` that has a `setter`

*Now create an instance of this class as below*

``` python
    test = Prop()
```

*Put a value for* `x` *into the* `test` *instance*

``` python
    test.x = 99
```

    set property x: 99

When python executes the above, it runs the setter method for the
property. As we can see from the output above.

*Now try to read the property*

``` python
    print(test.x)
```

    got property x
    99

When reading the property, python runs the property method, as indicated
above

*We can combine getting and setting in complex expressions, execute the
following*

``` python
    test.x = test.x + 1
```

    got property x
    set property x: 100

We can see that first the getter is called to get the current value of
`x`, then the setter is called to update it to the expression on the
right

To convert the `Contact` class to use properties for `name`, `telephone`
and `address` we have to add properties and then setters

- The relevant changes to the `Contact` class are then,

``` python
class Contact:
    """
    Contact with a name, address and telephone number.
    Tracks the hours worked with a client

    Attributes
    ----------
    name : str
        Contact Name
    address : str
        Contact's postal or street address.
    telephone : str
        Contact phone number (stored as a string).


    Examples
    --------
    >>> Contact("Rob Miles", "18 Pussycat Mews, London, NE1 410S", "+44(1234) 56789")
    <Contact ...>
    """

    __min_session_length = 0.5
    __max_session_length = 3.5

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
        if (
            session_length < Contact.__min_session_length
            or session_length > Contact.__max_session_length
        ):
            return False
        return True

    __min_text_length = 4

    @staticmethod
    def valid_text(text):
        """
        Validates text to be stored in the contact storage

        Valid input must be have a length greater than or
        equal to Contact.__min_text_length

        Parameters
        ----------
        text : str
            text string to store

        Returns
        -------
        bool
            `True` if the text is valid, else `False`
        """
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        """
        name : str
            Contact Name

        Raises
        ------
        Exception
            raised if new name is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__name

    @name.setter
    def name(self, name):
        if not Contact.valid_text(name):
            raise Exception("Invalid name")
        self.__name = name

    @property
    def address(self):
        """
        address : str
            Contact Address

        Raises
        ------
        Exception
            raised if new address is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__address

    @address.setter
    def address(self, address):
        if not Contact.valid_text(address):
            raise Exception("Invalid address")
        self.__address = address

    @property
    def telephone(self):
        """
        telephone : str
            Contact Telephone

        Raises
        ------
        Exception
            raised if new telephone is invalid

        See Also
        --------
        Contact.valid_text : validates text input
        """
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if not Contact.valid_text(telephone):
            raise Exception("Invalid telephone")
        self.__telephone = telephone

    def __init__(self, name, address, telephone):
        """
        Create a new Contact instance

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        """
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
```

- The great thing about properties is they can be effectively drop in
  for traditional attributes
  - We make the attributes themselves name mangled
  - Define properties to mask the original names
- No need to update the downstream calling code
  - property syntax matches the traditional access pattern
- The complete integration is seen in
  [TimeTrackerWithPropertie.py](./Examples/09_TimeTrackerWithProperties/TimeTrackerWithProperties.py)

> [!CAUTION]
>
> **Failures in property code can be confusing**
>
> The [example
> program](./Examples/09_TimeTrackerWithProperties/TimeTrackerWithProperties.py)
> implements the name, address and telephone number elements of a
> contact as properties. Setting a property to an invalid value will
> cause an exception. The initialiser looks like,
>
> ``` python
>     def __init__(self, name, address, telephone):
>         self.name = name
>         self.address = address
>         self.telephone = telephone
>         self.__hours_worked = 0
> ```
>
> These statements look like normal variable assignments, nothing here
> indicates that these steps can fail. However, the following statement
> fails,
>
> ``` python
>     rob = Contact(name="Rob", address="18 Pussycat Mews, London NE1 410S", telephone="1234 56789")
> ```
>
>     Exception: Invalid name
>     ---------------------------------------------------------------------------
>     Exception                                 Traceback (most recent call last)
>     Cell In[31], line 1
>     ----> 1 rob = Contact(name="Rob", address="18 Pussycat Mews, London NE1 410S", telephone="1234 56789")
>
>     Cell In[30], line 154, in Contact.__init__(self, name, address, telephone)
>         141 def __init__(self, name, address, telephone):
>         142     """
>         143     Create a new Contact instance
>         144
>        (...)    152         Contact phone number (stored as a string).
>         153     """
>     --> 154     self.name = name
>         155     self.address = address
>         156     self.telephone = telephone
>
>     Cell In[30], line 92, in Contact.name(self, name)
>          89 @name.setter
>          90 def name(self, name):
>          91     if not Contact.valid_text(name):
>     ---> 92         raise Exception("Invalid name")
>          93     self.__name = name
>
>     Exception: Invalid name
>
> The above raises an exception because the value `Rob` passed for the
> `name` property is too short. `__init__` attempts to set `name` which
> calls the setter, and the property code raises an exception.
>
> Programmers may expect methods or functions to cause exceptions but
> they typically do not expect statements that look like variable
> assignments. When implementing properties you need to be clear about
> how they work and how to handle failure.
>
> We could extend our previous [error handling
> code](#make-something-happen-catching-exceptions) to add additional
> exception handlers to handle invalid assignments

### Evolve Class Design

> Scenario
>
> The lawyer likes your program but would now like to use it for
> billing. The program should track both the hours worked for a client
> and the the billing amount owed by each contact
>
> Prices are calculated as follows, for every session worked there is -
> A \$30 flat case fee - A \$50 hourly fee
>
> For example a one hour session would cost \$80
>
> The client wants the billing amount to be automatically updated each
> time they add a session. Displaying a contact should then also display
> the billing amount
>
> ``` text
> Name: Rob Miles
> Address: 18 Pussycat Mews, London, NE1 410S
> Telephone: 1234 56789
> Hours on the case: 2.0
> Billing amount: 130.0
> ```

#### Code Analysis: Managing the Billing Amount

*Work through the following questions to understand how we design
managing the billing amount*

1. *How would we store the billing amount for a contact?*

    - Store as a data attribute on a `Contact` object
    - Manage like `__hours_worked` with validators
    - Let’s call it `__billing_amount`

2. *Why does* `__billing_amount` *have two leading underscores in the
    name?*

    - Indicates the variable is private to the class

    - Provides name-mangling to reduce chance for accidental use

    - Provide access via a read-only property

      ``` python
        @property
        def billing_amount(self):
            return self.__billing_amount
      ```

    - We omit a setter, the property cannot be directly modified

    - Can then access the property as we would expect

      ``` python
        print("Rob owes:", rob.billing_amount)
      ```

    - Same output might look like,

      ``` python
        #| echo: false
        print("Rob owes:", 130.0)
      ```

3. *What would the statement calculating the billable amount for a
    session look like?*

    - At it’s most basic the statement might look like,

      ``` python
        amount_to_bill = 30 + (50 * session_length)
      ```

    - `session_length` value is multipled by the hourly rate ($50$)

    - flat fee $30$ is added to the total

    - Can then add this to the billing amount

      ``` python
        self.__billing_amount = self.billing_amount + amount_to_bill
      ```

    - Observe that this approach means that each session incurs the same
      $30$ case opening fee

    - It’s possible multiple sessions might be spent on the same case

      - Might not incur the $30$ fee each time
      - This would be something to confirm with the client

4. *Is it sensible to just use the values* $30$ *and* $50$ *in this
    code?*

    - No

    - They are magic constants

    - Better to make them internal class variables of the `Contact`
      class

      ``` python
        class Contact
            __open_fee = 30
            __hourly_fee = 50
      ```

    - Observe that we flag them as private, they are internals for the
      class

    - The new amount to bill statement is then,

      ``` python
        amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
      ```

5. *Where should the above statement go?*

    - Adjusting the billing is something that occurs when we add a
      session

    - Makes sense to go in the `add_session` code of the `Contact` class

      ``` python
        def add_session(self, session_length):
            """
            Adds a session (in hours) to the Contacts hours

            Updates the Contact's session hours and calculates
            the billable amount owed

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
            if not Contact.validate_session_length(session_length):
                raise Exception("Invalid session length")
            self.__hours_worked = self.__hours_worked + session_length
            amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
            self.__billing_amount = self.__billing_amount + amount_to_bill
            return
      ```

    - Billing amount is updated *after* we have validated and updated
      the hours worked

- We change the `display_contact` method to add the billing amount

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
    print("Hours worked for this Contact:", contact.get_hours_worked(), "\n")
    print("Amount to bill:", contact.billing_amount)
```

- The complete program can be found in [Time Tracker with Billing
  Amount](./Examples/11_TimeTrackerWithBillingAmount/TimeTrackerWithBillingAmount.py)

#### Manage Class Versions

- The new program works, but it has a problem
- Contacts saved under the old system, won’t work
  - They will load

  - But whe we try to display or add a session we’ll get an error, like

        AttributeError: 'Contact' object has no attribute '_Contact__billing_amount'
        ---------------------------------------------------------------------------
        AttributeError                            Traceback (most recent call last)
        Cell In[32], line 1
        ----> 1 raise AttributeError("'Contact' object has no attribute '_Contact__billing_amount'")

        AttributeError: 'Contact' object has no attribute '_Contact__billing_amount'
- This occurs because the program attempts to access the
  `__billing_access` attribute
- Old versions of the `Contact` class didn’t have this
  - So error occurs
- Same might occur if we make more modifications in the future

##### Add a version attribute to a class

- We can solve this by *versioning* a class
- Add a version attribute to each class
  - Simply a numeric attribute

  ``` python
    def __init__(self, name, address, telephone):
        """
        Create a new Contact instance

        Parameters
        ----------
        name : str
            Contact Name
        address : str
            Contact's postal or street address.
        telephone : str
            Contact phone number (stored as a string).
        """
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
        self.__billing_amount = 0
        self.__version = 1
  ```

- version is set as a private variable

##### Check Version Numbers

- Then create a method to check the version of a `Contact`

  - Let’s us check that a `Contact` object matches the current version

  ``` python
    def check_version(self):
        """
        Check the version of a Contact instance

        Upgrades the instance to the most recent version
        if required
        """
        pass
  ```

- Leave it as a stub for now

- We want to use it when we load contacts to check versions

- Updated `load_contacts` is below

  ``` python
    def load_contacts(file_name):
    """
    Loads the contacts from the given file

    Contacts are stored in binary as a pickled file

    Parameters
    ----------
    file_name : str
        string giving the path to the file where the contacts data is stored

    Returns
    -------
    None
        Contact detail is loaded into the global contacts value

    Raises
    ------
        Exceptions if contacts failed to load

    See Also
    --------
    save_contacts : saves contacts to a pickled file
    """
    global contacts
    print("Load contacts")
    with open(file_name, "rb") as input_file:
        contacts = pickle.load(input_file)
    # Update version of loaded contacts if required
    for contact in contacts:
        contact.check_version()
  ```

##### Upgrade a Class

- Now we want to write code to upgrade a `Contact`

- For our version $1$, we want to upgrade any class that *does not* have
  a `__billing_amount` attribute

- In future we might define a version $2$, then we would redefine the
  `check_version` method to upgrade any class that isn’t version $2$

  ``` python
    def check_version(self):
    """
    Check the version of a Contact instance

    Upgrades the instance to the most recent version
    if required
    """
    try:
        if not self.__version == 1:
            self.__billing_amount = 0
            self.__version = 1
    except AttributeError:
        self.__billing_amount = 0
        self.__version = 1
  ```

- We first attempt to check the version number

- If it’s not the current version ($1$) we upgrade the class

  - Add a `.__billing_amount` attribute defaulted to zero
  - Upgrade the version number

- Use a `try...except` block to catch the `AttributeError` if the
  version doesn’t exist (i.e. for old instances pre-versioning)

  - Perform the upgrade

##### Make Something Happen: Explore Version Management

*To get a better understanding of versioning, work through the following
steps*

*Start by running the program
[TimeTrackerWithPropertiesAndExceptionHandling.py](./Examples/10_TimeTrackerWithPropertiesAndExceptionHandling/TimeTrackerWithPropertiesAndExceptionHandling.py).
Create a new contact as below*

    Enter your command: 1
    Create new contact
    Enter the contact name: Rob Miles
    Enter the contact address: 18 Pussycat Mews, London, NE1 410S
    Enter the contact phone: 1234 56789

This creates a new contact, which looks like, (use Find Contact)

    Name: Rob Miles
    Address: 18 Pussycat Mews, London, NE1 410S
    Telephone: 1234 56789
    Hours on the case: 0

As we can see this version is missing the billable hours information

*Exit the program so the contact is saved. Now load this pickle file
with
[TimeTrackerWithVersion.py](./Examples/12_TimeTrackerWithVersion/TimeTrackerWithVersion.py)*

This should load the contact (which is unversioned), and upgrade it to
the versioned variant with a billing amount

*Attempt to display this contact, you should see something like*

    Name: Rob Miles
    Address: 18 Pussycat Mews, London, NE1 410S
    Telephone: 1234 56789
    Hours on the case: 0
    Amount to bill: 0

As we can see, the amount to bill is now correctly displayed

> [!IMPORTANT]
>
> **Add version management when you design data storage**
>
> When starting a project you should consider which items are being
> stored and if they need version management. For example in the Time
> Tracker program we expect that the client will request changes to the
> features, so we should consider versioning it from the start
>
> Everytime a new version of a program is installed, we then have to go
> through the process of updating the underlying data to the new version
>
> When writing a program for a customer, you should consider how long it
> will take to write code that deal with data updates (or migrations).
> This can make trivial programs significantly more complex

#### The `__str__` Method in a Class

- Each time we add a new attribute to the `Contact` class we have to
  modify `display_contact`

- Would be nice just to be able to print a `Contact` directly

- However, doing so, we find the output is pretty useless (using the
  mock below)

  ``` python
    class Contact:
        def __init__(self, name, address, telephone):
            self.name = name
            self.address = address
            self.telephone = telephone

    contact = Contact("Rob Miles", "Pussycat Mews", "1234")

    def display_contact(contact):
        print(contact)

    display_contact(contact)
  ```

      <__main__.Contact object at 0x7fdb885cc500>

- default for objects is the class name following by the memory address
  of the object

- python objects have a `__str__` method

  - Used whenever the an object needs to be converted to a string

- To change the default behaviour for our objects we need to redefine
  `__str__`

  ``` python
    class Contact:
        ...
        def __str__(self):
            return "Name: " + self.name + "\n" + \
            "Address: " + self.address + "\n" + \
            "Telephone: " + self.telephone + "\n" + \
            "Hours on the case: " + str(self.hours_worked) + "\n" + \
            "Amount to bill: " + str(self.billing_amount)
  ```

- The `\` character above is used to continue the string onto a new line

- printing now, we get what we expect

  ``` python
    display_contact(contact)
  ```

      Name: Rob Miles
      Address: Pussycat Mews
      Telephone: 1234
      Hours on the case: 0
      Amount to bill: 0

##### Python String Formatting

- Writing the string as a series of concatenations isn’t the cleanest
- Difficult to maintain and ensure correctness as we modify the class
- We can use `format` to create a formatted string
  - Lets us write a shorter string
  - `format` is a string method
  - `format` takes in values as arguments and injects them into the
    string

  ``` python
    class Contact:
        ...
        def __str__(self):
            template = """Name: {0}
  Address: {1}
  Telephone: {2}
  Hours on the case: {3}
  Amount to bill: {4}"""
            return template.format(self.name, self.address, self.telephone, self.hours_worked, self.billing_amount)
  ```

- Values in format are inserted at marked points in the string
- Marked points are `{n}` where $n$ is the index of the argument to
  substitue
  - Starting from $0$

##### Make Something Happen: Adventures with String Formatting

*Open the python interpreter and work through the following steps to
understand how string formatting works*

*Enter the statements below*

``` python
name = "Rob Miles"
age = 21
```

The above creates two variables `name` and `age`

*Now create the following template string*

``` python
template = "My name is {0} and my age is {1}"
```

The just creates a string called `template`, `{0}` and `{1}` are two
placeholder indicators for the `format` function

*Now call the* `format` *method on* `template`

``` python
template.format(name, age)
```

    'My name is Rob Miles and my age is 21'

As we can see the placeholder values have been substituted with the
values of the `name` and `age` value

*We can add additional formatting information. Redefine and format the
template as follows*

``` python
template = "My name is {0:20} and my age is {1:10}"
template.format(name, age)
```

    'My name is Rob Miles            and my age is         21'

We write the placeholder as `{n:w}` where $n$ is the index of the
placeholder. $w$ is the width value, as you can see from above, the
value is still substituted but then spaces are added to pad out to the
width. This is useful for defining columns. We use a `:` to seperate the
*format specifiers* from the placeholder index

For floating point values you can also specify the number of decimal
places to be printed

``` python
template = "My name is {0:20} and my age is {1:10.2f}"
template.format(name, age)
```

    'My name is Rob Miles            and my age is      21.00'

The above now prints the age with two decimal places. The full details
of the string formatting mini language can be found at the [python
docs](https://docs.python.org/3/library/string.html#format-string-syntax)

You can find the full version of Time Tracker using the string method in

### Session Tracking in Time Tracker

- Our client now gives us a new scenario

> The client would like to record *when* each specific session for a
> contact took place. You and the client specify the following design,
>
> ``` text
>
> Time Tracker
> 1. New Contact
> 2. Find Contact
> 3. Edit Contact
> 4. Add Session
> 5. Exit Program
>
> Enter you command: 2
> Enter  the contact name: Rob
> Name: Rob Miles
> Address: 18 Pussycat Mews, London, NE1 410S
> Telephone: 1234 56789
> Hours on the case: 10.0
> Amount to bill: 470.0
> Sessions
> Date: Mon Jul 10 11:30:00 2017 Length: 1.0
> Date: Tue Jul 12 11:30:00 2017 Length: 2.0
> Date: Wed Jul 19 11:30:00 2017 Length: 2.5
> Date: Wed Jul 26 10:30:00 2017 Length: 2.5
> Date: Mon Jul 31 16:51:45 2017 Length: 1.0
> Date: Mon Aug 14 16:51:45 2017 Length: 1.0
> ```

- Finding a contact now displays the sessions as a list
- Not immediately clear how we would add this to our class

#### Code Analysis: Creating a Session Class

*Let’s do some design work, for handling a session. Work through the
following questions*

1. *How will we store information about a session?*

    - We need to store a bunch of heterogenous related data

    - Good idea to consider a class, say `Session`

    - Need to consider data to store

      1. length of a session
      2. date and time of the session

    - We should also move the `Contact` class attributes validating a
      session length to the `Session` class

    ``` python
     import time
     class Session:
         """
         Session with a length and a date time it was conducted
         """

         __min_session_length = 0.5
         __max_session_length = 3.5

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
             if (
                 session_length < Session.__min_session_length
                 or session_length > Session.__max_session_length
             ):
                 return False
             return True

         def __init__(self, session_length):
             """
             Create a new Session instance

             Parameters
             ----------
             session_length : int | float
                 length of a session

             Raises
             ------
             Exception
                 Raised if `session_length` is invalid

             See Also
             --------
             Session.valid_session_length : validates session lengths
             """
             if not Session.valid_session_length(session_length):
                 raise Exception("Invalid session length")
             self.__session_length = session_length
             self.__session_end_time = time.localtime()
             self.__version = 1
    ```

    - We can now create `Session` objects

      ``` python
        session_length = 2
        session_record = Session(session_length)
        print(session_record)
      ```

          <__main__.Session object at 0x7fdb88739520>

    - creates a `Session` with the passed `session_length` parameter

    - `validate_session_length` moved to `Session`

      - validates session lengths at object creation
      - Exception raised if invalid session length is passed

    - `__init__` uses `time` library to get the local time

      - Stored in `__session_end_time` attribute

2. *Are we using version control for the* `Session` *class?*

    - Yes

    - Highly likely the `Session` object might change

    - Especially if we change our mind on what responsibility is in the
      `Contact` class vs the `Session` class

    - Thus also want to implement a `check_version` method

      ``` python
        def check_version(self):
            """
            Check the version of a Contact instance

            Upgrades the instance to the most recent version
            if required
            """
            pass
      ```

    - Currently does nothing

      - All `Session` instances will be versioned
      - Only one version, so no need to edit

3. *How will we allow users of the* `Session` *class to get the session
    length and session end time items from a* `Session` *object?*

    - We add these as properties
    - Want these to be read-only so no setter is provided

    ``` python
     @property
     def session_length(self):
         """
         session_length : int | float
             length (in hours) of this session
         """
         return self.__session_length

     @property
     def session_end_time(self):
         """
         session_end_time : time.struct_time
             date and time of the session
         """
         return self.__session_end_time
    ```

4. *Will the* `Session` *class have a* `__str__` *method?*

    - Yes
    - Return a string describing a `Session` instance

    ``` python
     def __str__(self):
         template = "Date: {0} Length: {1}"
         #convert time object string
         date_string = time.asctime(self.__session_end_time)
         return template.format(date_string, self.__session_length)
    ```

    - `time` library contains `asctime`
      - Takes a `localtime` value and returns a string representation
    - Then format the string

- Given the `Session` object, we now need to incorporate this into the
  `Contact` object

- `Contact` objects contain a list of sessions

  - Initialised empty

- We also need to bump the version number

  - Which means we also need to update the `check_version` method
  - Now need to handle the conversion from no version to version 2 and
    version 1 to version 2

  ``` python
    def check_version(self):
        """
        Check the version of a Contact instance

        Upgrades the instance to the most recent version
        if required. This includes upgrading any Session
        instances associated with this Contact instance

        See Also
        --------
        Session.check_version : Checks and upgrades Session instances
        """
        try:
            if self.__version == 1:
                # does not have session list
                self.__sessions = []
                self.__version = 2
        except AttributeError:
            self.__billing_amount = 0
            self.__sessions = []
            self.__version = 2

        # now upgrade all sessions in a contact
        for session in self.__sessions:
            session.check_version()
  ```

- Any version $1$ instance will be upgraded to version $2$

- For old, unversioned instances, we still use the `try...except` to
  force an upgrade to the most recent

- We also want to check that the sessions stored with a `Contact` are up
  to date

  - So after upgrading a `Contact` we check that the `Session` instances
    are up to date

- We’ve written the code so that if the `Session` is upgraded, instances
  will still be upgraded *even* if the `Contact` object is the most
  recent version

- We now need to modify adding a session to add a new `Session`
  instance, rather than just update the hours

  ``` python
    def add_session(self, session_length):
        """
        Adds a session (in hours) to the Contacts sessions

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
        try:
            self.__sessions.append(Session(session_length))
            self.__hours_worked = self.__hours_worked + session_length
            amount_to_bill = Contact.__open_fee + (
                Contact.__hourly_fee * session_length
            )
            self.__billing_amount = self.__billing_amount + amount_to_bill
        except Exception as e:
            print(e)
  ```

- We could validate the session length in `add_session` explicitly

  - However, the `Session` constructor does this, via exceptions

- We first try to create the `Session`

  - If it’s invalid we get an exception which we catch and handle

- If created successfully we then update the hours worked and amount to
  bill

- Last step is to now work out how we want to display our `Session`
  instances when we report on a client

  - Our client wants a line for each individual session
  - We need to convert the list of sessions to a string in this format

  ``` python
    @property
    def session_report(self):
        """
        session_report : str
            provides a string representation of a Contact's sessions
        """

        # map converts each session to a string
        report_strings = map(str, self.__sessions)
        result = "\n".join(report_strings)
        return result
  ```

- Uses `map` to convert a list of session objects to a list of their
  string representations

- Uses `join` to then convert the list of strings to a single string
  with each element seperated by a newline

#### The Python `map` Function

- Our aim is to convert a list of `Session` objects into a list of
  strings

- Could do this with a loop

- Alternative is to use `map`

- `map` takes two arguments

  1. A function name
      - The function must accept a single argument and return a result
  2. List of items to apply the function to

- functions can be stored in variables and passed as arguments

- `map` applies the function provided (first argument) to the list
  (second argument) and returns the result

##### Make Something Happen: Investigating the `map` Function and Iteration

*These next few steps go on for a quite a while. So work through it at
your own pace. However, this will give you a good understanding of not
just* `map` *but also some fundamentals for python*

*Open up a python interpreter and work through the following steps.
We’ll use* `map` *to indent a list of strings. Run the following steps*

``` python
code = ['line1', 'line2', 'line3']
```

This creates a list containing three strings, we can easily view the
contents

``` python
code
```

    ['line1', 'line2', 'line3']

*Now we need to create our indentation function. We can do this by
adding four spaces (or a tab etc.) at the beginning of a string. Define
the following python funcion*

``` python
def indent(x):
    return "    " + x
```

We can test this function, on a sample string,

``` python
print("Rob")
indent("Rob")
```

    Rob

    '    Rob'

We would like to apply the `indent` function to every string in the
`code` list. We could do this using a `for` loop, instead we use a `map`
function

*Now run the following statements*

``` python
indented_code = map(indent, code)
indented_code
```

    <map at 0x7fdb88557f70>

Naively we expected a list of indented strings. Instead we have
something called a *map object*. `map` returns something called an
iterator. Iterators return items from a collection or sequence one at a
time. We can work through iterators using a `for` loop. This is how we
can work through lists. `range` also returns an iterator

*Now run the following* `for` *loop to get the* `indented_code` *values*

``` python
for s in indented_code:
    print(s)
```

        line1
        line2
        line3

Now we have the list of strings as we were expecting. Each time around
the loop the next `s` value is retrieved from the iterator

Iterators allow us to save memory, rather than having to store the
entire result in memory we can simply generate each one as needed. Each
time we ask for a new result from the map object, `map` gets the next
value from the original collection (`code`) and applies the function
`indent` to it. Once the map iterator runs out of values to return, it
raises `StopIteration` as an exception. This stops the loop.

Lets explore this in more detail

*Recreate the statement creating the map*

``` python
indented_code = map(indent, code)
```

We can then ask for the next item from an iterator using the `__next__`
method.

*Call this method on* `indented_code`

``` python
indented_code.__next__()
```

    '    line1'

We can see this produces the *next* value, though in this case, it’s the
first item. We can keep repeating this

*Run the following*

``` python
print(indented_code.__next__())
print(indented_code.__next__())
print(indented_code.__next__())
```

        line2
        line3

    StopIteration:
    ---------------------------------------------------------------------------
    StopIteration                             Traceback (most recent call last)
    Cell In[54], line 3
          1 print(indented_code.__next__())
          2 print(indented_code.__next__())
    ----> 3 print(indented_code.__next__())

    StopIteration:

We can see that we get the next two items from the iterator, and then
finally after trying to get an non-existent value we see a
`StopIteration` exception is raised

*You can’t reuse a iterator once it has run out of items. You have to
recreate it*

``` python
indent_iterator = map(indent, code)
```

If we want to convert this to normal collection, we can do something
like call `list` to convert to a list

*Check this out by running the following statements*

``` python
indented_code = list(indent_iterator)
indented_code
```

    ['    line1', '    line2', '    line3']

What happens if we make the input of a `map` function an iterator

*Enter the following statements to explore*

``` python
i1 = map(indent, code)
i2 = map(indent, i1)
```

We first create the iterator `i1` to apply the `indent` function to the
list `code`. We then create a second iterator `i2` to apply the `indent`
function to the items of the `i1` iterator

*Use* `list` *to convert* `i2` *to a list*

``` python
list(i2)
```

    ['        line1', '        line2', '        line3']

We can see that each item is indented twice. Once by `i1` and again by
`i2`. Observe that the nested iterator `i1` was also applied as part of
the conversion process. Python makes it very easy to chain iterators
together

Let us return to our original use of `map`

``` python
report_strings = map(str, self.__sessions)
```

Here `self.__sessions` is a list of `Session` objects. `map` creates an
iterator that applies `str` to each element of `self.__sessions`. `str`
itself converts each `Session` to a string by calling the `__str__`
method. We then use the `join` method to work through this iterator to
build the final output string

#### The Python `join` Method

- We can call string methods on string literals, e.g.

  ``` python
    "FRED".lower()
  ```

      'fred'

- Another string method is `join`

- Takes an iterator as an argument

- `join` merges all strings in an iterator

  - the string on which `join` is called is inserted between each item

  ``` python
    report_strings = ["1", "2", "3"]
    report_results = "\n".join(report_strings)
  ```

##### Make Something Happen: Investigating the `join` Function

*Work through the following steps with the python interpreter to
understand* `join`

*Enter the statement below*

``` python
report_strings = ["report1", "report2", "report3", "report4"]
```

The above creates a list of four strings, `report_strings`. Lists are
iterators so we can pass this to `join`

*Call the join function as below*

``` python
"**".join(report_strings)
```

    'report1**report2**report3**report4'

As observed we iterate over the strings, merging them with `**` inserted
in between. Observe that `**` is not placed at the start or end of the
resulting string

*Rerun the statement with the newline character below*

``` python
print("\n".join(report_strings))
```

    report1
    report2
    report3
    report4

This does the same but instead each string is printed on its own line

We can use `join` to concatenate strings by using the empty string

*Run the following statement*

``` python
"".join(report_strings)
```

    'report1report2report3report4'

- After this discussion, we have completed this version of the Time
  Tracker

- Aside from one final thing, updating the `__str__` method in `Contact`
  to use the `session_report` property

  ``` python
    def __str__(self):
        template = """Name: {0}
    Address: {1}
    Telephone: {2}
    Hours on the case: {3}
    Amount to bill: {4}
    Sessions: \n{5}"""
        return template.format(
            self.name,
            self.address,
            self.telephone,
            self.hours_worked,
            self.billing_amount,
            self.session_report,
        )
  ```

- You can find the final implementation in [Time Tracker with Session
  History](./Examples/14_TimeTrackerWithSessionHistory/TimeTrackerWithSessionHistory.py)

#### Exercise: Playlist Storage App

*The time tracker application is a very good starting point for any
program that you might like to write that stores and manages
information. You could replace the sessions with albums and music
tracks, salesman and sales artists and pictures - or anything else you
want to track*

In the previous chapter we created a [Music Storage
app](../09_UsingClasses/Chapter_09_ExtensionExercises.qmd#make-something-happen-music-storage-app)
that stored songs and could be used to manage a single playlist. Using
the framework provided by [Time Tracker](#create-a-time-tracker) extend
the Music Storage app to be able to manage and store multiple playlists
at a time

Thankfully this isn’t as in depth as building the application the first
time around. We start by defining our `Playlist` class

Let us first focus on the data attributes, we want a name and a list of
songs. We also want the total runtime. Now for simplicity we’ll leave
the `name` and `tracks` as public attributes, but we’ll define the
`runtime` as a property, intefacing with a protected variable
`__runtime`. We do this because the runtime is calculated from `tracks`
so we don’t want the caller to modify it themselves.

Inspired by Time Tracker’s `session_report` we’ll also define a
`track_report` property using that interfaces with `map` to provide a
string representation of the tracks in a playlist where each track is on
its own line

``` python
class Playlist:
    """
    A class representing a music playlist with a name and list of tracks

    Tracks and records the length of the playlist
    """

    def __init__(self, name, tracks=[]):
        """
        Create a new Playlist instance

        Parameters
        ----------
        name : str
            name to associate with the playlist
        tracks : list, optional
            list of songs in the playlist, by default []
        """
        self.name = name
        self.tracks = tracks
        self.__runtime = 0
        for song in self.tracks:
            self.__runtime += song.length_in_seconds

    def __str__(self):
        template = """Playlist: {0}
Total Length: {1} s
Songs:
{2}"""
        return template.format(self.name, self.runtime, self.track_report)

    @property
    def runtime(self):
        """
        runtime : int
            total run time of the playlist in seconds
        """
        return self.__runtime

    @property
    def track_report(self):
        """
        track_report : str
            string representation of tracks in the playlist, giving each track
            on its own line
        """
        song_strings = map(str, self.tracks)
        return "\n".join(song_strings)
```

Observe that the constructor takes an optional list of tracks (by
default its empty). This means that a user can create a `Playlist` by
name only and then add songs to it (as used in `create_playlist` below)
or we can create a playlist with a list of songs already (as used by
`suggest_playlist_of_given_length`)

Now we want to keep the internal track list and the runtime
synchronised, so we add methods on the `Playlist` class to handle
adding, removing and clearing tracks from the playlist

``` python
def add_track(self, track):
    """
    Add a new track to the playlist

    Updates the playlist length

    Parameters
    ----------
    track : MusicTrack
        track to add to the playlist

    Returns
    -------
    None

    See Also
    --------
    Playlist.remove_track : removes a track from a playlist
    """
    # first update runtime so a non-track objects causes an error
    self.__runtime += track.length_in_seconds
    self.tracks.append(track)

def remove_track(self, track):
    """
    Remove a track from the playlist

    Parameters
    ----------
    track : MusicTrack
        track to remove from the playlist

    See Also
    --------
    Playlist.add_track : add a track to a playlist
    Playlist.clear_tracks : remove all tracks from a playlist
    """
    try:
        self.tracks.remove(track)
        self.__runtime -= track.length_in_seconds
    except ValueError:
        print("Could not find track:", track.name, "in the playlist")

def clear_tracks(self):
    """
    Remove all tracks from a playlist

    Runtime is set to 0
    """
    self.tracks.clear()
    self.__runtime = 0
```

These are all relatively simple, the takeaway is that as we update the
track list, we also ensure the runtime is kept synchronised

> [!WARNING]
>
> **It is important to keep data synchronised**
>
> We store the runtime as a seperate variable so that we don’t need to
> calculate it on the fly everytime a function requires it. However this
> introduces the difficulty that we have to keep `runtime` synched with
> the data it is representing (the sum of the length of the tracks in
> the `tracks` attribute). This is important in real world scenarios, as
> if these two data attributes diverge we might get nonsense results.
>
> This is actually one of the big reasons why we like to make data
> attributes private, it ensures we can maintain the relationships
> between elements.

As written our code has the problem that data could become
desynchronised because the user can directly modify the `tracks` list.
We can’t get around this easily by making a read-only property, because
it we return a reference to a list, than any changes on that reference
would propagate to the original list

One option would be to provide a deep copy (a unique copy for each
call), or another would be make `tracks` private and define methods on
the class for all the nessecary interactions. I haven’t done this to
minimise the disruption to the overall API, since this current API lets
us reuse the adding and searching functionality we defined for the
complete list of tracks. This could be something we change in the future

Lets now consider how we want to program to work. Previously we had one
playlist. Now like the tracks, we want a list of them. However we still
want to be able to work on and modify a playlist. To minimise the
changes from the original design lets use the following approach

1. There will be a list of playlists
    - These will be loaded and saved to memory like the track list
2. There will be one active playlist at a time
    - At the start there is no active playlist
    - The user can create a new playlist
    - The user can select an existing playlist
    - The user can use the existing playlist generation feature

By keeping the one active global playlist we can minimise the disruption
to our program. We can reuse existing functions making note that the
current playlist has changed from a list of tracks to a `Playlist`
object

Our new Playlist menu now looks like,

``` python
def run_playlist_management_menu():
    """
    Provides the user with a looping playlist menu

    1. Create a new playlist
    2. Select playlist
    3. Get a suggested playlist of a target length
    4. Add a track to the playlist
    5. Remove a track from the playlist
    6. Clear the playlist
    7. Display the playlist
    8. Show the runtime of the playlist
    9. Export the current playlist
    10. Return to the main menu

    Returns
    -------
    None

    Raises
    ------
    ValueError
        An invalid number is encountered in menu selection, should not
        occur in live code, please raise a bug report if encountered
    """
    playlist_management_menu = """Playlist Management
Current playlist is {0}

1. Create a new playlist
2. Select playlist
3. Get a suggested playlist of a target length
4. Add a track to the playlist
5. Remove a track from the playlist
6. Clear the playlist
7. Display the playlist
8. Show the runtime of the playlist
9. Export the current playlist
10. Return to the main menu

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            prompt=playlist_management_menu.format(current_playlist.name),
            min_value=1,
            max_value=10,
        )
        if command == 1:
            create_playlist()
        elif command == 2:
            select_playlist()
        elif command == 3:
            suggest_playlist_of_given_length()
        elif command == 10:
            break
        elif current_playlist.name == "None":
            print("There is no active playlist. Please select or create one")
            continue
        elif command == 4:
            add_track_to_playlist()
        elif command == 5:
            remove_tracks_from_playlist()
        elif command == 6:
            clear_playlist()
        elif command == 7:
            display_playlist(current_playlist, name_only=False)
        elif command == 8:
            calculate_playlist_length()
        elif command == 9:
            export_playlist()
        else:
            raise ValueError(
                "Invalid command id "
                + str(command)
                + " found in playlist management sub-menu"
            )
```

You can see that we’ve defined new functions,

1. `create_playlist`
2. `select_playlist`
3. `display_playlist`

and that we’ve renamed the old `save_playlist` function to
`export_playlist`. This last change is because we’ve introduced
`save_playlists` and `load_playlists` as functions to pickle and
unpickle the playlists binary data. Renaming `save_playlist` to
`export_playlist` makes it clear that this function is not related to
those two.

You also might notice that we’ve reordered the menu so that all the
functions dealing with changing the current playlist (`create_playlist`,
`select_playlist`, `suggest_playlist_of_given_length`) come first. This
allows us to then check that we have an active playlist before running
any of the other commands. We also check if user has decided to exit
here to, since if we put it after the check for an active playlist the
user can’t exit the playlist menu if the don’t have an active playlist

As mentioned, at the start there is no active playlist. Now the simplest
way to implement this would be to initially set the `current_playlist`
to `None`. However you can see this has a problem, we want the playlist
menu to display the name of the current playlist, this doesn’t work if
the current playlist is `None`. We could add some error checking, but
we’ll instead use a technique called a `None` or `Null` object. This is
an instance of an object that is designed to represent cases where the
object does not actually exist. For us, we simply define a `Playlist`
with the name `None`

``` python
# null object
no_playlist = Playlist(name="None")
current_playlist = no_playlist
```

Let us look now at the new functions we’ve defined, the first pair

``` python
def valid_playlist_name(name):
    """
    Verifies that a playlist name is valid

    Playlist names must be unique

    Parameters
    ----------
    name : str
        proposed name for a playlist

    Returns
    -------
    bool
        `True` if playlist name is valid else, `False`
    """
    if name == "None":
        return False
    for playlist in playlists:
        if name == playlist.name:
            return False
    return True


def create_playlist(tracks=[]):
    """
    Create a new playlist and make it the active playlist

    Prompts the user for a new name for the playlist, and ensures its valid
    then constructs a playlist and sets it as the current active playlist

    Parameters
    ----------
    tracks : list, optional
        tracks to assign to the playlist, by default []

    See Also
    --------
    valid_playlist_name : validates a playlist name
    Playlist : class used to represent a playlist
    """
    print("Create a new playlist")
    global current_playlist

    new_playlist_name = BTCInput.read_text("Enter the playlist name: ")
    while not valid_playlist_name(new_playlist_name):
        print("That playlist name is already in use")
        new_playlist_name = BTCInput.read_text("Enter the playlist name: ")

    new_playlist = Playlist(new_playlist_name, tracks)
    current_playlist = new_playlist
    playlists.append(new_playlist)
```

Prompts the user for the name of a new playlist. We add code that means
the user can’t override the `NoneObject` or use duplicate names which is
given by the function `valid_playlist_name`. Unlike the validation code
in the Time Tracker this is not in the class, because it is part of the
business logic of the application layer, not the playlist itself

We then define the `select_playlist` function,

``` python
def select_playlist():
    """
    Select an existing playlist to be the current playlist

    Prompts the user for a search name then returns all playlists
    that match that string. The user will be displayed each playlist
    in turn and asked if they want to make that the current playlist

    Notes
    -----
    Passing the empty string can be used to display all playlists
    """
    print("Select a playlist")
    global current_playlist

    search_name = BTCInput.read_text("Enter playlist name (enter to see ): ")

    matched_playlists = []

    for playlist in playlists:
        if playlist.name.strip().lower().startswith(search_name.strip().lower()):
            matched_playlists.append(playlist)

    if len(matched_playlists) > 0:
        print("Found {0} matches".format(len(matched_playlists)))
        for playlist in matched_playlists:
            display_playlist(playlist)
            select = BTCInput.read_int_ranged(
                "Select this playlist? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            )
            if select:
                current_playlist = playlist
                return
    else:
        print("No playlists found matching that name")
```

Since no other method needs to search for playlist names, we forgo our
usual pattern of defining a `find` and `filter` function and just
combine it all in the one function. Additionally `select` is also used
for letting the user see what playlists are stored in the program. A
future version might add an explicit function called this (perhaps
`list_playlists`)

This program works pretty simply. We use the standard name matching
pattern, then for each match the user is shown the playlist name and
runtime, and is given the option to select it. If they do then the
current playlist is set to that playlist and the function ends, else it
continues to the next.

Lastly we have our `display_playlist` function, to print a playlist

``` python
def display_playlist(playlist, name_only=True):
    """
    Display a playlist

    Can optionally list all the tracks or just the name and length

    Parameters
    ----------
    playlist : Playlist
        playlist to display
    name_only : bool, optional
        only display the playlists name and runtime, by default `True`

    Returns
    -------
    None
    """
    if name_only:
        print("{0} ({1} s)".format(playlist.name, playlist.runtime))
    else:
        print(playlist)
```

The optional `name_only` parameter is used indicate that we only want to
print the playlist name and length, otherwise we defer to the `Playlist`
`__str__` method and print everything.

This captures the last of the high level changes. As mentioned, we have
to make minor changes to the existing functions, such as to
`suggest_playlist_of_given_length` shown below

``` python
def suggest_playlist_of_given_length():
    """
    Suggests a playlist of length less than or equal to
    a user prompted length

    Asks the user for a maximum playlist length, and
    then suggests a playlist by combining tracks randomly
    such that the suggested playlist is no greater than
    the length

    The user has the option to review the proposed list
    and either accept, reject or regenerate the list

    Returns
    -------
    None
    """
    print("Suggest playlist of given length")
    global current_playlist

    target_length = read_min_valued_integer(
        "Enter maximum playlist length: ", min_value=1
    )

    while True:
        suggested_tracks = []
        suggested_tracks_total_length = 0
        # find tracks that could fit in the playlist
        candidate_songs = filter_tracks_shorter_than_length(target_length, tracks)

        if len(candidate_songs) == 0:
            print("Could not generate a playlist of that length. Try a longer playlist")
            return

        while len(candidate_songs) > 0:  # stop when no more eligable songs
            # add a random song and update the playlist length
            song_choice = random.choice(candidate_songs)
            suggested_tracks.append(song_choice)
            suggested_tracks_total_length = (
                suggested_tracks_total_length + song_choice.length_in_seconds
            )

            # filter out songs that no longer fit
            candidate_songs = filter_tracks_shorter_than_length(
                target_length - suggested_tracks_total_length, candidate_songs
            )
        print("Generated a playlist...")
        # let the user review the playlist
        display_tracks(suggested_tracks)
        if BTCInput.read_int_ranged(
            "Accept this playlist? (1 - Yes, 0 - No): ", min_value=0, max_value=1
        ):
            create_playlist(suggested_tracks)
            return
        else:
            if BTCInput.read_int_ranged(
                "Generate again? (1 - Yes, 0 - No): ", min_value=0, max_value=1
            ):
                continue
            return
```

Here we still build up the suggested playlist as before (using a list)
but once the user decides to keep this playlist, we then call
`create_playlist` passing in the track list to create a proper named
`Playlist` object

You are encouraged to work through the full program yourself
([PlaylistStorage.py](./Exercises/01_PlaylistStorageApp/PlaylistStorage.py))

### Make Music with Snaps

- Let’s build a simple music keyboard

- We’ll add a simple music player

- Extend with some playback options

- The snaps library code provides some music notes to use

  - stored in `MusicNotes`

  - `play_note` lets us play a note

    > [!WARNING]
    >
    > If when running the program you get a file not found error, you
    > may need to modify the path in `play_note` to either
    > `MusicNotes\\` or `MusicNotes/`
    >
    > This path is relative to snaps and so the folder must in the same
    > directory as snaps

- We can start with a simple program that [plays all the
  notes](./Examples/15_MusicWithSnaps/01_PlayNotes.py),

  ``` python
    # Example 10.15.1 Play Notes
    #
    # Demonstrates using snaps to play notes

    import time

    import snaps

    for note in range(0, 13):
        snaps.play_note(note)
        time.sleep(0.5)
    input("Press enter to continue...")
  ```

- We use `time.sleep(0.5)` to stagger playing the notes

- We could also play a tune,

  ``` python
    # Example 10.15.2 Twinkle Twinkle
    #
    # Uses snaps to play a simple tune

    import time

    import snaps

    snaps.play_note(0)
    time.sleep(0.4)
    snaps.play_note(0)
    time.sleep(0.4)
    snaps.play_note(7)
    time.sleep(0.4)
    snaps.play_note(7)
    time.sleep(0.4)
    snaps.play_note(9)
    time.sleep(0.4)
    snaps.play_note(9)
    time.sleep(0.4)
    snaps.play_note(7)
    time.sleep(0.8)
    snaps.play_note(5)
    time.sleep(0.4)
    snaps.play_note(5)
    time.sleep(0.4)
    snaps.play_note(4)
    time.sleep(0.4)
    snaps.play_note(4)
    time.sleep(0.4)
    snaps.play_note(2)
    time.sleep(0.4)
    snaps.play_note(2)
    time.sleep(0.4)
    snaps.play_note(0)
    time.sleep(0.8)
  ```

- We can see this is already becoming tedious

- We repeatedly write the `play_note` followed by a `sleep` time

- Have to manuually modify the code

- We could make this *data-driven*

- We supply a list of tuples

  - Each tuple contains the id for a note and the time to sleep after
    playing that note

- Then simply loop over the list to play the tune

- Can then play anything by just changing the embedded data

  ``` python
    # Example 10.15.3 Twinkle Twinkle with Tuples
    #
    # Converts play notes to a data-driven program using tuples to specify notes
    # and how long to pause after

    import time

    import snaps

    tune = [
        (0, 0.4),
        (0, 0.4),
        (7, 0.4),
        (7, 0.4),
        (9, 0.4),
        (9, 0.4),
        (7, 0.8),
        (5, 0.4),
        (5, 0.4),
        (4, 0.4),
        (4, 0.4),
        (2, 0.4),
        (2, 0.4),
        (0, 0.8),
    ]

    for note in tune:
        note_id, sleep_time = note
        snaps.play_note(note_id)
        time.sleep(sleep_time)
  ```

- Each tuple stores the note and the sleep time

- We then loop over the tuples

- We use unpacking to assign the elements of the tuple meaningful names
  (`note_id` and `sleep_time`)

- While playback is simple, constructing is not nessecarily

  - The tuples are undocumented and rely on the programmer knowing the
    indices

- We could instead define a lightweight class

  ``` python
    # Example 10.15.4 Twinkle Twinkle with Classes
    #
    # Modifies the data driven tuple implementation by definining a lightweight
    # Note class

    import time

    import snaps


    class Note:
        """
        Musical note with a playback duration.
        """

        def __init__(self, note, duration):
            """
            Create a Note instance

            Parameters
            ----------
            note : int
                id of the note to play
            duration : int | float
                duration of the note
            """
            self.__note = note
            self.__duration = duration

        def play(self):
            """
            play the note

            plays the note then pauses for the specified duration
            """
            snaps.play_note(self.__note)
            time.sleep(self.__duration)


    tune = [
        Note(note=0, duration=0.4),
        Note(note=0, duration=0.4),
        Note(note=7, duration=0.4),
        Note(note=7, duration=0.4),
        Note(note=9, duration=0.4),
        Note(note=9, duration=0.4),
        Note(note=7, duration=0.8),
        Note(note=5, duration=0.4),
        Note(note=5, duration=0.4),
        Note(note=4, duration=0.4),
        Note(note=4, duration=0.4),
        Note(note=2, duration=0.4),
        Note(note=2, duration=0.4),
        Note(note=0, duration=0.8),
    ]

    for note in tune:
        note.play()
  ```

- `Note` is a lightweight class holding the note’s id and the note
  duration

  - Keep these private, since no need to access once set

- `Note` has a `play` method that captures playing a note

- Program then defines a list of `Note` objects which are then played

#### Code Analysis: The `Note` Class

*Consider the following questions about the design of the note class*

1. *Why does the* `Note` *class contain a* `Play` *method?*

    - cohesion
    - `Note` contains all the information about a note
    - So should keep the behaviour with the information, i.e. in the
      `Note` class
    - If we want to change how a note is played we can change it in the
      `Note` class without impacting downstream callers
      - So long as we keep the same API

2. *Could the* `Note` *class have a* `__str__` *method?*

    - It’s probably a good idea

    - A simple implementation is,

      ``` python
      def __str__(self):
        template = "Note: {0} Duration: {1}"
        return template.format(self.__note, self.duration)
      ```

    - We can then print the tune super easily,

      ``` python
        tune_strings = map(str, tune)
        print("\n".join(tune_strings))
      ```

- All the music playing examples can be found in the [Music With
  Snaps](./Examples/15_MusicWithSnaps) example folder

#### Make Something Happen: Make Your Own Music

*Modify the sample programs to make your own tunes*

For fun we’ll make two little tunes

1. The classic [Macca’s
    jingle](./Exercises/02_SnapsTunes/MaccasJingle.py)

    ``` python
     # Exercise 10.2.1 Maccas Jingle
     #
     # Uses the Note playback program to play the Maccas jingle

     import time

     import snaps


     class Note:
         """
         Musical note with a playback duration.
         """

         def __init__(self, note, duration):
             """
             Create a Note instance

             Parameters
             ----------
             note : int
                 id of the note to play
             duration : int | float
                 duration of the note
             """
             self.__note = note
             self.__duration = duration

         def __str__(self):
             template = "Note: {0} Duration: {1}"
             return template.format(self.__note, self.__duration)

         def play(self):
             """
             play the note

             plays the note then pauses for the specified duration
             """
             snaps.play_note(self.__note)
             time.sleep(self.__duration)


     tune = [
         Note(note=7, duration=0.3),
         Note(note=11, duration=0.3),
         Note(note=2, duration=0.3),
         Note(note=5, duration=0.3),
         Note(note=7, duration=0.5),
     ]

     for note in tune:
         note.play()

     tune_strings = map(str, tune)
     print("\n".join(tune_strings))
    ```

    - This doesn’t sound exactly correct because we don’t have the
      correct octave progression in the provided wav files but we get a
      decent approximation
    - You might like to play around with the timings to see if you can
      make it better

2. [Three Blind Mice](./Exercises/02_SnapsTunes/ThreeBlindMice.py)

    ``` python
     # Exercise 10.2.2 Three Blind Mice
     #
     # Uses the Note playback program to play three blind mice

     import time

     import snaps


     class Note:
         """
         Musical note with a playback duration.
         """

         def __init__(self, note, duration):
             """
             Create a Note instance

             Parameters
             ----------
             note : int
                 id of the note to play
             duration : int | float
                 duration of the note
             """
             self.__note = note
             self.__duration = duration

         def __str__(self):
             template = "Note: {0} Duration: {1}"
             return template.format(self.__note, self.__duration)

         def play(self):
             """
             play the note

             plays the note then pauses for the specified duration
             """
             snaps.play_note(self.__note)
             time.sleep(self.__duration)


     tune = [
         Note(note=4, duration=0.4),
         Note(note=2, duration=0.4),
         Note(note=0, duration=0.8),
         Note(note=4, duration=0.4),
         Note(note=2, duration=0.4),
         Note(note=0, duration=0.8),
         Note(note=7, duration=0.4),
         Note(note=5, duration=0.4),
         Note(note=5, duration=0.4),
         Note(note=4, duration=0.8),
         Note(note=7, duration=0.4),
         Note(note=5, duration=0.4),
         Note(note=5, duration=0.4),
         Note(note=4, duration=0.8),
         Note(note=7, duration=0.4),
         Note(note=12, duration=0.4),
         Note(note=12, duration=0.4),
         Note(note=11, duration=0.4),
         Note(note=9, duration=0.4),
         Note(note=11, duration=0.4),
         Note(note=12, duration=0.4),
         Note(note=7, duration=0.4),
         Note(note=7, duration=0.8),
     ]

     for note in tune:
         note.play()

     tune_strings = map(str, tune)
     print("\n".join(tune_strings))
    ```

    - This one we get a much better sounding tune

#### Exercise: Simple Tune Creator

*By combining the structure and style of [Time
Tracker](#create-a-time-tracker) with the [music
playback](#make-music-with-snaps) provided by the* `Note` *class we
could make a simple program that lets users create, edit and play their
own tunes. Create this program. A user should be able to create a tune,
edit a tune, delete a tune and play a selected tune. Tunes should be
saved and persist between uses*

If you can follow the [Playlist Storage
App](#exercise-playlist-storage-app) and the [Recipe Storage
App](../09_UsingClasses/Chapter_09_ExtensionExercises.qmd#make-something-happen-recipe-storage-app)
then this program should fairly easy to follow

Let’s first define our `Note` class

``` python
class Note:
    """
    Musical note with a playback duration.

    Class Attributes
    ----------------
    min_note_id : int
        minimum valid note id
    max_note_id : int
        maximum valid note id
    """

    min_note_id = 0
    max_note_id = 12

    @staticmethod
    def valid_note(note):
        """
        Checks if a note id is valid

        Parameters
        ----------
        note : int
            id of the note to validate

        Returns
        -------
        bool
            `True` if note is valid, else `False`
        """
        if note < 0 or note > 12:
            return False
        return True

    def __init__(self, note, duration):
        """
        Create a Note instance

        Parameters
        ----------
        note : int
            id of the note to play
        duration : int | float
            duration of the note
        """
        if not Note.valid_note(note):
            raise ValueError(
                "invalid note {0} passed. note must be between {1} and {2}".format(
                    note, Note.min_note_id, Note.max_note_id
                )
            )
        self.__note = note
        self.__duration = duration

    @property
    def duration(self):
        """
        duration : str
            time in seconds the note is played for
        """
        return self.__duration

    def __str__(self):
        template = "Note: {0} Duration: {1}"
        return template.format(self.__note, self.__duration)

    def play(self):
        """
        play the note

        plays the note then pauses for the specified duration
        """
        snaps.play_note(self.__note)
        time.sleep(self.__duration)
```

This is pretty much the same as the `Note` class in the [Making Music
Section](#make-music-with-snaps). However we need the duration so that
we can report how long the total tune is so we add a read only property
for duration. Additionally since we’re now going to be taking user input
to create notes we’ll want to validate that input. It makes sense for it
to be in the `Note` class, so we define class variables `min_note_id`
and `max_note_id` and a corresponding validation method, `valid_note`
that can be used to check that a note (represented by an integer) is
valid. We leave the class variables as public so we can use them in the
prompts we display to the user

Now when making [our own
music](#make-something-happen-make-your-own-music), we used a list of
notes to create a tune. We want to use this structure but wrap it in a
class that captures behaviour. We’ll call this class `Tune`

``` python
class Tune:
    def __init__(self, name):
        """
        Create a new Tune instance

        Parameters
        ----------
        name : str
            name of the tune
        """
        self.name = name
        self.__notes = []
        self.__length = 0

    def __str__(self):
        notes_string = ""
        for idx, note in enumerate(map(str, self.__notes)):
            notes_string = notes_string + str(idx) + ": " + note + "\n"

        template = """name: {0}
duration: {1}
notes:
{2}
"""
        return template.format(self.name, self.__length, notes_string)

    @property
    def length(self):
        """
        length : int | float
            total length of the tune in seconds
        """
        return self.__length

    @property
    def number_of_notes(self):
        """
        number_of_notes : int
            number of notes in the tune
        """
        return len(self.__notes)
```

The class has a simple structure. The tune constructor only needs a
name, we then create an empty list of notes, and a seperate variable
that tracks the full length of the tune. Our string representation
(`__str__`) follows the usual pattern, we print the name and duration of
the `Tune`, the the list of `Note` objects in the tune. We use
`enumerate` to make this a numbered list with each item on its own line.
This is because most of our edits will require an index, so we want to
user to be able to easily see the index of all the notes. Additionally
we define two useful properties, one to get the length of the tune, and
the second that returns the total number of notes in the tune. Both
properties are read-only, while this last one is mostly used to help
with validating user input

As you can see the list of notes is private, so we also want to provide
some methods that allow us to modify the notes list

``` python
    def add_note(self, note, index=None):
        """
        Add a new note to the tune

        Adds a new note to the tune, if the index is specified
        the note is inserted at that index, else the note is appended

        Parameters
        ----------
        note : Note
            note to add to the tune
        index : int | None, optional
            index to insert the note at, if None, the Note is appended,
            by default None

        Returns
        -------
        None
        """
        if index is not None:
            self.__notes.insert(index, note)
        else:
            self.__notes.append(note)
        self.__length += note.duration

    def remove_note(self, index):
        """
        Remove a note from the tune

        Parameters
        ----------
        index : int
            index of the note to remove

        Returns
        -------
        Note
            the removed Note
        """
        try:
            note = self.__notes.pop(index)
            self.__length -= note.duration
            return note
        except IndexError:
            print("Failed to remove the {0}-th note".format(index + 1))

    def clear_tune(self):
        """
        Clear all notes from the tune

        Returns
        -------
        None
        """
        self.__notes.clear()
        self.__length = 0
```

The first `add_note` takes a note, and an optional index. If the index
is specified the note is inserted into the list (at the specified
index), otherwise we append it. The second `remove_note` *requires* an
index, and removes the note at that index. The removed note is returned
as part of this process. We also provide some error handling in case the
provided index does not actually exist. Last we provide a `clear_tune`
method which simply removes all the notes

The arguably most important function for the `Tune` class however is
`play` which simply plays the tune

``` python
    def play(self):
        """
        Plays the tune

        Returns
        -------
        None
        """
        for note in self.__notes:
            note.play()
```

We define our main menu function as,

``` python
def run_main_menu():
    first_option_id = 1
    last_option_id = 7

    main_menu_template = """Tune Editor
Current Tune: {0}

1. New Tune
2. List Tunes
3. Select Tune
4. Play Tune
5. Edit Tune
6. Delete Tune
7. Exit program

Enter your command: """

    while True:
        command = BTCInput.read_int_ranged(
            main_menu_template.format(current_tune.name),
            min_value=first_option_id,
            max_value=last_option_id,
        )
        if command == 1:
            new_tune()
        elif command == 2:
            list_tunes()
        elif command == 3:
            select_tune()
        elif command == 7:
            try:
                save_tunes(tune_file_name)
            except:  # noqa: E722
                print("Failed to save tunes")
            break
        elif current_tune.name == "None":
            print("No tune currently selected")
            continue
        elif command == 4:
            current_tune.play()
        elif command == 5:
            run_edit_menu()
        elif command == 6:
            delete_tune()
        else:
            raise ValueError(
                "Unexpected command id: {0} found in Main Menu".format(command)
            )
```

We use the same `save` and `load` paradigm as with all the previous
examples so we won’t look at that code again. Of the functions here we
have,

1. `new_tune`

    ``` python
     def valid_tune_name(name):
         """
         Verifies that a tune name is available

         Tune names must be unique

         Parameters
         ----------
         name : str
             proposed name for a tune

         Returns
         -------
         bool
             `True` if tune name is valid else, `False`
         """
         if name == "None":
             return False
         for tune in tunes:
             if name == tune.name:
                 return False
         return True


     def prompt_valid_name(prompt):
         """
         Prompts the user for a valid tune name

         Loops until a valid name is provided

         Parameters
         ----------
         prompt : str
             prompt to display to the user

         Returns
         -------
         str
             string containing a valid tune name
         """
         tune_name = BTCInput.read_text(prompt)
         while not valid_tune_name(tune_name):
             print("That tune name is already in use")
             tune_name = BTCInput.read_text(prompt)

         return tune_name


     def new_tune():
         """
         Create a new tune and make it the active tune

         Prompts the user for a new name for the tune, and ensures its valid
         then constructs a Tune and sets it as the current active tune

         Returns
         -------
         None

         See Also
         --------
         valid_tune_name : validates a tune name
         Tune : class used to represent a tune
         """
         print("New tune")
         global current_tune
         new_tune_name = prompt_valid_name("Enter the tune name: ")
         new_tune = Tune(new_tune_name)
         current_tune = new_tune
         tunes.append(new_tune)
    ```

    - We start by defining a function `valid_tune_name`
      - boolean function that ensures a proposed name is unique
      - returns `True` if the name is valid, else `False`
    - We then wrap this in `prompt_valid_name`
      - Since we want to reuse the code that gets a name from a user
        later
      - Prompts the user for a valid name, looping until one is received
      - Returns the valid name
    - Our `new_tune` is now simple
      - call `prompt_valid_name` to get a new name
      - Create a new `Tune` object
      - set the current tune to this new object
      - Add it to the tunes list

2. `list_tunes`

    ``` python
     def filter_tunes_by_name(search_name):
         """
         Finds tunes matching a search name

         Tunes are matched if their name is prefixed by the search name
         after normalisation (striping whitespace and lowercasing)

         Parameters
         ----------
         search_name : str
             name to search for (search uses prefix matching)

         Returns
         -------
         list[Tune]
             list of tunes matching the name. If no matches
             exist the list is empty

         """
         search_name = search_name.strip().lower()
         print(search_name)
         matched_tunes = []
         for tune in tunes:
             tune_name = tune.name.strip().lower()
             if tune_name.startswith(search_name):
                 matched_tunes.append(tune)
         return matched_tunes


     def list_tunes():
         """
         List all tunes matching a user-specified search string

         Returns
         -------
         None

         See Also
         --------
         filter_tunes_by_name : handles searching for tunes by name
         """
         print("List tunes")
         search_name = BTCInput.read_text("Tune names to search (press enter for all): ")
         matched_tunes = filter_tunes_by_name(search_name)
         if len(matched_tunes) == 0:
             print("No matches found")
             return
         print("Found {0} matches".format(len(matched_tunes)))
         for tune in matched_tunes:
             print("- {0} ({1:.2f} s)".format(tune.name, tune.length))
    ```

    - We use the usual pattern of defining a `filter_tunes_by_name`
      function to perform the search
    - We then print out the matches as per usual

3. `select_tune`

    ``` python
     def select_tune():
         """
         Select a tune from tunes matching a user-specified search string

         Returns
         -------
         None

         See Also
         --------
         filter_tunes_by_name : handles searching for tunes by name
         """
         print("Select tune")
         search_name = BTCInput.read_text("Enter name of tune to select: ")
         matched_tunes = filter_tunes_by_name(search_name)
         if len(matched_tunes) == 0:
             print("No matches found")
             return
         print("Found {0} matches".format(len(matched_tunes)))
         for tune in matched_tunes:
             select = BTCInput.read_int_ranged(
                 "Tune: {0}, select this tune? (1 - Yes, 0 - No): ".format(tune.name),
                 min_value=0,
                 max_value=1,
             )
             if select:
                 global current_tune
                 current_tune = tune
                 break
    ```

    - Uses `filter_tunes_by_name` to get matching tunes
    - User is then prompted for each match if they want to make this the
      new current tune
    - Execution stops once they’ve decided to select a new track

4. `delete_tune`

    ``` python
     def delete_tune():
         """
         Optionally delete tunes matching a user-specified search string

         Returns
         -------
         None

         See Also
         --------
         filter_tunes_by_name : handles searching for tunes by name
         """
         print("Delete tune")
         search_name = BTCInput.read_text("Enter name of tune to select: ")
         matched_tunes = filter_tunes_by_name(search_name)
         if len(matched_tunes) == 0:
             print("No matches found")
             return
         print("Found {0} matches".format(len(matched_tunes)))
         for tune in tunes:
             select = BTCInput.read_int_ranged(
                 "Tune: {0}, delete this tune? (1 - Yes, 0 - No): ".format(tune.name),
                 min_value=0,
                 max_value=1,
             )
             if select:
                 global current_tune
                 if tune == current_tune:
                     current_tune = no_tune
                 tunes.remove(tune)
    ```

    - Again, use `filter_tunes_by_name` to match names
    - Then prompt the user if they want to delete
    - Only caveat we have to be careful is that if we delete the
      currently selected tune we have to set the current tune to
      `no_tune` (a null object)

Now, the last thing we have to look at is the edit menu. Our edit menu
looks as follows,

``` python
def run_edit_menu():
    first_option_id = 1
    last_option_id = 8

    edit_tune_menu_template = """Editing Tune
Current Tune: {0}
1. Rename Tune
2. Display Tune
3. Play Tune
4. New Note
5. Edit Note
6. Remove Note
7. Clear Tune
8. Finish Editing

Enter your command: """
    while True:
        command = BTCInput.read_int_ranged(
            edit_tune_menu_template.format(current_tune.name),
            min_value=first_option_id,
            max_value=last_option_id,
        )

        if command == 1:
            rename_tune()
        elif command == 2:
            print(current_tune)
        elif command == 3:
            print("Playing", current_tune.name)
            current_tune.play()
        elif command == 4:
            add_note_to_tune()
        elif command == 5:
            edit_note()
        elif command == 6:
            if current_tune.number_of_notes == 0:
                print("No notes to remove")
            remove_note()
        elif command == 7:
            print("Cleared", current_tune.name)
            current_tune.clear_tune()
        elif command == 8:
            break
        else:
            raise ValueError(
                "Unexpected command id: {0} found in Edit Menu".format(command)
            )
```

Lets work through these functions

1. `rename_tune`

    ``` python
     def rename_tune():
         """
         Rename the current tune to a user prompted string

         Returns
         -------
         None
         """
         print("Rename current tune")
         new_name = prompt_valid_name("Enter new name (or . to leave unchanged): ")
         if new_name != ".":
             current_tune.name = new_name
    ```

    - Reuses the `prompt_valid_name` function from `new_tune` to get a
      new name
      - This has the issue that we can’t write the same name as the
        current tune
      - So use `.` to indicate that we don’t actually want to change

2. `add_note_to_tune`

    ``` python
     def get_new_note_from_user():
         """
         Prompts the user for a new Note

         The user is prompted for the note and duration, and the input validated
         to ensure that a valid Note object is created

         Returns
         -------
         Note
             Note object containing the user specified note id and duration
         """

         note_prompt = "Enter note ({0} - {1}): ".format(Note.min_note_id, Note.max_note_id)
         note = BTCInput.read_int_ranged(
             prompt=note_prompt, min_value=Note.min_note_id, max_value=Note.max_note_id
         )

         min_note_length = 0.1
         max_note_length = 1
         duration_prompt = "Enter duration ({0} - {1}): ".format(
             min_note_length, max_note_length
         )
         duration = BTCInput.read_float_ranged(
             duration_prompt, min_value=min_note_length, max_value=max_note_length
         )

         return Note(note, duration)


     def add_note_to_tune():
         """
         Adds a note to the current tune

         Prompts the user to specify a new note as well as an index of
         where to insert the note in the tune (-1 indicating append). The created
         note is then added to the current tune at the indicated index (or appended)

         Returns
         -------
         None
         """
         print("Add note to current tune")
         new_note = get_new_note_from_user()
         if current_tune.number_of_notes == 0:
             current_tune.add_note(new_note)
             print("Added note:", new_note)
             return

         insert_prompt = "Enter index to add note (0 - {0}) or -1 to append: ".format(
             current_tune.number_of_notes - 1
         )
         insertion_idx = BTCInput.read_int_ranged(
             insert_prompt, -1, current_tune.number_of_notes - 1
         )
         if insertion_idx == -1:
             insertion_idx = None
         current_tune.add_note(new_note, insertion_idx)
         print("Added note:", new_note)
    ```

    - We start by defining a function `get_new_note_from_user`
      - Gets a valid `Note` object from the user
      - Uses the class attributes on `Note` to limit the user’s input
        for the note id
      - Enforces a program set limit on the duration
    - Then define `add_note_to_tune`
      - We get a new note from the user
      - If there’s no notes on the `Tune` we can immediately add the
        note to the tune
      - Otherwise we prompt the user for the index to add
        - $-1$ is used to indicate that the value should be appended
      - Can then call the `add_note` method on the `Tune` object

3. `edit_note`

    ``` python
     def edit_note():
         """
         Modifies an existing note in the current tune

         Prompts the user for the index of the existing note to overwrite and
         then the details of the new note

         Returns
         -------
         None
         """
         print("Edit note in current tune")
         if current_tune.number_of_notes == 0:
             print("There are no notes in the current tune to edit")
             return

         edit_prompt = "Enter index of note to edit (0 - {0}): ".format(
             current_tune.number_of_notes - 1
         )
         insertion_idx = BTCInput.read_int_ranged(
             edit_prompt, 0, current_tune.number_of_notes - 1
         )
         old_note = current_tune.remove_note(insertion_idx)

         if insertion_idx == current_tune.number_of_notes:
             insertion_idx = None  # we removed the last index, so now need to append

         new_note = get_new_note_from_user()
         current_tune.add_note(new_note, insertion_idx)
         print("Note successfully edited")
         print("Note was:", old_note)
         print("Note now:", new_note)
    ```

    - Works similar to `add_note_to_tune`
      - This time however we first prompt the user for which note they
        want to edit
    - We create a new `Note`
    - “Editing” a note is achieved by removing the old note, and
      inserting the new note, where the old one was

4. `remove_note`

    ``` python
     def remove_note():
         """
         Remove the note at a user prompted index from the current tune

         Returns
         -------
         None
         """
         print("Remove note from current tune")
         remove_prompt = "Enter index of note to remove (0 - {0}): ".format(
             current_tune.number_of_notes - 1
         )
         remove_idx = BTCInput.read_int_ranged(
             remove_prompt, 0, current_tune.number_of_notes - 1
         )
         current_tune.remove_note(remove_idx)
    ```

    - Calling code responsible for ensuring that we don’t call this on
      an empty tune
    - Removes the note at the user prompted index

With those functions worked through that covers pretty much all the
functionality of the program. You can see the full implementation in
[TuneCreator.py](./Exercises/03_TuneCreator/TuneCreator.py). The
associated pickle file should load the [example
tunes](#make-something-happen-make-your-own-music) we created earlier
which you can play and edit to test the program

## Summary

- Classes can be used to store data attributes
  - When a class instance is created, the data is stored in the object
  - The `__init__` or constructor is a function that can be used to set
    instance attributes at creation
- Classes can contain method attributes
  - an object can asked to perform a function by calling the method
  - methods are effectively functions that contain a reference to the
    object itself as a first argument
    - Traditionally called `self`
- Classes should strive to be *cohesive*
  - Methods let us create cohesive classes
  - Cohesive classes are less reliant on the internals of other classes
  - self contained objects can validate method calls or data assignments
- Invalid data or failed methods can be handled in two ways
  - return a status message
    - User has the option of ignoring it
  - raise an exception
    - User is forced to handle it or the program crashes
- Python provides mechanisms for protecting data
  - No absolute runtime guarantees
  - `_` indicates an attribute is supposed to be private to a class
  - `__` name mangles a variable making it harder to access outside the
    class
- Static methods can be defined on a class and called without a specific
  instance
- Useful for creating validation methods, that do not rely on specific
  instance values
- Properties let us write methods that behave like attributes
  - Can be used to return values that can be calculated on the fly
  - Return read-only versions of data attributes
  - perform data validation on data attribute assignment while still
    keeping the same syntax i.e. `obj.param = new_value`
- Version management is important whenever you want to store classes
  that might change long-term
  - You should incorporate methods for upgrading older versions of a
    class to a new version
- The `__str__` method is used to define how a class is represented as a
  string
- Python string formatting provides a simple way for creating strings
  containing formatted variable values
- Iterators are objects that can produce elements of a sequence for
  iteration
  - Iterators can come from a list or a different iterator
- `map` can be used to create an iterator that applies a function to an
  existing iteration
- `join` can be used to merge a list of strings into a larger string

## Questions and Answers

1. *Why doesn’t python provide a way for a programmer to completely
    protect data attributes in an object?*

    - The creator of python didn’t believe in the traditional
      object-oriented concepts of public, protected and private
      variables
    - Even these techniques can’t protect against a malicious actor with
      access to your source code
      - They could modify a public function to reveal a private variable
      - Or they could just add one
    - It is important to still be able to review code to ensure it is
      secure

2. *When would we use a property in a program?*

    - Properties let us control how data attributes are accessed
    - Properties let us write traditional `get` and `set` methods that
      still behave like simple data attributes
    - We can also define *read-only* properties that have no set methods
    - Properties are good when you want to manage access to data (or
      validate it) but without the user having to call methods

3. *When would we create static class attributes?*

    - Static class data attributes are useful to store information about
      a class
      - i.e. independent on any specific object instance
    - A good example is data validation values
      - These will typically be common across all instances
    - Similarly static method attributes are good for performing this
      validation

4. *Must all objects be highly cohesive?*

    - Not strictly
    - It’s about scale
      - For a small program, that does one thing, that will be used once
        (or a few times by one person)
      - Little harm in being uncohesive
      - The time spent making it cohesive as opposed to making it is
        probably wasted
    - An overriding rule is to keep it simple
    - If a program is likely to be maintained, or developed by multiple
      people
      - Probably beneficial
      - Short-term costs of good design are better than the long-term of
        maintaining a poor design
    - [Time Tracker](#create-a-time-tracker) is pretty close to final
      product quality

5. *What is an iterator again?*

    - An *iterator* is an object that provides the `__next__` method
      - Provides the next value in a sequence
    - Some objects, e.g. `list` behave as iterators
    - Some methods, e.g. `map` and `range` return objects that behave as
      iterators
    - Python constructs like `for` that use iterators can work on *any*
      type of iterator
      - So long as it fulfills the protocol (`__next__` method and
        raises `StopIteration`)
      - construction doesn’t know *what* its dealing with, just sees the
        `__next__` method
      - `StopIteration` raised once there are no more elements left
