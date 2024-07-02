import tkinter as tk

root = tk.Tk()

root.title('Aptech Python')


window_width = 800
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()  #600
screen_height = root.winfo_screenheight() #400

# find the center point
center_x = int(screen_width/2 - window_width / 2) # 150
center_y = int(screen_height/2 - window_height / 2) # 100

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# root.geometry('300x200+50-50')

root.resizable(True, True)

root.iconbitmap('C:/Users/ISU_375/Desktop/pythontutorial/tkinter/favicon.ico')

message = tk.Label(root, text="Hello World")

message.pack()

root.mainloop()