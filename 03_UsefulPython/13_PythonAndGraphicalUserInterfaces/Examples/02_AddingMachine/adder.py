"""
Example 13.2 Adding Machine

A demonstrative graphical program for adding two numbers
"""

import tkinter


class Adder:
    """
    GUI-based adding machine

    Call `display` to initiate the display

    Notes
    -----
    Uses `Tkinter` as the GUI framework
    """

    def display(self):
        """
        Display the user interface

        Returns
        -------
        None
        """

        def do_add():
            """
            get and add the two numbers

            Returns
            -------
            int | float
                the result of adding both numbers
            """

            first_number = float(first_number_entry.get())
            second_number = float(second_number_entry.get())

            result = first_number + second_number
            result_label.config(text=str(result))

        root = tkinter.Tk()

        first_number_label = tkinter.Label(root, text="First Number")
        first_number_label.grid(sticky=tkinter.E, padx=5, pady=5, row=0, column=0)

        second_number_label = tkinter.Label(root, text="Second Number")
        second_number_label.grid(sticky=tkinter.E, padx=5, pady=5, row=1, column=0)

        first_number_entry = tkinter.Entry(root, width=10)
        first_number_entry.grid(padx=5, pady=5, row=0, column=1)

        second_number_entry = tkinter.Entry(root, width=10)
        second_number_entry.grid(padx=5, pady=5, row=1, column=1)

        add_button = tkinter.Button(root, text="Add numbers", command=do_add)
        add_button.grid(
            sticky=tkinter.E + tkinter.W, padx=5, pady=5, row=2, column=0, columnspan=2
        )

        result_label = tkinter.Label(root, text="Result")
        result_label.grid(
            sticky=tkinter.E + tkinter.W, padx=5, pady=5, row=3, column=0, columnspan=2
        )

        root.mainloop()


if __name__ == "__main__":
    app = Adder()
    app.display()
