import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# root.geometry("300x100+50+50")

frame = ttk.Frame(root, width=400, height=300, borderwidth=12, padding=100)
# frame.pack()

frame.columnconfigure(index=0, weight=1)
frame.rowconfigure(index=0, weight=2)

userlabel = ttk.Label(root, text='User Name')
userlabel.grid(column=0, row=0)
# userlabel.pack()

userentry = ttk.Entry()
userentry.grid(column=1, row=0)
# userentry.pack()

passwordlabel = ttk.Label(root, text='Password')
passwordlabel.grid(column=0, row=1)
# userlabel.pack()

passwordentry = ttk.Entry()
passwordentry.grid(column=1, row=1)
# userentry.pack()


loginbtn = ttk.Button(root, text='Sign In')
loginbtn.grid(column=1, row=2)


root.mainloop()