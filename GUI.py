from tkinter import *
from tkinter import messagebox
from Save_Statistics import save

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
        # display button detailed statistics
        self.stat_button = Button(self.parent, text = "Detailed statistics", command = self.onInfo)
        self.stat_button. grid(row = 3, column = 0, sticky = W)
        # attribute for saving statistics
        self.statistic = dict()
        # button for saving statistics
        self.save_stat_button = Button(self.parent, text = "Save statistics", command = self.save_file)
        self.save_stat_button. grid(row = 4, column = 0, sticky = W)
    # creating a report
    def create_report(self):
        # adding the total number of actions
        self.statistic["Total Cliks"] = self.count_cliks.cget("text")
        self.statistic["Total Keystrokes"] = self.count_keystrokes.cget("text")
        info = ""
        for i in sorted(self.statistic.keys(), key = len, reverse = True):
            info += " {0} = {1} \n".format(i, self.statistic[i])
        return info

    # show detailed information
    def onInfo(self):
        messagebox.showinfo("Detailed statistics", "{0}".format(self.create_report()))
    # save as file
    def save_file(self):
        save(self.create_report().split("\n"))