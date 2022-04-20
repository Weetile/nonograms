from tkinter import *

root = Tk()
root.title("Nonograms")
root.geometry("324x550")
root.iconbitmap("@icon.xbm")

label = Label(root,text="This is a basic prototype of the Nonogram project.").grid(row=0, column=1, columnspan=10)
failLabel = Label(root, text="", fg="red")
failLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)
