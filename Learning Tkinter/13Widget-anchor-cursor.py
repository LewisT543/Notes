                                #### WIDGET ANCHOR + CURSOR ####

# ANCHOR
# The anchor is an imaginary (invisible) point inside the widget to which the text (if any) is anchored.
# We can change where the text is anchored by using: 
    
    # button['anchor'] = <compass direction>
    
# Compass directions : n, s, e, w, ne, nw, se, sw, venter

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
button_1 = tk.Button(window, text="Regular button");
button_1["anchor"] = 'e'
button_1["width"] = 20  # pixels!
button_1.pack()
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = 'sw'
button_2["width"] = 20
button_2["height"] = 3  # rows
button_2.pack()
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
# CURSOR
# The default mouse cursor reveals itself as an arrow. Sometimes, when it enters a specific area, its shape can change.
# You have the power to order the cursor to change to a different cursor over each of the widgets, 
# as every widget has the property we’re talking about.
# Example of different cursors: 
def click(dummy):
    messagebox.showinfo('You clicked', 'Close')

window = tk.Tk()
label_1 = tk.Label(window, height=3, text="arrow", cursor="arrow")
label_1.pack()
label_2 = tk.Label(window, height=3, text="clock", cursor="clock")
label_2.pack()
label_3 = tk.Label(window, height=3, text="heart", cursor="heart")
label_3.bind('<Button-1>', click)
label_3.pack()
window.mainloop()
