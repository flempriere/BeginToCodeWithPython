# Example 11.11 b FashionShop Application
#
# Implements the FashionShopApplication class which provides a UI layer to the
# FashionShop and StockItem system

import BTCInput
import FashionShop
import StockItem


class FashionShopApplication:
    """
    Provides a text-based interface for Fashion Shop inventory management
    """

    def __init__(self, filename):
        """
        Creates a new `FashionShopApplication`

        Attempts to load a `FashionShop` from the provided file. Otherwise
        an empty instance is created

        Parameters
        ----------
        filename : str
            path to a file containing pickled `FashionShop` data

        See Also
        --------
        FashionShop : Main class for handling inventory management
        """
        FashionShopApplication.__filename = filename
        try:
            self.__shop = FashionShop.FashionShop.load(filename)
        except:  # noqa: E722
            print("Failed to load Fashion Shop")
            print("Creating an empty Fashion Shop")
            self.__shop = FashionShop.FashionShop()

    def main_menu(self):
        """
        Provides a looping main menu. Users are able to

        1. Create a new item
        2. add stock to an existing item
        3. sell stock
        4. show a stock report
        5. exit

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
5. Exit

Enter your command: """

        while True:
            command = BTCInput.read_int_ranged(prompt, 1, 5)
            if command == 1:
                self.create_new_stock_item()
            elif command == 2:
                self.add_stock()
            elif command == 3:
                self.sell_stock()
            elif command == 4:
                self.do_report()
            elif command == 5:
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

        Prompts the user for the type of item to create and
        the necessary descriptors of the item. The item is
        then added to the system

        Returns
        -------
        None

        Raises
        ------
        ValueError
            Raised if an invalid stock item type id is encountered.
            Should not arise in production, please report if found.
        """

        menu = """
        Create a new stock item

1. Dress
2. Pants
3. Hat
4. Blouse
5. Jeans

Enter item to add: """

        first_menu_option = 1
        last_menu_option = 5

        min_stock_item_size = 0
        max_stock_item_size = 99

        item = BTCInput.read_int_ranged(menu, first_menu_option, last_menu_option)

        if item < first_menu_option or item > last_menu_option:
            raise ValueError(
                "Unexpected value {0} found in menu. Please raise a bug report".format(
                    item
                )
            )
        # now we have a valid item so get the common attributes
        stock_ref = BTCInput.read_text("Enter Stock reference: ")
        price = BTCInput.read_float_ranged(
            "Enter price: ",
            min_value=StockItem.StockItem.min_price,
            max_value=StockItem.StockItem.max_price,
        )
        colour = BTCInput.read_text("Enter colour: ")
        location = BTCInput.read_text("Enter location: ")

        if item == 1:
            print("Creating a Dress")
            pattern = BTCInput.read_text("Enter pattern: ")
            size = BTCInput.read_int_ranged(
                "Enter size: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            stock_item = StockItem.Dress(
                stock_ref, price, colour, pattern, size, location
            )

        elif item == 2:
            print("Creating a pair of Pants")
            pattern = BTCInput.read_text("Enter pattern: ")
            length = BTCInput.read_int_ranged(
                "Enter length: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            waist = BTCInput.read_int_ranged(
                "Enter waist size: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            stock_item = StockItem.Pants(
                stock_ref, price, colour, pattern, length, waist, location
            )

        elif item == 3:
            print("Creating a Hat")
            size = BTCInput.read_int_ranged(
                "Enter size: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            stock_item = StockItem.Hat(stock_ref, price, colour, size, location)

        elif item == 4:
            print("Creating a Blouse")
            pattern = BTCInput.read_text("Enter pattern: ")
            style = BTCInput.read_text("Enter style: ")
            size = BTCInput.read_int_ranged(
                "Enter size: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            stock_item = StockItem.Blouse(
                stock_ref, price, colour, pattern, style, size, location
            )

        elif item == 5:
            print("Creating a pair of Jeans")
            pattern = BTCInput.read_text("Enter pattern: ")
            style = BTCInput.read_text("Enter style: ")
            length = BTCInput.read_int_ranged(
                "Enter length: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            waist = BTCInput.read_int_ranged(
                "Enter waist size: ",
                min_value=min_stock_item_size,
                max_value=max_stock_item_size,
            )
            stock_item = StockItem.Jeans(
                stock_ref, price, colour, pattern, length, waist, style, location
            )
        else:
            raise ValueError(
                "Invalid stock item type id {0} encountered, please report".format(item)
            )
        self.__shop.store_new_stock_item(stock_item)

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


ui = FashionShopApplication("fashionshop.pickle")
ui.main_menu()
