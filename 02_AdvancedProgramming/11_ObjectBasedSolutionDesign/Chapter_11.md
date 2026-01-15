# Chapter 11: Object-based Solution Design

- [Notes](#notes)
  - [Fashion Shop Application](#fashion-shop-application)
    - [Application Data Design](#application-data-design)
    - [Object-oriented Design](#object-oriented-design)
    - [Creating superclasses and
      subclasses](#creating-superclasses-and-subclasses)
      - [Abstraction in Software
        Design](#abstraction-in-software-design)
      - [Code Analysis: Understanding
        Inheritance](#code-analysis-understanding-inheritance)
      - [Storing Data in a Class
        Hierachy](#storing-data-in-a-class-hierachy)
      - [Manage the Item Name in the Fashion Shop
        Program](#manage-the-item-name-in-the-fashion-shop-program)
        - [Abstract Methods](#abstract-methods)
      - [Add a `__str__` Method to
        Classes](#add-a-__str__-method-to-classes)
        - [Make Something Happen: Method Overriding in
          Classes](#make-something-happen-method-overriding-in-classes)
      - [Code Analysis: Understanding Method
        Overriding](#code-analysis-understanding-method-overriding)
      - [Version Management in the Fashion Shop
        Program](#version-management-in-the-fashion-shop-program)
      - [Polymorphism in Software
        Design](#polymorphism-in-software-design)
        - [Code Analysis: Understanding
          Polymorphism](#code-analysis-understanding-polymorphism)
      - [Protect Data in a Class
        Hierarchy](#protect-data-in-a-class-hierarchy)
    - [Data Design Recap](#data-design-recap)
      - [Code Analysis: Data Design](#code-analysis-data-design)
      - [Make Something Happen: Instrumented Stock
        Items](#make-something-happen-instrumented-stock-items)
    - [Implement Application
      Behaviours](#implement-application-behaviours)
      - [Create a New Stock Item](#create-a-new-stock-item)
- [Summary](#summary)
- [Questions and Answers](#questions-and-answers)

## Notes

- The [previous
  chapter](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd) looked
  at creating useful objects
- In this chapter we’ll explore how to create systems comprising large
  numbers of different but related objects
- We’ll also look at connecting objects via their methods

### Fashion Shop Application

- Consider the following scenario

> A friend who runs a fashion shop would like you to build an
> application to help manage her stock. She sells a large range of
> clothing items and wants to be able to track inventory. Her workflow
> is as follows, stock arrvies from suppliers, the details are entered
> in the system. When an item is sold it should be removed from the
> stock. She would also like to be produce reports indicating how many
> of each item are in stock.

- Working with the client you define the following information about how
  her stock operates

- Each item has a unique reference

- Each reference contains:

  - A description
  - A price
  - A number in stock
  - A list of delivery amounts and dates, and sales

- For now the client is happy to just print out the entire stock list

- Has indicated in future they may wish to have more analytics, e.g.

  - determine which item has the lowest stock

- Our prototype interface is then,

  ``` text
    Mary's Fashion Shop

    1. Create a new stock item
    2. Add stock to an existing item
    3. Sell stock
    4. Stock report
    5. Exit

    Enter your command:
  ```

- The above options are all pretty straightforward for now

#### Application Data Design

- Before designing the program we need to understand the data we have to
  represent

- Our client tells us that each stock item requires,

  1. Stock reference id
  2. Price
  3. Colour
  4. Number in stock

- The client also has specifics for different types of stock items

  - For Dresses we require

    1. Size
    2. Style
    3. Pattern

  - For pants we require

    1. Length
    2. Waist size
    3. Style
    4. Pattern

  - For hats we require

    1. Size

  - For blouses we require

    1. Size
    2. Style
    3. Pattern

- We can map out some descriptions

  ``` text
    Dress: stock reference: 'D0001' price: 100.0 color: red pattern: swirly size: 12
    Pants: stock reference: 'TR12327'price: 50 color: black pattern: plain length: 30 waist: 30
  ```

- Now that we have our *data requirements* and some mock items, we want
  to carry out *data design*

- Data design is the process of specifying how we represent a programs
  data

#### Object-oriented Design

- A design paradigm we could use is to represent each data object as a
  class
  - This object-centric approach is called *object-oriented programming*
- Solution elements are mapped to software objects
- A way to formulate classes is to break a problem statement down into
  *nouns*
- *nouns* describe *things* which naturally translate to *objects*
  - e.g. a food service point-of-sale system might be described as

        The customer will select a dish from the menu and add it to his order.

  - The four nouns above (written in red) could map to classes in the
    application

    - This is only a starting point
    - We would have to dive deeper into the design requirements with the
      client

> [!TIP]
>
> **Don’t write any code before you have completed your data design**
>
> Design mistakes are easiest to correct early in a project’s lifecycle.
> For this reason data design is almost always carried out and completed
> before we actually starting to right code.
>
> If we were to continue developing the restaurant point of sale system
> above, we would have to work through the data requirements with the
> client. For example if we were developing a `Customer` class, we might
> map out paper variants of the class, and work through usage scenarios
> with the client to ensure all the details are captured.
>
> For example if a customer needed to provide a telephone number we
> would want to capture this design requirement early.

- For our first design we could implement all these different stock
  items as different classes, (you can find the code in
  [SeperateClasses.py](./Examples/01_SeperateClasses/SeperateClasses.py))

``` python
# Example 11.1 Fashion Items as Seperate Classes
#
# Mocks out the class-based implementation of the fashion items, treating
# each different item type as it's own standalone class


class Dress:
    """
    Represents the inventory details for a Dress
    """

    def __init__(self, stock_ref, price, colour, pattern, size):
        """
        Creates a `Dress` instance

        Parameters
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            dress price
        colour : str
            description of the dress colour
        pattern : str
            description of the dress pattern
        size : int
            dress size
        """
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.colour = colour
        self.pattern = pattern
        self.size = size

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        return self.__stock_level


class Pants:
    """
    Represents the inventory details for a pair of Pants
    """

    def __init__(self, stock_ref, price, colour, pattern, length, waist):
        """
        Creates a `Pants` instance

        Parameters
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            pants price
        colour : str
            description of the pants colour
        pattern : str
            description of the pants pattern
        length: int
            length of the pants
        waist : int
            pants waist size
        """
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.colour = colour
        self.pattern = pattern
        self.length = length
        self.waist = waist

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        return self.__stock_level


x = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
y = Pants(
    stock_ref="TR12327", price=50, colour="Black", pattern="Plain", length=30, waist=25
)

print(x.price)
print(y.stock_level)
```

    100
    0

- We define a `Dress` and a `Pants` class
- Each class has to have an `__init__` to set them up
- Both classes have private price and stock levels
  - These are important parts of the inventory system that should have
    controlled modification
  - We don’t want the price being modified and overcharging customers
  - We don’t want the stock level being off causing us to misorder
- Both classes have properties to access price and stock levels
  - Later we’ll make methods to control these

> [!CAUTION]
>
> **Avoid overusing block-copy**
>
> Using a text editor it might seem convenient to copy a large block of
> code when we have to reuse it elsewhere. Whenever you feel yourself
> copying lets of code to different sections this is usually a good
> indicator that something is not right. You should aim to write a piece
> of code *once*. Code written once is more maintainable, as we only
> need to modify it in one place. If the code is used multiple times, it
> is a good candidate to be converted into a function or a method
>
> As mentioned block copying is liable to introduce bugs. If we need to
> slightly modify the code in the new section we have to make sure we do
> it correctly (which might be hard if you’ve copied a big chunk).
> Additionally if you latter find a bug, you may have to fix *all* the
> copies (which requires you to remember where they are).
>
> Use this as advice, if you find yourself copying lots of code, its a
> good time to take a step back at look at your overall design

#### Creating superclasses and subclasses

- Many languages (including python) let us use *inheritance*

- Inheritance allows one class to *base* itself on another

  - i.e. it *inherits* the behaviour of another class

- The original class is called the *superclass*

- Creating this new class is called *extending the superclass*

- By default all python classes extend the `object` class

- We could write this explicitly

  ``` python
    class Contact(object)
  ```

- We can replace the `object` in the above with the class we want to use
  as a superclass

- Looking at our data design we can see there is a bunch of behaviour
  common to all stock items

- We can start by defining a `StockItem` to act as a superclass

  - `StockItem` stores all common attributes

    1. Stock reference
    2. Price
    3. Colour
    4. Stock level

- `Dress` and `Pants` now extend `StockItem`

  - The other stock items will do so as well

- The diagram below shows what’s called a *class diagram* or
  *inheritance hierachy*

``` mermaid
---
title: Fashion Shop Class Diagram
---

classDiagram
    class object

    class StockItem {
        str stock_ref
        str item_name
        str colour
        number price
        int stock_level
    }

    class Dress {
        str pattern
        int size
    }

    class Pants {
        int length
        str pattern
        int waist
    }

    object <|-- StockItem
    StockItem <|-- Dress
    StockItem <|--  Pants
```

- We can see that *both* `Pants` and `Dress` are *subclasses* of
  `StockItem`
- The inverse relationship is `StockItem` is the *superclass* of `Pants`
  and `Dress`
- We call this inheritance because the subclasses inherit the attributes
  of the superclass
- When building an inheritance hierachy you need to focus on your data
  - Here we have a collection of related data items
  - The basic behaviour of a data item is the same
  - The related items also have some common data attributes
- We capture the common behaviour and data in a superclass
  - Then *extend* with subclasses the specific behaviour of different
    data items
- Also means that if we add *new* common behaviour we only have to add
  it in one place
  - i.e. the superclass
  - Otherwise we would have to put it in all the classes

##### Abstraction in Software Design

- Abstraction is a term used to describe attempting to capture
  behaviours and data of a system at a higher level
- Here by introducing a `StockItem` class we are attempting to talk
  about the behaviour of stock items in generality as opposed to any
  specific type of stock item
  - i.e. We know that a stock item should be,

    1. Able to be added
    2. Able to be sold
    3. Find out what stock items we have

  - We do not capture the specifics of *how* these processes occur

    - Just know that we need to capture them in our program
- Abstract lets us look at processes without getting caught up in the
  details
- Later we can go and fill those details in
- Typically as we move *down* a class hierachy, we should move from the
  *more abstract* to the *more concrete*
  - At the highest level a class or interface might just say what
    methods an object should have
  - The next level down might implement some common attributes and
    methods (`StockItem`)
  - The next level down might provide specialised attributes and
    specific methods (`Dress` and `Pants`)

##### Code Analysis: Understanding Inheritance

*Work through the following questions on object-oriented design and
inheritance. It’s a good idea to consider your own thoughts on the
topic*

1. *Why don’t we put all the attributes in one class and not bother
    with subclasses?*

    - We could add every possible attribute to *one* class
    - However then we would have to handle the fact that some attributes
      are not defined for certain types
      - e.g. `Dress` has no `waist` attribute and `Pants` has no `size`
    - As we add more classes we would have to consider all the valid
      possible combinations of attributes and manage them
      - Exactly the kind of thing that the subclass approach does
        naturally
    - Additionally if we want to customise behaviour by type, we would
      have to add an attribute to track this
      - Inheritance provides *polymorphism* as a way to do this
        naturally

2. *Why is the superclass called super?*

    - It is derived from mathematical terminology around sets
    - In maths $A$ is a subset of $B$ if $A$ is entirely contained in
      $B$
    - $A$ is a superset of $B$ if $A$ contains $B$
    - The idea carries onto the language of classes, where the
      superclass is called super because every *subclass* **is** also an
      instance of the superclass.

3. *Which is most abstract, a superclass or a subclass?*

    - Recall, the concept of the class hierachy
    - Moving *down* into subclasses is getting more concrete (less
      abstract)
    - Moving *up* into superclasses is getting more abstact

4. *Can you extend a subclass?*

    - Yes
    - We can see this in the class hierachy
    - `StockItem` is a subclass of `Object`
    - `Dress` *extends* `StockItem` to create a new subclass

5. *Why is the* `pattern` *attribute not in the* `StockItem` *class?*

    - Looking at our current class diagram this does make sense
      - Both `Dress` and `Pants` have a pattern attribute
    - However our client had other types of items e.g. Hat that didn’t
      have a pattern attribute
    - If we wanted to remove the duplication we might introduce a
      `PatternedItem` between `StockItem` and the `Dress` and `Pants`
      classes
      - However for one specific attribute this is probably not
        nessecary right now
      - Especially as the `PatternedItem` seems partially arbitrary
        rather than reflecting an actual category of item

6. *Will our system ever create a* `StockItem` *object?*

    - Nothing prevents us from doing so
    - However, in practice we there’s no real use case
      - `StockItem` is not representing an actual physical item
      - It represents the concept of a stock item
    - If we wanted to do we could define `StockItem` as an *abstract
      class*
      - Abstract classes can’t be instantiated
      - They are good for defining the structure and behaviour of a
        class
      - Implementation left to the subclasses

7. *The client decides in future she may like to track which customers
    have bought which stock items. Here are three potential
    implementations. Which implementation makes the most sense?*

    1. Extend the `StockItem` class to make a `Customer` subclass that
        contains the customer details because customers buy `StockItems`
    2. Add `Customer` details to each `StockItem`
    3. Create a new `Customer` class that contains a list of the
        `StockItems` that the `Customer` has bought

    - Class hierachies should reflect an *is-a* relationship
    - A Customer *is not* a Stock item
    - So option 1 is out
    - Multiple customers might buy the same stock item
    - The stock item also represents a category of stock as opposed to
      one specific item
    - So we don’t want to have a `Customer` field
      - We could have a list of customers if we wanted to do it this way
    - However, in the future we might want to add more behaviour for
      interacting with a customer itself
      - Thus makes sense to define a `Customer` class

##### Storing Data in a Class Hierachy

- Now lets refactor our code to use a class hierachy
- The naive implementation looks like,

``` python
from abc import ABC


class StockItem(ABC):
    """
    Abstract base class representing a single inventory item.

    Attributes
    ----------
    stock_ref : str
        reference id of the stock item
    colour : str
        description of the item's colour
    """

    def __init__(self, stock_ref, price, colour):
        """
        Creates a `StockItem` instance

        Parameters
        ----------
        stock_ref : str
            stock reference id
        price : int | float
            stock price
        colour : str
            description of stock item's colour
        """
        self.stock_ref = stock_ref
        self.__price = price
        self.colour = colour
        self.__stock_level = 0
        self.__stock_level = 0

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        return self.__stock_level
```

- The `StockItem` looks pretty standard for a class

- You may observe that we import `ABC` from the `abc` module

  - `abc` is a python module to provide abstract classes
  - `ABC` is the superclass for abstract classes

- We inherit from `ABC` to make `StockItem` abstract

  - For now this only indicates that the user should not directly
    instantiate it
  - We’ll see later the concept of [abstract methods](#abstract-methods)
    which can be used to prevent instantiation of an abstract class

- We move the common attributes and properties to the class

- Define an `__init__` as usual

- Now lets define our `Dress` class, naively you might write,

  ``` python
    class Dress(StockItem):
        """
        Represents the inventory details for a Dress

        Inherits from `StockItem`

        Attributes
        ----------
        stock_ref : str
            dress reference id
        price : int | float
            dress price
        colour : str
            description of dress's colour
        pattern : str
            description of the dress pattern
        size : int
            dress size

        See Also
        --------
        `StockItem` : Parent Class
        """

        def __init__(self, stock_ref, price, colour, pattern, size):
            """
            Creates a `Dress` instance

            Parameters
            ----------
            stock_ref : str
                stock reference code
            price : int | float
                dress price
            colour : str
                description of the dress colour
            pattern : str
                description of the dress pattern
            size : int
                dress size
            """
            self.pattern = pattern
            self.size = size
  ```

- `Dress` subclasses `StockItem`

- We add the unique attributes

- Currently no need to define any new behaviour

- However, when we try to create a `Dress` instance and use it we see

  ``` python
    x = Dress(stock_ref="D0001", price=100, colour="red", pattern="swirly", size=12)
    print(x.pattern)
    print(x.price)
  ```

      swirly

      AttributeError: 'Dress' object has no attribute '_StockItem__price'
      ---------------------------------------------------------------------------
      AttributeError                            Traceback (most recent call last)
      Cell In[152], line 3
            1 x = Dress(stock_ref="D0001", price=100, colour="red", pattern="swirly", size=12)
            2 print(x.pattern)
      ----> 3 print(x.price)

      Cell In[150], line 41, in StockItem.price(self)
           35 @property
           36 def price(self):
           37     """
           38     price : int | float
           39         dress price
           40     """
      ---> 41     return self.__price

      AttributeError: 'Dress' object has no attribute '_StockItem__price'

- We see that we have no issue creating the object

- Can also access the attributes defined in the subclass (`pattern`)

- But we get an error, when we try to access a property on the
  superclass (`price`)

- In fact the error tells us that we can’t find the attribute
  `_StockItem__price`

- Why? Well if we look at the initialiser we never seem to have set up
  the stock level, price, stock reference or color

  - We can’t just write `self.colour = colour` etc
  - Because this adds an attribute on the subclass
  - Also basically means we’ve rewritten the superclass `__init__` again

- Need a way to pass arguments to the `__init__` method of the
  superclass

- We can do this using `super()`

  - `super()` is like `self`
  - Used to return a reference to the superclass instance

``` python
class Dress(StockItem):
    """
    Represents the inventory details for a Dress

    Inherits from `StockItem`

    Attributes
    ----------
    stock_ref : str
        dress reference id
    price : int | float
        dress price
    colour : str
        description of dress's colour
    pattern : str
        description of the dress pattern
    size : int
        dress size

    See Also
    --------
    `StockItem` : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, size):
        """
        Creates a `Dress` instance

        Parameters
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            dress price
        colour : str
            description of the dress colour
        pattern : str
            description of the dress pattern
        size : int
            dress size
        """
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.size = size


x = Dress(stock_ref="D0001", price=100, colour="red", pattern="swirly", size=12)
print(x.pattern)
print(x.price)
```

    swirly
    100

- We use `super()` to get a reference to the super object
- Then call the `__init__` object on the instance and pass the required
  parameters
- **Key Takeaway:** When initialising a subclass you must explicitly
  initialise the superclass too
- The complete code for our class hierachy incorporating `Pants` can be
  found in
  [ClassHierachy.py](./Examples/02_ClassHierachy/ClassHierachy.py)

##### Manage the Item Name in the Fashion Shop Program

- So far each class name matches the stock type being stored

- We might not want to maintain this relationship

- e.g. if we introduced an “Evening Dress” we can’t create a
  `Evening Dress` class

  - Since class names must be contiguous

- The client thus wants us to provide a way of giving a user friendly
  string description off the item name

- In the class diagram we defined a property called an `Item Name` in
  the `Stock Item`

  - Intended to hold the item name

- Provides a user friendly string name

- Implement as a class property

  ``` python
    class StockItem(object):

        @property
        def item_name(self):
            """
            stock_level : int
                amount of stock in inventory
            """
            return "Stock Item"
  ```

- We can then override this attribute in the subclasses

  - Overridden attributes are used inplace of the superclass
    implementation

- e.g. For the `Dress` class we might write

  ``` python
    class Dress(StockItem):
        ...
        @property
        def item_name(self):
            return "Dress"
  ```

  - Then calling `item_name` on a `Dress` instance should return
    `"Dress"` instead of `"Stock Item"` as demonstrated below

    ``` python
        item = StockItem()
        print("item name is", item.item_name)
        dress = Dress()
        print("dress name is", dress.item_name)
    ```

        item name is Stock Item
        dress name is Dress

###### Abstract Methods

- We’ve just seen how `StockItem` defines a property `item_name` which
  returns a string
- However, the intention is that this is overwritten by a subclass
- It would be good if we could force a subclass to define this method
- We saw that the `abc` module allowed us to inherit a class `ABC` that
  meant the class should not be directly instantiated
  - Is there something similar for methods
- Turns out there is!
  - `abc` contains a `abstractmethod` decorator
  - If a class has methods decorated with `@abstractmethod` subclasses
    can’t be instantiated unless they override all the abstract methods
- We can see this in practice below

``` python
    import abc
    class StockItem(abc.ABC):

        @property
        @abc.abstractmethod
        def item_name(self):
            """
            stock_level : int
                amount of stock in inventory
            """
            pass

    class Dress(StockItem):

        @property
        def item_name(self):
            return "Dress"

    class Pants(StockItem):
        pass
```

- Here we define `StockItem` with `item_name` as an abstract property

  - We do this by using both the `@property` and `@abstractmethod`
    decorators on the method

- Since `item_name` is always overridden, rather than return a value, we
  simply use `pass` to indicate a placeholder

- We next define `Dress` and `Pants` as two subclasses

  - `Dress` overrides the `item_name` method
  - `Pants` does not

- Let’s see what happens when we try to instantiate these

  ``` python
    d = Dress()
    print(d.item_name)

    p = Pants()
    print(p.item_name)
  ```

      Dress

      TypeError: Can't instantiate abstract class Pants without an implementation for abstract method 'item_name'
      ---------------------------------------------------------------------------
      TypeError                                 Traceback (most recent call last)
      Cell In[158], line 4
            1 d = Dress()
            2 print(d.item_name)
      ----> 4 p = Pants()
            5 print(p.item_name)

      TypeError: Can't instantiate abstract class Pants without an implementation for abstract method 'item_name'

- We can see that the `Dress` instantiation works as expected

- We can call `Dress` and access the overridden `item_name` property

- However, when we try to instantiate `p` as `Pants` we get a
  `TypeError`!

  - The message tells us we need to implement the abstract method
    `item_name`

##### Add a `__str__` Method to Classes

- As [seen
  earlier](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd#the-__str__-method-in-a-class)
  objects can use the `__str__` method to define a string representation
- We should add these to `StockItem` and it’s derived classes
- Defining a `__str__` method is technically overriding the `__str__`
  method on the parent
  - Including the `object` class

###### Make Something Happen: Method Overriding in Classes

*Open the python interpreter and work through the following steps to
understand method overriding*

*Enter the following statement*

``` python
o = object()
```

This creates an `object` instance referenced by `o`. If we print the
value of `o` we are calling the `__str__` method on the `object` class

*Run the print statement as below*

``` python
print(o)
```

    <object object at 0x7210e7caf2b0>

`print` requires a `str` argument, so `o` is converted to a string by
calling its `__str__` method. In this case the `__str__` method of the
`object` class. We can see the result is a message that indicates the
type of the object and the memory address where the instance is stored.

This should be familiar to what we see in the earlier `Contact` class
before we defined a `__str__` method. What happened there was that when
`__str__` was called to convert a `Contact` to an string, it deferred to
the superclass `__str__` method which was `object`

To define different behaviour we have to provide our own `__str__`
method which is said to *override* the superclass `__str__` method.

*Define a new class* `StrTest` *by entering the statements below*

``` python
class StrTest(object):
    def __str__(self):
        return "string from StrTest"
```

Remember that we don’t have to explicitly inherit from `object` we’ve
just done it to be clear

If we now print this new `StrTest` object, we can see that the new
`__str__` method on the `StrTest` is used.

*Test this by running the line below*

``` python
print(StrTest())
```

    string from StrTest

But what if we want to use the `__str__` method from the superclass as
part of the `__str__` method of the subclass? Well we can do so by using
`super()` to access the superclass instance associated with the subclass
instance. We can then directly reference the `__str__` method

*Demonstrate this by defining a new class, as below*

``` python
class StrTestSub(StrTest):
    def __str__(self):
        return super().__str__() + "..with sub"
```

The `__str__` method still overrides the superclass, but `super()` lets
us incorporate the `__str__` result from the `StrTest` superclass. We
can see this behaviour if we try to print the object.

*Call print on an instance of* `StrTestSub` *as below*

``` python
print(StrTestSub())
```

    string from StrTest..with sub

- Now let’s define `__str__` methods for our `StockItem` and
  `Subclasses`

  ``` python
    class StockItem(abc.ABC):
        ...
        def __str__(self):
            template = """Stock Reference: {0}
  Type: {1}
  Price: {2}
  Stock level: {3}
  Colour: {4}"""
            return template.format(
                self.stock_ref, self.item_name, self.price, self.stock_level, self.colour
            )
  ```

- This `__str__` item uses a template string which is formatted

- `StockItem` attributes are printed one per line

- Why are we making a `__str__` method for the `StockItem` when we’re
  going to override this?

- Well the subclasses all have to refer to the common attributes in the
  `StockItem`

- Makes sense to use the `__str__` method for the superclass to handle
  how we represent these common attributes

- Let’s see how we put this into practice with the `Dress` subclass

``` python
class Dress(StockItem):
    ...
    def __str__(self):
        stock_details = super().__str__()
        template = """{0}
Pattern: {1}
Size: {2}"""
        return template.format(stock_details, self.pattern, self.size)
```

- We use the `super()` to get the intial part of the string
- Then again use a template string
  - First inject the superclasses string
  - Then add on the new attributes in the same style
- Let us look at this in practice

``` python
x = Dress(stock_ref="D001", price=100, colour="red", pattern="swirly", size=12)
print(x)
```

    Stock Reference: D001
    Type: Dress
    Price: 100
    Stock level: 0
    Colour: red
    Pattern: swirly
    Size: 12

- We can the final result merges the superclasses string with the added
  attributes of the `Dress` class. You can see the complete code in
  [Stock Items with
  Str](./Examples/03_StockItemsWithStr/StockItemsWithStr.py)

##### Code Analysis: Understanding Method Overriding

*Consider the following questions about method overriding*

1. *How does method overriding work?*

    - When a method is called, python looks at the object to see if the
      method exists
    - If it doesn’t python looks up the class hierachy to see if it can
      find a matching method
    - First matching method found is called
    - If all the superclasses are exhausted then an `AttributeError` is
      raised

2. *Is an overriding method forced to call the method it is
    overriding?*

    - No
    - You only need to do it, if you need to access the superclasses
      implementation
    - `__str__` method in the `Dress` class calls the `__str__` in the
      `super` because the functionality is useful
      - Means if `StockItem` is updated, we can update the `__str__`
        method and it automatically propagates through to the `Dress`
        class

##### Version Management in the Fashion Shop Program

- Recall in the [Time
  Tracker](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd#manage-class-versions)
  we versioned our `Session` and `Contact` classes
- There the goal was to keep old data files usable
  - We want to do the same for our Fashion Shop
- Where should the version numbers go?
  - For example `Dress` is a subclass of `StockItem`, so we could

    1. Version in the `StockItem` superclass
    2. Version in the `Dress` superclass
    3. Version in both the `StockItem` and the `Dress` superclass

  - We want both, why?

    - `StockItem` might change, but the subclasses don’t
      - We don’t want to bump every subclass version
    - `Dress` might change
      - `StockItem` doesn’t, so don’t want to bump it because then that
        would propagate through to all the other subclasses
- So we need to implement a `version` and `check_version` for both

``` python
class StockItem(abc.ABC):

    def __init__(self, stock_ref, price, colour):
        self.stock_ref = stock_ref
        self.__price = price
        self.colour = colour
        self.__stock_level = 0
        self.__StockItem_version = 1

    ...

    def check_version(self):
        """
        Checks the version of a StockItem instance and upgrades it if required

        Returns
        -------
        None
        """
        pass  # for version 1, no need to check
```

- For `StockItem` we add a version attribute labeled
  `__StockItem_version` to distinguish from the version numbers of the
  subclasses
  - Version number is hard-coded by the constructor
  - When we create a new version of the `StockItem` this is where we
    bump the version
- Currently there is only one version of the `StockItem` class, so the
  corresponding `check_version` method doesn’t need to do anything
  - We still need to include it for the future API
  - We just use `pass` to make it a placeholder method for now
- We can now define versions and version checking for our subclasses,
  e.g. for `Dress`

``` python
class Dress(StockItem):

    def __init__(self, stock_ref, price, colour, pattern, size):
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.size = size
        self.__Dress_version = 1

    ...

    def check_version(self):
        """
        Checks the version of a `Dress` instance and upgrades it if required

        Returns
        -------
        None
        """
        super().check_version()
```

- As before we add a version attribute (here `__Dress_version`)
- We define a new `check_version`
  - Again, right now there is only one version of the `Dress` so we
    don’t need to do any self upgrades
  - However, `Dress` doesn’t know about the version of `StockItem` so we
    have to call `super` to run `check_version` for the superclass
    instance
- Together this means we can update `Dress` and `StockItem`
  independently and saved objects will still be synchronised across both
  class definitions
- The implementation for `Pants` is similar and can be found along with
  the complete implementation in [Versioned Stock
  Items](./Examples/04_VersionedStockItems/VersionedStockItems.py)

##### Polymorphism in Software Design

- Overriding methods is an example of a more broader concept of
  *polymorphism*
- Polymorphism refers to the same behaviour being able to be applied
  differently depending on the specific context or object
  - e.g. all python objects have a `__str__` method
  - defines how they are converted to a string representation
  - We can override the `__str__` method to make different objects have
    different behaviours
    - e.g. default `object` prints the memory address, an `int` gives a
      string representation of its number, and our `StockItem` class
      prints its attributes as a newline seperated list
  - This behaviour is said to be polymorphic, because different objects
    have different responses to the same behaviour (string conversion)
- Software is frequently polymorphic
  - e.g. a Play button might be used to start playback of music, video
    or a slide show
    - Same concept (play button)
    - Different outcome
- Polymorphism and Abstraction are typically a partnership
  - At an abstract level one might define a general set of behaviours a
    group of similar objects or classes need to do (e.g. “be played”)
  - Then use polymorphic behaviour to capture that common concept in one
    function, say `play` that is implemented differently for each class
    e.g. music, video, slide show

###### Code Analysis: Understanding Polymorphism

*Try and work through the following questions about polymorphism before
reading the answers*

1. *Is polymorphism all about providing methods in a class hierachy?*

    - No
    - In this example we’ve used a class hierachy
      - `__str__` behaves differently, but all objects have a `__str__`
      - However we have defined a `check_version`
      - `StockItem` and `Dress` both behave differently when
        `check_version` is called
        - *But* another object say `Book` might also have a
          `check_version` function
        - Again behaves completely differently
        - But no direct method overwrite chain
        - Would still say this behaviour is polymorphic
    - Polymorphism is a broader concept that a class hierachy
      - Though we’ve seen, a class hierachy is one way of structuring
        polymorphic behaviour

2. *How do I know which methods in my application should be
    polymorphic?*

    - This is part of the design process
    - Identify the similar behaviours performed by different objects
      that work differently for each
    - e.g. in a video game all enemies might *attack* but different
      enemy types might do so differently
      - Could then define a class hierachy with some base enemy type
      - This could then define `attack`, etc.
        - Subclasses then override the behaviour polymorphically
        - But we can still talk about “enemies” as a whole

##### Protect Data in a Class Hierarchy

- When constructing our classes we made some attributes private

- How does this carry through the class hierachy? e.g.

  ``` python
    class StockItem(abc.ABC):
        """
        Abstract base class representing a single inventory item.

        Subclasses are expected to overwrite the `item_name` abstract
        property with a user friendly string description

        Attributes
        ----------
        stock_ref : str
            reference id of the stock item
        colour : str
            description of the item's colour
        """
        def __init__(self, stock_ref, price, colour):
            """
            Creates a `StockItem` instance

            Parameters
            ----------
            stock_ref : str
                stock reference id
            price : int | float
                stock price
            colour : str
                description of stock item's colour
            """
            self.stock_ref = stock_ref
            self.__price = price
            self.colour = colour
            self.__stock_level = 0
            self.__StockItem_version = 1
  ```

- The above shows the `__init__` method for `StockItem`

- We can see some public attributes

  1. `stock_ref`
  2. `colour`

- These can be accessed by anyone

  - Including subclasses

- Also some private ones

  1. `__price`
  2. `__stock_level`
  3. `__StockItem_version`

- Private means restricted to the class in which it was declared

  - Subclasses are still regarded as other classes
  - Private variables are thus not accessible in subclasses

- Sometimes people refer to variables marked with `_` i.e. one
  underscore as *Protected*

  - A protected variable is one that can be accessed by the class it is
    defined in, *or* any subclasses of that class

- When designing a class hierachy you should think about how the data
  may be used by subclasses

- If you think you might need to customise behaviour on an attribute

  - Consider a read-only property, or making it protected/public

#### Data Design Recap

- Let’s recap our design

- The client owns a fashion shop

- She sells several different clothing types

- She needs a stock management system

- All clothing items have

  1. A stock reference
  2. Price
  3. Stock level
  4. Colour

- Specific clothing items define additional attributes

- To avoid duplicate code we define a `StockItem` class

  - We define subclasses for specific items

    1. `Dress`
    2. `Pants`
    3. `Hat`
    4. `Blouse`

  - subclasses extend the attributes on a `StockItem`

- Each class has an `__init__` to initialise it

  - Each subclass calls the superclass `__init__`
  - Sets up the superclass instance

- We independently version the sub and super classes

##### Code Analysis: Data Design

*Try to answer the following questions about data design*

1. *Is the data design process now complete?*

    - No
    - To account for this we’ve introduced versioning to a our data
      objects
      - the version attributes and `check_version` should allow us to
        add new attributes or modify the objects

2. *What happens if the fashion shop owner decides to sell a new kind
    of stock item? Suppose that she wanted to start selling Jeans, which
    are a type of pants that also has a style, which can be flared,
    bootleg or straight. What’s the best way to do this?*

    - We can add a new subclass

      1. We could subclass `StockItem` as before
          - But then would have to duplicate the `Pants` code
      2. We can subclass `Pants`

    ``` python
     class Jeans(Pants):
         """
         Represents the inventory details for a pair of Jeans

         Inherits from `Pants`

         Attributes
         ----------
         stock_ref : str
             pants reference id
         price : int | float
             pants price
         colour : str
             description of pants's colour
         pattern : str
             description of the pants pattern
         length : int
             length of the pants
         waist : int
             waist size of the pants
         style : str
             style of the pants

         See Also
         --------
         Pants : Parent Class
         """

         def __init__(self, stock_level, price, colour, pattern, length, waist, style):
             """
             Creates a `Jeans` instance

             Parameters
             ----------
             stock_ref : str
                 stock reference code
             price : int | float
                 pants price
             colour : str
                 description of the pants colour
             pattern : str
                 description of the pants pattern
             length: int
                 length of the pants
             waist : int
                 pants waist size
             style : str
                 jeans style
             """
             # pants constructor
             super().__init__(stock_level, price, colour, pattern, length, waist)
             self.style = style # new attribute
             self.__Jeans_version = 1 # versioning

         def __str__(self):
             pants_details = super().__str__()
             template = """{0}
     Style: {1}"""
             return template.format(pants_details, self.style)

         @property
         def item_name(self):
             return "Jeans"

         def check_version(self):
             """
             Checks the version of a `Pants` instance and upgrades it if required

             Returns
             -------
             None
             """
             super().check_version()
    ```

3. *What happens if the fashion shop owner decides to store something
    new about the stock? For example suppose the client now adds a
    location attribute to stock items. Location is a string description
    of where in the store the stock item is stocked. She tells your her
    plan is to later provide a program that will allow customers to find
    where items are located in the store. How can we add this attribute
    and to which class would we add it?*

    - All items need this property so most appropriate to add to
      `StockItem`
    - Should be added to the `__init__`

    ``` python
     class StockItem(abc.ABC):

         def __init__(self, stock_ref, price, colour, location):
             self.stock_ref = stock_ref
             self.__price = price
             self.__stock_level = 0
             self.colour = colour
             self.location = location
             self.__StockItem_version = 2 # we have to bump the version number
    ```

    - This has a problem that it breaks our program!

    - If we try create a new `Dress` we find

      ``` python
         d = Dress("D001", 100, "red", "swirly", 12)
      ```

          TypeError: StockItem.__init__() missing 1 required positional argument: 'location'
          ---------------------------------------------------------------------------
          TypeError                                 Traceback (most recent call last)
          Cell In[170], line 1
          ----> 1 d = Dress("D001", 100, "red", "swirly", 12)

          Cell In[169], line 3, in Dress.__init__(self, stock_ref, price, colour, pattern, size)
                2 def __init__(self, stock_ref, price, colour, pattern, size):
          ----> 3     super().__init__(stock_ref, price, colour)
                4     self.pattern = pattern
                5     self.size = size

          TypeError: StockItem.__init__() missing 1 required positional argument: 'location'

    - `Dress` does not know about the new `location` argument to the
      `StockItem` constructor

      - Thus generates an error when trying to call the constructor

    - To fix this we have to update the `Dress` `__init__` method

      - Same for every other subclass

      ``` python
        class Dress(StockItem):
            def __init__(self, stock_ref, price, colour, location, pattern, size):
                super().__init__(stock_ref, price, colour, location)
                self.pattern = pattern
                self.size = size
                self.__Dress_version = 1 # no attribute changes to `Dress`
      ```

    - Now the instantiation should work

      ``` python
        d = Dress("D001", 100, "red", "front shelf", "swirly", 12)
        print(d)
      ```

          <__main__.Dress object at 0x7210c1551df0>

    - The takeaway is that class hierachies are *very* brittle to
      changes

      - Especially changes high up in the abstraction hierachy

    - Hence you should aim to be very sure of the design of your high
      level classes

    - An alternative approach is to use *properties*, e.g.

    ``` python
     class StockItem(abc.ABC):

         @property
         def location(self):
             """
             location : str
                 location in the store where the stock item is stored
             """
             result = getattr(self, "_location", None)
             return result

         @location.setter
         def location(self, location):
             self._location = location
    ```

    - We define a getter and setter pair as usual. The setter looks
      pretty much as we would expect

    - The `location` get method is interesting though

      ``` python
        result = getattr(self, "_location", None)
      ```

    - `getattr` is a python built-in function

    - Takes three arguments

      1. An object to get the attribute from
      2. The attribute to get (as a string)
      3. A default value to return if the attribute is not found

    - The default value is returned if the attribute has not been set
      yet

      - Attempting to read the location from a `StockItem` without one
        will thus return `None`

    - `None` is discussed in [Chapter
      7](../../01_ProgrammingFundamentals/07_UsingFunctions/Chapter_07.qmd#code-analysis-functions-and-return)

    - This approach is good because we can dynamically update objects

      - However it has the downside of we now need to find a new in our
        program to make sure that the location is set

    - A third option would be to just dynamically add the attribute
      directly, e.g.

    ``` python
     d = Dress("D001", price=100, colour="red", pattern="swirly", size=12)
     d.location = "Front of Shop"
    ```

    - If we use this approach we would probably want to pair it with
      `hasattr`

    - `hasattr` is a similar function to `getattr`

    - Takes two arguments

      1. An object to check for the attribute
      2. name of the attribute (as a string)

    - `hasattr` returns `True` if the attribute exists, else `False`

    ``` python
     d = Dress("D001", 100, "red", "swirly", 12)
     d.location = "Front of Shop"

     e = Dress("D002", 100, "green", "swirly", 12)

     def demo_hasattr(obj):
         if hasattr(obj, "location"):
             print("The dress is location: ", d.location)
         else:
             print("The dress does not have location information")

     demo_hasattr(d)
     demo_hasattr(e)
    ```

        The dress is location:  Front of Shop
        The dress does not have location information

    - Of the three methods, what are the pros and cons of each?

      1. Adding `location` to the `__init__` is the most robust, but
          requires the most changes to the class hierachy
          - Enforces `location` defined
      2. Is robust, and still maintains a cohesive well-defined class
          via properties, but requires external management of when to
          define a location
          - Provides sensible behaviour if an attribute has not been set
          - This behaviour is also hidden from the user
      3. Is simple and easy to write, but fragile since it relies on
          python’s dynamic attributes
          - Requires a mental model of how we add those attributes
          - Likely breaks a lot of tooling

    - The third approach is easy and probably fine for small personal
      projects

      - Not suitable for large professional applications
      - Liable to break and hard to maintain

    - Generally when in doubt, the best approach is to use the
      `__init__`

      - Makes it easy to follow since all the attribute code is in the
        same place

##### Make Something Happen: Instrumented Stock Items

*A technique for following the flow of a program is to add
instrumentation to code. The most basic form of instrumentation is to
add print statements that show the flow of the program. Work through the
following exercise to see how this works.*

For example the below code demonstrates adding instrumentation to the
`StockItem` class. We add a class level variable `show_instrumentation`
that lets us toggle on or off the instrumentation. The most basic
implementation just adds print statements that let us know which classes
are called.

``` python
import abc

class StockItem(abc.ABC):

    show_instrumentation = True # make it optional

    def __init__(self, stock_ref, price, colour, location):
        if StockItem.show_instrumentation:
            print("**StockItem __init__ called")
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.__StockItem_version = 1
        self.colour = colour
        self.location = location
```

Each instrumentation call string is given by the `**` prefix to
distinguish it from the normal code.

*The code for the instrumentation is replicated below, and can be found
in* [Instrumented Stock
Items](./Examples/05_InstrumentedStockItems/InstrumentedStockItems.py)*.
Work through the following code and consider the examples below*

``` python
# Example 11.5 Fashion Items using Instrumentation
#
# Adds optional instrumentation to the StockItem hierachy to demonstrate the
# control flow

import abc


class StockItem(abc.ABC):
    """
    Abstract base class representing a single inventory item.

    Subclasses are expected to overwrite the `item_name` abstract
    property with a user friendly string description

    Attributes
    ----------
    stock_ref : str
        reference id of the stock item
    colour : str
        description of the item's colour

    Class Attributes
    ----------------
    show_instrumentation : bool
        Indicates if instrumentation should be printed
    """

    show_instrumentation = True

    def __init__(self, stock_ref, price, colour):
        """
        Creates a `StockItem` instance

        Parameters
        ----------
        stock_ref : str
            stock reference id
        price : int | float
            stock price
        colour : str
            description of stock item's colour
        """
        if StockItem.show_instrumentation:
            print("**StockItem __init__ called")
        self.stock_ref = stock_ref
        self.__price = price
        self.colour = colour
        self.__stock_level = 0
        self.__StockItem_version = 1

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**StockItem __str__ called")
        template = """Stock Reference: {0}
Type: {1}
Price: {2}
Stock level: {3}
Colour: {4}"""
        return template.format(
            self.stock_ref, self.item_name, self.price, self.stock_level, self.colour
        )

    @property
    @abc.abstractmethod
    def item_name(self):
        """
        item_name : str
            the stock item's name as a user friendly string
        """
        if StockItem.show_instrumentation:
            print("**StockItem item_name called")
        pass

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        if StockItem.show_instrumentation:
            print("**StockItem get price called")
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        if StockItem.show_instrumentation:
            print("**StockItem get stock_level called")
        return self.__stock_level

    def check_version(self):
        """
        Checks the version of a StockItem instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**StockItem check_version called")
        pass  # for version 1, no need to check


class Dress(StockItem):
    """
    Represents the inventory details for a Dress

    Inherits from `StockItem`

    Attributes
    ----------
    stock_ref : str
        dress reference id
    price : int | float
        dress price
    colour : str
        description of dress's colour
    pattern : str
        description of the dress pattern
    size : int
        dress size

    See Also
    --------
    StockItem : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, size):
        """
        Creates a `Dress` instance

        Parameters
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            dress price
        colour : str
            description of the dress colour
        pattern : str
            description of the dress pattern
        size : int
            dress size
        """
        if StockItem.show_instrumentation:
            print("**Dress __init__ called")
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.size = size
        self.__Dress_version = 1

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**Dress __str__ called")
        stock_details = super().__str__()
        template = """{0}
Pattern: {1}
Size: {2}"""
        return template.format(stock_details, self.pattern, self.size)

    @property
    def item_name(self):  # type: ignore
        if StockItem.show_instrumentation:
            print("**Dress get item_name called")
        return "Dress"

    def check_version(self):
        """
        Checks the version of a `Dress` instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**Dress check_version called")
        super().check_version()


class Pants(StockItem):
    """
    Represents the inventory details for a pair of Pants

    Inherits from `StockItem`

    Attributes
    ----------
    stock_ref : str
        pants reference id
    price : int | float
        pants price
    colour : str
        description of pants's colour
    pattern : str
        description of the pants pattern
    length : int
        length of the pants
    waist : int
        waist size of the pantts

    See Also
    --------
    StockItem : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, length, waist):
        """
        Creates a `Pants` instance

        Parameters
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            pants price
        colour : str
            description of the pants colour
        pattern : str
            description of the pants pattern
        length: int
            length of the pants
        waist : int
            pants waist size
        """
        if StockItem.show_instrumentation:
            print("**Pants __init__ called")
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.length = length
        self.waist = waist
        self.__Pants_version = 1

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**Pants __str__ called")
        stock_details = super().__str__()
        template = """{0}
Pattern: {1}
Length: {2}
Waist: {3}"""
        return template.format(stock_details, self.pattern, self.length, self.waist)

    @property
    def item_name(self):  # type: ignore
        if StockItem.show_instrumentation:
            print("**Pants get item_name called")
        return "Pants"

    def check_version(self):
        """
        Checks the version of a `Pants` instance and upgrades it if required

        Returns
        -------
        None
        """
        print("**Pants check_version called")
        super().check_version()
```

*First define a new* `Dress` *item as described*

``` python
dress = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
```

    **Dress __init__ called
    **StockItem __init__ called

- We can see that first the `Dress` `__init__` is called
- Then the `StockItem` `__init__` is called (from within the previous
  `__init__`)

*Now define a new* `Jeans` *item as below*

``` python
jeans = Jeans(
    stock_ref="TR12327",
    price=50,
    colour="Black",
    pattern="Plain",
    length=30,
    waist=25,
    style="flared",
)
```

    NameError: name 'Jeans' is not defined
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    Cell In[178], line 1
    ----> 1 jeans = Jeans(
          2     stock_ref="TR12327",
          3     price=50,
          4     colour="Black",
          5     pattern="Plain",
          6     length=30,
          7     waist=25,
          8     style="flared",
          9 )

    NameError: name 'Jeans' is not defined

- We can see this time there are three `__init__` calls, in order they
  are

  1. `Jeans`
  2. `Pants`
  3. `StockItem`

- Now lets see what happens when we try to print a `Jeans` item

``` python
print(jeans)
```

    NameError: name 'jeans' is not defined
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    Cell In[179], line 1
    ----> 1 print(jeans)

    NameError: name 'jeans' is not defined

- We can see that when we the `__str__` method is called from the
  `Jeans` subclass
- We propagate up the class hierachy calling `__str__` for `Pants` then
  `StockItem`
- Within the `StockItem` `__str__` we see that the getter for
  `item_name` is called
  - *But* it resolves to the method on the `Jeans` object
  - This is because `Jeans` overrides the `item_name` property
- Within the `StockItem` we also call the getters for
  - `price` and `stock_level`
  - These are not overwritten by `Jeans` and so resolve to the original
    `StockItem`
- If we want to turn off the instrumentation we can change the value of
  `StockItem.show_instrumentation` e.g.

``` python
StockItem.show_instrumentation = False
print(jeans)
```

    NameError: name 'jeans' is not defined
    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)
    Cell In[180], line 2
          1 StockItem.show_instrumentation = False
    ----> 2 print(jeans)

    NameError: name 'jeans' is not defined

- We can see now there is no instrumentation printed
- A more advanced form of instrumentation is called *logging*
  - Logs are typically stored in a seperate file
  - Can provide more detailed information and triage of problems

#### Implement Application Behaviours

- We use our standard menu structure for the Fashion Shop

``` text
    Mary's Fashion Shop

    1: Create a new stock item
    2: Add stock to an existing structure
    3: Sell stock
    4: Stock report
    5: Exit

Enter your command:
```

##### Create a New Stock Item

- If a user selects to create a new stock item we then need to decide
  what stock item to create

- We do this by using a sub menu

  ``` text
    Create a new stock item

    1. Dress
    2. Pants
    3. Hat
    4. Blouse
    5. Jeans

    Enter item to add:
  ```

## Summary

## Questions and Answers
