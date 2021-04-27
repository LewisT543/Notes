                                #### WIDGET PROPERTIES ####

# As you already know, every widget has a set of properties, and the widget’s user is able to change them 
# by modifying the widget’s appearance and behavior.

# A widget's property is not just an object property. You have to use one of two possible ways of reading 
# and setting widget properties’ values.
# The first method is based on using a dictionary which exists inside every widget.
    # old_val = Widget["prop"]
    # Widget["prop"] = new_val
    
import tkinter as tk

def on_off():
    global button
    # accessing the 'text' property of the button widget
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()

# Note: we use the text property to:
    # DIAGNOSE the current button’s state
    # CHANGE the button’s state to the contrary one
    # UPDATE the button’s title

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
# CGET() AND CONFIG()
# The second method relies on two specialised widget methods, the first named cget() designed to READ the properties
# value, and the second config(), which allows you to SET new values to the property.

def on_off():
    global button
    # Read the button text
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    # Set the button text
    button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off)
button.place(x=50, y=100, width=100)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> # 
# THE FONT PROPERTY

# Every widget presenting a piece of text (e.g., Button and Label but not Frame) can be made to use a font different 
# from the default.
# Tkinter represents fonts as tuples
# Any font can be described as two- or three-element tuples:
    
    # The TWO-element tuple contains two strings: the first containing the font’s family name, and the second carrying the font’s 
    # size measured in points; note: the second element has to be a string, although it specifies strictly numerical information
    
    # The tHREE-element tuple uses the third string to specify the font’s style, which can be expressed using the following strings:
        # "bold"
        # "italic"
        # "underline"
        # "overstrike"

window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()
