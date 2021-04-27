                                #### TKINTER GEOMETRY MANAGERS ####

# Geometry managers are ways of putting widgets inside of windows.
# They are called:
    # place
        # The most detailed geometry manager. Forces you to precisely declare a widgets location pixel by pixel.
        # It will not prevent overlapping either eachother or the edges of the window.
    # pack
        # An interpretive method, allows tkinter to take control and try to decide the best location for each widget
        # on its own. 
        # Be prepared for disappointment however, as it often underperforms.
    # grid
        # GRID lies in the middle, you express general wishes and it tries to deploy widgets accordingly.
        # More precise than PACK, but less precise than PLACE
# IMPORTANT:
    # THESE 3 METHODS CANNOT BE MIXED! Only one may be used in a single application.

# The 'place' geometry manager demands the usage of the place() method. 
# place() is invoked from within the OBJECT, not the window. The widget is always aware of the window it belongs to.

# place() parameters:
    # height=h - the widgets desired height measured in pixels. If ommited, it will be determined automatically.
    # width=w - the widgets desires width measured in pixels. If ommited, it will be determined automatically.
    # x=x - top left horizontal coordinate
    # y=y - top left vertical coordinate

#Example:

import tkinter as tk

window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_2 = tk.Button(window, text="Button #2")
button_3 = tk.Button(window, text="Button #3")

                    # PLACE() #
'''
button_1.place(x=10, y=10, width=150)
button_2.place(x=20, y=40)
button_3.place(x=30, y=70, height=50)
window.mainloop()
'''
# place() allows for full responsibility, the buttons will be located exactly where they are coded to be.

                    # GRID() #
'''
button_1.grid(row=0, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0, columnspan=2)
# button_3.grid(row=2, column=2)
window.mainloop()
'''
# The grid() method allows us to 'auto-snap' widgets to an invisible grid.
    # as well as row=x and column=y, grid has some other params:
        # columnspan=cs - determines how many columns the widget will occupy, default is 1.
        # rowspan=rs - same as columnspan for rows.

                    # PACK() #

button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()

# the pack() method has a few other params too:
    # side=s - forces the manager to pack the widgets in a specific direction, where s can be:
        # TOP, BOTTOM, LEFT, RIGHT
    # fill=f - suggests to the manager how to expand the widget if you want it to occupy more space, where f can be:
        # None - do nothing
        # X - expand in the HORIZONTAL direction
        # Y - expand in the VERTICAL direction
        # BOTH - expand in both directions

# A note:
# For serious programming, pack() is not recommended as the results can be very surprising and often lead to a bit of a mess.
# It can be useful to get a program functional but should be implemented with grid() (for simple situations) or place().
