# Example 11.1 Fashion Items as Seperate Classes
#
# Mocks out the class-based implementation of the fashion items, treating
# each different item type as it's own standalone class


class Dress:
    """
    Represents the inventory details for a Dress
    """

    def __init__(self, stock_ref, price, colour, pattern, size):
        """
        Creates a Dress instance

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
        """
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.colour = colour
        self.pattern = pattern
        self.size = size

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        return self.__stock_level


class Pants:
    """
    Represents the inventory details for a pair of Pants
    """

    def __init__(self, stock_ref, price, colour, pattern, length, waist):
        """
        Creates a Pants instance

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
        """
        self.stock_ref = stock_ref
        self.__price = price
        self.__stock_level = 0
        self.colour = colour
        self.pattern = pattern
        self.length = length
        self.waist = waist

    @property
    def price(self):
        """
        price : int | float
            dress price
        """
        return self.__price

    @property
    def stock_level(self):
        """
        stock_level : int
            amount of stock in inventory
        """
        return self.__stock_level


x = Dress(stock_ref="D001", price=100, colour="Red", pattern="Swirly", size=12)
y = Pants(
    stock_ref="TR12327", price=50, colour="Black", pattern="Plain", length=30, waist=25
)

print(x.price)
print(y.stock_level)
