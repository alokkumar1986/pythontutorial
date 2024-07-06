import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.Frame(root, width=100, height=300, borderwidth=12, padding=[50, 100, 100, 50])
frame.pack()


label1 = ttk.Label(frame, text='Frame with a label')

label1.pack()



root.mainloop()