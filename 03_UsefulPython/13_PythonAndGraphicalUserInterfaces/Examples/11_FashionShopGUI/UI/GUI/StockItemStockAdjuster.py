"""
Example 13.11f Stock Item Stock Adjuster

A graphical component for adjusting the Stock level of a Stock Item
"""

import tkinter
import tkinter.messagebox

from Data import StockItem


class StockItemStockAdjuster:
    """
    Graphical Component for adjusting a Stock Item

    Parameters
    ----------

    receiver
        Object to send a message to when the stock changes. Must
        support a method `stock_level_updated()`
    frame: tkinter.Frame
        the tkinter `Frame` this component is contained within

    Notes
    -----
    Implemented as a `tkinter` frame
    """

    def __init__(self, root, receiver):
        """
        Create a new `StockItemAdjuster`

        Parameters
        ----------
        root
            The parent frame or window to attach this component to
        receiver
            Object to send a message to when the stock changes. Must
            support a method `stock_level_updated()`

        Raises
        ------
        AttributeError
            raised if `receiver` does not support `stock_level_updated()`
        """
        if not hasattr(receiver, "stock_level_updated"):
            raise AttributeError(
                "Supplied receiver does not support stock_level_updated"
            )
        self.receiver = receiver
        self._current_item = None
        self.frame = tkinter.Frame(root)

        self._add_stock_entry = tkinter.Entry(self.frame, width=10)
        self._remove_stock_entry = tkinter.Entry(self.frame, width=10)

        def add_stock():
            """
            binding function for adding stock when the button is pressed

            Returns
            -------
            None
            """
            # Entry box must not be empty
            try:
                if self._current_item is None:
                    raise ValueError("No stock item currently selected")
                self._current_item.add_stock(int(self._add_stock_entry.get()))
                self.receiver.stock_level_updated()
                self._add_stock_entry.delete(0, tkinter.END)
            except ValueError as e:
                tkinter.messagebox.showerror(
                    title="Failed to Add Stock", message=str(e)
                )

        def remove_stock():
            """
            binding function for removing stock when the button is pressed

            Returns
            -------
            None

            Raises
            ------
            ValueError
                raised if no stock item is selected
            ValueError
                raised if the value provided stock amount is not a positive
                whole number, or larger than the maximum allowed to sell
            """
            # Entry box must not be empty
            try:
                if self._current_item is None:
                    raise ValueError(
                        "Failed to remove stock:\nno stock item currently selected"
                    )
                self._current_item.sell_stock(int(self._remove_stock_entry.get()))
                self.receiver.stock_level_updated()
                self._remove_stock_entry.delete(0, tkinter.END)
            except ValueError as e:
                tkinter.messagebox.showerror(
                    title="Failed to Remove Stock", message=str(e)
                )

        add_stock_button = tkinter.Button(
            self.frame, text="Add stock:", command=add_stock
        )
        remove_stock_button = tkinter.Button(
            self.frame, text="Remove stock:", command=remove_stock
        )

        add_stock_button.grid(row=0, column=0, sticky=tkinter.E, padx=5, pady=5)
        self._add_stock_entry.grid(row=0, column=1, sticky=tkinter.E, padx=5, pady=5)
        remove_stock_button.grid(row=1, column=0, sticky=tkinter.E, padx=5, pady=5)
        self._remove_stock_entry.grid(row=1, column=1, sticky=tkinter.E, padx=5, pady=5)

    @property
    def current_item(self):
        """
        current_item : StockItem | None
            The currently active `StockItem`

        Raises
        ------
        TypeError
            raised if `item` is not a `StockItem`
        """
        return self._current_item

    @current_item.setter
    def current_item(self, item):
        if not isinstance(item, StockItem.StockItem) and item is not None:
            raise TypeError("item must be of type StockItem or None")
        self._current_item = item
