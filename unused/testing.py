# grid_layout.py
import tkinter as tk
import random

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Nonogram Project')
        self.geometry('400x400')
        self.iconbitmap("@icon.xbm")

        self.frame = tk.Frame()
        self.frame.pack(expand=True)


        self.button = [None] * 25
        for i in range(25):
            r, c = divmod(i, 5)
            self.button[i] = tk.Button(self.frame, text=' ', font='TkFixedFont',
                                       command=lambda n=i: self.button_click(n))
            self.button[i].grid(row=r, column=c)

    def button_click(self, n):
        choice = random.randrange(2)
        character, color = (('x', 'red'), ('o', 'green'))[choice]
        self.button[n]['text'] = character
        self.button[n]['fg'] = color

if __name__ == '__main__':
    root = Root()
    root.mainloop()
