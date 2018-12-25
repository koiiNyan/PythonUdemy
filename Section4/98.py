# Program that asks the user to submit a text through a GUI.

from tkinter import *

# Making a new window
window = Tk()

file = open("user_gui.txt", "a")

def add():
    # Adding new line to file
    file.write(user_input.get() + "\n")
    # Deleting text from the text field
    entry.delete(0, END)

def save():
    # Closing and opening file for saving
    global file
    file.close()
    file = open("user_gui.txt", "a")

def close():
    # Closing window and file for saving
    file.close()
    window.destroy()

# User input
user_input = StringVar()
entry = Entry(window, textvariable=user_input)
entry.grid(row=0, column=0)

# Buttons
button_add = Button(window, text="Add new line", command=add)
button_add.grid(row=0, column=1)

button_save = Button(window, text="Save changes", command=save)
button_save.grid(row=0, column=2)

button_close = Button(window, text="Save and Close", command=close)
button_close.grid(row=0,column=3)

window.mainloop()
