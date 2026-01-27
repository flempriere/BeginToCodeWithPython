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
