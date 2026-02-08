# Example 12.8a Modular Fashion Shop
#
# Provides the entry point and coordinating behaviour for a modularised
# implementation of the Fashion Shop Application


from Data import FashionShop
from UI import FashionShopApplication

# load the UI implementation
ui = FashionShopApplication.FashionShopApplication

# load the data management implementation
shop = FashionShop.FashionShop

app = ui(filename="fashionshop.pickle", storage_class=shop)
app.main_menu()
