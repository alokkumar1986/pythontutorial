import tkinter as tk

from tkinter import ttk, messagebox

root = tk.Tk()

root.geometry('500x400+50+50') #window width and height set

root.title('Button widget') #title of the window

labelName = tk.Label(root, text="Button Widgets") #To a Label
labelName.pack()

def btnCall():
    print('Button is clicked')
    messagebox.showinfo('Button is clicked')

button = ttk.Button(root, text='Click Me', command=btnCall)
button.pack()

root.mainloop()

