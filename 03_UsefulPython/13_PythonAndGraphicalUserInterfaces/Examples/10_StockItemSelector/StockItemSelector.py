"""
Example 13.10 Stock Item Selector

Implements a Graphical Element for selecting a stock item from a list
"""

import tkinter

import StockItem


class StockItemSelector:
    """
    Widget providing a list selection for StockItem objects

    Parameters
    -----------

    receiver
        A receiver object that is informed of any change in selection.
        The receiver must support a method, `got_selection(str)`
    frame : tkinter.Frame
        The tkinter `Frame` this component is contained in
    listbox : tkinter.Listbox
        list box to populate with stock item references

    """

    def __init__(self, root, receiver):
        """
        Create a new `StockItemSelector`

        Parameters
        ----------
        root
            The parent frame or window to attach this component to
        receiver
            Object to send a message to when the selection changes.
            Must support a method `got_selection(str)`

        Raises
        ------
        AttributeError
            raised if `receiver` does not support `got_selection`
        """
        if not hasattr(receiver, "got_selection"):
            raise AttributeError(
                "Supplied receiver does not support got_selection(str)"
            )
        self.receiver = receiver
        self.frame = tkinter.Frame(root)
        self.listbox = tkinter.Listbox(self.frame)
        self.listbox.grid(row=0, column=0)

        def on_select(event):
            """
            Find the selected text in the Listbox and send it to the
            receiving object

            Bound to the `ListboxSelect` event

            Parameters
            ----------
            event
                event that triggered the function

            Returns
            -------
            None
            """
            lb = event.widget
            index = int(lb.curselection()[0])
            receiver.got_selection(lb.get(index))

        self.listbox.bind("<<ListboxSelect>>", on_select)

    def populate_listbox(self, items):
        """
        Populate the Listbox with a list of StockItem's

        Parameters
        ----------
        items : list[StockItem]
            a list of stock items to add to the selection

        Returns
        -------
        None
        """
        self.listbox.delete(0, tkinter.END)
        for item in items:
            self.listbox.insert(tkinter.END, item.stock_ref)


if __name__ == "__main__":

    class MessageReceiver:
        def got_selection(self, stock_ref):
            print("stock item selected:", stock_ref)

    stock_list = []

    for i in range(1, 100):
        stock_ref = "D{0}".format(i)
        item = StockItem.StockItem(
            stock_ref,
            120 + (i * 10),
            "dress, colour:red, loc:shop window,pattern:swirly, size:12, evening, long",
        )
        stock_list.append(item)

    receiver = MessageReceiver()
    root = tkinter.Tk()
    stock_selector = StockItemSelector(root, receiver)
    stock_selector.populate_listbox(stock_list)
    stock_selector.frame.grid(row=0, column=0)
    root.mainloop()
