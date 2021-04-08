                                #### BASIC CALCULATOR ####

# Basics, a simple calculator
    # Two entry fields (type checked)
    # Radio buttons for operators (mutually exclusive)
    # Evaluate button

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Basic Calculator')
window.geometry('400x400')


class Calculator:

    def __init__(self, master):
        # Inputs frames
        self.inputs_frame = tk.LabelFrame(master, width=200, height=200, text='Inputs')
        self.inputs_frame.place(x=10, y=10)
            # Input 1
        self.entry_1_frame = tk.Frame(self.inputs_frame, width=100, height=100)
        self.entry_1_frame.place(x=10, y=10)
        self.entry_1_var = tk.StringVar()
        self.entry_1_var.set('0')                   
        # self.entry_1_var.trace('w', self.digit_only)                                # TRACER # 
        self.entry_1_label = tk.Label(self.entry_1_frame, text='First entry')
        self.entry_1_label.place(x=10, y=10)
        self.entry_1 = tk.Entry(self.entry_1_frame, font=('Ariel',14), textvariable=self.entry_1_var, width=20)
        self.entry_1.place(x=10, y=40)
            # Input 2
        self.entry_2_frame = tk.Frame(self.inputs_frame, width=100, height=100)
        self.entry_2_frame.place(x=10, y=80)
        self.entry_2_var = tk.StringVar()
        self.entry_2_var.set('0')
        self.entry_2_label = tk.Label(self.entry_2_frame, text='Second entry')
        self.entry_2_label.place(x=10, y=10)
        self.entry_2 = tk.Entry(self.entry_2_frame, font=('Ariel',14), textvariable=self.entry_2_var, width=20)
        self.entry_2.place(x=10, y=40)
        
        # Radiobuttons
        self.rb_frame = tk.LabelFrame(master, width=100, height=200, text='Operator')
        self.rb_frame.place(x=250, y=10)
        self.radios_var = tk.StringVar()
        self.radio1 = tk.Radiobutton(self.rb_frame, text='+', value='+', variable=self.radios_var)
        self.radio1.place(x=20, y=10)
        self.radio2 = tk.Radiobutton(self.rb_frame, text='-', value='-', variable=self.radios_var)
        self.radio2.place(x=20, y=55)
        self.radio3 = tk.Radiobutton(self.rb_frame, text='*', value='*', variable=self.radios_var)
        self.radio3.place(x=20, y=100)
        self.radio4 = tk.Radiobutton(self.rb_frame, text='/', value='/', variable=self.radios_var)
        self.radio4.place(x=20, y=145)
        self.radios_var.set('+')

        # Output
        self.output_frame = tk.LabelFrame(master, width=380, height=140, text='Results')
        self.output_frame.place(x=10, y=250)
            # Readback
        self.readback_var = tk.StringVar()
        self.readback_label = tk.Label(self.output_frame, textvariable=self.readback_var, anchor='w', font=('Ariel', 14), width=25)
        self.readback_label.place(x=10, y=10)
            # Results
        self.results_var = tk.StringVar()
        self.results_label = tk.Label(self.output_frame, textvariable=self.results_var, anchor='w', font=('Ariel', 14), width=25)
        self.results_label.place(x=10, y=50)
        self.readback_var.set('Readback:')
        self.results_var.set('Results')
        
        # Calc button
        self.calc_button = tk.Button(master, text='Calculate', command=self.calc)
        self.calc_button.place(x=10, y=220)

    def calc(self):
        oper = self.radios_var.get()
        try:
            first = float(self.entry_1_var.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter digits only.')
            self.entry_1.focus()
        try:
            second = float(self.entry_2_var.get())
        except ValueError:
            messagebox.showerror('Error', 'Please enter digits only.')
            self.entry_2.focus()
        try:
            if oper == '+':
                result = first + second
            elif oper == '-':
                result = first - second
            elif oper == '*':
                result = first * second
            elif oper == '/':
                result = first / second
            self.readback_var.set(f'{first} {oper} {second} = ')
            self.results_var.set(result)
        except ZeroDivisionError:
            messagebox.showerror('Error', 'Cannot divide by Zero.')
        except UnboundLocalError:
            pass

    def digit_only(self, *args):
        last_string = ''
        string = self.entry_1_var.get()
        if string == '' or string.isdigit():
            last_string = string
        else:
            self.entry_1_var.set(last_string)
    

gui = Calculator(window)

window.mainloop()