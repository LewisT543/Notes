                                #### EVENT HANDLING ####

# Events are the fuel which propell an applications movements. All events come to THE EVENT MANAGER, 
# which is responsible for dispatching them to all the application components.       

# showinfo(), a replacement for print().
# messagebox.showinfo(title, info)
# 2 arguments, both strings.
    # The first string will be used by the function to title the message box which will appear on the screen; 
    # you can use an empty string, and the box will be untitled then;
    # The second string is a message to display inside the box; the string can be of any length                        

# Example:

import tkinter
from tkinter import messagebox

'''
def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tkinter.Tk()
button_1 = tkinter.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tkinter.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()

import tkinter as tk
from tkinter import messagebox
'''

# Example 2 - Clickable and non-clickable:

import tkinter as tk
from tkinter import messagebox

def click():
    tk.messagebox.showinfo("Click!","I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click) # Clickable widget allows binding of callback to 'command'
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack();

window.mainloop()

# Some of the widgets (especially those that are not clickable by nature) 
# have neither a command property nor a constructor parameter of that name.

# Fortunately we can use bind() to bind a callback to any events it may receive.

    #   widget.bind(event, callback)
    # event being the 'input' event (eg. mouse click)
    # callback being the function to be called

# Q: What is an event from the event controller’s point of view?
# A: It’s an object carrying some useful info about what actually happens when the event has been 
# induced (by the user or by another factor).

# Q: How are the events identified?
# A: By unique names – each event has its own name and the name is just a unified string.