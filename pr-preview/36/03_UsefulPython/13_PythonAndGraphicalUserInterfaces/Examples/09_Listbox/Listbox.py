"""
Example 13.9 List box

Demonstrates using a tkinter Listbox
"""

import tkinter

root = tkinter.Tk()

lb = tkinter.Listbox(root)
lb.grid(row=0, column=0)

lb.insert(0, "hello")
lb.insert(1, "goodbye")
lb.insert(0, "top line")
lb.insert(tkinter.END, "bottom line")


def on_select(event):
    """
    Get's the text associated with a selected Listbox item
    """
    lb = event.widget
    index = int(lb.curselection()[0])
    print(lb.get(index))


lb.bind("<<ListboxSelect>>", on_select)

root.mainloop()
