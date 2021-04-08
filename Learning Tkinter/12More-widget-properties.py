                                #### WIDGET SPACING ####

# Every widget occupies a part of the window’s area, thus it’s obvious the widgets must have sizes.
# Widgets also have properties describing many more sizes than just width (usually specified in pixels) and height:
    
    # borderwidth	        The width of the 3D-frame surrounding some widgets (e.g., Button)
    
    # highlightthickness	The width of the additional frame drawn around the widget when it gains the focus
    
    # padx/pady	            The width/height of an additional empty space/margin around the widget
    
    # wraplength	        If the text filling the widget becomes longer than this property’s value, it will be wrapped 
    #                       (possibly more than once)
    
    # height	            The height of the widget
    
    #       	            The index of the character inside the widget’s text, which should be presented as underlined or -1 
    # underline             otherwise (the underlined letter/digit can be used as a shortcut key, but it needs a specialized callback 
    #                       to work – no automation here, sorry)

    # width	                The width of the widget


import tkinter as tk


window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
window.mainloop()

# Widget property name	 Property role
# background/bg	         The color of the widget’s background (you can freely use either of these two forms)
#                        foreground

# fg	                 The color of the widget’s foreground (note: it can mean different things in different 
#                        widgets; in general, it’s used to specify text color)

# activeforeground/      Like bg and fg but used when the widget becomes active
#  activebackground
	
# disabledforeground	 ???

# Example:
window = tk.Tk()
button_1 = tk.Button(window, text="Ordinary button");
button_1.pack()
button_2 = tk.Button(window, text="Colorful button")
button_2.pack()
button_2.config(bg ="#000000")
button_2.config(fg ="yellow")
button_2.config(activeforeground ="#FF0000")
button_2.config(activebackground ="green")
window.mainloop()

