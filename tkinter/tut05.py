import tkinter as tk
from tkinter import Entry, Label, ttk

top = tk.Tk()

# top.geometry("500x600+30+30")

l1 = Label(top, text="User name")
l1.pack(side="left")

e1 = Entry(top, bd=2)
e1.pack(side="right")

top.mainloop()