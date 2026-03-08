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


x = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
y = Jeans(
    stock_ref="TR12327",
    price=50,
    colour="Black",
    pattern="Plain",
    length=30,
    waist=25,
    style="flared",
)

print(x)
print(y)
