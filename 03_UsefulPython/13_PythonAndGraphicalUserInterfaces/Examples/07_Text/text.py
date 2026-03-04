"""
Example 13.7 Text Widget

Demonstrates the tkinter text widget
"""

import tkinter

root = tkinter.Tk()

t = tkinter.Text(width=80, height=10)
t.grid(row=0, column=0)

root.mainloop()
