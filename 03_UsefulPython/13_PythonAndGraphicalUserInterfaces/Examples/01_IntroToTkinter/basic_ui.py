"""
Example 13.1 Basic UI

Introduction to building user interfaces through UI
"""

import tkinter

root = tkinter.Tk()
hello = tkinter.Label(root, text="Hello")
hello.grid(row=0, column=0)
goodbye = tkinter.Label(root, text="Goodbye")
goodbye.grid(row=1, column=0)


def been_clicked():
    print("Click")


btn = tkinter.Button(root, text="Click Me!", command=been_clicked)
btn.grid(row=2, column=0)

hello.config(text="New Hello")
ent = tkinter.Entry(root)
ent.grid(row=3, column=0)
