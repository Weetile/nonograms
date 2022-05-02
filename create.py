from tkinter import * # CORE to the program, GUI toolkit
from tkinter import simpledialog # Simple ask dialog inputting a string
from tkinter import messagebox # For displaying message boxes and erorrs

horizontalSize = int(simpledialog.askstring(title="Nonogram Horizontal Size", prompt="How many tiles wide do you want your nonogram to be? Enter number."))
verticalSize = int(simpledialog.askstring(title="Nonogram Vertical Size", prompt="How many tiles tall do you want your nonogram to be? Enter number."))
    

root = Tk() # Initialise Tk root

frame = Frame(root) # Base frame
frame.grid(row=0, column=0, sticky="news")

root.title('Nonogram Creator') # Sets window title to 'Nonograms'
root.iconbitmap("@icon.xbm") # Sets basic window icon

grid = Frame(frame) # Grid frame
grid.grid(sticky="news", column=0, row=2, columnspan=1, padx=(10,10),pady=(10,10))

def toggle(event): # LEFT CLICK - Event to toggle BG color when button is pressed
    button = event.widget # Passing through button to subroutine
    if button.cget("bg") == "white": # If button is white...
        button.configure(text="") # ...empty text in case of mark
        button.configure(bg="black",activebackground="#0d0d0d") # ...set colour to black
    elif button.cget("bg") == "black": # If button is black...

        button.configure(bg="white",activebackground="#f0f0f0") # ... set colour to white
    else:
        pass

def save():
    print("Save")

saveButton = Button(frame,text="Save",command=save)
saveButton.grid(row=4,column=1,padx=(10,10),pady=(10,10))

# This below section of code has the following purposes:
# We are iterating through horizontally the length of the nonogram puzzle + the hints.
# We are iterating through vertically the height of the nonogram puzzle + the hints.
# We are defining a button for every single cell of the nonogram puzzle and every hint.
#
buttonArray = []

for x in range(horizontalSize): # Iterate per row...
    rowButtonArray = []
    for y in range(verticalSize): # Iterate per column...
        button = Button(grid, width="2",height="2", bg="white") # Initialise a new button...
        button.grid(column=x, row=y) # ...as part of grid
        button.configure(bg="white") # Set to default BG colour
            
        button.bind("<Button-1>", toggle) # When the left mouse button is pressed, call the toggle function
        buttonArray.append(rowButtonArray)

root.mainloop()
