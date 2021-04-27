                            #### CALCULATOR V2 ####

# Learn practical skills related to:

# dealing with observable variables,
# working with the Entry widget,
# constructing complex interfaces with many cooperating Button widgets.

# Calculator must have:
    # +, -, *, /, ...? functions
    # change sign button
    # decimal point button
    # clear button
    # resistance to zero-div errors
        # produce an error message instead of raising an exception
        # (or do both?, A custom exception raised by a zero-div error?)

#### Assumptions ####
# clicks only
# display width = 10
# No more than 10 chars, throw an error if it is longer
    # but allowed to remove small decimal point numbers to keep it len<10 (using round())
# If no decimal points on display, dont show the point (10 not 10.0)
    # could do this using try: int(x) >>> else: float(x)


import tkinter as tk
from tkinter import messagebox, font
import operator
import simpleeval as se


window = tk.Tk()
window.title('Calculator v2')
window.geometry('400x450')

se.MAX_STRING_LENGTH = 10

class CalculatorTwo():

    def __init__(self, master):

        # Set up display frame
        self.displayframe = tk.Frame(master, width=400, height=50)
        self.displayframe.place(x=0, y=0)
        
        # Entry variable setup
        self.entry_var = tk.StringVar()
        self.entry_var.trace("w", lambda *args: self.validate(self.entry_var))
        self.panel = tk.Entry(self.displayframe, width=10, textvariable=self.entry_var, font=('MonoLisa', 30), 
                                justify='right', borderwidth=0)
            # Very clever line to unbind all 'Keyboard' presses.
        self.panel.bind('<Key>', lambda e: 'break')
        self.panel.place(x=175, y=0)

        # Set up Buttons and container frame
            # button font
        self.button_font = font.Font(family='MonoLisa', size=34)
        self.buttonframe = tk.Frame(master, width=400, height=400)
        self.buttonframe.place(x=0, y=50)    
        self.button_dict = {'1': (0, 0), '2': (0, 1), '3':(0, 2), '4':(1, 0), '5':(1, 1), '6':(1, 2), '7':(2, 0), '8':(2, 1), '9':(2, 2), '0': (3, 0),
                            'C': (3, 1), '.': (3, 2), 'Del':(0, 3), '=': (2, 3), '+/-': (3, 3), '+': (0, 4), '-': (1, 4), '*': (2, 4), '/': (3, 4)}

        for key, val in self.button_dict.items():
            self.button = tk.Button(self.buttonframe, width=2, height=1, padx=8, pady=8,text=str(key), font=self.button_font)
            self.button.grid(row=val[0], column=val[1])
            if self.button['text'] in ['=', '+/-', 'Del']:
                self.button.config(width=3)
            if not self.button['text'] in ['C', '=', 'Del']:
                self.button.bind('<Button-1>', self.button_clicked)
            elif self.button['text'] == 'C':
                self.button.config(command=self.clear_screen)
            elif self.button['text'] == '=':
                self.button.config(command=self.parse_calc)
            elif self.button['text'] == 'Del':
                self.button.config(command=self.del_one)
        
    def button_clicked(self, event):
        btn = event.widget
        entrant = btn['text']
        current = self.entry_var.get()
        try:
            self.entry_var.set(str(current) + str(entrant))
        except:
            print('pass')

    def parse_calc(self):
        try:
            self.entry_var.set(se.simple_eval(self.entry_var.get()))
            self.validate()
        except ZeroDivisionError:
            messagebox.showerror('Error', 'Cant divide by zero.')
            self.clear_screen()
        except SyntaxError:
            messagebox.showerror('Error', 'Invalid calculation.\n(Last digit was probably an operator)')
        
    def clear_screen(self):
        self.entry_var.set('')

    def del_one(self):
        self.entry_var.set(self.entry_var.get()[:-1]) 

    def validate(self, *args):
        if len(self.entry_var.get()) > 10:
            self.entry_var.set(self.entry_var.get()[:-1])
            messagebox.showerror('Error', 'Too many digits.\n(Max 10)')


calc = CalculatorTwo(window)
window.mainloop()