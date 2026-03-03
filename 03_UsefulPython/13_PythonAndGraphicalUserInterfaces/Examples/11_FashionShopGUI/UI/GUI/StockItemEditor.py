"""
Example 13.11d Stock Item Editor

Implements a graphical editor object for editing `StockItem` objects
"""

import tkinter

from Data import StockItem


class StockItemEditor:
    """
    Graphical Editor for a StockItem

    Notes
    -----
    Implemented as a `Tkinter` Frame
    """

    def __init__(self, root):
        """
        Create a new `StockItemEditor`

        Parameters
        ----------
        root
            Tkinter root frame for the editor
        """
        self.frame = tkinter.Frame(root)

        stock_ref_label = tkinter.Label(self.frame, text="Stock ref:")
        stock_ref_label.grid(sticky=tkinter.E, row=0, column=0, padx=5, pady=5)
        self._stock_ref_entry = tkinter.Entry(self.frame, width=30)
        self._stock_ref_entry.grid(sticky=tkinter.W, row=0, column=1, padx=5, pady=5)

        price_label = tkinter.Label(self.frame, text="Price:")
        price_label.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)
        self._price_entry = tkinter.Entry(self.frame, width=30)
        self._price_entry.grid(sticky=tkinter.W, row=1, column=1, padx=5, pady=5)

        self._stock_level_label = tkinter.Label(self.frame, text="Stock level: 0")
        self._stock_level_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        tags_label = tkinter.Label(self.frame, text="Tags:")
        tags_label.grid(sticky=tkinter.E + tkinter.N, row=3, column=0, padx=5, pady=5)
        self._tags_text = tkinter.Text(self.frame, width=50, height=5)
        self._tags_text.grid(row=3, column=1, padx=5, pady=5)

    def clear_editor(self):
        """
        Clears the editor window

        Returns
        -------
        None
        """
        self._stock_ref_entry.delete(0, tkinter.END)
        self._price_entry.delete(0, tkinter.END)
        self._tags_text.delete("0.0", tkinter.END)
        self._stock_level_label.config(text="Stock level: 0")

    def load_into_editor(self, item):
        """
        Load a `StockItem` into the edit display

        Parameters
        ----------
        item : StockItem
            stock reference to be loaded
        """
        self.clear_editor()
        self._stock_ref_entry.insert(0, item.stock_ref)
        self._price_entry.insert(0, str(item.price))
        self._stock_level_label.config(text="Stock level {0}".format(item.stock_level))
        self._tags_text.insert("0.0", item.text_tags)

    def get_from_editor(self, item):
        """
        Get an updated `StockItem` from the editor

        Parameters
        ----------
        item : StockItem
            stock reference to update

        Raises
        ------
        ValueError
            raised if the price entry cannot be converted to a number
        """
        item.set_price(self._price_entry.get())
        item.stock_ref = self._stock_ref_entry.get()
        item.text_tags = self._tags_text.get("1.0", tkinter.END)


if __name__ == "__main__":
    item = StockItem.StockItem(
        "D001",
        price=120,
        tags="dress,colour:red,loc:shop window,pattern:swirly,size:12,evening,long",
    )

    item.add_stock(5)

    root = tkinter.Tk()
    stock_frame = StockItemEditor(root)
    stock_frame.frame.grid(row=0, column=0)
    stock_frame.load_into_editor(item)

    def save_edit():
        stock_frame.get_from_editor(item)
        stock_frame.clear_editor()

    save_button = tkinter.Button(root, text="Save", command=save_edit)
    save_button.grid(row=1, column=0)

    root.mainloop()
