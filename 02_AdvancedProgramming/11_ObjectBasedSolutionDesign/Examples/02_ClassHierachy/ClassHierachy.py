# Example 11.2 Fashion Items using a Class Hierachy
#
# Mocks out the Fashion stock items classes using an inheritance hierachy

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
        Creates a StockItem instance

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
        Creates a Dress instance

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


class Pants(StockItem):
    """
    Represents the inventory details for a pair of Pants

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
    `StockItem` : Parent Class
    """

    def __init__(self, stock_ref, price, colour, pattern, length, waist):
        """
        Creates a Pants instance

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


x = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
y = Pants(
    stock_ref="TR12327", price=50, colour="Black", pattern="Plain", length=30, waist=25
)

print(x.price)
print(y.stock_level)
