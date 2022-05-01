print("=================================================================")
print("Nonograms by Candidate 0367 for OCR A Level Computer Science 2022")
print("=================================================================")

filename = "puzzles/pixels.txt" # Relative .txt file to be loaded
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

# STRUCTURE SECTION 3:
# Graphical user interface in Tkinter
#from tkinter import *
#root = Tk()

# Title label widget
#title = Label(root, text="Nonogram Project for OCR Computer Science")
#title.pack()


#root.mainloop()

from tkinter import *

root = Tk() # Initialise Tk root
frame = Frame(root) # Base frame
frame.grid(row=0, column=0, sticky="news")

root.title('Nonograms') # Sets window title to 'Nonograms'
root.iconbitmap("@icon.xbm") # Sets very basic window icon

grid = Frame(frame) # Grid frame
grid.grid(sticky="news", column=0, row=0, columnspan=1)

def toggle(event): # Event to toggle BG color when button is pressed
    button = event.widget # Passing through button to subroutine
    if button.cget("bg") == "white": # If button is white...
        button.configure(bg="black",activebackground="black") # ...set colour to black
    elif button.cget("bg") == "black": # If button is black...
        button.configure(text="") # ...empty text in case of mark
        button.configure(bg="white",activebackground="white") # ... set colour to white
    else:
        pass

for x in range(len(nonogram[0]) + hintsHorizontalMinimum): # Iterate per row...
    for y in range(len(nonogram) + hintsVerticalMinimum): # Iterate per column...
        button = Button(frame, bg="white") # Initialise a new button...
        button.grid(column=x, row=y, sticky="news") # ...as part of grid
        if x < hintsHorizontalMinimum and y < hintsVerticalMinimum:
            button.grid_forget()
        if x >= hintsHorizontalMinimum and y >= hintsVerticalMinimum:
            pass # Do nothing
        else:
            button.configure(bg="#f0f0f0") # Set to default BG colour
        button.bind("<Button-1>", toggle)

root.mainloop()
