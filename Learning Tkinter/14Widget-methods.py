                                #### WIDGET METHODS ####

# Widgets have methods:
    
    # Widget.after(time_ms, function)
    # after() - This method expects two arguments: the first is a time interval specification (expressed in milliseconds:
    # 1 s = 1000 ms) and the second points to an existing function;
    # When the number of milliseconds elapses, the manager will invoke the function (only once).
    # note: this the only possible way of controlling the passage of time when using an event-driven environment.
    
    
    # Widget.after_cancel(id)
    # after_cancel(id) – This method cancels the planned invocation identified by the id argument.

    #
import tkinter as tk


def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    # we continue to encourage it every time the blink() function is invoked
    frame.after(500, blink)


is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
# we initially encourage it to make the invocation before the frame widget is packed into the main window;
frame.after(500, blink)
frame.pack()
window.mainloop()

# Note: there is no explicit invocation of the function inside the code. 
# Moreover, it isn’t assigned as a callback. The question is – who invokes it?
    # The event managers do.
# Initially invoked after initialising the frame. Then once again at the end of every execution of blink.


# THE DESTROY() METHOD
# The destroy() method deletes a widget entirely, from your view and from the event managers memory.
# Note: if the widget you want to destroy has children (when other widgets are embedded inside it, which can happen with frames) 
# the children will be destroyed, too (this rule works recursively).

import tkinter as tk


def suicide():
    frame.destroy()


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=10, y=10)
frame.after(5000, suicide)
frame.pack()
window.mainloop()

# This program creates a frame which destroys itself after 5 seconds


# GET_FOCUS
# Widgets may or may not have the focus. At most one widget can have the focus. 
# you can use the Tab and Shift-Tab keys to move the focus forward and backward. But the focus can be controlled
# programmatically too.
    # wi.focus_get()
    # the focus_get() method returns a reference to the currently focused widget, or None when no widget owns the focus 
    # (note: you can invoke the method from any widget, including the main window)
    
    # wi.focus_set()
    # the focus_set() method focuses the widget from the method which was invoked, so you have to choose it carefully.

import tkinter as tk


def flip_focus():
    if window.focus_get() is button_1:
        button_2.focus_set()
    else:
        button_1.focus_set()
    window.after(1000, flip_focus)


window = tk.Tk()
button_1 = tk.Button(window, text="First")
button_1.pack()
button_2 = tk.Button(window, text="Second")
button_2.pack()
window.after(1000, flip_focus)
window.mainloop()
