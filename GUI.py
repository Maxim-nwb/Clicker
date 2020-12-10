from tkinter import *
from tkinter import messagebox
from Save_Statistics import save
from Tray import Tray

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent["bg"] = "#87CEEB"
        self.parent.title("Cliker") 
        self.parent.geometry("225x150+300+300")
        self.parent.resizable(width=False, height=False)
        self.parent.iconbitmap('tap.ico')
        self.parent.protocol('WM_DELETE_WINDOW', self.close_app)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self.parent, text = "Actions", font="Arial 16", bg = "#87CEEB")
        self.title.grid(row = 0, column = 0, columnspan = 4)
        # element that displays the count of clicks
        self.count_cliks = Label(self.parent, text = 0, bg = "#87CEEB", width = 3)
        self.count_cliks.grid(row = 1, column = 1, sticky = W)
        self.label_cliks = Label(self.parent, text = "Cliks: ", font="Arial 12", bg = "#87CEEB")
        self.label_cliks.grid(row = 1, column = 0, sticky = W)

        # element that displays the count of keystrokes
        self.count_keystrokes = Label(self.parent, text = 0, bg = "#87CEEB", width = 3)
        self.count_keystrokes.grid(row = 2, column = 1, sticky = W)
        self.label_keystrokes = Label(self.parent, text = "Keystrokes: ", font="Arial 12", bg = "#87CEEB")
        self.label_keystrokes.grid(row = 2, column = 0, sticky = W)
        # display button detailed statistics
        self.stat_button = Button(self.parent, text = "Detailed statistics", command = self.onInfo, bg = "#E0FFFF")
        self.stat_button. grid(row = 3, column = 0, sticky = W)
        # attribute for saving statistics
        self.statistic = dict()
        # button for saving statistics
        self.save_stat_button = Button(self.parent, text = "Save statistics", command = self.save_file, bg = "#E0FFFF")
        self.save_stat_button. grid(row = 4, column = 0, sticky = W)
        # button for mininmize to tray
        self.save_stat_button = Button(self.parent, text = "Minimize to tray", command = self.minimize_tray, bg = "#E0FFFF")
        self.save_stat_button. grid(row = 3, column = 2, sticky = W)
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
        # handling a save error
        try:
            save(self.create_report().split("\n"))
        except FileNotFoundError:
            pass
    # minimize to tray
    def minimize_tray(self):
        # hiding the main window
        self.parent.withdraw()
        START = True
        while START:
            # start tray
            tray = Tray()
            tray.run()
            # calling save from a tray
            if tray._status == "SAVE":
                self.save_file()
            # close tray
            if tray._status == "STOP":
                START = False
        # return main window
        self.parent.deiconify()
    # ask about saving when exit
    def close_app(self):
        save_ansver = messagebox.askyesno("Save data", "Save detailed statistics?")
        if save_ansver:
            self.save_file()
        self.parent.destroy()

