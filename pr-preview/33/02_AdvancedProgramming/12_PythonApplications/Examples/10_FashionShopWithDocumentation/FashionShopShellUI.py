"""
Example 12.10a FashionShopShellUI

Loads and runs a shell-based Fashion Shop Inventory Management System. Only
runs if executed as the main program
"""

if __name__ == "__main__":
    from Data import FashionShop
    from UI import FashionShopApplication

    # load the UI implementation
    ui = FashionShopApplication.FashionShopApplication

    # load the data management implementation
    shop = FashionShop.FashionShop

    app = ui(filename="fashionshop.pickle", storage_class=shop)
    app.main_menu()
