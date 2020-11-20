from tkinter import *

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Cliker")
        self.parent.geometry("250x250+300+300")
        self.parent.minsize(width = 150, height = 150)
        self.parent.maxsize(width = 250, height = 250)
        title = Label(parent, text = "Actions", font="Arial 14")
        title.grid(row = 0, column = 0, columnspan = 2)
        # element that displays the count of clicks
        cliks = StringVar()
        cliks.set("0")
        count_cliks = Label(parent, textvariable = cliks)
        count_cliks.grid(row = 1, column = 1)
        label_cliks = Label(parent, text = "Cliks: ")
        label_cliks.grid(row = 1, column = 0, sticky = W)
        # element that displays the count of keystrokes
        keystrokes = StringVar()
        keystrokes.set("0")
        count_keystrokes = Label(parent, textvariable = keystrokes)
        count_keystrokes.grid(row = 2, column = 1)
        label_keystrokes = Label(parent, text = "Keystrokes: ")
        label_keystrokes.grid(row = 2, column = 0, sticky = W)