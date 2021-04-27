                                #### CATCH ME IF YOU CAN ####

# Write a simple game
    # User vs Tkinter
    # 500x500 window
    # Create 'Catch me' button
    # Button moves on mouseover
        # must be far enough away that the user is not able to click the button
        # cannot cross window boundries on jump
    # use place() to move the button, user bind() to assign callbacks.

import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title('Catch Me If You Can')
window.geometry('500x500')

class CatchMeGame:

    def __init__(self, master):

        self.canvas=tk.Canvas(master, width=500, height=500)
        self.canvas.place(x=0, y=0)
        self.snitch_button = tk.Button(self.canvas, text='Catch Me!', font=('Ariel', 12), command=self.assignment_fail)#, command=move_away
        self.snitch_button.bind('<Enter>', self.move_away)
        self.snitch_button.place(x=10, y=10)

    def move_away(self, master):
        
        def get_randoms():
            x_coord = random.randint(1, 420)
            y_coord = random.randint(1, 420)
            return (x_coord, y_coord)

        # Find middle of button and draw a circle round it.    
        button_mid_loc = (self.snitch_button.winfo_x() + 40, self.snitch_button.winfo_y() + 12)
        x0, x1, y0, y1 = (button_mid_loc[0] - 50), (button_mid_loc[1] - 50), (button_mid_loc[0] + 50), (button_mid_loc[1] + 50) 
        self.canvas.create_oval(x0, x1, y0, y1, outline='', tags='ovals')
        
        # Assign new coords, but make sure the distance from previous is larger than 50
        rands = get_randoms()
        while abs(rands[0] - button_mid_loc[0]) < 50 or abs(rands[1] - button_mid_loc[1]) < 50:
            # If it is larger than 50, we just go again until it isnt
            rands = get_randoms() 

        # Move the button and clear the canvas of ovals
        self.snitch_button.place(x=rands[0], y=rands[1])
        self.canvas.delete('ovals')
        

    def assignment_fail(self):
        messagebox.showerror('Error', 'You caught me!\nMission failed, back to the drawing board.')

gme = CatchMeGame(window)
window.mainloop()