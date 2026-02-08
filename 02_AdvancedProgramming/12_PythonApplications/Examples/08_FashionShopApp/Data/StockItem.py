# Example 12.8c Stock Item
#
# Tag only implementation of a Stock Item


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

    def __str__(self):
        if StockItem.show_instrumentation:
            print("**StockItem __str__ called")
        template = """Stock Reference: {0}
Price: {1}
Stock level: {2}
Tags: {3}"""
        return template.format(self.stock_ref, self.price, self.stock_level, self.tags)

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
        if self.__StockItem_version != 4:
            print("Stock item uses old data model, please recreate this item")

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
