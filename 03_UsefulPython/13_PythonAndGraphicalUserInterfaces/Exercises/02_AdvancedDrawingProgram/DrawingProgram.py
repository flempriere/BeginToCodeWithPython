"""
Exercise 13.2 Advanced Drawing Program

Improves the drawing program by adding support for an oval brush, the ability
to change the brush size, access a help menu and erase.

1. Draw
2. Change brush colour
3. Clear the canvas
4. Erase over the canvas
5. Change the brush size
6.
"""

import tkinter
import tkinter.messagebox


class Drawing:
    """
    GUI element for a drawing program

    Notes
    -----
    Uses `tkinter` for the GUI framework
    """

    def display(self):
        """
        Display the Drawing Program

        Returns
        -------
        None
        """
        root = tkinter.Tk()
        canvas = tkinter.Canvas(root, width=500, height=500, bg="white")
        canvas.grid(row=0, column=0, sticky=tkinter.E + tkinter.W, columnspan=2)

        draw_colour = "red"
        size = 5

        brush_label = tkinter.Label(root, text="Brush: square")
        brush_label.grid(row=1, column=0, padx=5, pady=5, sticky=tkinter.W)

        colour_label = tkinter.Label(root, text="Colour: {0}".format(draw_colour))
        colour_label.grid(row=2, column=0, padx=5, pady=5, sticky=tkinter.W)

        size_label = tkinter.Label(root, text="Size: {0}".format(size))
        size_label.grid(row=1, column=1, padx=5, pady=5, sticky=tkinter.E)

        help_label = tkinter.Label(root, text="Press H for help")
        help_label.grid(row=2, column=1, padx=5, pady=5, sticky=tkinter.E)

        def mouse_move_square(event):
            """
            Draw a 10 by 10 pixel rectangle centred on the mouse

            Parameters
            ----------
            event
                the triggering event

            Returns
            -------
            None
            """
            canvas.create_rectangle(
                event.x - size,
                event.y - size,
                event.x + size,
                event.y + size,
                fill=draw_colour,
                outline=draw_colour,
            )

        def mouse_move_oval(event):
            """
            Draw an oval inscribed in an 10 x 10 pixel rectangle centred on
            the mouse

            Parameters
            ----------
            event
                the triggering event
            """
            canvas.create_oval(
                event.x - size,
                event.y - size,
                event.x + size,
                event.y + size,
                fill=draw_colour,
                outline=draw_colour,
            )

        def erase(event) -> None:
            """
            Erase the canvas

            Parameters
            ----------
            event
                triggering event

            Notes
            -----
            Erase is implemented by drawing a white rectangle centred on the mouse
            """
            canvas.create_rectangle(
                event.x - size,
                event.y - size,
                event.x + size,
                event.y + size,
                fill="white",
                outline="white",
            )

        canvas.bind("<B1-Motion>", mouse_move_square)
        canvas.bind("<B3-Motion>", erase)

        def key_press(event):
            """
            Change the drawing program state in response to a key press

            Parameters
            ----------
            event
                key press that triggered the function

            Returns
            -------
            None
            """
            nonlocal draw_colour
            nonlocal size
            ch = event.char.upper()
            if ch == "C":
                canvas.delete("all")
            elif ch == "R":
                draw_colour = "red"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "G":
                draw_colour = "green"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "B":
                draw_colour = "blue"
                colour_label.config(text="Colour: {0}".format(draw_colour))
            elif ch == "S":
                canvas.bind("<B1-Motion>", mouse_move_square)
                brush_label.config(text="Brush: square")
            elif ch == "O":
                canvas.bind("<B1-Motion>", mouse_move_oval)
                brush_label.config(text="Brush: oval")
            elif ch == "+":
                size = min(size + 5, 50)
                size_label.config(text="Size: {0}".format(size))
            elif ch == "-":
                size = max(size - 5, 5)
                size_label.config(text="Size: {0}".format(size))

            elif ch == "H":
                tkinter.messagebox.showinfo(
                    title="Simple Canvas",
                    message="""Controls:
C - clear canvas
R - change colour to red
B - change colour to blue
G - change colour to green
S - change brush to square brush
O - change brush to oval brush
+ - increase brush size
- - decrease brush size

Right click to erase""",
                )

        canvas.bind("<KeyPress>", key_press)
        canvas.focus_set()

        root.mainloop()


if __name__ == "__main__":
    app = Drawing()
    app.display()
