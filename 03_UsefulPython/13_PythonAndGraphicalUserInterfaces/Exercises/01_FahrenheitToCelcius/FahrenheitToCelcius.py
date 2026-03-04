"""
Exercise 13.1 Fahrenheit to celsius

Provides a graphical interface for converting between fahrenheit and celsius
"""

import tkinter
import tkinter.messagebox


class Converter:
    """
    GUI-based Fahrenheit to celsius converter (and vice-versa)

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

        cent_label = tkinter.Label(root, text="Celsius:")
        cent_label.grid(row=0, column=0, padx=5, pady=5, stick=tkinter.E)

        fah_label = tkinter.Label(root, text="Fahrenheit:")
        fah_label.grid(row=2, column=0, padx=5, pady=5, stick=tkinter.E)

        cent_entry = tkinter.Entry(root, width=5)
        cent_entry.grid(row=0, column=1, padx=5, pady=5, stick=tkinter.E + tkinter.W)

        fah_entry = tkinter.Entry(root, width=5)
        fah_entry.grid(row=2, column=1, padx=5, pady=5, stick=tkinter.E + tkinter.W)

        def fahrenheit_to_celsius():
            """
            Convert from Fahrenheit to celsius and display the result

            Returns
            -------
            None
            """
            try:
                fah_string = fah_entry.get()
                fah_entry.config(background="white", foreground="black")
                fah_float = float(fah_string)
            except ValueError:
                tkinter.messagebox.showerror(
                    title="Temperature Converter", message="Fahrenheit must be a number"
                )
                fah_entry.config(background="red", foreground="blue")
                return

            result = (fah_float - 32) / 1.8
            cent_entry.delete(0, tkinter.END)  # remove old text
            cent_entry.insert(0, "{0:.2f}".format(result))
            cent_entry.config(background="white", foreground="black")

        def celsius_to_fahrenheit():
            """
            Convert from celsius to Fahrenheit and display the result

            Returns
            -------
            None
            """
            try:
                cent_string = cent_entry.get()
                cent_entry.config(background="white", foreground="black")
                cent_float = float(cent_string)
            except ValueError:
                tkinter.messagebox.showerror(
                    title="Temperature Converter", message="Celsius must be a number"
                )
                cent_entry.config(background="red", foreground="blue")
                return
            result = cent_float * 1.8 + 32
            fah_entry.delete(0, tkinter.END)
            fah_entry.insert(0, "{0:.2f}".format(result))
            fah_entry.config(background="white", foreground="black")

        fahrenheit_to_celsius_button = tkinter.Button(
            root, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius
        )
        fahrenheit_to_celsius_button.grid(row=1, column=0, padx=5, pady=5)

        celsius_to_fahrenheit_button = tkinter.Button(
            root, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit
        )
        celsius_to_fahrenheit_button.grid(row=1, column=1, padx=5, pady=5)

        root.mainloop()


if __name__ == "__main__":
    app = Converter()
    app.display()
