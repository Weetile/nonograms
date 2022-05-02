from tkinter import *
from tkinter import messagebox
print("=================================================================")
print("Nonograms by Candidate 0367 for OCR A Level Computer Science 2022")
print("Program written in Python using the Tkinter toolkit.")
print("=================================================================")

filename = "puzzles/heart.txt" # Relative .txt file to be loaded
debug = True # NOT VISIBLE TO END USER, for development output only!

# DATA STRUCTURE SECTION 1:
# Basic input of the nonogram text file into an array

with open(filename) as file_in:
    nonogram = [] # Initialises blank nonogram 
    for line in file_in: # Iterates through each line in the file...
        nonogram.append(line.rstrip('\n')) # Calls rstrip function to remove linebreaks and /n

if debug == True:
    print("Nonogram data file = " + filename + "\n") # Debug: prints relative data file
    print("Nonogram data structure = " + str(nonogram) + "\n") # Debug: prints the actual data structure array

# Basic validation to make sure the nonogram has a minimum size of 2x2
if (len(nonogram) < 2 or len(nonogram[0]) < 2):
    messagebox.showerror("Puzzle size error","Nonogram must have a minimum size of 2x2.\nThe loaded nonogram '" + filename + "' has a size of " + str(len(nonogram[0])) + "x" + str(len(nonogram)) + ".")
    quit()

# STRUCTURE SECTION 2: 
# Algorithm below is to generate the horizontal key/hints for the current puzzle
hintsHorizontal = []

for row in nonogram: # Iterate through each row
    consecutiveCount = 0 # For every row, reset consecutiveCount to 0
    rowHints = []
    for value in row: # Iterate through each value within row
        if value == "1":
            consecutiveCount += 1 # Count is incremented per filled-in box
        elif value == "0":
            if int(consecutiveCount) > 0: # Test to see if > 0
                rowHints.append(consecutiveCount) # Count is appended...
            consecutiveCount = 0 # ...and then reset.
    if consecutiveCount > 0: # JUST IN CASE the last value of a row is a 1
        rowHints.append(consecutiveCount) # Gives it a chance to be appended
    hintsHorizontal.append(rowHints)

if debug == True:
    print("hintsHorizontal = " + str(hintsHorizontal)) # For debugging/output purposes

# Code to generate the minimum number of squares to represent the row hints
# This will be very important later for the GUI grid size
hintsHorizontalMinimum = 0
for row in hintsHorizontal:
    count = 0
    for hint in row:
        count += 1
    if count > hintsHorizontalMinimum:
        hintsHorizontalMinimum = count

if debug == True:
    print("hintsHorizontalMinimum = " + str(hintsHorizontalMinimum) + "\n") # For debugging/output purposes

# STRUCTURE SECTION 3:
# Algorithm below is to generate the vertical key/hints for the current puzzle

hintsVertical  = []

for column in range(len(nonogram[0])): # Iterating column
    consecutiveCount = 0 # For every column, reset consecutiveCount to 0
    columnHints = []
    for value in range(len(nonogram)): # Iterating number in column
        if nonogram[value][column] == "1":
            consecutiveCount += 1 # Consecutive count is incremented by one
        elif nonogram[value][column] == "0":
            if int(consecutiveCount) > 0: # Test to see if > 0
                columnHints.append(consecutiveCount) # Count is appended...
                consecutiveCount = 0 # ...and then reset.
    if consecutiveCount > 0: # JUST IN CASE the last value of a column is a 1
        columnHints.append(consecutiveCount) # Gives it a chance to be appended
    hintsVertical.append(columnHints)

if debug == True:
    print("hintsVertical = " + str(hintsVertical)) # For debugging/output purposes

# Code to generate the minimum number of squares to represent the column hints
# This will be very important later for the GUI grid size
hintsVerticalMinimum = 0
for column in hintsVertical:
    count = 0
    for hint in column:
        count += 1
    if count > hintsVerticalMinimum:
        hintsVerticalMinimum = count

if debug == True:
    print("hintsVerticalMinimum = " + str(hintsVerticalMinimum) + "\n") # For debugging/output purposes

print("=================================================================")
print("DEBUG END")
print("=================================================================")

# STRUCTURE SECTION 4:
# Graphical user interface in Tkinter

root = Tk() # Initialise Tk root
frame = Frame(root) # Base frame
frame.grid(row=0, column=0, sticky="news")

root.title('Nonograms') # Sets window title to 'Nonograms'
root.iconbitmap("@icon.xbm") # Sets very basic window icon



grid = Frame(frame) # Grid frame
grid.grid(sticky="news", column=0, row=2, columnspan=1, padx=(10,10),pady=(10,10))

puzzleText = Label(frame, text="Puzzle: " + filename)
puzzleText.grid(row=0,column=0)
#puzzleText2 = Label(frame, text=filename, font=('TkDefaultFont', 10, 'bold'))
#puzzleText2.grid(row=0,column=1,columnspan=2)

elapsedTime = Label(frame, text="Time: ")
elapsedTime.grid(row=3)

verifyButton = Button(frame,text="Verify")
verifyButton.grid(row=4,column=1,padx=(10,10),pady=(10,10))

def toggle(event): # Event to toggle BG color when button is pressed
    button = event.widget # Passing through button to subroutine
    if button.cget("bg") == "white": # If button is white...
        button.configure(text="") # ...empty text in case of mark
        button.configure(bg="black",activebackground="#0d0d0d") # ...set colour to black
    elif button.cget("bg") == "black": # If button is black...

        button.configure(bg="white",activebackground="#f0f0f0") # ... set colour to white
    else:
        pass

def mark(event): # Event to mark the cell with an X
    button = event.widget # Passing through button to subroutine
    if button.cget("bg") == "black":
        button.configure(bg="white",activebackground="#f0f0f0")
        button.configure(text="X")
    elif button.cget("bg") == "white":
        if button.cget("text") == "X":
            button.configure(text="")
        else:
            button.configure(text="X")

# This below section of code has the following purposes:
# We are iterating through horizontally the length of the nonogram puzzle + the hints.
# We are iterating through vertically the height of the nonogram puzzle + the hints.
# We are defining a button for every single cell of the nonogram puzzle and every hint.
# 

for x in range(len(nonogram[0]) + hintsHorizontalMinimum): # Iterate per row...
    for y in range(len(nonogram) + hintsVerticalMinimum): # Iterate per column...
        button = Button(grid, width="2",height="2", bg="white") # Initialise a new button...
        button.grid(column=x, row=y, sticky="news") # ...as part of grid
        if x < hintsHorizontalMinimum and y < hintsVerticalMinimum: # If the button is in the top left corner (redundant)...
            button.grid_forget() # Forget the buttons on the grid
        if x >= hintsHorizontalMinimum and y >= hintsVerticalMinimum:
            pass # Do nothing, this section of code was useful for debugging purposes
        else:
            button.configure(bg="#f0f0f0") # Set to default BG colour

        if x < hintsHorizontalMinimum: # Selecting JUST the horizontal hints...
            if (hintsHorizontalMinimum-x-1 < len(hintsHorizontal[y-hintsVerticalMinimum])): # Only applying if in range
                #button.configure(text=hintsHorizontal[y-hintsVerticalMinimum][hintsHorizontalMinimum-x-1]) # Setting the text to the correct hint
                button.configure(text=hintsHorizontal[y-hintsVerticalMinimum][x-hintsHorizontalMinimum]) # Setting the text to the correct hint
            else: # If there is no text to set,
                if (hintsHorizontalMinimum-x-1 > 0): # If it is not the only button on that row,
                    button.grid_forget() # remove the horizontal button.
                else:
                    button.configure(text="0") # Set to 0 otherwise
        if y < hintsVerticalMinimum: # Selecting JUST the vertical hints...
            if (hintsVerticalMinimum-y-1 < len(hintsVertical[x-hintsHorizontalMinimum])): # Only applying if in range
                button.configure(text=hintsVertical[x-hintsHorizontalMinimum][y-hintsVerticalMinimum]) # Setting the text to the correct hint
            else: # If there is no text to set,
                if (hintsVerticalMinimum-y-1 > 0): # If it is not the only button on that column,
                    button.grid_forget() # remove the vertical button.
                else:
                    button.configure(text="0") # Set to 0 otherwise
            
        button.bind("<Button-1>", toggle) # When the left mouse button is pressed, call the toggle function
        button.bind("<Button-3>", mark) # When the right mouse button is pressed, call the mark function

root.mainloop()
