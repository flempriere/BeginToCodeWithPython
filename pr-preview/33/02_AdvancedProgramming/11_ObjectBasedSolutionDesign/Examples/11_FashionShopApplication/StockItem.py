# Example 11.11 c Stock Item
#
# Contains the Stock Item class

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
    min_price : int | float
        minimum price of any stock item

    max_price : int | float
        maximum price of any stock item
    """

    show_instrumentation = True

    max_stock_add = 10

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

    def sell_stock(self, count):
        """
        Sell stock of an item

        Decreases the item's stock level

        Parameters
        ----------
        count : int
            amount of stock to sell

        Returns
        -------
        None

        Raises
        ------
        Exception
            raised if `count` < 1 or `count` is greater than the available stock
        """
        if StockItem.show_instrumentation:
            print("**StockItem sell_stock called")
        if count < 1:
            raise Exception("Invalid number of items to sell")
        if count > self.__stock_level:
            raise Exception("Not enough stock to sell")
        self.__stock_level = self.__stock_level - count


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
