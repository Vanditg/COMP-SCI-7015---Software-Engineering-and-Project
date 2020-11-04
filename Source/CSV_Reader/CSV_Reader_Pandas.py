import csv 
import sys
import pandas
 
file = pandas.read_csv('C:/Users/gajja/Desktop/winequality-red.csv')
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
#pandas.set_option('display.width', 200)
print(file)

# This is upto us how we wanted to show the output in terminal/dashboard
# Thus, I need to work out with the Dashboard team as well, and 
# If we will not using Pandas then custom file has been made.