print("=================================================================")
print("Nonograms by Candidate 0367 for OCR A Level Computer Science 2022")
print("=================================================================")
filename = "heart.txt"
debug = True
# DATA STRUCTURE SECTION 1:
# Basic input of the nonogram text file
with open(filename) as file_in:
    nonogram = []
    for line in file_in:
        nonogram.append(line.rstrip('\n'))

if debug == True:
    print("Nonogram data structure = " + str(nonogram))

# for row in nonogram:
#     print(row) # For debugging/output purposes

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

# STRUCTURE SECTION 2:
# Algorithm below is to generate the vertical key/hints for the current puzzle

hintsVertical  = []


    

# STRUCTURE SECTION 3:
# Graphical user interface in Tkinter
#from tkinter import *
#root = Tk()

# Title label widget
#title = Label(root, text="Nonogram Project for OCR Computer Science")
#title.pack()


#root.mainloop()
