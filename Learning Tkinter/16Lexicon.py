                                #### A LEXICON OF WIDGETS ####

# Each tkinter widget is created by a constructor of its class. The very first argument of the constructor invocation is always the master widget 
# i.e., the widget that owns the newly created object.

    # widget = Widget(master, option, ... )

# all widgets fall into two categories: clickable and non-clickable. We’ll start with the first.
    # CLICKABLE WIDGETS

# BUTTON
    # A basic button, press it.
# BUTTON PROPERTY	PROPERTY MEANING
# command	        the callback being invoked when the button is clicked
# justify	        the way in which the inner text is justified: possible (self-describing) values are: LEFT, CENTER, and RIGHT
# state	            if you set the property to DISABLED, the button becomes deaf and doesn’t react to clicks, while its title is shown in gray; 
                    # setting it to NORMAL restores normal button functioning; when the mouse is located above the button, 
                    # the property changes its value to ACTIVE

# BUTTON METHOD 	METHOD ROLE
# flash()	        the button flashes a few times but doesn’t change its state
# invoke()	        activates the callback assigned to the widget and returns the same value the callback returned; note: this is the only way 
                    # to invoke your own callback explicitly, as the event manager must be aware of the fact

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# CHECKBUTTON
    # A two-state switch that can be checked or not. Good for yes/no choices.
# CHECKBUTTON PROPERTY	    PROPERTY MEANING
# bd	                    the checkbutton frame width (default is two pixels)
# command	                the callback being invoked when the checkbutton changes its state
# justify	                the same as for Button
# state	                    the same as for Button
# variable	                an OBSERVABLE IntVar variable reflecting the widget’s state; defaultly it’s set to 1 when the checkbutton is checked, 
                            # and to 0 otherwise
# offvalue	                the non-default value being assigned to a variable when the checkbutton is not checked
# onvalue	                the non-default value being assigned to a variable when the checkbutton is checked

# CHECKBUTTON METHOD 	    METHOD ROLE
# deselect()	            unchecks the widget
# flash()                   the same as for Button
# invoke()                  the same as for Button
# select()	                checks the widget
# toggle()	                toggles the widget (changes its state to the opposite one)

import tkinter as tk
from tkinter import messagebox


def count():
    global counter
    counter += 1


def show():
    messagebox.showinfo("", "counter=" + str(counter) + ",state=" + str(switch.get()))


window = tk.Tk()
window.title('Checkbutton')
switch = tk.IntVar()
counter = 0
button = tk.Button(window, text="Show", command=show)
button.pack()
checkbutton = tk.Checkbutton(window, text="Tick", variable=switch, command=count)
checkbutton.pack()
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# RADIOBUTTON
    # A button usable in groups. Only one may be mutually selected at any given time. Tt’s a good tool to represent one of many user choices.
    # Assigning the same observable variable to more than one Radiobutton creates a group. 
    # This also means that when two Radiobuttons use different observable variables, they belong to different groups by definition.
# rdbutton = Radiobutton(master, option, ...)

# RADIOBUTTON PROPERTIES        PROPERTY MEANING
# command	                    the callback being invoked when the Radiobutton (not the group it belongs to!) changes its state
# justify                       same as button
# state                         same as button
# variable	                    an observable IntVar or StringVar variable reflecting the current selection within the Radiobutton’s group; 
                                # changing the variable’s value automatically changes the selection
# value	                        a unique (inside the group) value identifying the Radiobutton; can be an integer value or a string, and should 
                                # be compatible with the variable’s type

# RADIOBUTTON METHODS           METHOD ROLE
# deselect()	                unchecks the widget
# flash()	                    the same as for Button
# invoke()	                    the same as for Button
# select()	                    checks the widget

import tkinter as tk
from tkinter import messagebox


def show():
    messagebox.showinfo("", "radio_1=" + str(radio_1_var.get()) +
                        ",radio_2=" + str(radio_2_var.get()))


def command_1():
    radio_2_var.set(radio_1_var.get())


def command_2():
    radio_1_var.set(radio_2_var.get())


window = tk.Tk()
window.title('Radiobutton')
button = tk.Button(window, text="Show", command=show)
button.pack()
radio_1_var = tk.IntVar()
radio_1_1 = tk.Radiobutton(window, text="pizza", variable=radio_1_var, value=1, command=command_1)
radio_1_1.select()
radio_1_1.pack()
radio_1_2 = tk.Radiobutton(window, text="clams", variable=radio_1_var, value=2, command=command_1)
radio_1_2.pack()
radio_2_var = tk.IntVar()
radio_2_1 = tk.Radiobutton(window, text="FR", variable=radio_2_var, value=2, command=command_2)
radio_2_1.pack()
radio_2_2 = tk.Radiobutton(window, text="IT", variable=radio_2_var, value=1, command=command_2)
radio_2_2.select()
radio_2_2.pack()
window.mainloop()

# This program defines two separate Radiobutton groups, consisting of two Radiobuttons each. These groups are coupled, 
# as their callbacks change the opposite group to reflect the state of their own group.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

#### NON-CLICKABLE WIDGETS #### 

# LABEL
    # A label displays some lines of text inside the window.
    # label = Label(master, option, ...)

# LABEL PROPERTIES          PROPERTY MEANING
# text	                    a string which will be shown within the Label; note: newline characters (\n) are interpreted in the usual way
# textvariable	            the same as for text, but makes use of an observable StringVar variable, so if you change the variable’s alteration, 
                            # it will be immediately visible on the screen.

# LABEL HAS NO USABLE METHODS

import tkinter as tk


def to_string(x):
    return "Current counter\nvalue is:\n" + str(x)


def plus():
    global counter
    counter += 1
    text.set(to_string(counter))


counter = 0
window = tk.Tk()
window.title('Label')
button = tk.Button(window, text="Go on!", command=plus)
button.pack()
text = tk.StringVar()
label = tk.Label(window, textvariable=text, height=4)
text.set(to_string(counter))
label.pack()
window.mainloop()                        

# The sample in the editor shows how the textvariable accompanied by an observable variable can be used to 
# continuously update the Label’s contents.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# MESSAGE
    # A message widget is very similar to a label, but is able to format the presented text by fitting it automattically to the widgets size
    # message = Message(master, option, ...)
    # HAS SAME PROPERTIES AS LABEL(See above)

import tkinter as tk


def do_it_again():
    text.set(text.get() + "and again...")


window = tk.Tk()
window.title('Message')
button = tk.Button(window, text="Go ahead!", command=do_it_again)
button.pack()
text = tk.StringVar()
message = tk.Message(window, textvariable=text, width=400)
text.set("You did it again... ")
message.pack()
window.mainloop()

# This program continually adds 'and again...' to the end of a string, increasing the size of the window to fit it.

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# FRAME
    # The frame widget is a container designed to hold other widgets. 
    # This means that the Frame can be used to separate a rectangular part of the window and to treat it as a kind of local window.
    # Such a window works as a master widget for all the widgets embedded within it.
    # Moreover, the Frame has its own coordinate system, so when you place a widget inside a Frame, you measure its location relative 
    # to the Frame’s upper-left corner, not the window’s one.
    # It also means that if you move the Frame to a new position, all its inner widgets will go with it.
    # Note: the Frame can grasp virtually any widget – including another Frame.

# FRAME PROPERTIES          PROPERTY MEANING
# takefocus	                normally, the Frame doesn’t take the focus (which would seem to be obvious) but if you really want it to behave 
                            # in this way, you can set the property to 1.

import tkinter as tk

window = tk.Tk()
window.title('Frame')

frame_1 = tk.Frame(window, width=200, height=100, bg='white')
frame_2 = tk.Frame(window, width=200, height=100, bg='yellow')

button_1_1 = tk.Button(frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

frame_1.pack()
frame_2.pack()

window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# LABELFRAME
    # A LabelFrame is a frame, enriched with a visible border and a title.
    # lfrm = LabelFrame(master, option, ...)

# LABELFRAME PROPERTIES         PROPERTY MEANING
# takefocus	                    the same as for the Frame
# text	                        the LabelFrame’s title
# labelanchor                   anchor points for the frame (n, ne, en, e, es, se, s, sw, ws, w, wn, nw)

import tkinter as tk

window = tk.Tk()
window.title('LabelFrame')
label_frame_1 = tk.LabelFrame(window, text="Frame #1",
                              width=200, height=100, bg='white')
label_frame_2 = tk.LabelFrame(window, text="Frame #2",
                              labelanchor='se', width=200, height=100, bg='yellow')

button_1_1 = tk.Button(label_frame_1, text="Button #1 inside Frame #1")
button_1_2 = tk.Button(label_frame_1, text="Button #2 inside Frame #1")
button_2_1 = tk.Button(label_frame_2, text="Button #1 inside Frame #2")
button_2_2 = tk.Button(label_frame_2, text="Button #2 inside Frame #2")

button_1_1.place(x=10, y=10)
button_1_2.place(x=10, y=50)
button_2_1.grid(column=0, row=0)
button_2_2.grid(column=1, row=1)

label_frame_1.pack()
label_frame_2.pack()
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# ENTRY
    # The entry widget presents a line of text, which is editable according to the users actions.
    # The widget implements all standard edit operations like inserting, removing, scrolling, selecting, copying and pasting, etc..

# ENTRY PROPERTIES          PROPERTY MEANING
# command	                although Entry is obviously a clickable widget, it doesn’t allow you to bind a callback through the command property. 
                            # You can observe and control all occurring changes instead by setting the tracer function for the 
                            # observable variable which cooperates with Entry (we’ll show you this – be patient!)
# show	                    a string assigned to this property will be displayed instead of the actual characters entered into the input field; 
                            # e.g., if you set show='*', this will enable the widget to safely edit the user’s password
# state	                    the same as for Button
# textvariable	            an observable StringVar reflecting the current state of the input field
# width	                    the input field’s width (in characters)

# ENTRY METHODS             METHOD ROLE
# get()	                    returns the current input field’s contents as a string
# set(s)	                sets the whole input field’s contents with the s string
# delete(first, last=None)	deletes a part of the input field’s contents; first and last can be integers with values indexing the string; 
                            # if the last argument is omitted, a single character is deleted; if last is specified as END, it points to the 
                            # place after the last field’s character
# insert(index, s)	        inserts the s string at the field position pointed to by index


# Example: DIGITS ONLY
# how to use an observable variable along with the trace callback (tracer) to force a user to enter only digits

import tkinter as tk


def digits_only(*args):
    global last_string
    string = text.get()
    # will not allow string to be longer than 5 chars.
    if len(string) >= 5:
        text.set(last_string[0:5])
    #
    if string == '' or string.isdigit():  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)


last_string = ''
window = tk.Tk()
window.title('Entry')
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text)
text.set(last_string)
text.trace('w', digits_only)
entry.pack()
entry.focus_set()
window.mainloop()

# The tracer is invoked each time the input field is modified.
# The tracer remembers its previous state (using the last_s variable) and restores the field to this state if its current contents are invalid.
# Note: we’ve had to use the focus_set() method, as the widget doesn’t take the focus itself.


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# MENUS
    # mnu = Menu(master, option, ...)
    # a classic menu is actually a horizontal bar located at the top of the application window;
    # the bar contains a number of horizontally deployed options, often referred to as items or entries;
    # these options can have hot-keys (keyboard shortcuts enabling the user to quickly access selected operations without using a mouse; 
    # usually, hot-keys are triggered by pressing Alt-hotkey on the keyboard)

    # selecting a menu’s option (it doesn’t matter whether through a hotkey or by a mouse click) causes one of two effects:
        # it launches a callback bound to the option;
        # it unrolls a new menu (actually a submenu)
    
    # if you want to have such a menu within your Tkinter application, you have to:
        # create a top-level menu object;
        # embed it inside the window;
        # bind a number of required submenus (this is called a cascade) or connect a single callback.

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure():
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")

window = tk.Tk()
window.title('Menus')

# main menu creation
main_menu = tk.Menu(window)
window.config(menu=main_menu)

# 1st main menu item: an empty (as far) submenu
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)

sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", underline=0, command=are_you_sure)

# 2nd main menu item: a simple callback
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.mainloop()

# If you want to add a dedicated hotkey, you must do 2 things:
    # 1). set the item’s property named accelerator with a string naming the hot-key (note: this has no other effect than just 
    # displaying the right-aligned string inside the item – no callback is set at the moment)
    # 2.) make a global binding linking the hotkey with a proper callback function.

import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


window = tk.Tk()
window.title('Menu-Hotkeys')

main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

sub_menu_file.add_separator()
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q",
                          underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)
main_menu.add_command(label="About...", command=about_app, underline=1)

window.bind_all("<Control-q>", are_you_sure)
window.mainloop()

# (NOTE:) you cannot modify any of the (sub)menu item by using the standard config() method invocation
# if you want to change the component, you must use: entryconfig()
    # item.entryconfigure(i, prop=value)
    # the first is an integer index of the modified item (entry)
    # the second is a keyworded argument pointing to the modified property.

import tkinter as tk


def on_off():
    global accessible
    if accessible == tk.DISABLED:
        accessible = tk.ACTIVE
    else:
        accessible = tk.DISABLED
    sub_menu.entryconfigure(1, state=accessible)


accessible = tk.DISABLED
window = tk.Tk()
window.title('SubMenus+entryconfig()')
menu = tk.Menu(window)
window.config(menu=menu)
sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=sub_menu)
sub_menu.add_command(label="On/Off", command=on_off)
sub_menu.add_command(label="Switch", state=tk.DISABLED)
window.mainloop()


# MENU PROPERTIES           PROPERTY MEANING
# postcommand	            a callback invoked every time a menu’s item is activated
# tearoff	                set to zero removes the tear-off decoration from the top of the cascade
# state	                    when set to DISABLED, the menu item is grayed and inaccessible; setting it to ACTIVE restores its normal functionality
# accelerator	            a string describing a hot-key bound to the menu’s item

# MENU METHODS                      METHOD ROLE
# add_cascade(prop=val, ...)	    adds a cascade to the menu’s item
# add_command(prop=val, ...)	    assigns an action to the menu’s item
# add_separator()	                adds an separator line to the menu
# entryconfigure(i, prop=val,...)	modifies the i-th menu item’s property named prop

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
