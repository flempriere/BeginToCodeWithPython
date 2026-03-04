"""
Example 13.5 Canvas

A basic drawing canvas
"""

import tkinter

root = tkinter.Tk()

c = tkinter.Canvas(root, width=500, height=500)
c.grid(row=0, column=0)


def mouse_move_draw(event):
    """
    Draw a rectangle at the location of an event

    Parameters
    ----------
    event
        event that triggered the function

    Returns
    -------
    None
    """
    c.create_rectangle(
        event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="red", outline="red"
    )


c.bind("<B1-Motion>", mouse_move_draw)

root.mainloop()
