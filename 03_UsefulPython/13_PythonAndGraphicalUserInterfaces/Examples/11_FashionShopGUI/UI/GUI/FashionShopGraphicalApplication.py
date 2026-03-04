"""
Example 13.11c Fashion Shop Graphical Application

Provides the implementations for a graphical user interface to a fashion shop program

Routine Listings
----------------
FashionShopGraphicalApplication
    Class wrapping a storage class in a graphical-based user interface layer.
    Assumes the underlying storage class supports the `Data.StockItem` interface
    for it's underlying items

See Also
--------
Data : Package defining storage and stock item modules for a fashion shop
"""

import tkinter
import tkinter.messagebox

from Data import StockItem

from UI.GUI import StockItemEditor, StockItemSelector, StockItemStockAdjuster


class FashionShopGraphicalApplication:
    """
    Provides a graphical interface for Fashion Shop inventory management
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
        if tag_text == "":
            return set()
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

        # load the storage class
        FashionShopGraphicalApplication.__filename = filename
        try:
            self.__shop = storage_class.load(filename)
        except:  # noqa: E722
            tkinter.messagebox.showwarning(
                title="Mary's Fashion Shop",
                message="Failed to load Fashion Shop\nCreating an empty Fashion Shop",
            )
            self.__shop = storage_class()

        # configure the starting state
        self._current_item = None
        self._search_tags = ""

        # configure the user interface
        self._setup_UI()

    def _setup_UI(self):
        """
        Setup's and initialises the GUI elements

        Returns
        -------
        None
        """
        self._program_title = "Mary's Fashion Shop"
        self._root = tkinter.Tk()

        title_label = tkinter.Label(self._root, text=self._program_title)
        title_label.grid(
            sticky=tkinter.E + tkinter.W, row=0, column=0, columnspan=2, padx=5, pady=5
        )

        self._setup_editor()
        self._setup_selector()

        self._adjuster = StockItemStockAdjuster.StockItemStockAdjuster(self._root, self)
        self._adjuster.frame.grid(sticky=tkinter.E, row=4, column=1, padx=5, pady=5)
        self._adjuster.current_item = self._current_item

    def _setup_editor(self):
        """
        Setup and configure the editor component

        Returns
        -------
        None
        """

        # set up the editor
        self._editor = StockItemEditor.StockItemEditor(self._root)
        self._editor.frame.grid(sticky=tkinter.W, row=2, column=1, padx=5, pady=5)

        # set up the editor buttons

        edit_buttons_frame = tkinter.Frame(self._root)
        edit_buttons_frame.grid(sticky=tkinter.E, row=3, column=1, padx=5, pady=5)

        def create_new_stock_item():
            """
            Configure the UI to create a new `StockItem`

            Returns
            -------
            None
            """
            self._current_item = None
            self._adjuster.current_item = self._current_item
            self._editor.clear_editor()

        def save_item():
            """
            Save the details of the item currently under edit

            If there is an actively selected item, then the save overwrites it,
            otherwise a new `StockItem` is created

            Returns
            -------
            None
            """
            try:
                item = StockItem.StockItem("", StockItem.StockItem.min_price, "")
                self._editor.get_from_editor(item)
            except ValueError:
                tkinter.messagebox.showerror(
                    title=self._program_title,
                    message="Failed to create a new item\nPrice invalid",
                )
                return
            if (
                self._current_item is not None
                and self._current_item.stock_ref == item.stock_ref
            ):
                # edited an item but kept the reference identical
                self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                self.__shop.store_new_stock_item(item)
            else:
                # edited an item to different reference or new - need to check doesn't clash
                try:
                    self.__shop.store_new_stock_item(item)
                    if self._current_item is not None:
                        self.__shop.remove_old_stock_item(self._current_item.stock_ref)
                except KeyError as e:
                    tkinter.messagebox.showerror(
                        title=self._program_title, message=str(e)
                    )
                    return

            self._filter_stock_items()
            create_new_stock_item()

        create_new_button = tkinter.Button(
            edit_buttons_frame,
            text="Create new item",
            command=create_new_stock_item,
        )
        create_new_button.grid(sticky=tkinter.W, row=0, column=0, padx=5, pady=5)

        save_button = tkinter.Button(edit_buttons_frame, text="Save", command=save_item)
        save_button.grid(sticky=tkinter.E, row=0, column=1, padx=5, pady=5)

    def _setup_selector(self):
        """
        Configure and set-up the selector components, including
        searching on tags

        Returns
        -------
        None
        """
        self._selector = StockItemSelector.StockItemSelector(self._root, self)
        self._selector.frame.grid(
            sticky=tkinter.N + tkinter.S,
            row=2,
            column=0,
            rowspan=3,
            padx=5,
            pady=5,
        )

        def update_search_tags():
            """
            Updates the search tags and the corresponding list box display

            Returns
            -------
            None
            """
            self._search_tags = self._search_tags_entry.get()
            self._filter_stock_items()

        search_tags_button = tkinter.Button(
            self._root, text="Search tags:", command=update_search_tags
        )
        self._search_tags_entry = tkinter.Entry(self._root, width=40)

        search_tags_button.grid(sticky=tkinter.E, row=1, column=0, padx=5, pady=5)
        self._search_tags_entry.grid(
            sticky=tkinter.E + tkinter.W, row=1, column=1, padx=5, pady=5
        )

        update_search_tags()

    def _filter_stock_items(self):
        """
        Populates the list box with item's matching the current search tags

        Returns
        -------
        None
        """
        self._selector.populate_listbox(
            self.__shop.find_matching_with_tags(
                FashionShopGraphicalApplication.tag_set_from_text(self._search_tags)
            )
        )

    def got_selection(self, selection):
        """
        Method to be called when the program detects that the Stock Item selection has changed

        Parameters
        ----------
        selection : str
            The new selection

        Returns
        -------
        None
        """
        self._current_item = self.__shop.find_stock_item(selection)
        self._adjuster.current_item = self._current_item
        self._editor.load_into_editor(self._current_item)

    def stock_level_updated(self):
        """
        Method to be called when the program detects the the Stock Item's stock level has changed

        Returns
        -------
        None
        """
        self._editor.load_into_editor(self._current_item)  # reload the current item

    def main_menu(self):
        """
        Run the program

        Notes
        -----
        The function is called `main_menu` to maintain legacy compatibility
        with the `ShellUI` interface for an application
        """
        self._root.mainloop()

        self.__shop.save(FashionShopGraphicalApplication.__filename)
