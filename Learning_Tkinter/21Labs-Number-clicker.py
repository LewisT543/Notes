                                #### NUMBER CLICKER ####

# Write a 'less' simple game
# Timed number clicker
    # 25 buttons each containing a UNIQUE integer between 1-999
    # A timer that starts at 0, beginning to count up once we click the window in anyway
    # Player must click the numbers in order, lowest to highest
# A properly clicked button will change its state to DISBALED
# improperly clicked button show no activity (allow exception)
# timer increases every second
# when all buttons are greyed out, stop the timer 

import tkinter as tk
from tkinter import Checkbutton, messagebox
import random
import time

window = tk.Tk()
window.title('Number Clicker')
window.geometry('400x240')

class NumberClickerGame:

    def __init__(self, master):
        self.scores_list = []
        self.clock_started = False
        self.current_record = max(self.scores_list, default=0)
        # Create main canvas
        self.canvas = tk.Canvas(master, width=400, height=240)
        self.canvas.place(x=0, y=0)
        
        # Create button frame and populate with buttons
        self.button_frame = tk.Frame(self.canvas, width=400, height=200)
        self.button_frame.place(x=0, y=0)
        self.make_number_buttons()
    
        # Bottom panel frame
        self.bot_frame = tk.Frame(self.canvas, width=400, height=40, bg='black')
        self.bot_frame.place(x=0, y=200)
        self.timer_var = tk.StringVar()
        self.time_label = tk.Label(self.bot_frame, font=('Ariel', 12), textvariable=self.timer_var, bg='black', fg='white')
        self.timer_var.set('0')
        self.time_label.place(x=193, y=5)
        

    def tick(self):
        if self.clock_started:
            current_time = int(self.timer_var.get())
            current_time += 1
            self.timer_var.set(str(current_time))
            self.after_id = self.time_label.after(1000, self.tick)

    def make_number_buttons(self):
        # Create the random numbers, assuring for unique assignment, filling num_list with our numbers
        self.num_list = []
        while len(self.num_list) < 25:
            number = random.randint(1, 999)
            if number not in self.num_list:
                self.num_list.append(number)
        
        # Creating the buttons for each number            
        i = 0
        for r in range(5):
            for c in range(5):
                value = str(self.num_list[i])
                my_button = tk.Button(
                    self.button_frame, 
                    text=value, 
                    width=10, height=2
                )
                my_button.grid(row=r, column=c)
                i += 1
                my_button.bind('<Button-1>', self.check_button)

        # Sort list
        self.num_list.sort()

    def check_button(self, event):
        if not self.clock_started:
            self.clock_started = True
            self.time_label.after(1000, self.tick)
        clicked_button = event.widget
        value = int(clicked_button['text'])

        if value == self.num_list[-1]:
            clicked_button['state'] = 'disabled'
            del self.num_list[-1]

        if len(self.num_list) == 0:
            self.clock_started = False
            self.time_label.after_cancel(self.after_id)
            self.timer_stopped_label = tk.Label(self.bot_frame, text='Timer Stopped.', bg='black', fg='white')
            self.timer_stopped_label.place(x=240, y=5)
            self.reset_button = tk.Button(self.bot_frame, text='Reset', command=self.reset)
            self.reset_button.place(x=350, y=5)

    def reset(self):
        self.reset_button.destroy()
        self.timer_stopped_label.destroy()
        self.scores_list.append(self.timer_var.get())
        self.timer_var.set('0')
        return self.make_number_buttons()
        

clicker = NumberClickerGame(window)
window.mainloop()