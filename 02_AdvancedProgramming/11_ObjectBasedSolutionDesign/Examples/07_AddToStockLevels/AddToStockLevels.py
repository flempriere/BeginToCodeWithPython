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


d = Dress(
    "D0001", price=100, colour="Red", pattern="Swirly", size=12, location="Shop Window"
)
d.add_stock(5)
print(d)
