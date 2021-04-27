                                #### EVENT CLASSES AND OBJECTS ####

# An event object is an instantiation of the Event class.
# Actually, it’s a container filled with some more or less helpful data.
# The data describe all the circumstances which are accompanied within the event, and it is dispatched to a number 
# of the object’s properties.
# Note: 
    # Not all properties have meaning for every event. If the event is related to some of the mouse actions, the object’s parts 
    # referring to the keyboard remain uninitialized, and vice versa.  

'''
Property name	Property role
widget	        The widget’s object (not the widget’s name!) to which the event is addressed

<x>             The mouse cursor’s coordinates at the moment of the event’s occurrence 
<y>             (both coordinates are counted relative to the target widget)
            
<x_root>        As above, but relative to the screen
<y_root>	    

<char>	        The pressed key character code (only for keyboard events)
<keysym>	    The pressed key symbol (only for keyboard events)
                The full list of all recognized key symbols is presented here: https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm

<keycode>   	The pressed key numerical code (only for keyboard events)
                Don’t confuse this with char, which is the ASCII/UNICODE code of the character bound to the key

<num>	        The number of the clicked mouse button (only for mouse events)
<type>	        The event’s type
'''                            

# Example of event objects and their properties.

import tkinter as tk
from tkinter import messagebox


def click(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = "x=" + str(event.x) + ",y=" + str(event.y) + \
                 ",num=" + str(event.num) + ",type=" + event.type
        tk.messagebox.showinfo("Click!", string)        


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)
frame.pack()

window.mainloop()

# If you want to modify a property named 'prop', existing within a widget named 'wid', 
# and you’re going set its value to 'val', you can use the config() method, just like here:

    #   wid.config(prop=val)

# This means that if you want to unbind your current callback from a Button named b1, you would use an invocation like this one:

    #   b1.config(command=lambda:None)
# This binds an empty (i.e., doing absolutely nothing) function to the widget’s callback.


# Example of binding and unbinding command statements:

import tkinter as tk
from tkinter import messagebox


def on_off():
    global switch
    if switch:
        ##### Important line - How to remove a binding from an object
        button_2.config(command=lambda: None)
        #####
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


switch = True
window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()

# Note: the information about a previously used callback is lost. 
# You cannot retrieve it automatically and you must repeat the bind() invocation.