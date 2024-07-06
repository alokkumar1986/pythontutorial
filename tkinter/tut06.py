import tkinter as tk

from tkinter import ttk, messagebox, Button

root = tk.Tk()

root.geometry('500x400+50+50') #window width and height set

root.title('Button widget') #title of the window

labelName = tk.Label(root, text="Button Widgets") #To a Label
labelName.pack()

def btnCall(event):
    print('Button is clicked')
    messagebox.showinfo('Button is clicked')

#Command Binding
# button = ttk.Button(root, text='Click Me', command=btnCall)
#button.pack(padx=50, pady=50)

#Event Binding
button1 = ttk.Button(root, text='Click Me')
button1.bind('<Enter>', btnCall)
button1.unbind('<Enter>')
button1.bind('<Leave>', btnCall)
button1.pack()


root.mainloop()

