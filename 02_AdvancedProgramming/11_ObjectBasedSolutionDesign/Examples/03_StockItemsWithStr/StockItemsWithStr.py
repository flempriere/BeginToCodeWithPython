# Example 11.3 Fashion Items using properties and __str__
#
# Mocks out the Fashion stock items classes using an inheritance hierachy
# Demonstrates using methods of the superclass in the subclass and
# abstractmethods

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

    def __str__(self):
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
        pass

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
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.size = size

    def __str__(self):
        stock_details = super().__str__()
        template = """{0}
Pattern: {1}
Size: {2}"""
        return template.format(stock_details, self.pattern, self.size)

    @property
    def item_name(self):  # type: ignore
        return "Dress"


class Pants(StockItem):
    """
    Represents the inventory details for a pair of

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
        super().__init__(stock_ref, price, colour)
        self.pattern = pattern
        self.length = length
        self.waist = waist

    def __str__(self):
        stock_details = super().__str__()
        template = """{0}
Pattern: {1}
Length: {2}
Waist: {3}"""
        return template.format(stock_details, self.pattern, self.length, self.waist)

    @property
    def item_name(self):  # type: ignore
        return "Pants"


x = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
y = Pants(
    stock_ref="TR12327", price=50, colour="Black", pattern="Plain", length=30, waist=25
)

print(x)
print(y)
