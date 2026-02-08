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
        Hierarchy](#storing-data-in-a-class-hierarchy)
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
      - [Add Stock to an Existing Item](#add-stock-to-an-existing-item)
      - [Sell a Stock Item](#sell-a-stock-item)
    - [Objects as Components](#objects-as-components)
  - [Create a `FashionShop` Component](#create-a-fashionshop-component)
    - [Create a `FashionShip` Object
      Instance](#create-a-fashionship-object-instance)
    - [Save the `FashionShop` Object](#save-the-fashionshop-object)
    - [Load the `FashionShop` Object](#load-the-fashionshop-object)
    - [Store a New Item](#store-a-new-item)
    - [Find a Stock Item](#find-a-stock-item)
    - [List the Stock Data](#list-the-stock-data)
    - [Exercise: Create a Banking
      Application](#exercise-create-a-banking-application)
  - [Create a User Interface Class](#create-a-user-interface-class)
    - [Initialise the User Interface](#initialise-the-user-interface)
    - [Implementing the User Menu](#implementing-the-user-menu)
    - [Implement the User Interface
      Behaviours](#implement-the-user-interface-behaviours)
    - [Exercise: Completing the Banking
      Application](#exercise-completing-the-banking-application)
      - [Design Review](#design-review)
  - [Design With Classes](#design-with-classes)
  - [Python Sets](#python-sets)
    - [Make Something Happen: Investigating
      Sets](#make-something-happen-investigating-sets)
    - [Sets and Tags](#sets-and-tags)
      - [Create a set from a String of
        Text](#create-a-set-from-a-string-of-text)
      - [Filter on Tags](#filter-on-tags)
    - [Sets versus Class Hierarchies](#sets-versus-class-hierarchies)
      - [Advantages of Using Sets and
        Tags](#advantages-of-using-sets-and-tags)
      - [Disadvantages of using
        Classes](#disadvantages-of-using-classes)
      - [Code Analysis: Design
        Decisions](#code-analysis-design-decisions)
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
> is as follows, stock arrives from suppliers, the details are entered
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
    Dress: stock reference: 'D0001' price: 100.0 colour: red pattern: swirly size: 12
    Pants: stock reference: 'TR12327'price: 50 colour: black pattern: plain length: 30 waist: 30
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
  [SeparateClasses.py](./Examples/01_SeparateClasses/SeparateClasses.py))

``` python
# Example 11.1 Fashion Items as Separate Classes
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
  - We don’t want the stock level being off causing us to mis-order
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
  *inheritance hierarchy*

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
- When building an inheritance hierarchy you need to focus on your data
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
- Typically as we move *down* a class hierarchy, we should move from the
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

    - Recall, the concept of the class hierarchy
    - Moving *down* into subclasses is getting more concrete (less
      abstract)
    - Moving *up* into superclasses is getting more abstract

4. *Can you extend a subclass?*

    - Yes
    - We can see this in the class hierarchy
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
        necessary right now
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

    - Class hierarchies should reflect an *is-a* relationship
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

##### Storing Data in a Class Hierarchy

- Now lets refactor our code to use a class hierarchy
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
      Cell In[5], line 3
            1 x = Dress(stock_ref="D0001", price=100, colour="red", pattern="swirly", size=12)
            2 print(x.pattern)
      ----> 3 print(x.price)

      Cell In[3], line 41, in StockItem.price(self)
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

- Why? Well if we look at the initializer we never seem to have set up
  the stock level, price, stock reference or colour

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
- The complete code for our class hierarchy incorporating `Pants` can be
  found in
  [ClassHierarchy.py](./Examples/02_ClassHierarchy/ClassHierarchy.py)

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
      Cell In[11], line 4
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

    <object object at 0x7f354876abe0>

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

- We use the `super()` to get the initial part of the string
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
    - If it doesn’t python looks up the class hierarchy to see if it can
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

- For `StockItem` we add a version attribute labelled
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
      prints its attributes as a newline separated list
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

1. *Is polymorphism all about providing methods in a class hierarchy?*

    - No
    - In this example we’ve used a class hierarchy
      - `__str__` behaves differently, but all objects have a `__str__`
      - However we have defined a `check_version`
      - `StockItem` and `Dress` both behave differently when
        `check_version` is called
        - *But* another object say `Book` might also have a
          `check_version` function
        - Again behaves completely differently
        - But no direct method overwrite chain
        - Would still say this behaviour is polymorphic
    - Polymorphism is a broader concept that a class hierarchy
      - Though we’ve seen, a class hierarchy is one way of structuring
        polymorphic behaviour

2. *How do I know which methods in my application should be
    polymorphic?*

    - This is part of the design process
    - Identify the similar behaviours performed by different objects
      that work differently for each
    - e.g. in a video game all enemies might *attack* but different
      enemy types might do so differently
      - Could then define a class hierarchy with some base enemy type
      - This could then define `attack`, etc.
        - Subclasses then override the behaviour polymorphically
        - But we can still talk about “enemies” as a whole

##### Protect Data in a Class Hierarchy

- When constructing our classes we made some attributes private

- How does this carry through the class hierarchy? e.g.

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

- When designing a class hierarchy you should think about how the data
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
          Cell In[23], line 1
          ----> 1 d = Dress("D001", 100, "red", "swirly", 12)

          Cell In[22], line 3, in Dress.__init__(self, stock_ref, price, colour, pattern, size)
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

          <__main__.Dress object at 0x7f3548d3f440>

    - The takeaway is that class hierarchies are *very* brittle to
      changes

      - Especially changes high up in the abstraction hierarchy

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
          requires the most changes to the class hierarchy
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
# Adds optional instrumentation to the StockItem hierarchy to demonstrate the
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
        waist size of the pants

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


class Jeans(Pants):
    """
    Represents the inventory details for a pair of Jeans

    Inherits from `Pants`

    Attributes
    ----------
    stock_ref : str
        jeans reference id
    price : int | float
        jeans price
    colour : str
        description of jeans colour
    pattern : str
        description of the jeans pattern
    length : int
        length of the jeans
    waist : int
        waist size of the jeans
    style : str
        style of the jeans

    See Also
    --------
    Pants : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, length, waist, style):
        """
        Creates a `Jeans` instance

        Parameters
        ----------
        stock_ref : str
            jeans reference id
        price : int | float
            jeans price
        colour : str
            description of jeans colour
        pattern : str
            description of the jeans pattern
        length : int
            length of the jeans
        waist : int
            waist size of the jeans
        style : str
            style of the jeans
        """
        if StockItem.show_instrumentation:
            print("**Jeans __init__ called")
        super().__init__(stock_ref, price, colour, pattern, length, waist)
        self.style = style
        self.__Jeans_version = 1

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**Jeans __str__ called")
        pants_details = super().__str__()
        template = """{0}
Style: {1}"""
        return template.format(pants_details, self.style)

    @property
    def item_name(self):  # type: ignore
        if StockItem.show_instrumentation:
            print("**Jeans get item_name called")
        return "Jeans"

    def check_version(self):
        if StockItem.show_instrumentation:
            print("**Jeans check_version called")
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

    **Jeans __init__ called
    **Pants __init__ called
    **StockItem __init__ called

- We can see this time there are three `__init__` calls, in order they
  are

  1. `Jeans`
  2. `Pants`
  3. `StockItem`

- Now lets see what happens when we try to print a `Jeans` item

``` python
print(jeans)
```

    **Jeans __str__ called
    **Pants __str__ called
    **StockItem __str__ called
    **Jeans get item_name called
    **StockItem get price called
    **StockItem get stock_level called
    Stock Reference: TR12327
    Type: Jeans
    Price: 50
    Stock level: 0
    Colour: Black
    Pattern: Plain
    Length: 30
    Waist: 25
    Style: flared

- We can see that when we the `__str__` method is called from the
  `Jeans` subclass
- We propagate up the class hierarchy calling `__str__` for `Pants` then
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

    Stock Reference: TR12327
    Type: Jeans
    Price: 50
    Stock level: 0
    Colour: Black
    Pattern: Plain
    Length: 30
    Waist: 25
    Style: flared

- We can see now there is no instrumentation printed
- A more advanced form of instrumentation is called *logging*
  - Logs are typically stored in a separate file
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

- The full code is given in [Creating Stock
  Items](./Examples/06_CreatingStockItems/CreatingStockItems.py)

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
        location : str
            description of where the pants are located

        Class Attributes
        ----------------
        show_instrumentation : bool
            Indicates if instrumentation should be printed

        min_price : int | float
            minimum price of any stock item

        max_price : int | float
            maximum price of any stock item
        """

        show_instrumentation = True

        min_price = 0.5
        max_price = 500

        def __init__(self, stock_ref, price, colour, location):
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
            location : str
                description of where the pants are located
            """
            if StockItem.show_instrumentation:
                print("**StockItem __init__ called")
            self.stock_ref = stock_ref
            self.__price = price
            self.colour = colour
            self.location = location
            self.__stock_level = 0
            self.__StockItem_version = 2

        def __str__(self):
            if StockItem.show_instrumentation:
                print("**StockItem __str__ called")
            template = """Stock Reference: {0}
    Type: {1}
    Price: {2}
    Stock level: {3}
    Location: {4}
    Colour: {5}"""
            return template.format(
                self.stock_ref,
                self.item_name,
                self.price,
                self.stock_level,
                self.location,
                self.colour,
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
            Checks the version of a `StockItem` instance and upgrades it if required

            Returns
            -------
            None
            """
            if StockItem.show_instrumentation:
                print("**StockItem check_version called")
            if self.__StockItem_version < 2:
                self.location = None
                self.__StockItem_version = 2


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
        location : str
            place where the dress is located

        See Also
        --------
        StockItem : Parent Class
        """

        def __init__(self, stock_ref, price, colour, pattern, size, location):
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
            location : str
                place where the dress is located
            """
            if StockItem.show_instrumentation:
                print("**Dress __init__ called")
            super().__init__(stock_ref, price, colour, location)
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
            waist size of the pants
        location : str
            description of where the pants are located

        See Also
        --------
        StockItem : Parent Class
        """

        def __init__(self, stock_ref, price, colour, pattern, length, waist, location):
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
            location : str
                description of where the pants are located
            """
            if StockItem.show_instrumentation:
                print("**Pants __init__ called")
            super().__init__(stock_ref, price, colour, location)
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


    class Jeans(Pants):
        """
        Represents the inventory details for a pair of Jeans

        Inherits from `Pants`

        Attributes
        ----------
        stock_ref : str
            jeans reference id
        price : int | float
            jeans price
        colour : str
            description of jeans colour
        pattern : str
            description of the jeans pattern
        length : int
            length of the jeans
        waist : int
            waist size of the jeans
        style : str
            style of the jeans
        location : str
            description of where the pants are located

        See Also
        --------
        Pants : Parent Class
        """

        def __init__(
            self, stock_ref, price, colour, pattern, length, waist, style, location
        ):
            """
            Creates a `Jeans` instance

            Parameters
            ----------
            stock_ref : str
                jeans reference id
            price : int | float
                jeans price
            colour : str
                description of jeans colour
            pattern : str
                description of the jeans pattern
            length : int
                length of the jeans
            waist : int
                waist size of the jeans
            style : str
                style of the jeans
            location : str
                description of where the jeans are located
            """
            if StockItem.show_instrumentation:
                print("**Jeans __init__ called")
            super().__init__(stock_ref, price, colour, pattern, length, waist, location)
            self.style = style
            self.__Jeans_version = 1

        def __str__(self):
            if StockItem.show_instrumentation:
                print("**Jeans __str__ called")
            pants_details = super().__str__()
            template = """{0}
    Style: {1}"""
            return template.format(pants_details, self.style)

        @property
        def item_name(self):  # type: ignore
            if StockItem.show_instrumentation:
                print("**Jeans get item_name called")
            return "Jeans"

        def check_version(self):
            if StockItem.show_instrumentation:
                print("**Jeans check_version called")
            super().check_version()


    class Hat(StockItem):
        """
        Represents the inventory details for a Hat

        Inherits from `StockItem`

        Attributes
        ----------
        stock_ref : str
            hat reference id
        price : int | float
            hat price
        colour : str
            description of hats colour
        size : int
            Hat size in diameter
        location : str
            description of where the hat is located

        See Also
        --------
        StockItem : Parent Class
        """

        def __init__(self, stock_ref, price, colour, size, location):
            """
            Creates a `Hat` instance

            Parameters
            ----------
            stock_ref : str
                hat stock reference id
            price : int | float
                hat price
            colour : str
                hat colour
            size : int
                hat size in diameter
            location : str
                where the hat is located in the store
            """
            if StockItem.show_instrumentation:
                print("**Hat __init__ called")
            super().__init__(stock_ref, price, colour, location)
            self.size = size
            self.__Hat_version = 1

        def __str__(self):
            if StockItem.show_instrumentation:
                print("** Hat __str__ called")
            stock_details = super().__str__()
            template = """{0}
    Size: {1}"""
            return template.format(stock_details, self.size)

        @property
        def item_name(self):  # type: ignore
            if StockItem.show_instrumentation:
                print("** Hat get item_name called")
            return "Hat"

        def check_version(self):
            """
            Checks the version and upgrades a `Hat` instance as requires
            """
            if StockItem.show_instrumentation:
                print("** Hat check_version called")
            super().check_version()


    class Blouse(StockItem):
        """
        Represents the inventory details for a Blouse

        Inherits from `StockItem`

        Attributes
        ----------
        stock_ref : str
            stock reference code
        price : int | float
            blouse price
        colour : str
            description of the blouse colour
        pattern : str
            description of the blouse pattern
        style : str
            description of the blouse style
        size : int
            blouse size
        location : str
            place where the blouse is located

        See Also
        --------
        StockItem : Parent Class
        """

        def __init__(self, stock_ref, price, colour, pattern, style, size, location):
            """
            Creates a `Blouse` instance

            Parameters
            ----------
            stock_ref : str
                stock reference code
            price : int | float
                blouse price
            colour : str
                description of the blouse colour
            pattern : str
                description of the blouse pattern
            style : str
                description of the blouse style
            size : int
                blouse size
            location : str
                place where the blouse is located
            """
            if StockItem.show_instrumentation:
                print("** Blouse __init__ called")
            super().__init__(stock_ref, price, colour, location)
            self.pattern = pattern
            self.style = style
            self.size = size
            self.__Blouse_version = 1

        def __str__(self):
            if StockItem.show_instrumentation:
                print("** Blouse __str__ called")
            stock_details = super().__str__()
            template = """{0}
    Size: {1}
    Style: {2}
    Pattern: {3}"""
            return template.format(stock_details, self.size, self.style, self.pattern)

        @property
        def item_name(self):  # type: ignore
            if StockItem.show_instrumentation:
                print("** Blouse get item_name called")
            return "Blouse"

        def check_version(self):
            """
            Checks the version and upgrades a `Blouse` instance as required

            Returns
            -------
            None
            """
            if StockItem.show_instrumentation:
                print("** Blouse check_version called")
            return super().check_version()
  ```

- We’ve implemented in all our remaining subclasses `Hat` and `Blouse`

- We’ve also added the [`location` variable](#code-analysis-data-design)

- Our Menu looks pretty straight forward now

- In `StockItem` we’ve also added extra class attributes

  - `min_price` and
  - `max_price`
  - These are designed to be used by external validators
    - We can add validation directly to the classes later

``` python
menu = """
Create a new stock item

1. Dress
2. Pants
3. Hat
4. Blouse
5. Jeans

Enter item to add: """

first_menu_option = 1
last_menu_option = 5

min_stock_item_size = 0
max_stock_item_size = 99

item = BTCInput.read_int_ranged(menu, first_menu_option, last_menu_option)

if item < first_menu_option or item > last_menu_option:
    raise ValueError(
        "Unexpected value {0} found in menu. Please raise a bug report".format(item)
    )
```

- We define our standard menu framework

- The `min_stock_item_size` and `max_stock_item_size` are variables that
  store the min and max of any size related properties like size,
  length, waist etc.

- We then get the user’s choice and check that it’s valid

  - This is our usual mechanism of making the code robust to changes
  - When we add a command `first_menu_option` and/or
    `second_menu_option` should be updated
  - Needs to be replicated through to getting user input
  - The guard clause makes sure these align

- Now we have a valid item we can get the common attributes for a
  `StockItem`

  ``` python
    # now we have a valid item so get the common attributes
    stock_ref = BTCInput.read_text("Enter Stock reference: ")
    price = BTCInput.read_float_ranged(
        "Enter price: ", min_value=StockItem.min_price, max_value=StockItem.max_price
    )
    colour = BTCInput.read_text("Enter colour: ")
    location = BTCInput.read_text("Enter location: ")
  ```

- Then we implement the menu choices as below

- We report to the user what object we’re creating

- We then ask for the attributes unique to that stock item type

- Then create the appropriate object

  ``` python
    if item == 1:
    print("Creating a Dress")
    pattern = BTCInput.read_text("Enter pattern: ")
    size = BTCInput.read_int_ranged(
        "Enter size: ", min_value=min_stock_item_size, max_value=max_stock_item_size
    )
    stock_item = Dress(stock_ref, price, colour, pattern, size, location)

    elif item == 2:
        print("Creating a pair of Pants")
        pattern = BTCInput.read_text("Enter pattern: ")
        length = BTCInput.read_int_ranged(
            "Enter length: ", min_value=min_stock_item_size, max_value=max_stock_item_size
        )
        waist = BTCInput.read_int_ranged(
            "Enter waist size: ",
            min_value=min_stock_item_size,
            max_value=max_stock_item_size,
        )
        stock_item = Pants(stock_ref, price, colour, pattern, length, waist, location)

    elif item == 3:
        print("Creating a Hat")
        size = BTCInput.read_int_ranged(
            "Enter size: ", min_value=min_stock_item_size, max_value=max_stock_item_size
        )
        stock_item = Hat(stock_ref, price, colour, size, location)

    elif item == 4:
        print("Creating a Blouse")
        pattern = BTCInput.read_text("Enter pattern: ")
        style = BTCInput.read_text("Enter style: ")
        size = BTCInput.read_int_ranged(
            "Enter size: ", min_value=min_stock_item_size, max_value=max_stock_item_size
        )
        stock_item = Blouse(stock_ref, price, colour, pattern, style, size, location)

    elif item == 5:
        print("Creating a pair of Jeans")
        pattern = BTCInput.read_text("Enter pattern: ")
        style = BTCInput.read_text("Enter style: ")
        length = BTCInput.read_int_ranged(
            "Enter length: ", min_value=min_stock_item_size, max_value=max_stock_item_size
        )
        waist = BTCInput.read_int_ranged(
            "Enter waist size: ",
            min_value=min_stock_item_size,
            max_value=max_stock_item_size,
        )
        stock_item = Jeans(
            stock_ref, price, colour, pattern, length, waist, style, location
        )
    else:
        stock_item = None
  ```

- An example output from this program might then look like

<!-- -->

    Create a new stock item

    1. Dress
    2. Pants
    3. Hat
    4. Blouse
    5. Jeans

    Enter item to add:  1
    Enter Stock reference: DO001
    Enter price: 100
    Enter colour: Red
    Enter location: Shop Window
    Creating a Dress
    Enter pattern: Swirly
    Enter size: 12
    Enter location: Front Window
    **Dress __init__ called
    **StockItem __init__ called
    **Dress __str__ called
    **StockItem __str__ called
    **Dress get item_name called
    **StockItem get price called
    **StockItem get stock_level called
    Stock Reference: D001
    Type: Dress
    Price: 100
    Stock level: 0
    Location: Front Window
    Colour: Red
    Pattern: Swirly
    Size: 12

- In the future we will look at how to wrap these user interactions in a
  class `FashionShopShellApplication`

##### Add Stock to an Existing Item

- When items are created they start with a default stock level of $0$
- We need some way to increase a stock item’s stock level when an order
  arrives
- We can’t directly modify `__stock_level` as it’s private
- So we need to add a method

``` python
# Example 11.7 Updating Stock Levels on an Item
#
# Continues demonstrating behaviours of the fashion shop, here we highlight how
# to implement adding to stock levels

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
    location : str
        description of where the pants are located

    Class Attributes
    ----------------
    show_instrumentation : bool
        Indicates if instrumentation should be printed

    max_stock_add : int
        maximum amount of stock that can be added to an item's stock level at a time
    """

    show_instrumentation = True

    max_stock_add = 10

    def __init__(self, stock_ref, price, colour, location):
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
        location : str
            description of where the pants are located
        """
        if StockItem.show_instrumentation:
            print("**StockItem __init__ called")
        self.stock_ref = stock_ref
        self.__price = price
        self.colour = colour
        self.location = location
        self.__stock_level = 0
        self.__StockItem_version = 2

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**StockItem __str__ called")
        template = """Stock Reference: {0}
Type: {1}
Price: {2}
Stock level: {3}
Location: {4}
Colour: {5}"""
        return template.format(
            self.stock_ref,
            self.item_name,
            self.price,
            self.stock_level,
            self.location,
            self.colour,
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
        Checks the version of a `StockItem` instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**StockItem check_version called")
        if self.__StockItem_version < 2:
            self.location = None
            self.__StockItem_version = 2

    def add_stock(self, count):
        """
        Add stock to an item

        Parameters
        ----------
        count : int
            amount of stock to add to an item

        Returns
        -------
        None

        Raises
        ------
        Exception
            raised if `count` < 0 or `count` > `StockItem.max_stock_add`

        See Also
        --------
        StockItem.max_stock_add : maximum amount of stock that can be added to a `StockItem`
        """
        if StockItem.show_instrumentation:
            print("**StockItem add_stock called")
        if count < 0 or count > StockItem.max_stock_add:
            raise Exception("Invalid add amount")
        self.__stock_level = self.__stock_level + count


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
    location : str
        place where the dress is located

    See Also
    --------
    StockItem : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, size, location):
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
        location : str
            place where the dress is located
        """
        if StockItem.show_instrumentation:
            print("**Dress __init__ called")
        super().__init__(stock_ref, price, colour, location)
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
```

- We add a new class attribute `max_stock_add` which defines the maximum
  amount of stock that can be added to an item in one go

- We then define an `add_stock` method

  ``` python
    def add_stock(self, count):
        """
        Add stock to an item

        Parameters
        ----------
        count : int
            amount of stock to add to an item

        Returns
        -------
        None

        Raises
        ------
        Exception
            raised if `count` < 0 or `count` > `StockItem.max_stock_add`

        See Also
        --------
        StockItem.max_stock_add : maximum amount of stock that can be added to a `StockItem`
        """
        if StockItem.show_instrumentation:
            print("**StockItem add_stock called")
        if count < 0 or count > StockItem.max_stock_add:
            raise Exception("Invalid add amount")
        self.__stock_level = self.__stock_level + count
  ```

- We first validate the `count` variable

  - Raising an `Exception` if invalid so it can be handled

- Once validated we can directly update the private variable

- Let us see how this works with a `Dress` now

  ``` python
    d = Dress(
        "D0001", price=100, colour="Red", pattern="Swirly", size=12, location="Shop Window"
    )
    d.add_stock(5)
    print(d)
  ```

      **Dress __init__ called
      **StockItem __init__ called
      **StockItem add_stock called
      **Dress __str__ called
      **StockItem __str__ called
      **Dress get item_name called
      **StockItem get price called
      **StockItem get stock_level called
      Stock Reference: D0001
      Type: Dress
      Price: 100
      Stock level: 5
      Location: Shop Window
      Colour: Red
      Pattern: Swirly
      Size: 12

- We can see the Stock Level is now $5$

- What happens if we try to add more than `StockItem.max_stock_add`?

``` python
d.add_stock(15)
```

    **StockItem add_stock called

    Exception: Invalid add amount
    ---------------------------------------------------------------------------
    Exception                                 Traceback (most recent call last)
    Cell In[38], line 1
    ----> 1 d.add_stock(15)

    Cell In[36], line 150, in StockItem.add_stock(self, count)
        148     print("**StockItem add_stock called")
        149 if count < 0 or count > StockItem.max_stock_add:
    --> 150     raise Exception("Invalid add amount")
        151 self.__stock_level = self.__stock_level + count

    Exception: Invalid add amount

- Well as expected we get an Exception, showing our error-handling is
  working correctly
- As the above shows, by adding the method directly to `StockItem` it is
  automatically available to all of the subclasses without the need to
  write extra code

##### Sell a Stock Item

- Now we need to account for the opposite case where stock is sold

- The stock level will correspondingly decrease

- We do this with another method on `StockItem`

  ``` python
    class StockItem(abc.ABC):
        """
        Stock Item for the Fashion Shop
        """
        ...

        def sell_stock(self, count):
            if count < 1:
                raise Exception("Invalid number of items to sell")
            if count > self.__stock_level:
                raise Exception("Not enough stock to sell")
            self.__stock_level = self.__stock_level - count
  ```

- The amount to sell is given by the `count` parameter

- We raise an exception in two cases

  1. The user tries to sell $< 1$ items, since this physically doesn’t
      make sense
  2. The user tries to sell more items than are available i.e. `count`
      $>$ `self.__stock_level`

- Let’s see how this plays out with the `Dress` class

  ``` python
    d = Dress(
        "D0001", price=100, colour="Red", pattern="Swirly", size=12, location="Shop Window"
    )
    d.add_stock(5)
    d.sell_stock(1)
    print(d)
  ```

      **Dress __init__ called
      **StockItem __init__ called
      **StockItem add_stock called
      **StockItem sell_stock called
      **Dress __str__ called
      **StockItem __str__ called
      **Dress get item_name called
      **StockItem get price called
      **StockItem get stock_level called
      Stock Reference: D0001
      Type: Dress
      Price: 100
      Stock level: 4
      Location: Shop Window
      Colour: Red
      Pattern: Swirly
      Size: 12

- And again what happens if we try to do something invalid like selling
  more stock than we have

  ``` python
    d.sell_stock(10)
  ```

      **StockItem sell_stock called

      Exception: Not enough stock to sell
      ---------------------------------------------------------------------------
      Exception                                 Traceback (most recent call last)
      Cell In[41], line 1
      ----> 1 d.sell_stock(10)

      Cell In[39], line 178, in StockItem.sell_stock(self, count)
          176     raise Exception("Invalid number of items to sell")
          177 if count > self.__stock_level:
      --> 178     raise Exception("Not enough stock to sell")
          179 self.__stock_level = self.__stock_level - count

      Exception: Not enough stock to sell

- As expected, an exception is raised

#### Objects as Components

- We have completed the `StockItem` and it’s associated class hierarchy
- All behaviours given by the fashion shop item data spec is now
  implemented by the class and its subclasses
- `StockItem` is a purely self-contained and cohesive
- We’ve done some basic testing of the external behaviours
  - Later we’ll look at how to implement automatic testing of our
    objects
- Sometimes we call a cohesive, self-contained part a *component*
- E.g. in a car production line different parts of the line produce
  different parts, like the motor, panels, transmission etc.
  - All are made separately and the final product is composed of all the
    parts
- We would like to do something similar with `StockItem`
  - Move it around as it’s own component
  - Can then potentially reuse it as it’s own feature in other projects

> [!TIP]
>
> **Self-contained components are a great way to build software**
>
> Breaking software projects down into individual components is a great
> design philosophy. When you’re working solo it lets you focus on a
> small completable part of the program and progressively build up the
> complexity. When working with a larger team, different parts of the
> team can be assigned to work on the different independent components
> without interfering with each others work.
>
> For example in our fashion shop project someone could be building the
> `StockItem` while another person works on the UI

### Create a `FashionShop` Component

- We have implemented a complete `StockItem` component

  - Represents everything about a single item of stock

- Now we want to create a component that handles the management of
  collections of stock

- We will call this component `FashionShop`

- We identify the following requirements

  1. Create a new fashion shop
  2. Save the fashion shop stock data to a file
  3. Load the data from a file
  4. Store a new stock item
  5. Find a particular stock item
  6. Provide a listing of all stock items

- We can start by stubbing out our class, (the template code is given by
  [Fashion Shop
  Prototype](./Examples/09_FashionShopPrototype/FashionShop.py))

  ``` python
    # Example 11.9 Fashion Stock Prototype
    #
    # Provides a stubbed out template for the FashionShop Class


    class FashionShop:
        """
        Represents the inventory management system of a Fashion Shop
        """

        def __init__(self):
            """
            Create a new `FashionShop` instance
            """
            pass

        def save(self, filename):
            """
            Save the `FashionShop` to a given file

            `FashionShop` is saved as a pickled binary file in the file given
            by `filename`. The file is created if it doesn't exist. If the file
            already exists it is overwritten

            Parameters
            ----------
            filename : str
                path to the file to save

            Returns
            -------
            None

            Raises
            ------
            Exceptions
                raised if the file fails to save

            See Also
            --------
            FashionShop.load : load a `FashionShop` object from a file
            """
            pass

        @staticmethod
        def load(filename):
            """
            Create a `FashionShop` instance from a pickled binary file

            Parameters
            ----------
            filename : str
                path to a file containing pickled `FashionShop` data

            Returns
            -------
            FashionShop
                the loaded `FashionShop` instance

            Raises
            ------
            Exceptions
                raised if the file fails to load

            See Also
            --------
            FashionShop.save : saves a `FashionShop` instance
            """
            pass

        def store_new_stock_item(self, item):
            """
            Store a new item in the reference system

            The provided `item` can be indexed by it's `stock_ref` parameter

            Parameters
            ----------
            item : StockItem
                item to add to the inventory system

            Returns
            -------
            None

            Raises
            ------
            KeyError
                Raised if the item's `stock_ref` is already registered as a key
            """
            pass

        def find_stock_item(self, stock_ref):
            """
            Find the stock item with the corresponding reference id

            Parameters
            ----------
            stock_ref : str
                stock reference id of the item to find

            Returns
            -------
            StockItem | None
                Returns a `StockItem` with a matching `stock_ref` else `None`
            """
            return None

        def __str__(self):
            return ""
  ```

- We’ll now start by filling in these methods one by one

- We provide a complete docstring which documents what the function
  *should* do

  - Means someone else could come and implement it if we were working in
    a team

- Some methods return placeholder values

  - These implement partial functionality
  - e.g. `find_stock_item` always returns `None` at the moment

- A program utilising `FashionShop` needs only call the methods based on
  the description

  - Does not need to know about the internals

#### Create a `FashionShip` Object Instance

- Our first step is to define our data attributes and define the
  `__init__`

- We’ll start by using a dictionary to store our items

  ``` python
    class FashionShop:

        def __init__(self):
            self.__stock_dictionary = {}
  ```

- The `__init__` takes no arguments

- Purely creates an empty dictionary (`self.__stock_dictionary`) to
  store future stock items

- We make the dictionary private to avoid accidental modification

- We can now create a new `FashionShop`

  ``` python
    shop = FashionShop()
    print(shop)
  ```

      <__main__.FashionShop object at 0x7f3548abcf20>

#### Save the `FashionShop` Object

- We’ll use the same approach we’ve used before of pickling our files

- Works exactly as we’ve seen before

  ``` python
    class FashionShop:

        def save(self, filename):
            with open(filename, "wb") as out_file:
                pickle.dump(self, out_file)
  ```

- We use `with` to handle making sure the file is properly cleaned up
  once we’re done

- We pass `self` to `pickle.dump` to save the object instance on which
  `save` is called

- The below example demonstrates creating an (empty) `FashionShop`
  `shop` and then saving it

  ``` python
    shop = FashionShop()
    shop.save("FashionShop.pickle")
  ```

#### Load the `FashionShop` Object

- The load in our [template](#create-a-fashionshop-component) is marked
  as a `@staticmethod`

- We can’t make it a object method, because there is no object yet

- Make it static so it’s still associated with the class

- This means we want the `load` method to create and return a new
  `FashionShop` item

  ``` python
    class FashionShop:
        ...
        def load(filename):
            with open(filename, "rb") as input_file:
                shop = pickle.load(input_file)
            return shop
  ```

- If we wanted to load the `FashionShop` object we had saved above we
  would write

  \`\`\`python loaded_shop = FashionShop.load(“FashionShop.pickle”)

#### Store a New Item

- `FashionShop` is effectively a container for `StockItem` objects

- At the moment the underlying model is a dictionary

- We can’t add new items directly to the dictionary for two reasons

  1. We’ve made it private so we can’t directly add them
  2. We want to prevent adding multiple items with the same reference

- As mentioned above we want to prevent duplicates

- How should we handle duplicates?

  - We could use a status code, but as said, we should favour exceptions
  - We’ll return a `KeyError` if the key already exists
  - We then need to document this in the docstring

  ``` python
    class FashionShop:
        ...
    def store_new_stock_item(self, item):
        """
        Store a new item in the reference system

        The provided `item` can be indexed by it's `stock_ref` parameter

        Parameters
        ----------
        item : StockItem
            item to add to the inventory system

        Returns
        -------
        None

        Raises
        ------
        KeyError
            Raised if the item's `stock_ref` is already registered as a key
        """
        if item.stock_ref in self.__stock_dictionary:
            raise KeyError("This stock reference is already used")
        self.__stock_dictionary[item.stock_ref] = item
  ```

- `store_new_stock_item` adds a new stock item to the container

- It does not create one, we have to do that separately

- The method checks for duplicates, throwing a `KeyError` if the stock
  reference is already used

- If no exception is raised, the item is inserted into the stock
  dictionary

- Let us see this in practice,

  ``` python
    dress = Dress(stock_ref="D001", price=100, colour="red", pattern="swirly", size=12, location="front")
    shop = FashionShop()
    shop.store_new_stock_item(dress)
  ```

      **Dress __init__ called
      **StockItem __init__ called

- And if we try to add it again…

  ``` python
    shop.store_new_stock_item(dress)
  ```

      KeyError: 'This stock reference is already used'
      ---------------------------------------------------------------------------
      KeyError                                  Traceback (most recent call last)
      Cell In[46], line 1
      ----> 1 shop.store_new_stock_item(dress)

      Cell In[44], line 93, in FashionShop.store_new_stock_item(self, item)
           73 """
           74 Store a new item in the reference system
           75
         (...)     90     Raised if the item's `stock_ref` is already registered as a key
           91 """
           92 if item.stock_ref in self.__stock_dictionary:
      ---> 93     raise KeyError("This stock reference is already used")
           94 self.__stock_dictionary[item.stock_ref] = item

      KeyError: 'This stock reference is already used'

#### Find a Stock Item

- Finding stock is implemented as a dictionary lookup
- Dictionaries provide the `get` method
  - Acts as a normal dictionary lookup
  - However if the key is missing a default value is returned
  - The default value for this default parameter is `None`

  ``` python
    class FashionShop:
        ...
        def find_stock_item(self, stock_ref):
            """
            Find the stock item with the corresponding reference id

            Parameters
            ----------
            stock_ref : str
                stock reference id of the item to find

            Returns
            -------
            StockItem | None
                Returns a `StockItem` with a matching `stock_ref` else `None`
            """
            return self.__stock_dictionary.get(stock_ref)
  ```

- The calling code is responsible for checking that the returned value
  is a valid `StockItem`
- Let’s demonstrate this by trying to find the dress we just added, and
  one that didn’t exist

``` python
print(shop.find_stock_item("D001"))
print(shop.find_stock_item("AAAA"))
```

    **Dress __str__ called
    **StockItem __str__ called
    **Dress get item_name called
    **StockItem get price called
    **StockItem get stock_level called
    Stock Reference: D001
    Type: Dress
    Price: 100
    Stock level: 0
    Location: front
    Colour: red
    Pattern: swirly
    Size: 12
    None

#### List the Stock Data

- Final step is to list the stock data
- We want this in the form a human-readable string
- We can use a similar approach seen with our
  `Session class in [Chapter 10](../10_UseClassesToCreateActiveObjects/Chapter_10.qmd#code-analysis-creating-a-session-class)     -`StockItem`provides a`**str**\`
  method
  - We can iterate over the container items to get all of these
  - Then just have to nicely format the container

  ``` python
    class FashionShop:
        ...
        def __str__(self):
            stock = map(str, self.__stock_dictionary.values())
            stock_list = "\n".join(stock)
            template = """Items in Stock
    {0}
    """
        return template.format(stock_list)
  ```

- Let’s put everything we’ve put together in practice
- We’ll create two items and add them to the shop then print the
  contents
- You can find the complete implementation of the fashion shop class in
  [Fashion Shop](./Examples/10_FashionShopClass/FashionShop.py)
  - Like our [instrumented
    version](#make-something-happen-instrumented-stock-items) of
    `StockItem`, `FashionShop` provides instrumentation so you can view
    the program flow

``` python
dress = Dress(
    stock_ref="D001",
    price=100,
    colour="red",
    pattern="swirly",
    size=12,
    location="front",
)
pants = Pants(
    stock_ref="A002",
    price=200,
    colour="cream",
    pattern="plain",
    length=12,
    waist=34,
    location="back right corner",
)

shop = FashionShop()
shop.store_new_stock_item(dress)
shop.store_new_stock_item(pants)
print(shop)
```

    **Dress __init__ called
    **StockItem __init__ called
    **Pants __init__ called
    **StockItem __init__ called
    **FashionShop __init__ called
    **FashionShop store new stock item called
    **FashionShop store new stock item called
    **Dress __str__ called
    **StockItem __str__ called
    **Dress get item_name called
    **StockItem get price called
    **StockItem get stock_level called
    **Pants __str__ called
    **StockItem __str__ called
    **Pants get item_name called
    **StockItem get price called
    **StockItem get stock_level called

    Stock Reference: D001
    Type: Dress
    Price: 100
    Stock level: 0
    Location: front
    Colour: red
    Pattern: swirly
    Size: 12
    Stock Reference: A002
    Type: Pants
    Price: 200
    Stock level: 0
    Location: back right corner
    Colour: cream
    Pattern: plain
    Length: 12
    Waist: 34

#### Exercise: Create a Banking Application

*You can use a similar structure to the* `FashionShop` *inventory
management class for any program that needs to manage a key-based lookup
of items, examples may include a bank account management system, a doll
collection or competition entries*

*Implement a basic bank account management system. The system should
have three different account types*

1. Savings accounts
    - Have an account number, a monthly interest rate, a balance, and a
      person associated with the account
    - A savings account can have money deposited or withdrawn
    - A savings account balance cannot be negative
    - Every month a savings account balance is increased by the interest
      rate
2. Long-term savings account
    - Like a savings account
    - However also has a start date, and a term maturation period
    - Money cannot be withdrawn from a long-term savings account before
      the maturation date
    - Once a long-term savings deposit has matured the interest rate is
      quartered
    - An account holder can either reinvest a matured long-term savings
      deposit (starting a new term and maturation)
      - Or close out a matured long-term deposit transferring it to
        another account
3. Credit Account
    - Have a maximum withdrawal limit
    - A credit account balance cannot be positive
    - Every month a credit account balance is increased by the interest
      rate (i.e. any unpaid credit is increased)
    - A credit account can not have a negative balance whose magnitude
      is greater than the maximum withdrawal limit

The bank system should have a similar interface to the `FashionShop`,
with the following,

1. Create a new bank system
2. Save the bank system data to a file
3. Load the data from a file
4. Store a new bank account
5. Find a particular bank account
6. Provide a listing of all accounts
7. Find all accounts associated with a particular person

Lets start by mapping out a class hierarchy for accounts. We can see
that all accounts have a number, interest rate, balance and an
associated account holder, each also supports being able to withdraw or
deposit money and have interest applied, however they each implement
these methods differently. So we’ll define an *abstract base class*
`Account` that provides these data attributes and declares these
methods. Subclasses then overwrite the method.

Our first subclass will be a savings account which requires no
additional data attributes. Our second is a long-term savings account.
This acts like a saving account but also has a maturation period and a
start date. There are additional restrictions on how the account
operates depending on if it has matured or not, so we’ll inherit from a
Savings Account. A credit account has different behaviours for its
deposit and withdraw methods and has a maximum withdrawal limit, so will
be a subclass derived from the base account class

``` mermaid
---
title: Account Class Diagram
---

classDiagram
    class object

    class Account {
        str account_number
        str account_holder
        number interest_rate
        number balance
        deposit()
        withdraw()
        apply_interest()
    }

    class SavingsAccount

    class LongTermSavingsAccount {
        date start_date
        int term_period
    }

    class CreditAccount {
        number max_withdrawal_limit
    }

    object <|-- Account
    Account <|-- SavingsAccount
    SavingsAccount <|--  LongTermSavingsAccount
    Account <|-- CreditAccount
```

Our abstract base class is fairly simple, it defines the properties and
the abstract methods. You’ll observe that we make the majority of data
attributes *read-only*. This is because when dealing with people’s money
we want to be really careful about inappropriate changes!

``` python
import datetime


class Account(abc.ABC):
    """
    Abstract class representing a single account

    Subclasses are expected to overwrite the `deposit`,
    `withdraw` and `apply_interest` abstract methods

    Attributes:
    -----------
    account_holder : str
        name of the account owner
    interest_rate : int | float
        interest rate applied to the account

    """

    def __init__(self, account_number, account_holder, interest_rate):
        """
        Creates a new `Account` instance

        `Account` is abstract and should never be called directly

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        """
        self.__account_number = account_number
        self.account_holder = account_holder.strip().lower()
        self.interest_rate = interest_rate
        self.__balance = 0

    def __str__(self):
        template = """Account Number: {0}
Account Holder: {1}
Interest Rate: {2}
Balance: ${3}"""
        return template.format(
            self.account_number, self.account_holder, self.interest_rate, self.balance
        )

    @property
    def account_number(self):
        """
        account_number : str
            Unique account number
        """
        return self.__account_number

    @property
    def balance(self):
        """
        balance: int | float
            account balance in dollars
        """
        return self.__balance

    @abc.abstractmethod
    def deposit(self, amount):
        """
        Deposit money in an account

        Parameters
        ----------
        amount : int | float
            amount in dollars to deposit in the account

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` cannot be deposited
        """
        self.__balance += amount

    @abc.abstractmethod
    def withdraw(self, amount):
        """
        Withdraw money from an account

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` cannot be withdrawn
        """
        self.__balance -= amount

    @abc.abstractmethod
    def apply_interest(self):
        """
        Apply the interest rate to the account and update the balance

        Returns
        -------
        None
        """
        self.__balance += self.__balance * self.interest_rate
```

- `Account` defines `__init__`, `__str__`, `withdraw`, `deposit`,
  `apply_interest` functions
  - `__init__` is a basic constructor
  - `__str__` is the string representation
  - `withdraw` is an abstract method for decreasing a balance
    - Since `balance` itself is a private attribute this method does the
      actual adjustment
    - Subclasses are expected to override the to modify the behaviour
      and provide validation, then forward the final result onto the
      super function
  - `deposit` is an abstract method for increasing a balance
    - Works like `withdraw` in that it should be overridden
  - `apply_interest` an abstract method that should be used to apply
    interest
    - Provides a simple default implementation
- We can then define our savings account

``` python
class SavingsAccount(Account):
    """
    Represents a standard savings account

    Savings accounts must have non-negative balances, and
    have interest paid on their balances

    See Also
    --------
    Account : Parent Class
    """

    def __init__(self, account_number, account_holder, interest_rate):
        """
        Creates a new `SavingsAccount` instance

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        """
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """==Savings Account==
{0}"""
        return template.format(super().__str__())

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit must be a non-negative number")
        super().deposit(amount)

    def withdraw(self, amount):
        """
        Withdraw money from an account

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance
        """
        if amount <= 0:
            raise ValueError("A withdrawal must be a non-negative number")
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than the account balance")
        super().withdraw(amount)

    def apply_interest(self):
        super().apply_interest()
```

- The savings account overwrites the `__str__` method to prepend the
  account type

- `__init__` just forwards to the base class

- `deposit` checks that the argument is valid (`> 0`) then forwards it
  to the base class method

  - depositing a negative number is effectively a withdrawal

- `withdraw` does the same but checks that the amount also does not
  exceed the balance

- Apply interest just uses the default implementation

- We then derive from `SavingsAccount` for `LongTermSavingsAccount`

``` python
class LongTermSavingsAccount(SavingsAccount):
    """
    Represents a long term savings account

    An account in which money cannot be withdrawn before the term limit expires.
    After the term limit has expired a reduced interest rate is applied.

    See Also
    --------
    SavingsAccount : Parent class
    """

    def __init__(
        self, account_number, account_holder, interest_rate, term_period_in_weeks
    ):
        """
        Creates a new `Account` instance

        `Account` is abstract and should never be called directly

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        term_period_in_weeks : int
            length of the high yield savings term in weeks
        """
        self.__start_date = datetime.date.today()
        self.__term_period = term_period_in_weeks
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """{0}
Term Period: {1} weeks
Start Date: {2}
Maturation Date: {3}
Has matured? {4}"""
        formatted = template.format(
            super().__str__(),
            self.term_period,
            self.start_date,
            self.maturation_date,
            self.has_matured(),
        )
        return formatted.replace("Savings Account", "Long Term Savings Account")

    @property
    def start_date(self):
        """
        start_date : datetime.date
            date the current term period started
        """
        return self.__start_date

    @property
    def term_period(self):
        """
        term_period : int
            length of the term in weeks
        """
        return self.__term_period

    @property
    def maturation_date(self):
        """
        maturation_date : datetime.date
            date the account matures
        """
        return self.__start_date + datetime.timedelta(weeks=self.__term_period)

    def has_matured(self):
        """
        Indicates if an account has matured

        Returns
        -------
        `True` if the account has matured else, `False`
        """
        return datetime.date.today() >= self.maturation_date

    def withdraw(self, amount):
        """
        Withdraw money from a Long Term Savings Account

        Money cannot be withdrawn unless the account has matured

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance.
        ValueError
            Raised if the account has not
            yet matured
        """
        if not self.has_matured():
            raise ValueError("Cannot withdraw from an immature account")
        super().withdraw(amount)

    def apply_interest(self):
        """
        Apply interest to a Long Term Savings Account

        The applied interest for a Long Term Savings account is quartered
        if the account has matured

        Returns
        -------
        None
        """
        effective_rate = self.interest_rate
        if self.has_matured():
            effective_rate /= 4
        self.deposit(self.balance * effective_rate)

    def manage_account(self, transfer_account=None):
        """
        Manage a matured long term savings account

        A mature long term savings account can be closed
        by providing an alternate account to transfer the
        balance into. Alternately if no account is provided
        the account is reinvested and a new term starts.

        The owner of the long term savings account and the
        account to transfer into must be the same

        Parameters
        ----------
        transfer_account : Account, optional
            account to transfer into, pass None to reinvest instead, by default None

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised in attempting to manage an immature account
        ValueError:
            Could not transfer to the new account
        """
        if not self.has_matured():
            raise ValueError("Cannot manage an immature account")
        if transfer_account is None:
            self.__start_date = datetime.date.today()
        else:
            balance = self.balance
            try:
                self.withdraw(balance)
                transfer_account.deposit(balance)
            except ValueError as e:
                # need to ensure balances preserved
                if not self.balance == balance:
                    self.deposit(balance - self.balance)
                    raise ValueError(str(e))
```

- This class has two new attributes, `start_date` and `term_period`

- The term period is passed to the constructor as an integer number of
  weeks

- The start date is calculated at `__init__` time

- Note that we use the `datetime` library rather than `time`

  - `datetime` provides similar time objects that we can perform
    comparisons and arithmetic on
  - `datetime.date.today()` is the equivalent of `time.localtime()` and
    returns the current `date`
    - `date` means there is no hours, minutes, seconds etc.
    - If we want this we would use `datetime.datetime.today()` instead

- We provide a property `maturation_date`

  - This is a bit different to other properties we’ve seen
  - It doesn’t mask a private attribute
  - Instead it quickly calculates the `maturation_date` on the fly
  - We use a `datetime.timedelta` object which handles performing the
    arithmetic correctly

  ``` python
    @property
    def maturation_date(self):
        """
        maturation_date : datetime.date
            date the account matures
        """
        return self.__start_date + datetime.timedelta(weeks=self.__term_period)
  ```

- We then define a simple helper function `has_matured` which checks if
  the account has matured

- Since we’re using `datetime` we can just get the current date and
  compare the two

  ``` python
    def has_matured(self):
        """
        Indicates if an account has matured

        Returns
        -------
        `True` if the account has matured else, `False`
        """
        return datetime.date.today() >= self.maturation_date
  ```

- The Long Term Savings Account can just use the `SavingsAccount`
  deposit method

- We update the `withdraw` method to throw an error if the account
  hasn’t matured

  ``` python
    def withdraw(self, amount):
        """
        Withdraw money from a Long Term Savings Account

        Money cannot be withdrawn unless the account has matured

        Parameters
        ----------
        amount : int | float
            amount to withdraw from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance.
        ValueError
            Raised if the account has not
            yet matured
        """
        if not self.has_matured():
            raise ValueError("Cannot withdraw from an immature account")
        super().withdraw(amount)
  ```

- We also have to redefine our `apply_interest`

  - We apply a different effective rate for a matured account
  - This does not fit the signature, so we can’t just use the super
    method
  - Instead we calculate the effective rate and then use `deposit`

  ``` python
    def apply_interest(self):
        """
        Apply interest to a Long Term Savings Account

        The applied interest for a Long Term Savings account is quartered
        if the account has matured

        Returns
        -------
        None
        """
        effective_rate = self.interest_rate
        if self.has_matured():
            effective_rate /= 4
        self.deposit(self.balance * effective_rate)
  ```

- We also add a new function for handling a matured account

  ``` python
    def manage_account(self, transfer_account=None):
        """
        Manage a matured long term savings account

        A mature long term savings account can be closed
        by providing an alternate account to transfer the
        balance into. Alternately if no account is provided
        the account is reinvested and a new term starts.

        The owner of the long term savings account and the
        account to transfer into must be the same

        Parameters
        ----------
        transfer_account : Account, optional
            account to transfer into, pass None to reinvest instead, by default None

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised in attempting to manage an immature account
        ValueError:
            Could not transfer to the new account
        """
        if not self.has_matured():
            raise ValueError("Cannot manage an immature account")
        if transfer_account is None:
            self.__start_date = datetime.date.today()
        else:
            balance = self.balance
            try:
                self.withdraw(balance)
                transfer_account.deposit(balance)
            except ValueError as e:
                # need to ensure balances preserved
                if not self.balance == balance:
                    self.deposit(balance - self.balance)
                    raise ValueError(str(e))
  ```

- This works in two ways

  1. If no `transfer_account` is provided, a new term period is started

  2. If a `transfer_account` is provided, the method attempts to
      transfer the balance to this account

      - This can potentially fail
      - We don’t want the user to lose money
      - So we wrap this in a `try...except` block
      - If transfer fails we ensure that both accounts maintain their
        original balances
      - Then report to the user

- Lastly we define a `CreditAccount` class

- Works very similar to a `SavingsAccount` but can only have negative
  balances

``` python
class CreditAccount(Account):
    """
    Represents a basic credit account

    Savings accounts must have non-positive balances, and
    charge interest on their debts

    See Also
    --------
    Account : Parent Class
    """

    def __init__(
        self, account_number, account_holder, interest_rate, max_withdrawal_limit
    ):
        """
        Creates a new `SavingsAccount` instance

        Parameters
        ----------
        account_number : str
            Unique account number
        account_holder : str
            Name of the account holder
        interest_rate : int | float
            interest rate applied to the account
        max_withdrawal_limit : int | float
            maximum account that can be loaned out at once
        """
        self.__max_withdrawal_limit = max_withdrawal_limit
        super().__init__(account_number, account_holder, interest_rate)

    def __str__(self):
        template = """==Credit Account==
{0}
Maximum Withdrawal Limit: {1}"""
        formatted_string = template.format(
            super().__str__(), self.__max_withdrawal_limit
        )
        return formatted_string.replace("Balance", "Balance owed").replace("$-", "-$")

    def deposit(self, amount):
        """
        Pay off a Credit loan

        Parameters
        ----------
        amount : int | float
            amount to pay off in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if 1amount` is not a positive integer
        ValueError
            Raised if deposit is greater than the current debt
        """
        if amount <= 0:
            raise ValueError("A deposit must be a non-negative number")
        if amount + self.balance > 0:
            raise ValueError(
                "Exceeded max deposit limit: {0}".format(-1 * self.balance)
            )
        super().deposit(amount)

    def withdraw(self, amount):
        """
        Take out a loan of credit

        Parameters
        ----------
        amount : int | float
            amount to loan from the account in dollars

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if `amount` is non-negative or the greater than
            the account balance
        """
        if amount <= 0:
            raise ValueError("A withdrawal must be a non-negative number")
        if self.balance - amount < -1 * self.__max_withdrawal_limit:
            raise ValueError("Cannot exceed withdrawal limit")
        super().withdraw(amount)

    def apply_interest(self):
        """
        Applies interest to any loans

        Returns
        -------
        None
        """
        super().apply_interest()
```

- We also add a new `max_withdrawal_limit` attribute passed in via the
  `__init__`
- This limits how much credit can be withdrawn
- `deposit` can now only be used to pay off a line of credit
  - Prevents the balance going positive
- `withdraw` checks that the withdrawal keeps the balance under the
  withdrawal limit

We can then define our `AccountSystem`, this is basically the
`FashionShop` renamed. However we also add a second dictionary
`account_name_dictionary` which stores all the accounts where the list
of accounts associated with a specific account holder is keyed by that
account holder. This means we can do fast lookup both by account number
(to get a specific account) or by client to get all their associated
accounts. We provide two methods `get_account` which performs the id
based lookup and `find_users_accounts` which finds the accounts
associated with a user

``` python
# Exercise 11.1b Account System
#
# Provides a class for managing and storing collections of accounts

import pickle


class AccountSystem:
    """
    Represents the account management system of a bank
    """

    def __init__(self):
        """
        Create a new `AccountSystem` instance
        """
        self.__account_dictionary = {}
        self.__account_name_dictionary = {}

    def __str__(self):
        print_string = ""
        for holder, accounts in self.__account_name_dictionary.items():
            print_string += "Client: " + str(holder) + "\n"
            account_list = "\n".join(map(str, accounts))
            print_string += account_list + "\n"
        return print_string

    def save(self, filename):
        """
        Save the `AccountSystem` to a given file

        `AccountSystem` is saved as a pickled binary file in the file given
        by `filename`. The file is created if it doesn't exist. If the file
        already exists it is overwritten

        Parameters
        ----------
        filename : str
            path to the file to save

        Returns
        -------
        None

        Raises
        ------
        Exceptions
            raised if the file fails to save

        See Also
        --------
        AccountSystem.load : load a `AccountSystem` object from a file
        """
        with open(filename, "wb") as output_file:
            pickle.dump(self, output_file)

    @staticmethod
    def load(filename):
        """
        Create an `AccountSystem` instance from a pickled binary file

        Parameters
        ----------
        filename : str
            path to a file containing pickled `FashionShop` data

        Returns
        -------
        AccountSystem
            the loaded `AccountSystem` instance

        Raises
        ------
        Exceptions
            raised if the file fails to load

        See Also
        --------
        AccountSystem.save : saves an `AccountSystem` instance
        """
        with open(filename, "rb") as input_file:
            accounts = pickle.load(input_file)
        return accounts

    def add_new_account(self, account):
        """
        Store a new account in the reference system

        The provided `account` can be indexed by it's `account_number` parameter

        Parameters
        ----------
        account : Account
            account to add to the inventory system

        Returns
        -------
        None

        Raises
        ------
        KeyError
            Raised if the accounts's `account_number` is already registered as a key
        """
        if account.account_number in self.__account_dictionary:
            raise KeyError("This account number is already in use")
        self.__account_dictionary[account.account_number] = account
        if account.account_holder in self.__account_name_dictionary:
            self.__account_name_dictionary[account.account_holder].append(account)
        else:
            self.__account_name_dictionary[account.account_holder] = [account]

    def get_account(self, account_number):
        """
        Get the account with the corresponding account number

        Parameters
        ----------
        account_number : str
            account_number of the account to find

        Returns
        -------
        Account | None
            Returns an `Account` with a matching `account_number` if it exists, else `None`
        """
        return self.__account_dictionary.get(account_number)

    def find_users_accounts(self, name):
        """
        Find the accounts associated with a given user

        Parameters
        ----------
        name : str
            account holder to search for

        Returns
        -------
        List[Account]
            list of accounts held by the given name, if there are no matches the list is empty
        """
        name = name.strip().lower()
        try:
            return self.__account_name_dictionary[name]
        except KeyError:
            return []
```

Below demonstrates how the code works

``` python
# Test Savings Account
new_saving = SavingsAccount(1, "Alice", 0.003)
new_saving.deposit(100)
new_saving.withdraw(50)
new_saving.apply_interest()

# Test long-term savings
new_long_term = LongTermSavingsAccount(2, "Alice", 0.012, 26)
new_long_term.deposit(100)
new_long_term.apply_interest()

# Test Credit
new_credit = CreditAccount(3, "Bob", 0.08, 1000)
new_credit.withdraw(500)
new_credit.apply_interest()

account_system = AccountSystem()
account_system.add_new_account(new_saving)
account_system.add_new_account(new_long_term)
account_system.add_new_account(new_credit)

print("Getting the account with a specific id")
print(account_system.get_account(1))
print("Getting all accounts associated with a specific client")
print(account_system.find_users_accounts("felix"))
print("Printing the entire system")
print(account_system)
```

    Getting the account with a specific id
    ==Savings Account==
    Account Number: 1
    Account Holder: alice
    Interest Rate: 0.003
    Balance: $50.15
    Getting all accounts associated with a specific client
    []
    Printing the entire system
    Client: alice
    ==Savings Account==
    Account Number: 1
    Account Holder: alice
    Interest Rate: 0.003
    Balance: $50.15
    ==Long Term Savings Account==
    Account Number: 2
    Account Holder: alice
    Interest Rate: 0.012
    Balance: $101.2
    Term Period: 26 weeks
    Start Date: 2026-02-08
    Maturation Date: 2026-08-09
    Has matured? False
    Client: bob
    ==Credit Account==
    Account Number: 3
    Account Holder: bob
    Interest Rate: 0.08
    Balance owed: -$540.0
    Maximum Withdrawal Limit: 1000

### Create a User Interface Class

- We now have our data items (`StockItem`) and how container for
  managing them `FashionShop`

- The last step is to provide a component that handles the user
  interface

- We’ll create a class `FashionShopShellApplication` to handle the UI

- The class should

  1. Initialise the application, by loading from a file (or creating a
      new instance if this fails)
  2. Display the menu to the user

- This class provides a text-based interface

- In future we may swap this for a graphical interface

#### Initialise the User Interface

- We’ll define our `__init__` method to try and load from a file

- If the load fails we then pass an empty instance

- We use an internal `__shop` attribute to store the inventory
  management component

  ``` python
    import FashionShop


    class FashionShopApplication:
        def __init__(self, filename):
            """
            Creates a new `FashionShopApplication`

            Attempts to load a `FashionShop` from the provided file. Otherwise
            an empty instance is created

            Parameters
            ----------
            filename : str
                path to a file containing pickled `FashionShop` data

            See Also
            --------
            FashionShop : Main class for handling inventory management
            """
            FashionShopApplication.__filename = filename
            try:
                self.__shop = FashionShop.FashionShop.load(filename)
            except:  # noqa: E722
                print("Failed to load Fashion Shop")
                print("Creating an empty Fashion Shop")
                self.__shop = FashionShop.FashionShop()
  ```

- We might then declare our `FashionShopApplication` as follows

  ``` python
    ui = FashionShopApplication("fashionshop.pickle")
  ```

#### Implementing the User Menu

- The next step is to implement our standard looping menu

- We’ll implement this as a method

- Each option will then correspond to another method defined on the
  `FashionShopApplication`

  ``` python
      def main_menu(self):
        """
        Provides a looping main menu. Users are able to

        1. Create a new item
        2. add stock to an existing item
        3. sell stock
        4. show a stock report
        5. exit

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid command is received. Should not arise in
            production. Report if encountered
        """

        prompt = """Fashion Shop Inventory Management

  1. Create a New Stock Item
  2. Add Stock to an Existing Item
  3. Sell Stock
  4. Stock Report
  5. Exit

  Enter your command: """

        while True:
            command = BTCInput.read_int_ranged(prompt, 1, 5)
            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
                self.__shop.save(self.__filename)
                print("Shop data saved")
                break
            else:
                raise ValueError(
                    "Invalid command id {0} encountered in main menu!".format(command)
                )
  ```

- This follows the same structure of all our previous menu setups

- The only difference is this time it’s been wrapped in a class

- Starting the program looks like,

  ``` python
    ui = FashionShopApplication("fashionshop.pickle")
    ui.main_menu()
  ```

#### Implement the User Interface Behaviours

- Now we need to implement the menu options

- We already partially implemented these before (see [Implement
  Application Behaviours](#implement-application-behaviours)) we just
  need to reimplement them as part of the class, or provide a connection

- For example, we write a `sell_stock` wrapper as below,

  ``` python
      def sell_stock(self):
        print("Sell Stock")

        item = self.__shop.find_stock_item(
            BTCInput.read_text("Enter the stock reference: ")
        )
        if item is None:
            print("Item not found")
            return

        print("Selling")
        print(item)

        number_sold = BTCInput.read_int_ranged(
            "How many to sell? (0 to abandon) - {0} in current stock: ".format(
                item.stock_level
            ),
            min_value=0,
            max_value=item.stock_level,
        )
        if not number_sold:
            print("Sell item cancelled")
            return

        item.sell_stock(number_sold)
        print("Items sold")
  ```

- This walks through the sales process

- First the user is prompted for a reference to get an item

- Then the user is prompted for an amount to sell

- We use the `read_input_ranged` to ensure the provided number is valid

- Once validated we then forward to the item’s `sell_stock` method

> [!NOTE]
>
> **You will spend a lot of time writing code to deal with failure**
>
> The `sell_stock` method does the following,
>
> 1. It handles invalid stock references
> 2. It ensures that we do not sell more inventory than we hold
> 3. It provides the user a way to back out of a sale
>
> The actual “happy path” code, i.e. the code that is followed when
> everything works fine is a very small part of the entire function.
> Multiply this across all the functions and the majority of the code is
> probably taken up with input validation and handling failure cases.

- A complete working version of the code is found in
  [11_FashionShopApplication](./Examples/11_FashionShopApplication)
- We’ve split the classes into their own files for readability purposes
- The program can be run by running
  [FashionShopApplication.py](./Examples/11_FashionShopApplication/FashionShopApplication.py)

#### Exercise: Completing the Banking Application

*Implement a banking application wrapper class to complete the [Bank
Account](#exercise-create-a-banking-application) system created earlier.
This class should work like `FashionShopApplication` attempting to load
from a file, then providing a looping menu. The user should be able to,*

1. *Create a new account*
2. *Deposit into an account*
3. *Withdraw from an account*
4. *View an account*
5. *View all their accounts*
6. *Manage a matured long term savings account*
7. *Apply interest to all accounts*

We first start by templating out our `BankApplication` class using a
similar framework to the FashionShop application

``` python
class BankAccountApplication:
    """
    Provides a text-based interface for Bank Account Management
    """

    def __init__(self, filename):
        """
        Creates a new `BankAccountApplication`

        Attempts to load an existing application from the provided file.
        Otherwise an empty instance is created

        Parameters
        ----------
        filename : str
            path to a file containing pickled `AccountSystem` data

        See Also
        --------
        AccountSystem : Main class for handling bank accounts
        """
        self.__filename = filename
        try:
            self.__accounts = AccountSystem.AccountSystem.load(filename)
        except:  # noqa: E722
            print("Failed to load accounts")
            print("Creating an empty instance")
            self.__accounts = AccountSystem.AccountSystem()

    def main_menu(self):
        """
        Provides a looping main menu

        Users are able to
        1. Create a new account
        2. Deposit into an account
        3. Withdraw from an account
        4. View an account
        5. View all accounts associated with a name
        6. Manage a matured long term savings account
        7. Apply interest to all accounts
        8. Exit

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid command is received. Should not arise in
            production. Report if encountered
        """

        prompt = """Account Management System

1. Create a new account
2. Deposit into an account
3. Withdraw from an account
4. View an account
5. View all accounts associated with a name
6. Manage a matured long term savings account
7. Apply interest to all accounts
8. Exit

Enter your command: """

        while True:
            command = BTCInput.read_int_ranged(prompt, 1, 8)
            if command == 1:
                self.create_new_account()
            elif command == 2:
                self.deposit_into_account()
            elif command == 3:
                self.withdraw_from_account()
            elif command == 4:
                self.view_account()
            elif command == 5:
                self.view_accounts_for_name()
            elif command == 6:
                self.manage_matured_long_term_savings()
            elif command == 7:
                self.__accounts.apply_interest()
            elif command == 8:
                self.__accounts.save(self.__filename)
                print("Accounts saved")
                break
            else:
                raise ValueError(
                    "Invalid command id {0} encountered in main menu! Please report!".format(
                        command
                    )
                )
```

The `__init__` is simple as it first tries to load the accounts from a
given file (storing this filename for later saving), else creating an
empty `AccountSystem` if one is not found.

The menu also uses our standard numeric interface. Now we need to start
implementing our methods. The most complicated for us being creating a
new account. To start with we know that all accounts have an interest
rate. Depending on if we are viewing this program as something that a
bank owner would use to manage their internal system, or something that
the a client uses we might want to implement this differently.

One question is around the interest rate we apply to accounts. If this
was client facing. We probably don’t want them specifying their own
interest rate. So instead the application provides some logic to
determine the interest rate to apply to a new account. This is done by
using class variables to define interest rates for `SavingsAccounts` and
`CreditAccounts`. We then also provide a static method that calculates
the interest rate for a long-term savings account based on the principle
that the longer the term is the higher the interest.

``` python
class BankAccountApplication:
    """
    Provides a text-based interface for Bank Account Management

    Class Attributes
    ----------------
    savings_account_interest : float
        current interest rate on newly opened savings accounts
    credit_account_interest : float
        current interest rate on newly opened credit accounts
    """

    savings_account_interest = 0.01
    credit_account_interest = 0.10

    @staticmethod
    def calculate_long_term_interest(term_limit):
        """
        Calculates the bonus interest assigned to a long term savings account

        Parameters
        ----------
        term_limit : int
            proposed term limit in weeks

        Returns
        -------
        float
            interest rate for a long-term savings account
        """
        term_contribution = (
            term_limit / Account.LongTermSavingsAccount.max_term_limit * (0.1)
        )
        return BankAccountApplication.savings_account_interest + term_contribution
```

Similarly here, we don’t want a client to be able to put an arbitrary
term limit in. So we’ll add class variables to the
`LongTermSavingsAccount` for the min and max term limits, and provide a
static validation method.

``` python
class LongTermSavingsAccount(SavingsAccount):
    """
    Represents a long term savings account

    An account in which money cannot be withdrawn before the term limit expires.
    After the term limit has expired a reduced interest rate is applied.

    Class Attributes
    ----------------
    min_term_limit: int
        minimum term limit in weeks
    max_term_limit: int
        maximum term limit in weeks

    See Also
    --------
    SavingsAccount : Parent class
    """

    min_term_limit = 12
    max_term_limit = 156

    @staticmethod
    def validate_term_limit(term_limit):
        """
        Validates a proposed term limit

        Parameters
        ----------
        term_limit : int
            proposed term limit in weeks

        Returns
        -------
        bool
            `True` if the proposed term limit is valid, else `False`
        """
        return (
            LongTermSavingsAccount.min_term_limit
            <= term_limit
            <= LongTermSavingsAccount.max_term_limit
        )
```

Now we can move on to implementing our account creation function. Here
the user has to specify the account type to create. Then they are
prompted to provide an account holder. The next bit of fun we introduce
is to have the user’s account number then be randomly generated. We’ll
make the account number a 4 character alphanumeric string. (We keep it
small to make it easy to demo)

``` python
    def create_new_account(self):
        """
        Create a new account and add it to the system

        Prompts the user for the type of account to create and
        the necessary descriptors of the item. The account is
        then added to the system

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid account type id is encountered.
            Should not arise in production, please report if found.
        """
        menu = """Create New Account

1. Savings Account
2. Long Term Savings Account
3. Credit Account

Enter account type: """

        def generate_account_number():
            """
            Generates an account number

            The generated account number is a 16 character random
            alphanumeric string

            Returns
            -------
            str
                string representing a valid account number
            """
            account_number_string_length = 4
            account_number_string_tuple = (
                "A",
                "B",
                "C",
                "D",
                "E",
                "F",
                "G",
                "H",
                "I",
                "J",
                "K",
                "L",
                "M",
                "N",
                "O",
                "P",
                "Q",
                "R",
                "S",
                "T",
                "U",
                "V",
                "W",
                "X",
                "Y",
                "Z",
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            )

            account_number = "".join(
                random.choices(
                    account_number_string_tuple, k=account_number_string_length
                )
            )
            return account_number

        account_type = BTCInput.read_int_ranged(menu, 1, 3)
        if account_type < 1 or account_type > 3:
            raise ValueError(
                "Invalid account type id {0} encountered while creating account".format(
                    account_type
                )
            )

        account_number = generate_account_number()
        account_holder = BTCInput.read_text("Enter account holder: ")
```

You can see we define a tuple that contains the possible characters. We
then use `random.choices` to select the appropriate number of characters
(with replacement) where the number of characters is defined by
`account_number_string_length` (so we can easily modify it). To convert
from a collection to a string we use `"".join` to join the characters
together, the empty string means that no extra characters are embedded.

Now that we’ve got the account number, the account holder and the type
of account we can proceed. For a `SavingsAccount` we have all the
details required to create the account. For a `LongTermSavingsAccount`
we have to get the term limit, (making sure it’s valid) and for a
`CreditAccount` we have to get the credit limit. Once that’s done we
then add it to the `AccountSystem`

``` python
        if account_type == 1:
            print("Creating a savings account")
            account = Account.SavingsAccount(
                account_number,
                account_holder,
                BankAccountApplication.savings_account_interest,
            )
            print("Created a new savings account {0}".format(account_number))
        elif account_type == 2:
            print("Creating a long-term savings account")
            while True:
                term_limit = BTCInput.read_int_ranged(
                    "Enter term limit ({0} - {1}): ".format(
                        Account.LongTermSavingsAccount.min_term_limit,
                        Account.LongTermSavingsAccount.max_term_limit,
                    ),
                    Account.LongTermSavingsAccount.min_term_limit,
                    Account.LongTermSavingsAccount.max_term_limit,
                )
                if Account.LongTermSavingsAccount.validate_term_limit(term_limit):
                    break
            account = Account.LongTermSavingsAccount(
                account_number,
                account_holder,
                BankAccountApplication.calculate_long_term_interest(term_limit),
                term_limit,
            )
            print("Created a new long-term savings account {0}".format(account_number))
        elif account_type == 3:
            print("Creating a  credit account")
            withdrawal_limit = BTCInput.read_float("Enter max withdrawal limit: ")
            account = Account.CreditAccount(
                account_number,
                account_holder,
                BankAccountApplication.credit_account_interest,
                withdrawal_limit,
            )
            print("Created a new credit account {0}".format(account_number))
        self.__accounts.add_new_account(account)  # type: ignore
```

Deposit, withdraw and view account are all implemented using similar
logic. First the user is prompted for an account number, then we perform
a function. We’ll extract this `get_account` behaviour into a function

``` python
    def get_account(self):
        """
        Prompts the user for an account number and returns any match

        Returns
        -------
        Account | None
            Account is the account number matches, else `None`
        """
        account_number = BTCInput.read_text("Enter account number: ").upper().strip()
        return self.__accounts.get_account(account_number)
```

The implementations for deposit, withdraw, and view then largely just
need to forward onto the appropriate message on the account, `deposit`,
`withdraw` and `__str__` respectively

``` python
    def deposit_into_account(self):
        """
        Deposit into a user-prompted account

        User is prompted for an account, if the account exists,
        the user is then prompted for how much to deposit

        Returns
        -------
        None
        """
        print("Deposit into account")

        account = self.get_account()

        if account is None:
            print("Account not found")
            return
        print("Depositing")
        print(account)

        try:
            amount = BTCInput.read_float(
                "Enter amount to deposit (Current balance: {0}): ".format(
                    account.balance
                )
            )
            account.deposit(amount)
        except ValueError as e:
            print(e)

    def withdraw_from_account(self):
        """
        Withdraw from a user-prompted account

        User is prompted for an account, if the account exists,
        the user is then prompted for how much to withdraw

        Returns
        -------
        None
        """
        print("Withdraw from account")

        account = self.get_account()
        if account is None:
            print("Account not found")
            return
        print("Withdrawing")
        print(account)

        try:
            amount = BTCInput.read_float(
                "Enter amount to withdraw (Current balance: {0}): ".format(
                    account.balance
                )
            )
            account.withdraw(amount)
        except ValueError as e:
            print(e)

    def view_account(self):
        """
        Display a user-specified account

        Returns
        -------
        None
        """
        print("View account")

        account = self.get_account()
        if account is None:
            print("Account not found")
            return
        print(account)
```

Next we want to implement the complement to `view_account` which is
`view_account_by_name`. This simply takes a user’s name and then
forwards onto the appropriate message on the `AccountSystem`. The
resulting list is then converted to a string representation using `map`
and displayed to the user

``` python
    def view_accounts_for_name(self):
        """
        Find and display accounts for a user prompted name

        Names are converted to lower case and stripped of
        leading and trailing whitespace

        Returns
        -------
        None
        """
        print("View account holders accounts")

        accounts = self.__accounts.find_users_accounts(
            BTCInput.read_text("Enter account holder: ")
        )
        print("\n".join(map(str, accounts)))
```

Our last major implementation detail is then to implement managing a
matured savings account. Recall from the [original
exercise](#exercise-create-a-banking-application) that a long-term
savings account that has matured can either be reinvested or transferred
to another account. To implement this structure as follows,

1. The user is prompted for an account number
2. We verify that account number is valid and a long-term account
3. We then validate that the account has matured
4. The user is then prompted if they want to reinvest
    - If yes, the account is reinvested and the process stops
    - Else we continue
5. The user is then prompted for the account to transfer to
6. We validate that the account exists, and the account holder matches
    the long term account
7. We then attempt to close out the account

The implementation is given below,

``` python
    def manage_matured_long_term_savings(self):
        """
        Close out or reinvest a user specified matured long-term account

        Returns
        -------
        None
        """

        account_number = BTCInput.read_text("Enter account number: ").upper().strip()

        account = self.__accounts.get_account(account_number)
        if account is None:
            print("Account not found")
            return
        if not isinstance(account, Account.LongTermSavingsAccount):
            print("Account is not a long term savings account")
            return
        if not account.has_matured():
            print("Account cannot be managed: has not matured")
            return

        reinvest = BTCInput.read_int_ranged(
            "Reinvest this account? (1 - yes, 0 - no): ", 0, 1
        )
        if reinvest:
            account.manage_account()
            return

        holder = account.account_holder
        other_accounts = set(self.__accounts.find_users_accounts(holder)).difference(
            {account}
        )
        if len(other_accounts) == 0:
            print("Account cannot be closed: No accounts to transfer to")
            return
        print("\n".join(map(str, other_accounts)))

        account_number = (
            BTCInput.read_text("Enter transfer account number: ").upper().strip()
        )

        transfer_account = self.__accounts.get_account(account_number)
        if transfer_account is None:
            print("Account not found")
            return
        if transfer_account.account_holder != holder:
            print("Could not transfer, account holder does not match")
            return
        try:
            account.manage_account(transfer_account)
            print(
                "Funds in account {0} transferred to account {1}".format(
                    account.account_number, transfer_account.account_number
                )
            )
        except ValueError as e:
            print("Failed to close account:", e)
```

Our last step is to implement the application of interest rates. This is
done to all accounts, typically at some specified point, e.g. the first
of each month. However, the natural place for this to be implemented is
on the `AccountSystem` class,

``` python
class AccountSystem:
    """
    Represents the account management system of a bank
    """
    ...
    def apply_interest(self):
        """
        Applies interest to all accounts in the system

        Returns
        -------
        None
        """
        for account in self.__account_dictionary.values():
            account.apply_interest()
```

We then just need to forward to this method from `BankApplication`, as
can be seen already in the `main_menu` function

``` python
def main_menu(self):
    ...
    elif command == 7:
        self.__accounts.apply_interest()
```

Running the program is the same as for our Fashion Shop Application

``` python
ui = BankAccountApplication("accounts.pkl")
ui.main_menu()
```

##### Design Review

Now that we’ve completed the program it’s worth reviewing the program.
Overall the design is one that we’re pretty happy with but there could
be some improvements. The most glaring is that account numbers must be
unique, yet our program doesn’t enforce this. There are a number of
solutions. The ideal way to handle this would be that when we try to add
an account if `self.__account.add_new_account(account)` returns a
`KeyError` would be to regenerate a new number. However this number is
private and can’t be changed once an object is created. We don’t want to
change this, so we would have to create an entire new object which is
fine, but the way the code is organised means that it’s not clear when
we get to adding the account, what type it is. Solutions include,

1. Moving the call to `add_new_account` to each individual account type
    path

    - This means we can catch the `KeyError` regenerate a new number,
      and then rebuild the appropriate account type
    - Has the downside that we replicate the code for adding the account
      for every account type

2. Implement a method on `AccountSystem` that tells us if a generated
    account number is valid.

    - This means we can check at the time of number generation
    - Repeat until we get a valid one
    - This has the downside that if we had a concurrent system, we could
      potentially be told that the account number is free, then have
      another process beat us to using that number
    - Plus we already have the `KeyError` to tell us if the number is
      free
      - In Python you generally prefer to *ask for forgiveness* rather
        than *permission*
        - i.e. use exceptions over checking then setting

3. Handle the Error, report it to the user and leave it up to them how
    they want to resolve

    - Simplest implementation
    - Probably not the best user experience (since user might have to
      enter the same details all over again)

None of the solutions above are strictly the *best* they are all just
options to consider. For this small program we’ve left the bug in as a
demonstration.

There are a couple other design considerations. One is about cohesion,
we have logic for defining the interest applied to accounts separate
from the `Account` class stored on arguably the UI class
`BankAccountApplication`. This is fine for this small system but perhaps
suggests a lack of cohesion. If we were to change out our UI class to a
GUI that GUI would then have to implement the same business logic. One
solution is to move those details to the `Account` class hierarchy. Here
each subclass might have to define a property `base_interest_rate` which
defines the default interest rate for an account. On the other hand if
we decide that an `Account` should have an interest rate, but has no
business knowing how that interest rate is set, we may have to implement
this behaviour either in the `AccountSystem` or in another class that
purely handles the business logic around interest rates and propagates
that through to the accounts. For the scale of this system, we probably
don’t need that extra layer (remember the simpler the solution the
easier, we can always refactor later)

The last question is more on of a philosophical design choice. This
program implements features that are very client focused such as
creating accounts, depositing and withdrawing (and arguably managing a
long-term account), and some that a more targeted towards an internal
user (applying interest, the ability to modify any account and see
anybody’s account). This is fine for a simple toy program like the one
we’re building. But if we were to scale this up we would probably want
to split out the client-facing functions from the internal user facing
components. Both would still talk to the same underlying data model
though.

### Design With Classes

- We can show the final class diagram and interactions of our program
  below
- (We’ve hidden some of the subclasses and `object` for simplicity)

``` mermaid
---
title: Complete Fashion Shop Class Diagram
---

classDiagram

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

    class FashionShop {
        dictionary __stock_dictionary
    }

    class FashionShopApplication {
        FashionShop __shop
    }

    StockItem <|-- Dress
    StockItem <|--  Pants

    FashionShop "1" o-- "0..n" StockItem
    FashionShopApplication "1" *-- "1" FashionShop


```

- Class diagrams more broadly discuss associations
- One form of association is inheritance which we’ve seen before is
  represented by a open arrow
- Another is aggregation represented by an open diamond-headed arrow
  - We say that `FashionShop` aggregates `StockItem` because it is a
    container
  - We can additionally specify *multiplicities*
  - i.e. how many items are represented in a relationship
  - We do this by adding number on either end of the arrow
  - Above we have $1$ next to the `FashionShop` and $0 \ldots n$ next to
    `StockItem`
  - This says that one `FashionShop` aggregates $0$ to an arbitrary
    finite number of `StockItems`
- A similar relationship is *composition*
  - Where as inheritance is a *is-a* relationship
  - Composition can be thought of as a *has-a* relationship
  - Again we can specify multiplicities
  - Here we indicate that there is one `FashionShopApplication` which
    contains one `FashionShop`
- These class diagrams help express the structure and relationship of a
  system
- Good way to describe how the elements of your program fit together

### Python Sets

- Sets are collections of values like tuples and lists
- They are mutable like lists
- Unlike lists each value in a set must be unique

#### Make Something Happen: Investigating Sets

*Work through the following steps in the python interpreter to
understand sets*

A set can be created by explicitly using the `set` initializer

``` python
set1 = set()
set1
```

    set()

This creates an empty set.

We can add to set like with a list, but we use `add` rather than
`append`

``` python
set1.add(1)
set1
```

    {1}

Sets can only hold one instance of a given value, what happens if we try
to add the same element twice?

``` python
set1.add(1)
set1
```

    {1}

As we can see the set contents have not changed, there is only one `1`
in the set. However the other thing to observe is that no error was
thrown, the second `add` fails silently

We can add multiple values as long as they are distinct

``` python
set1.add(2)
set1
```

    {1, 2}

Like with lists and dictionaries there is a quick set declaration
syntax. We simply provide a comma-separated list enclosed in curly
braces

``` python
set2 = {2,3,4,5}
set2
```

    {2, 3, 4, 5}

This is similar but distinct to the dictionary case where the curly
brace list is comma separated `key:value` pairs

For those familiar with set theory, sets provide the standard suite of
set operations.

`difference` is called on one set, and takes another set as an argument.
It returns a new set containing the elements in the original set that
are not in the argument set, e.g.

``` python
set1.difference(set2)
```

    {1}

and

``` python
set2.difference(set1)
```

    {3, 4, 5}

`Union` returns a set containing the elements that are in either of the
sets

``` python
set1.union(set2)
```

    {1, 2, 3, 4, 5}

`intersection` returns a set containing the elements that are in both of
the sets

``` python
set1.intersection(set2)
```

    {2}

There are also a number of methods for comparing the contents of a set.
`isdisjoint` returns `True` if the two sets have no common elements

``` python
set1.isdisjoint(set2)
```

    False

`issubset` takes the form `seta.issubset(setb)` and returns `True` if
`seta` is a subset of `setb`. $A$ being a subset of $B$ means all the
elements of $A$ are in $B$

``` python
set3 = {2, 3}
set3.issubset(set2)
```

    True

The opposite method is `issuperset` which returns true if the set the
method is called on is a superset of the argument. $A$ is a superset of
$B$ if $A$ contains every element of $B$

``` python
set3.issuperset(set2)
```

    False

- How are sets useful?
  - Let us remove duplicates in a collection

``` python
set("Hello World")
```

    {' ', 'H', 'W', 'd', 'e', 'l', 'o', 'r'}

- Python’s sets are unordered
- They can be sorted using the function `sorted`

``` python
print(sorted("Hello World"))
print(sorted(set("Hello World")))
```

    [' ', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
    [' ', 'H', 'W', 'd', 'e', 'l', 'o', 'r']

- We might also use them to manage a collection of items
  - e.g. a players inventory

``` python
pocket = {"axe", "apple", "herbs", "flashlight"}
```

- Sets allow for easy membership checks

- especially when we want to look at multiple members

  ``` python
    apple_potion = {"apple", "herbs"}
    if apple_potion.issubset(pocket):
        print("Making an apple potion")
  ```

      Making an apple potion

- In the above example we check that the player’s inventory has the
  ingredients for an apple potion

  - This is done by checking the ingredients are a subset of the
    inventory

- We can then make the apple potion using set operations

  - Use set difference to remove the ingredients
  - Then add an apple potion

  ``` python
    pocket = pocket - apple_potion
    pocket.add("apple potion")
    pocket
  ```

      {'apple potion', 'axe', 'flashlight'}

- The subtraction operator on sets works like the set difference
  operation we’ve seen before

#### Sets and Tags

- Sets are less common than dictionaries and lists
- However they can be very useful
- Our Fashion Shop client has provided an updated spec

> Customers often pursue a similar “look” or “style” e.g. flowery,
> summer, formal, etc. She would like to be able to *tag* stock items so
> they can be easily searched

- Tagging items with descriptors is very common
- Blogs or Youtube videos are often tagged with metadata that describes
  their content
- Sets are a good technique here since each tag should be unique

##### Create a set from a String of Text

- Each `StockItem` should have a `tags` attribute
- `tags` comprises a set of tag values
- Creating a `StockItem` now requires us to input the tag values at
  object creation
- A sample UI might look like,

``` python
print("Enter tags (separated by commas): \033[31moutdoor, spring, informal, short\033[0m")
```

    Enter tags (separated by commas): outdoor, spring, informal, short

- Then need to convert the comma separated list into individual tag
  items

- First we want to normalise tags, i.e. lowercase and leading / trailing
  whitespace stripped

- However, we want to split the individual tags before we strip the
  whitespace

  - Since there might be white space between the words

- So we can first lower, then separate the words using `split`

  - `split` takes a string to split and a separator character (here `,`)
    to split on
  - The separator is not included in the split strings
  - Returns a list containing the new strings

- We can then use `map` to apply the string method `str.strip` to each
  individual tag

  ``` python
    tag_list = str.split(str.lower(tag_string), sep=',')
    tag_list = map(str.strip, tag_list)
    print(list(tag_list))
  ```

      ['outdoor', 'spring', 'informal', 'short']

- The last step is to ensure all the tags are unique by converting to a
  set

  ``` python
    tags = set(tag_list)
  ```

- Now that we’ve defined this pipeline for creating our sets, we should
  really encapsulate it as a method

``` python
class FashionShopApplication:
    ...
    @staticmethod
    def tag_set_from_text(tag_text):
        """
        Create a set of tags from a comma-separated list

        Tags are normalised as lowercase with leading and
        trailing whitespace stripped

        Parameters
        ----------
        tag_text: str
            comma-separated list of tags

        Returns
        -------
        set
            set containing unique tags. Tags are lowercase with
            no leading or trailing whitespace
        """
        tags = set(map(str.strip, str.split(str.lower(tag_text), sep=",")))
        return tags
```

- Implemented as a static method
  - The behaviour is associated with the class
  - But not associated with any specific instance

##### Filter on Tags

- Now that we’ve added tags we need a way to use them to search for
  items

- The client wants to provide a list of tags and receive a list of items
  matching those tags

- Below is a proposed interface

  ``` python
    print("Enter the tags to look for (comma separated): \033[31moutdoor, spring\033[0m")
    print("Stock Reference: BL343")
    print("Type: Blouse\033[0m")
    print("Price: 100")
    print("Stock Level: 0")
    print("Colour: Pink")
    print("""Tags: {"spring", "friendly", "city", "outdoor"}""")
    print("Size: 14")
    print("Style: plain")
    print("Pattern: check")
  ```

      Enter the tags to look for (comma separated): outdoor, spring
      Stock Reference: BL343
      Type: Blouse
      Price: 100
      Stock Level: 0
      Colour: Pink
      Tags: {"spring", "friendly", "city", "outdoor"}
      Size: 14
      Style: plain
      Pattern: check

- We can reuse `get_tag_set_from_text` to create a search set

- We take match to mean the search tags are a *subset* of the item’s
  tags

  - This means that an item must match *all* the tags

- An alternative approach might be to match any items that match *at
  least* one of the tags

  - This could be done by checking the intersection is non-empty

- In the above example we can see the blouse matched because the search
  tags (`{"outdoor", "spring"}`) are a subset of the blouse’s tags
  (`{"spring", "friendly", "city", "outdoor"}`)

- This implementation is thus a simple application of `issubset`

  ``` python
    def match_tags(item):
        """
        Checks if the given item matches the specified search tags

        Parameters
        ----------
        item : StockItem
            StockItem to check for matching tags

        Returns
        -------
        `True` if the search tags are a subset of `item.tags`, else `False`
        """
        return search_tags.issubset(item.tags)
  ```

- We can see that the search tags are passed in via a global parameter
  rather than explicitly through the function signature

- This is so we can use the `filter` python function

- `filter` works like map

  - `map` returns the result of a applying a function to each member of
    a collection
  - `filter` applies a boolean function (one that returns `True` or
    `False`) to each member of a collection, and returns the
    subcollection of all elements that evaluate `True`

  ``` python
    filtered_list = filter(match_tags, stock_list)
  ```

- The above uses `filter` to find all items in the `stock_list` that
  match the specified tags. Putting this all together

``` python
class FashionShop:
    def find_matching_with_tags(self, search_tags):
        """
        Get stock items that match all the specified search tags

        Parameters
        ----------
        search_tags : str
            set of tags to search against.
            Item's must match all tags

        Returns
        -------
        list[StockItem]
            list containing all StockItem's matching the
            specified set of tags. If no matches are found
            the list is empty
        """

        def match_tags(item):
            """
            Checks if the given item matches the specified search tags

            Parameters
            ----------
            item : StockItem
                StockItem to check for matching tags

            Returns
            -------
            `True` if the search tags are a subset of `item.tags`, else `False`
            """
            return search_tags.issubset(item.tags)

        return filter(match_tags, self.__stock_dictionary.values())
```

- `find_matching_with_tags` is added to the `FashionShop` class as it is
  a method for handling a collection of stock items

- It returns the list of matching stock items

- You may notice something odd, we have declared the `match_tags`
  function inside the `find_matching_with_tags` function

- This is allowed in python

- Means that `match_tags` can access variables in the scope of the
  `find_matching_with_tags` function

- The full tags based implementation is given in the
  [FashionShopWithTags](./Examples/12_FashionShopWithTags) folder

- One of the minor implementation details is that as `tags` adds a data
  attribute to `StockItem` we have to bump the version number (for the
  versions in our implementations this is $2 \rightarrow 3$), and update
  `check_version`

- The new implementation below, simply adds a empty tags field to older
  items

  - Note we don’t need to update the version of the subclasses
  - However, we do need to update all their `__init__` signatures too

  ``` python
    class StockItem:
        def check_version(self):
        """
        Checks the version of a `StockItem` instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**StockItem check_version called")
        if self.__StockItem_version < 2:
            self.location = None
            self.__StockItem_version = 2
        if self.__StockItem_version < 3:
            self.tags = set()
            self.__StockItem_version = 3
  ```

#### Sets versus Class Hierarchies

- It’s quite common for customers to provide feedback on the usability
  of their product
- For example our client might prefer the tag-based interface more
  generally over a rigid class structure

> Your client would like to make changes to how the program functions.
> She enjoys using tags to identify stock elements. She finds having to
> specify a specific item type (e.g. pants, jeans, hat etc.) a painful
> process. She would prefer to index all stock using tags. Dresses would
> have the `dress` tag, etc. Together you propose the following mock-up

    Enter stock reference: D001
    Enter price: 120
    Enter tags (separated by commas): dress, colour:red, location:shop window, pattern:swirly, size:12, evening, long

- The client finds searching by tags easy to work with

- Tags are more flexible and remind her more of how she would organise
  stock by hand

- Tags give the flexibility to add new items or change how items are
  described without needing to recompose the class hierarchy

- The only additional request the client has is to allow the ability to
  edit the tags on a stock item

  - Can add or remove tags
  - Can correct edits

- The downside is that any tags that are not entered correctly will
  result in failed searches

  - The class hierarchy enforces that the specified attributes for each
    `StockItem` subclass exist

- A tags only implementation is given by in the
  [TagOnlyFashionShop](./Examples/13_TagOnlyFashionShop/) folder

- The `StockItem` implementation becomes much simpler

- First since there are no longer subclasses, we no longer define it as
  an abstract class

- We update the docstrings and `__init__` method

  - This involves removing all the attributes that do not describe the
    stock id, price or stock level
  - We also increment the version number

  ``` python
    class StockItem:
    """
    Represents a single inventory item

    Attributes
    ----------
    stock_ref : str
        reference id of the stock item
    tags : set[str]
        set of tags describing the stock item

    Class Attributes
    ----------------
    show_instrumentation : bool
        Indicates if instrumentation should be printed
    max_stock_add : int
        maximum amount of stock that can be added to an item's stock level at a time
    min_price : int | float
        minimum price of any stock item
    max_price : int | float
        maximum price of any stock item
    """

    show_instrumentation = True

    max_stock_add = 10

    min_price = 0.5
    max_price = 500

    def __init__(self, stock_ref, price, tags):
        """
        Creates a `StockItem` instance

        Parameters
        ----------
        stock_ref : str
            stock reference id
        price : int | float
            stock price
        tags : set[str]
            set of tags describing the stock item
        """
        if StockItem.show_instrumentation:
            print("**StockItem __init__ called")
        self.stock_ref = stock_ref
        self.__price = price
        self.tags = tags
        self.__stock_level = 0
        self.__StockItem_version = 4
  ```

- Since we no longer have multiple subclasses we can remove the
  `item_name` property

- Then we have to update the `__str__` method

  ``` python
    def __str__(self):
        if StockItem.show_instrumentation:
            print("**StockItem __str__ called")
        template = """Stock Reference: {0}
  Price: {1}
  Stock level: {2}
  Tags: {3}"""
        return template.format(self.stock_ref, self.price, self.stock_level, self.tags)
  ```

- All our actual core functions can stay the same, but we just need to
  adjust the `check_version`

- We could make `check_version` convert all the previous attributes to
  tags, *but* this has a problem

  - All the subclasses that are actually instantiated no longer exist!
  - So really the customer will likely have to remake these objects
  - In our implementation, even though a `StockItem` should not be
    created directly, we can provide a warning message that the user
    should manually update the current object

  ``` python
    def check_version(self):
        """
        Checks the version of a `StockItem` instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**StockItem check_version called")
        if self.__StockItem_version != 4:
            print("Stock item uses old data model, please recreate this item")
  ```

> [!IMPORTANT]
>
> **Data Migration is Painful**
>
> In moving from the class hierarchy to a tags based implementation,
> we’ve encountered one common problem. Data Migration. Before we’ve
> used simple versioning on classes to update them when we change their
> implementation. But here we have a bigger scale problem. What do we do
> when we change the application architecture? We can’t just update the
> subclasses because they no longer exist. For our small toy problem
> manually recreating objects probably works fine.
>
> However if we were working on a larger project we would have to create
> a migration plan. This might be a simple script that converts the old
> data to the new data schema, or for larger projects this might be a
> longer term project where we slowly phase in the new system and phase
> the old system out.

- The `FashionShop` class needs no updates
- It only ever sees objects as `StockItem`s and manages the collection
- We do need to make minor updates to `FashionShopApplication`
  - This is just adjusting how we create new items to reflect that we
    don’t have a class hierarchy

  ``` python
    def create_new_stock_item(self):
        """
        Create a new stock item and add it to the system

        Prompts the user for the necessary descriptors and
        any optional tags then creates a corresponding stock
        item and adds it to the store

        Returns
        -------
        None
        """

        # now we have a valid item so get the common attributes
        stock_ref = BTCInput.read_text("Enter Stock reference: ")
        price = BTCInput.read_float_ranged(
            "Enter price: ",
            min_value=StockItem.StockItem.min_price,
            max_value=StockItem.StockItem.max_price,
        )
        tags = FashionShopApplication.tag_set_from_text(
            BTCInput.read_text("Enter tags (separated by commas): ")
        )

        self.__shop.store_new_stock_item(StockItem.StockItem(stock_ref, price, tags))
  ```

- We’ve also updated the docstring

> [!WARNING]
>
> **Comments can easily go stale**
>
> One of the reasons that people argue against using comments is that
> like code itself, they need to be maintained. As we’ve seen above,
> whenever we modify the code we have to ensure that the comments still
> correctly describe the behaviour. Since the comments we’re talking
> about are the docstrings it’s important to have these, *and* even more
> important they are up to date. Especially if we want to release
> documentation for our API.
>
> However, you should be considered in how you document your code. A
> comment is a maintenance overhead, and an incorrect comment can result
> in a lot of frustration if it confuses someone looking at the code
> base

##### Advantages of Using Sets and Tags

- Client is now in control of how stock is organised
- Tags can be added and searched for on the fly
  - This may get unwieldy if the number of tags gets very large
- The program implementation is much simpler
  - No need for complicated, synchronised class hierarchy
  - Everything is now a stock item

##### Disadvantages of using Classes

- Class hierarchies allow you to implement strict business or
  application logic
- All objects created must obey the specified interfaces
  - For example we enforce that a dress has a size, pattern and colour
- Using open-ended tags means that a required tag (say size) might be
  missing
  - No obligation to specify in the size embedded in the code
- Classes also allow for polymorphism
  - Can make a dress behave differently from a hat for example
  - We saw this with the `__str__` method
  - Each subclass defined it’s own logic for conversion to a string
  - tags don’t provide an easy way to have an item-type dependent
    presentation

> [!IMPORTANT]
>
> **What’s important to the programmer may not be important to the
> customer**
>
> Often when writing programs for other clients it is easy to get
> fixated on developing a piece of logic that the customer may not
> actually like. Equally as a programmer, you may not fully understand
> or appreciate the nature of the businesses logic.
>
> In the case of the Fashion Shop application we created a complex
> hierarchy based on the assumption that the it was important to store
> all the details for different categories of stock. The class hierarchy
> enforces that all objects are fully described.
>
> However, from the client’s perspective as long as the item is properly
> referenced, priced and it’s stock levels tracked, the other
> information is just a useful bonus. She finds it much more useful to
> be able to add and modify tags or organise stock as needed.
>
> Properly understanding the business needs of a client and what their
> important use cases are is a crucial part of project management. One
> of the techniques for solving this is called *[domain-driven
> design](https://en.wikipedia.org/wiki/Domain-driven_design)* which
> strives to make sure that software accurately models the *domain* it
> is applied to

##### Code Analysis: Design Decisions

*Look at the following scenarios and decide if a class-based or tags
based implementation makes sense*

1. *You’re creating banking software for a local bank to manage their
    accounts. The bank offers credit and checking accounts. Should we
    use a class hierarchy?*

    - Yes
    - Accounts are likely to have a rigid set of attributes that all
      need to be specified and validated
    - Some elements are likely common
      - e.g. the account holder details
    - Different account types might specify different attributes
      - e.g. credit account requires a credit limit
    - We can thus use an abstract `Account` class, and then subclass
      this to provide specific implementations
    - Means we can also use method overloading and polymorphism
      - e.g. Different accounts will process funds withdrawals in
        different ways
    - You can see an example in our model [bank
      system](#exercise-create-a-banking-application) class structure

2. *You’ve been approached to help a local gallery track their artwork.
    The gallery holds pictures, sculptures, and manuscripts. Should we
    use a class hierarchy?*

    - Likely not
    - There is likely not a lot of common functionality between the
      objects
    - The items are also likely to be flexibly described rather than
      have a rigid data model
    - The gallery may evolve and change how they categorise
      - e.g. They may switch from categorising by type to categorising
        by artist etc.
    - Sets and tags makes sense here
    - In theory you could just reuse the [tags-only fashion shop
      application](#sets-and-tags) (maybe renaming some items so they
      contextually make sense)

## Summary

- Inheritance can be used to manage a large number of related items
  - Inheritance lets (sub)classes be based on other (super)classes
  - Subclasses inherit the attributes and methods of their parent
  - Subclasses can redefine attributes and methods to override the
    behaviour of the parent
- Structuring a program as individual cohesive components make it easy
  to develop, test and modify parts of a program
  - Components can be implemented as classes that provide specific
    methods
  - e.g. `StockItem` which managed a stocked inventory item
    - Had a `add_stock` to adjust its stock level
  - Different components communicate purely through each others methods
  - e.g. `FashionShop` stores `StockItem` objects via a dictionary
    - Could instead use a database implementation
    - No need to rewrite the other classes as long as the method
      interface is the same
  - Components can be developed and tested independently and
    cooperatively once their interfaces are defined
- Python provides a `set` collection
  - A set is a collection of unique values
  - Mutable like a list
  - An example use for sets is specifying unique, dynamic tags on an
    object
  - The `set` implementation supports all standard set operations
- It’s important to understand client requirements when developing a
  program

## Questions and Answers

1. *Do I have to use a class hierarchy if I want to store many related
    items?*

    - No
    - They are useful when you want to use polymorphism
      - i.e. treat them all as one common object
      - But have each specific type behave differently

2. *What turns an object into a software component?*

    - A component is cohesive
    - It can perform all the functions of it’s domain without needing
      another object
    - e.g. `StockItem`’s methods only rely on it’s internal state and
      some passed in basic parameters
      - No need to reach out to another external object instance
      - `FashionShop` or `FashionShopApplication` may call methods on
        `StockItem` objects
        - These are internally encapsulated in the object
        - So all good, these are still cohesive
      - We don’t want to be calling out to *external* objects
      - Poor cohesion would have methods like `add_stock` and
        `sell_stock` outside in a separate class
    - Considering how easy it would be to swap the class for one with a
      similar interface is a good test of how cohesive a class is
      - If the class is cohesive this should be easy
      - For example if we wanted to swap `FashionShop` from a dictionary
        implementation to a database implementation with the same
        interface
    - When using component based design, it’s a good idea to ensure you
      define your components *before* you start implementing a design
      - Need to ensure that you understand correctly what data is needed
        where and how components will communicate
    - Components can then be implemented individually

3. *Do I have to use object-oriented design to make my programs?*

    - No
    - Python uses duck-typing, which means if we try to call a method on
      an object, it will be called so long as it’s defined
    - Thus we can implement polymorphism without a rigid class hierarchy
    - The downside is without a clear class hierarchy it can be hard to
      propagate method or design changes between related implementations
    - Remember that typically the largest time cost of code is
      maintaining and understanding existing code

4. *Why is the relationship between a subclass and a superclass so
    confusing?*

    - Recall that the *sub* and *super* names derive from set theory
    - So while a *super* class may have less functionality than a *sub*
      class that is because every subclass is an instance of a
      superclass
    - A subclass can be thought of as a more specialised implementation
      of a superclass

5. *What exactly happens when a method in a class is overridden?*

    - When the method is called in python, python first looks for the
      method on the object class
    - If it exists, it’s used, else it looks in the next superclass
    - This continues until the base class for all python instances
      `object` is found
    - If the object is *still* not found an error will be found, for
      example with the `int` object below we try to call the fictitious
      method `foo`

    ``` python
     x = 10
     x.foo()
    ```

        AttributeError: 'int' object has no attribute 'foo'
        ---------------------------------------------------------------------------
        AttributeError                            Traceback (most recent call last)
        Cell In[81], line 2
              1 x = 10
        ----> 2 x.foo()

        AttributeError: 'int' object has no attribute 'foo'

    - Overriding methods can slow a program down as this method
      resolution takes time
    - This is typically not a bottleneck in python programs

6. *What things in my class should be made static?*

    - Static items are always present
    - They are associated with the class, not a specific instance
    - static data attributes are good for storing class wide values
      - For example variables associated with validating data such as a
        max and min value
      - We don’t want to store a copy of these for every object instance
      - So we instead store it as a class attribute
    - static methods are for methods that don’t need an instance of the
      class
      - Validation or object creation methods are a common use case
      - Keeps code associated with the class packaged with the class
      - For example `load` on `FashionShop`, there’s no `FashionShop`
        instance to load into yet

7. *When do I use abstraction?*

    - Used when thinking about an object
    - Abstraction helps reducing noise when considering a system
      - e.g. rather than considering a range of different customers we
        just consider a *Customer*
        - We can then define the basic operations we need on a customer
        - Later we might then specialise for different customers
