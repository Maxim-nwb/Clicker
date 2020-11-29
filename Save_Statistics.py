import csv
from tkinter import filedialog

def save(stat):
    # getting the save path
    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Save file",filetypes=(('CSV files', '*.csv'),("TXT files","*.txt"),("All files","*.*")), defaultextension = ".txt")
    # save to .csv
    if filepath.endswith(".csv"):
        # processing data for normal saving
        stat_list = []
        for i in stat:
            stat_list.append(i.split("="))

        with open(filepath, "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=':')
            for line in stat_list:
                writer.writerow(line)
    # save to .txt
    elif filepath.endswith(".txt"):
        with open(filepath, "w", newline='') as txt_file:
            for i in stat:
                txt_file.write(i+'\n')
    else:
        with open(filepath, "w", newline='') as some_file:
            for i in stat:
                some_file.write(i+'\n')