# Example 11.13a Fashion Shop
#
# Contains the fashion shop class


import pickle


class FashionShop:
    """
    Represents the inventory management system of a Fashion

    Class Attributes
    ----------------
    show_instrumentation : bool
        indicates if instrumentation should be printed
    """

    show_instrumentation = True

    def __init__(self):
        """
        Create a new `FashionShop` instance
        """
        if FashionShop.show_instrumentation:
            print("**FashionShop __init__ called")
        self.__stock_dictionary = {}

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
        if FashionShop.show_instrumentation:
            print("**FashionShop save called")
        with open(filename, "wb") as output_file:
            pickle.dump(self, output_file)

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
        if FashionShop.show_instrumentation:
            print("**FashionShop load called")
        with open(filename, "rb") as input_file:
            shop = pickle.load(input_file)
        return shop

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
        if FashionShop.show_instrumentation:
            print("**FashionShop store new stock item called")
        if item.stock_ref in self.__stock_dictionary:
            raise KeyError("This stock reference is already used")
        self.__stock_dictionary[item.stock_ref] = item

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
        if FashionShop.show_instrumentation:
            print("**FashionShop find stock item called")
        return self.__stock_dictionary.get(stock_ref)

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

    def __str__(self):
        stock_list = "\n".join(map(str, self.__stock_dictionary.values()))
        template = """
{0}
"""
        return template.format(stock_list)
