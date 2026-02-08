"""
Example 12.10f FashionShopApplication

Provides implementations for a shell-based user interface to a Fashion Shop Inventory System

Routine Listings
----------------
FashionShopApplication
    Class wrapping a storage class in a shell-based user interface layer.
    Assumes the storage class supports the `Data.StockItem` interface
    for it's underlying items

See Also
--------
Data : Package defining storage and stock item modules for a fashion shop
"""

from Data import StockItem
from UI import BTCInput


class FashionShopApplication:
    """
    Provides a text-based interface for Fashion Shop inventory management
    """

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

    def __init__(self, filename, storage_class):
        """
        Creates a new `FashionShopApplication`

        Attempts to load a `FashionShop` from the provided file. Otherwise
        an empty instance is created

        Parameters
        ----------
        filename : str
            path to a file containing pickled `FashionShop` data
        storage_class : Data Manager
            class that supports the Fashion Shop Data Management API

        See Also
        --------
        FashionShop : Main class for handling inventory management
        """
        FashionShopApplication.__filename = filename
        try:
            self.__shop = storage_class.load(filename)
        except:  # noqa: E722
            print("Failed to load Fashion Shop")
            print("Creating an empty Fashion Shop")
            self.__shop = storage_class()

    def main_menu(self):
        """
        Provides a looping main menu. Users are able to

        1. Create a new item
        2. add stock to an existing item
        3. sell stock
        4. show a stock report
        5. search by tags
        6. exit

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
5. Search by Tags
6. Exit

Enter your command: """

        while True:
            command = BTCInput.read_int_ranged(prompt, 1, 6)
            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
                self.search_by_tags()
            elif command == 6:
                self.__shop.save(self.__filename)
                print("Shop data saved")
                break
            else:
                raise ValueError(
                    "Invalid command id {0} encountered in main menu!".format(command)
                )

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

    def add_stock(self):
        """
        Add stock to a user specified item

        User is prompted to select an item by reference id, the user
        is then prompted for how much stock to add

        Returns
        -------
        None
        """
        print("Add Stock")

        item_stock_ref = BTCInput.read_text("Enter the stock reference: ")
        item = self.__shop.find_stock_item(item_stock_ref)
        if item is None:
            print("Item not found")
            return

        print("Adding")
        print(item)

        number_add = BTCInput.read_int_ranged(
            "How many to add? (0 to abandon) - {0} in current stock: ".format(
                item.stock_level
            ),
            min_value=0,
            max_value=StockItem.StockItem.max_stock_add,
        )
        if not number_add:
            print("Add Item cancelled")
            return

        item.add_stock(number_add)

    def sell_stock(self):
        """
        Sell stock of a user specified item

        User is prompted to select an item by reference id, the user
        is then prompted for how much stock to sell

        Returns
        -------
        None
        """
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

    def do_report(self):
        """
        Generates and prints a summary report of the stock inventory

        Returns
        -------
        None
        """
        print("Stock Report")
        print(self.__shop)

    def search_by_tags(self):
        print("Filter on Tags")
        search_tags = FashionShopApplication.tag_set_from_text(
            BTCInput.read_text("Enter the tags to search for (separated by commas): ")
        )
        items = self.__shop.find_matching_with_tags(search_tags)

        matching_items_report = """Matching Items:
{0}""".format("\n".join(map(str, items)))
        print(matching_items_report)
        print(matching_items_report)
