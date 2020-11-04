import csv
import sys 
import os

with open('C:/Users/gajja/Desktop/winequality-red.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {', '.join(row)}")
            line_count += 1
        else:
            print(f"\t{row[0]}.")
            line_count += 1