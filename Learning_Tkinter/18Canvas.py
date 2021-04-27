                                #### CANVAS ####

# A canvas is a flat rectangular surface which can be covered with drawings, text, frames and other widgets.

import tkinter as tk


window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


# PROPERTY NAME 	PROPERTY ROLE
# borderwidth	    canvas border’s width in pixels (default: 2)
# background (bg)	canvas border’s color (default: the same as the underlying window’s color)
# height        	canvas height (in pixels)
# width         	canvas width (in pixels)

    # THE CREATE_LINE() METHOD  
# To create a polygonal chain, we must use create_line():
    # canvas.create_line(x0, y0, x1, y1, ... , xn, yn, option...)
    # The (x0, y0, ...) are the coordinates of the shape
    # Some of the additional OPTIONS are as follows:

# CREATE_LINE(...OPTIONS)
# OTPION NAME       OPTION MEANING
# arrow	            normally, the chain ends aren’t marked in any special way, but you may want them to be finished with arrowheads; 
                    # setting the arrow option to FIRST results in drawing an arrowhead at the chain’s beginning, LAST at the chain’s 
                    # end, BOTH at both sides of the chain.
# fill	            chain color (setting the option to an empty string causes the line to be transparent)
# smooth	        setting it to True rounds the chain’s corners using a set of connected parabolas
# width	            line width (default: 1 pixel)

# EXAMPLE:  

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380,
                   arrow=tk.BOTH, fill='red', smooth=True, width=3)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_RECTANGLE() METHOD
# Similar to create_line() but uses two opposite vertices at (x0, y0) and (x1, y1) points.

# OPTION NAME       OPTION MEANING
# outline	        rectangle edge color (if specified as an empty string, the edge is transparent)
# fill	            rectangle interior color
# width	            rectangle edge width in pixels (default: 1)

# EXAMPLE:

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_POLYGON() METHOD
# Again similar to create_line() but you do not have to draw the last point, it is drawn automatically.
    # canvas.create_polygon(x0, y0, x1, y1, xn, yn, option...)
    # Uses same set of options as create_line()

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='black')
canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_OVAL() METHOD
# Options are the same as create_polygon()
    # canvas.create_oval(x0, y0, x1, y1, xn, yn, option...)
    # This method draws a rectangle and populates it with an elipses.

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_ARC() METHOD
# Same as create_oval()
    # canvas.create_arc(x0,y0,x1,y1,option...)
    # Options are the same as create_polygone PLUS a few more:

# OPTION NAME           OPTION MEANING
# style	                can be set to one of the following: PIESLICE (default), CHORD and ARC
# start	                the angle (in degrees) of the arc’s start relative to the X-axis (e.g., 90 means the highest point of the ellipse, 
                        # while 0 is the right-most point. The default is 0)
# extent                the arc’s span (in degrees) relative to the start point; note: the span is calculated counter-clockwise. 
                        # the default is 90 (a quarter of an ellipse).

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
canvas.create_arc(10, 100, 380, 300, outline='red', width=5)
canvas.create_arc(10, 100, 380, 300, outline='blue', width=5,
                  style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, outline='green', width=5,
                  style=tk.ARC, start=180, extent=180)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_TEXT() METHOD
# The create_text() method puts text on the canvas. The text is placed in a rectangle whose center point is located at (x, y).
    # canvas.create_text(x, y, option...)
    # Options are as foolows:

# OPTION NAME       OPTION MEANING
# fill              text colour
# font              text font
# justify           text Justification (ie, left, center, right)
# text              text to display
# width             normally the rectangle is as wide as the longest text line: using width allows you to force the text to be aligned
                    # with that size.

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='blue')
canvas.create_text(200, 200, text="Mary\nhad\na\nlittle\nlamb",
                   font=("Arial","40","bold"),
                   justify=tk.CENTER,
                   fill='white')
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()


# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
    # THE CREATE_IMAGE() METHOD
# The create_image() method draws a bitmap on the canvas. The drawing is located inside a rectangle with centre (x, y).
    # canvas.create_image(x, y, option...)
    # options as follows:

# OPTION NAME           OPTION MEANING
# image	                an object of the PhotoImage class containing the image itself; the PhotoImage class constructor needs a keyword argument 
                        # named file pointing to a bitmap file (note: only GIF and PNG formats are accepted); the argument should specify the 
                        # file’s path

import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
image = tk.PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()

# This is for a simple PNG bitmap.

    # Using JPEG format with create_image()
# If we want to use jpeg format we must do some additional steps:
    # 1). import the Image and ImageTk classes from the PIL (Python Image Library) module;
    # 2). build an object of the Image() class and use its open() method to fetch the bitmap from the file 
          # (the argument should specify the file’s path)
    # 3). convert this object into a PhotoImage class object using an ImageTk function of the same name;
    # 4). continue as usual.

# EXAMPLE:

import tkinter as tk
import PIL

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='red')
jpg = PIL.Image.open('logo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()



