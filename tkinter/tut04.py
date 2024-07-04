import tkinter as tk

from tkinter import Checkbutton, ttk

top = tk.Tk()

top.geometry("500x500+200+200")

ckeckval1 = Checkbutton(top, text="Male", onvalue=1, offvalue=0)
ckeckval2 = Checkbutton(top, text="Female", onvalue=1, offvalue=0)
ckeckval3 = Checkbutton(top, text="Others", onvalue=1, offvalue=0)

ckeckval1.pack()
ckeckval2.pack()
ckeckval3.pack()


top.mainloop()