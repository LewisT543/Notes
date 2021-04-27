                            #### TRAFFIC LIGHTS MODEL ####

# Tik tak toe... again. This time with more gui.
    # use grid() geometry manager
    # define and use callbacks
    # identifying and servicing GUI events

# pc plays x's, who are always red
# player plays O's, who are always green
# 9 tiles (buttons)
# first move:
    # PC will always play first and place an X in the middle of the board
# user choses a tile by clicking them
# check for win on every turn and display messagebox if there is a win condition met
    # PC will choose a move RANDOMLY, because no I dont want to mess about with AI right now.

import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import randrange


window = tk.Tk()
window.title('TicTacToe')
window.geometry('400x440')

class TicTacToe:
    def __init__(self, master):
        self.player_turn = tk.BooleanVar()
        self.player_turn.set(True)

        # Make the buttonframe
        self.button_frame = tk.Frame(master, width=400, height=400)
        self.button_frame.place(x=0,y=0)
        self.set_buttons()
        self.display_frame = tk.Frame(master, width=400, height=60, bg='black')
        self.display_frame.place(x=0, y=380)
        self.player_turn_label = tk.Label(self.display_frame, textvariable=str(self.player_turn.get()), bg='black', fg='white')
        self.player_turn_label.place(x=80, y=10)
        self.p_turn_plus_label = tk.Label(self.display_frame, text='Player Turn?', bg='black', fg='white')
        self.p_turn_plus_label.place(x=10, y=10)

        self.button_font = font.Font(family='Ariel', size=24)

        self.set_ox(self.board[1][1], 'X')

    def set_buttons(self):
        self.board = [[None for c in range(3)]for r in range(3)]
        for r in range(3):
            for c in range(3):
                self.button = tk.Button(self.button_frame, width=1, height=1, padx=45, pady=6, text=(''), font=('Ariel', 45))
                self.button.bind('<Button-1>', self.button_clicked)
                self.button.grid(row=r, column=c)
                self.board[r][c] = self.button

    def set_ox(self, btn, sign):
        btn["fg"] = btn["activeforeground"] = "red" if sign == 'X' else "green"
        btn["text"] = sign

    def winner(self):
            for sign in ['X', 'O']:
                for x in range(3):
                    if sign == self.board[x][0]['text'] == self.board[x][1]['text'] == self.board[x][2]['text']:
                        return sign
                    if sign == self.board[0][x]['text'] == self.board[1][x]['text'] == self.board[2][x]['text']:
                        return sign
                if sign == self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text']:
                    return sign
                if sign == self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text']:
                    return sign
            return None

    def win_message(self, sign=None):
        if sign:
            messagebox.showinfo('Game Over!', ('Player wins' if sign == 'O' else 'Computer wins'))
        else:
            messagebox.showinfo('Draw!', 'Its a Draw.\nTry again!')
        window.destroy()

    def free_cells(self):
        list = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col]['text'] == '':
                    list.append( (row, col) )
        return list

    def button_clicked(self, event):
        target = event.widget
        if target['text'] != '':    
            return
        # Player Move
        self.set_ox(target, 'O')
        if not self.winner() is None:
            self.win_message('O')
        # Cpu Move
        free_cells = self.free_cells()            
        selection = free_cells[randrange(0, len(free_cells))]
        self.set_ox(self.board[selection[0]][selection[1]], 'X')
        if not self.winner() is None:
            self.win_message('X')
        # Check for draw
        if len(self.free_cells()) == 0:
                self.win_message()

    

tiktak = TicTacToe(window)
window.mainloop()