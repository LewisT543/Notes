import tkinter as tk
from tkinter import messagebox

def Click():
    replay = messagebox.askquestion('Quit?', 'Are, you sure?')
    if replay == 'yes':
        window.destroy()


window = tk.Tk()

# Label
label = tk.Label(window, text = "Little label:")
label.pack()

# Frame
frame = tk.Frame(window, height=30, width=100, bg="#000099")
frame.pack()

# Button
button = tk.Button(window, text="Button", command = Click)
button.pack(fill=tk.X)

# Switch
switch = tk.IntVar()
switch.set(1)
# Switch is not visible. 
# IntVar objects are set to hold integer values and controls internal communication between different widgets
# to set a value to and IntVar obj, we must use the set() method.

# Checkbutton
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)
checkbutton.pack()
# If you check or uncheck the checkbutton, because of the variable=switch argument above, the switch will change its
# state from a 1 (checked), to a 0 (unchecked) and vice-versa.
# If you change the state of the SWITCH object, the CHECKBUTTON object would IMMEDIATELY reflect the change. This means
# we do not have to access the checkbutton object directly, we can modify the switch value instead.

# Entry
entry = tk.Entry(window, width=30)
entry.pack()
# This allows us to input small data, of width 30 chars.

# Radio Buttons
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)
radiobutton_2.pack()
# Radiobuttons are similar to switches but work in groups, while 1 is active, the other(s) is/are not.
# ONLY ONE OF THE PAIR (OR MORE) OF RADIOBUTTONS MAY BE ACTIVE AT ONCE
    # Radiobutton arguments:
        # The VARIABLE argument binds a SWITCH object to both of the widgets, 
        # and this is the clue – the fact that both Radiobuttons are bound to 
        # the SAME OBJECT creates the GROUP. Don’t forget that!

        # The value argument distinguishes the Radiobuttons inside the group, 
        # and thus each of the Radiobuttons has to use a different value (we’ve used 0 and 1)

# all pack()'ed so potentially messy.
window.mainloop()