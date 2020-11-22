from tkinter import *

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.title("Cliker")
        self.parent.geometry("150x150+300+300")
        self.parent.resizable(width=False, height=False)
        self.create_widgets()
    
    def create_widgets(self):
        self.title = Label(self.parent, text = "Actions", font="Arial 14")
        self.title.grid(row = 0, column = 0, columnspan = 2)
        # element that displays the count of clicks
        self.count_cliks = Label(self.parent, text = 0)
        self.count_cliks.grid(row = 1, column = 1)
        self.label_cliks = Label(self.parent, text = "Cliks: ")
        self.label_cliks.grid(row = 1, column = 0, sticky = W)
        # element that displays the count of keystrokes
        self.count_keystrokes = Label(self.parent, text = 0)
        self.count_keystrokes.grid(row = 2, column = 1)
        self.label_keystrokes = Label(self.parent, text = "Keystrokes: ")
        self.label_keystrokes.grid(row = 2, column = 0, sticky = W)
        self.stat_button = Button(self.parent, text = "Detailed statistics")
        self.stat_button. grid(row = 3, column = 0)