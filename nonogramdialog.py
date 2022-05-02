import tkinter as tk # Base toolkit
import os # For listing directory functionality
from tkinter import simpledialog # Simple ask dialog inputting a string
from tkinter import messagebox # To display error in case of non-existent file
from os.path import exists # To check if file exists

valid = False
root = tk.Tk()
root.withdraw()

while valid == False:
    # Below line is inputting dialog from user and storing it in a variable
    filename = simpledialog.askstring(title="Nonogram Selector", prompt="Nonograms by Candidate 0367 for OCR A Level Computer Science 2022\nProgram written in Python using the Tkinter toolkit.\n=========================================================\nPlease input the relative path to a nonogram file in the puzzles directory.\nAvaliable puzzles: " + str(os.listdir("puzzles")).translate({ord(c): None for c in '[]'}) + "\nAlternatively, type 'create' to create a new nonogram puzzle.")
    filename = filename.lower()
    if filename == "create":
        valid = True
    else:
        if filename[:8] != "puzzles/": # If the string doesn't start with 'puzzles/',
            filename = "puzzles/" + filename # Pretend as if it does
        if filename[-4:] != ".txt": # If file does not end in .txt...
            filename = filename + ".txt" # Pretend as if it does
        if exists(filename) == False: # If file exists on drive...
            messagebox.showerror(title="Error",message="File must exist.") # Message box to user
        else:
            valid = True # Break clause to escape loop/program

