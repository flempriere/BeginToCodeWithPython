"""
Example 13.11i FashionShopGraphicalUI

Loads and runs a graphical-based Fashion Shop Inventory Management System. Only
runs if executed as the main program
"""

if __name__ == "__main__":
    from Data import FashionShop
    from UI.GUI import FashionShopGraphicalApplication

    # load the UI implementation
    ui = FashionShopGraphicalApplication.FashionShopGraphicalApplication

    # load the data management implementation
    shop = FashionShop.FashionShop

    app = ui(filename="fashionshop.pickle", storage_class=shop)
    app.main_menu()
