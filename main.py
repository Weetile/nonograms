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
    print("Nonogram data file = " + filename) # Debug: prints relative data file
    print("Nonogram data structure = " + str(nonogram)) # Debug: prints the actual data structure array

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
    print("hintsHorizontalMinimum = " + str(hintsHorizontalMinimum)) # For debugging/output purposes

# STRUCTURE SECTION 3:
# Algorithm below is to generate the vertical key/hints for the current puzzle

hintsVertical  = []

for i in range(len(nonogram[0])): # Iterating column
    consecutiveCount = 0 # For every column, reset consecutiveCount to 0
    columnHints = []
    for j in range(len(nonogram)): # Iterating number in column
        if nonogram[j][i] == "1":
            consecutiveCount += 1
        elif nonogram[j][i] == "0":
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
    print("hintsVerticalMinimum = " + str(hintsVerticalMinimum)) # For debugging/output purposes

# STRUCTURE SECTION 3:
# Graphical user interface in Tkinter
#from tkinter import *
#root = Tk()

# Title label widget
#title = Label(root, text="Nonogram Project for OCR Computer Science")
#title.pack()


#root.mainloop()
