                                #### ADDING COLOUR ####

import tkinter as tk

window = tk.Tk()
button = tk.Button(window, text="Button #1", 
                   bg="Black", 
                   fg="Yellow", 
                   activebackground='Gray', 
                   activeforeground='DarkSlateGray')
button.pack()
window.mainloop()

# Tkinter has over 750 different predefined colours, just google em if you need them.
# This is cool but...


    # RGB colour model

# The RGB model allows us to set the saturation of each of the 3 primary colours. 
# saturation ranges from <0...255>, for each primary colour.
# When all the components are set to ZERO (absence of the colors), we get BLACK as a result.
# When all the components are set to 256 (full presence of colours), we get WHITE as a result.
# When one of the components is set to 255 while others are set to 0, we get one of the primary colors – red, green or blue.

# Representation can be done using a hexadecimal string.
# Each pair of digits forms a value from range <0x00...0xFF> (<0...255>) that determines the specific component level.

    # The format is '#RRGGBB'
    # Therefor:
        #) #000000 is black
        #) #FFFFFF is white
        #) #FF0000 is red
        #) #00FF00 is green
        #) #0000FF is blue
        #) #00FFFF is turquoise
        #) #FF00FF is violet

window = tk.Tk()
button = tk.Button(window, text="Button #1", 
                   bg="#000000", 
                   fg='#FFFF00', 
                   activebackground='#A9A9A9', 
                   activeforeground='#696969')
button.pack()
window.mainloop()
