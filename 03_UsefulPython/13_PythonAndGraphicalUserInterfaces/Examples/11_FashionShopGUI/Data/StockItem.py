"""
Example 13.11b Stock Item

Provides implementations for representing an individual stock item

Routine Listings
----------------
StockItem
    class representing an in-memory stock item with a reference, stock level, price and descriptive tags
"""


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

    show_instrumentation = False

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
        tags : str
            tags provided as a comma-separated string of values
        """
        if StockItem.show_instrumentation:
            print("**StockItem __init__ called")
        self.stock_ref = stock_ref
        self.__price = price
        self.text_tags = tags
        self.__stock_level = 0
        self.__StockItem_version = 5

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**StockItem __str__ called")
        template = """Stock Reference: {0}
Price: {1}
Stock level: {2}
Tags: {3}"""
        return template.format(
            self.stock_ref, self.price, self.stock_level, self.text_tags
        )

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

    @property
    def text_tags(self):
        """
        text_tags : str
            item tags as a comma separated string
        """
        tag_list = list(self.tags)
        tag_list.sort()
        return ",".join(tag_list)

    @text_tags.setter
    def text_tags(self, tag_string):
        self.tags = set(map(str.strip, str.split(str.lower(tag_string), sep=",")))

    def check_version(self):
        """
        Checks the version of a `StockItem` instance and upgrades it if required

        Returns
        -------
        None
        """
        if StockItem.show_instrumentation:
            print("**StockItem check_version called")
        if self.__StockItem_version < 4:
            print("Stock item uses old data model, please recreate this item")
        if self.__StockItem_version == 4:
            pass  # tags will still be a set of strings

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
        ValueError
            raised if `count` < 0 or `count` > `StockItem.max_stock_add`

        See Also
        --------
        StockItem.max_stock_add : maximum amount of stock that can be added to a `StockItem`
        """
        if StockItem.show_instrumentation:
            print("**StockItem add_stock called")
        if count <= 0 or count > StockItem.max_stock_add:
            raise ValueError("Invalid add amount")
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
        ValueError
            raised if `count` < 1 or `count` is greater than the available stock
        """
        if StockItem.show_instrumentation:
            print("**StockItem sell_stock called")
        if count < 1:
            raise ValueError("Invalid number of items to sell")
        if count > self.__stock_level:
            raise ValueError("Not enough stock to sell")
        self.__stock_level = self.__stock_level - count

    def set_price(self, new_price):
        """
        Set a new price on the stock item

        Parameters
        ----------
        new_price : int | float
            new price of the item

        Raises
        ------
        ValueError
            Raised if the price is outside of the valid range
        ValueError
            Raised if the price is not a number

        """
        if StockItem.show_instrumentation:
            print("** StockItem set_price called")
        try:
            new_price = int(new_price)
        except ValueError:
            new_price = float(new_price)
        if new_price < StockItem.min_price or new_price > StockItem.max_price:
            raise ValueError("Price out of range")
        self.__price = new_price
