import csv
import xlwt
from tkinter import filedialog

def save(stat):
    # del void element
    stat.pop()
    # getting the save path
    filepath = filedialog.asksaveasfilename(initialdir = "/",title = "Save file",filetypes=(('CSV files', '*.csv'),("TXT files","*.txt"),("Excel files","*.xls"),("All files","*.*")), defaultextension = ".txt")
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
    # save to .xls
    elif filepath.endswith(".xls"):
        excel = xlwt.Workbook()
        sheet = excel.add_sheet("Clicker")
        for i in range(len(stat)):
            row = sheet.row(i)
            key,count = stat[i].split("=")
            row.write(0, key)
            row.write(1, count)
        excel.save(filepath)
    else:
        with open(filepath, "w", newline='') as some_file:
            for i in stat:
                some_file.write(i+'\n')