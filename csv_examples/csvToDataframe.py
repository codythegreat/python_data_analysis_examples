# csvExamples.py - opens and reads a csv file's contents
#                  creates a pandas DataFrame from data
#                  and prints cars in order of horsepower

import csv
import numpy as np
import pandas as pd

csvFile = open("MOCK_DATA.csv")
readCSV = csv.reader(csvFile, delimiter=",")

# use a pandas DataFrame to store the data
# we don't need the id when creating the dataframe
# so we'll just use 5 lists
rawData = [[],[],[],[],[]]
for row in readCSV:
    rawData[0].append(row[1]) 
    rawData[1].append(row[2]) 
    rawData[2].append(row[3]) 
    rawData[3].append(row[4]) 
    rawData[4].append(row[5]) 

carDataDict = {
    rawData[0][0]: rawData[0][1:],
    rawData[1][0]: rawData[1][1:],
    rawData[2][0]: rawData[2][1:],
    rawData[3][0]: rawData[3][1:],
    rawData[4][0]: rawData[4][1:]
}

carDF = pd.DataFrame(carDataDict)
# print the entire dataframe by horsepower ascending
# .to_string() is used to print entire table
print(carDF.sort_values("horsepower").to_string()) 