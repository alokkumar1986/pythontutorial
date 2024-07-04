import tkinter as tk
from tkinter import Canvas, ttk

root = tk.Tk()

root.geometry("800x600+100+100")

canvas = Canvas(root, bg="yellow", width=200, height=200)

# cords = [20, 30, 40, 50]

canvas.create_line(20, 50, 80, 150)
canvas.pack()

root.mainloop()