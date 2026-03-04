"""
Example 13.6 Drawing Program

A simple drawing program where the user can

1. Draw
2. Change brush colour
3. Clear the canvas
"""

import tkinter


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
        canvas = tkinter.Canvas(root, width=500, height=500)
        canvas.grid(row=0, column=0)

        draw_colour = "red"

        def mouse_move(event):
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
                event.x - 5,
                event.y - 5,
                event.x + 5,
                event.y + 5,
                fill=draw_colour,
                outline=draw_colour,
            )

        canvas.bind("<B1-Motion>", mouse_move)

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
            ch = event.char.upper()
            if ch == "C":
                canvas.delete("all")
            elif ch == "R":
                draw_colour = "red"
            elif ch == "G":
                draw_colour = "green"
            elif ch == "B":
                draw_colour = "blue"

        canvas.bind("<KeyPress>", key_press)
        canvas.focus_set()

        root.mainloop()


if __name__ == "__main__":
    app = Drawing()
    app.display()
