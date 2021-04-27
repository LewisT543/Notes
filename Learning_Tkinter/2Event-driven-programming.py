                                #### EVENT DRIVEN PROGRAMMING ####

# First of all, detecting, registering and classifying all of a user's actions is beyond the programmer's control,
# there is a dedicated component called the EVENT CONTROLLER which takes care of this.

# You have to inform the event controller what you want to perform when a particular event (e.g., a mouse click) occurs. 
# This is done by writing specialized functions called event HANDLERS

# You write these handlers only for the events you want to serve – all other 
# events will activate default behaviors (e.g., focus moving and window closing).
# Of course, just implementing an event handler is not enough – you also have to make the event controller aware of it.

    # EVENTS
# An event is any 'occurance', such as:
    # ressing the mouse button
    # releasing the mouse button (actually, an ordinary mouse click consists of these two subsequent events)
    # moving the mouse cursor
    # dragging something under the mouse cursor
    # pressing and releasing a key
    # tapping a screen
    # tracking the passage of time
    # monitoring a widget’s state change
    # and many, many more...

# If we want to build portable GUI applications (i.e., apps able to work under different operating environments that always look the same) 
# we need something more – we need an adapter. A set of uniform facilities enables us, the programmers, 
# to write one code and not worry about portability.

# One of these toolkits, which is very attractive to us, is Tk.
# The module that brings TK to python is called TKinter.

