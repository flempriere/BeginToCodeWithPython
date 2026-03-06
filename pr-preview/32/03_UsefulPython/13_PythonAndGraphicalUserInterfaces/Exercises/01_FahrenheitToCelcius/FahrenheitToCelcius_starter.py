"""
Exercise 13.1 Fahrenheit to Celcius

Provides a graphical interface for converting between fahrenheit and celcius

This file contains the incomplete starter code for you to complete
"""

import tkinter


class Converter:
    """
    GUI-based Fahrenheit to Celcius converter (and vice-versa)

    Call `display` to initiate the display

    Notes
    -----
    Uses `Tkinter` as the GUI framework
    """

    def display(self):
        """
        display the user interface

        Returns
        -------
        None
        """
        root = tkinter.Tk()

        cent_label = tkinter.Label(root, text="Celcius:")
        cent_label.grid(row=0, column=0, padx=5, pady=5, stick=tkinter.E)

        cent_entry = tkinter.Entry(root, width=5)
        cent_entry.grid(row=0, column=1, padx=5, pady=5)

        fah_entry = tkinter.Entry(root, width=5)
        fah_entry.grid(row=2, column=1, padx=5, pady=5)

        def fahrenheit_to_celcius():
            """
            Convert from Fahrenheit to celcius and display the result

            Returns
            -------
            None
            """
            fah_string = fah_entry.get()
            fah_float = float(fah_string)
            result = (fah_float - 32) / 1.89
            cent_entry.delete(0, tkinter.END)  # remove old text
            cent_entry.insert(0, str(result))

        def celcius_to_fahrenheit():
            """
            Convert from Celcius to Fahrenheit and display the result

            Returns
            -------
            None
            """
            cent_string = cent_entry.get()
            cent_float = float(cent_string)
            result = cent_float * 1.8 + 32
            print(result)  # to avoid unused variable errors

        fahrenheit_to_celcius_button = tkinter.Button(
            root, text="Fahrenheit to Celcius", command=fahrenheit_to_celcius
        )
        fahrenheit_to_celcius_button.grid(row=1, column=0, padx=5, pady=5)

        root.mainloop()


if __name__ == "__main__":
    app = Converter()
    app.display()
