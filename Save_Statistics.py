import csv
from tkinter import filedialog

def save(stat):
    # processing data for normal saving
    stat_list = []
    for i in stat:
        stat_list.append(i.split("="))
    # getting the save path
    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Save file",filetypes=[('CSV files', '*.csv')])
    # check .csv.csv
    if not filepath.endswith(".csv"):
        filepath +=".csv"
    # save
    with open(filepath, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=':')
        for line in stat_list:
            writer.writerow(line)