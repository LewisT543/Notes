                                #### SHAPING THE MAIN WINDOW AND CONVERSING WITH THE USER ####

# CHANGING ASPECTS OF THE WINDOW

# Changing the TITLE
import tkinter as tk
def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


counter = 10
window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)
window.mainloop()


# Changing the ICON
from tkinter import PhotoImage

window = tk.Tk()
window.title('Icon?')
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))
window.bind("&lt;Button-1&gt;", lambda e: window.destroy())
window.mainloop()


# Changing the SIZE of the window
# + limiting the size of a window
import tkinter as tk


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


size = 100
grows = True
window = tk.Tk()
window.title('Geometry+Minsize')
####
window.minsize(width=250, height=250) # we use two keyword arguments for this
window.maxsize(width=1000, height=1000) # and this
####
window.geometry("500x500")  # We use a string in format 'width x height' as a parameter for geometry()
####
window.bind("&lt;Button-1&gt;", click)
window.mainloop()


# Enabling and diabling resizign
import tkinter as tk

window = tk.Tk()
window.title('Resizable')
####
window.resizable(width=False, height=False) # Boolean values not integers - IMPORTANT
####
window.geometry("400x200")
window.mainloop()

# True allows the user to alter the window size along that diemension, false disables this.

####
# BINDING CALLBACKS TO THE CLOSURE OF THE MAIN WINDOW
    # protocol("WM_DELETE_WINDOW", callback)

import tkinter as tk
from tkinter import messagebox


def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()


window = tk.Tk()
window.title('Exit - protocol()')
window.protocol("WM_DELETE_WINDOW", really)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# USER CONVERSATION

# There are built in methods that allow us to handle simple yes/no questions:
    # one of these is:
        # messagebox.askyesno(title, message, options)
        # title – a string displayed in the dialog’s title bar
        # message – a string displayed inside the dialog; note: the \n plays its normal role and breaks up the message’s lines;
        # options – a set of options shaping the dialog in a non-default way, two of which are useful to us:
            # default – sets the default (pre-focused) answer; usually, it’s focused on the button located first from the left; this can be changed 
                        # by setting the keyword argument with identifiers like CANCEL, IGNORE, OK, NO, RETRY, and YES;
            # icon – sets the non-default icon for the dialog: possible values are: ERROR, INFO, QUESTION, and WARNING.    


# RETRIEVING BOOLEAN (YES/NO) ANSWERS FROM USER
import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askyesno("?", "YES OR NO")    
    print(answer)

def question2():
    answer = messagebox.askokcancel("?", "OK OR CANCEL")     
    print(answer)

def question3():
    answer = messagebox.askretrycancel("?", "RETRY OR CANCEL") # Makes os perform a 'bing' noise on messagebox opening
    print(answer)



window = tk.Tk()
window.title('Return-True/False')
button = tk.Button(window, text="Ask the question! (1)", command=question)
button.pack()
button2 = tk.Button(window, text="Ask the question! (2)", command=question2)
button2.pack()
button3 = tk.Button(window, text="Ask the question! (3)", command=question3)
button3.pack()
window.mainloop()


# RETRIEVING STRING ANSWERS FROM USER
    # The askquestion() function 

import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive") # Return 'Yes' if user response is positive
    print(answer)                                                               # Return 'No' if user response is negative
                                                                                    # Both of these are STRINGS

window = tk()
window.title('Returning Strings')
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()


####
    # The showerror() function

import tkinter as tk
from tkinter import messagebox


def question():
    answer = messagebox.showerror("!", "Your code does nothing!")   # Returns 'OK' string in every case
    print(answer)


window = tk.Tk()
window.title('Return Errors + Warnings Strings')
button = tk.Button(window, text="Alarming message", command=question)
button.pack()
window.mainloop()

