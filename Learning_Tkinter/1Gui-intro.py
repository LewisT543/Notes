                                #### GRAPHICAL USER INTERFACES ####

# Gui's are bidirectional displays
# Creating apps able to utilise GUI features can be called VISUAL PROGRAMMING

# WIDGETS / CONTROLS
# Widgets are the GUI elements designed to receive the inputs. Be that mouse movements or clicks (taps on mobile), or
# any combination of movements/clicks.

# One of the widgets living inside a particular window owns the focus (often called the focus widget).
# The focus widget is the default recipient of some or all of the user's actions.
# The focus may be changed (usually using the 'Tab' key.)

# Elements of a window:
    # title bar
    # closing button
    # title

# The window's interior is equipped with a set of widgets responsible for implementing the window's functionalities. 
# Some of them are active (they can receive a user's clicks or, in other words, they are clickable) while others aren't.

# Unclickable elements:
    # icon (small picture for identifying)
    # label (describing text)
# Clickable elements:
    # 'Yes' button (In this example it is FOCUSED, shown by a dotted blue line surrounding the button. Pressing the spacebar now
    #  would be taken as an affirmative response).
    # 'No' button (plain button, not the focus)

# At this point we can press 'Tab' to switch to the next clickable element, in this case its the 'No' button.

# >>>:
    # 'No' button (now the focus, denotted by dotteb blue border line.)
    # 'Yes' button (no longer the focus)

# This style of programming would require code that looked similar to below, and would require extensive development for any
# sort of useful results.
'''
while True:
    wait_for_user_action()
    if user_pressed_button_yes():
    :
    elif user_pressed_button_no():
    :
    elif user_move_mouse_coursor_over_button_yes():
    :
    elif user_move_mouse_coursor_over_button_no():
    :
    elif user_pressed_Tab_key():
        if isfocused(button_yes):
        :
        elif isfocused(button_no):
       :
    :
    :
'''
# not the most efficient approach
