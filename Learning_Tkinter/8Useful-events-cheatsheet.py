'''
Event name	        Event role
<Button-1>	        Single left-click (if your mouse if configured for a right-handed user)
<Button-2>	        Single middle-click
<Button-3>	        Single right-click
<ButtonRelease-1>	Left mouse button release

Note: there are also events named <ButtonRelease-2> and <ButtonRelease-3>
<DoubleButton-1>	Double left-click

Note: there are also events named <DoubleButton-2> and <DoubleButton-3>

Note again: the <Button-1> event is a part of <DoubleButton-1> too; if you assign a callback to <Button-1>, it will be launched, too!

Event name	        Event role
<Enter>	            Mouse cursor appears over the widget
<Leave>	            Mouse cursor leaves the widget area
<Focus-In>	        The widget gains the focus
<Focus-Out>     	The widget loses the focus
<Return>	        The user presses the Enter/Return key
<Key>	            The user presses any key

Event name	        Event role
x	                The user presses x key (x can be neither a space nor the < key)
<space>	            The user presses the spacebar
<less>	            The user presses the < key
<Cancel>	        The user presses the key/keys used by the current OS to stop the program (e.g., Ctrl-C or Ctrl-Break)
<BackSpace>	        The user presses the Backspace key
<Tab>	            The user presses Tab key


Event name	        Event role
<Shift_L>	        The user presses one of the Shift keys
<Control_L>	        The user presses one of the Control keys
<Alt_L>	            The user presses one of the Alt keys
<Pause>	            The user presses the Pause key
<Caps_Lock>	        The user presses the Caps Lock key
<Esc>	            The user presses the Escape keys

Event name	        Event role
<Prior>	            The Page Up key
<Next>	            The Page Down key
<End>	            The End key
<Home>	            The Home key

<Left>              Cursor (arrows) keys
<Right>
<Up>
<Down>	            

<Num_Lock>          The two Lock keys
<Scroll_Lock>	    

<Shift-x>           The x key has been pressed along with any of the Shift, Alt, or Control keys
<Alt-x>
<Control-x>	
'''

# A callback designed for usage with the command property/parameter is a parameterless function;
# A callback intended to cooperate with the bind() method is a one-parameter function (the callback’s 
# argument carries some info about the captured event)
# Fortunately, it doesn’t mean that you have to define two different callbacks for those two applications, 
# and this is how we’ll cope with the above requirements:


import tkinter as tk
from tkinter import messagebox

# This code allows us to bind non naturally clickable widgets. Clicking on either the label or frame
# calls click() in this case.

def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # Line I
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click)   # Line II
frame.pack()

window.mainloop()