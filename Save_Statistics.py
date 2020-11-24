import csv
from tkinter import filedialog

def save(stat):
    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("CSV files","*.csv"),("all files","*.*")))
    filepath
    with open(filepath, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='=')
        for line in stat.split("\n"):
            writer.writerow(line)