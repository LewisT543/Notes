                                #### TKinter ####

# Tkinter consist of 4 essential elements:
    # Importing the needed tkinter components
    # Creating an application’s main window
    # Adding a set of necessary widgets to the window
    # Launching the event controller

import tkinter

# often Tk() is enough for a fully formed tkinter object, however it is invisible until the controller's mainloop starts
# Entering the mainloop means that yo no longer have direct control over the codes execution. It is down to the controller.
'''
def Click():
    skylight.destroy(); 

skylight = tkinter.Tk()  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< initialise Tk() object 
skylight.title('Skylight')  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< change title to 'skylight'
button = tkinter.Button(skylight, text='Bye', command=Click)  # Initialise button, adding 'click' as the executable function.
button.place(x=50, y=50)    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< place the button on the window
skylight.mainloop()   # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Run that shit
'''
# Click() is an example of a HANDLER or CALLBACK function. Designed to be invoked by someone/something else.

# Some notes:
# Binding the callback with the widget by using the command constructor's parameter is not the only way offered by tkinter 
# for this purpose; moreover, callbacks can be replaced during program execution – we'll tell you more about that soon
# The one and same callback can be bound with more than one widget – it's a very useful solution in some cases.

# Introducing messageboxes
from tkinter import messagebox

# Callback function
def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();

skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=25, y=25)
skylight.mainloop()


# Messagebox is able to create dialog boxes intended to ask questions, display messages, and to receive a user's reply.