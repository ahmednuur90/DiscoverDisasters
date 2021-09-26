# Reading an excel file using Python
import xlrd
import csv

# Give the location of the file
# loc = "DisasterDataSet.csv"

# To open Workbook
# wb = xlrd.open_workbook(loc, encoding_override="utf-8")
# sheet = wb.sheet_by_index(0)

# For row 0 and column 0
# print(sheet.cell_value(0, 0))

# Step 1: Make file object

f = open('DisasterDataSet.csv', encoding="utf8")

# Step 2: Make csv reader object

csv_reader_object = csv.reader(f)


# Step 3: Loop through rows

def findCountryDisasters(country):
    print("Natural Disasters in country of: "+country)
    for line in csv_reader_object:
        if line[1] == country:
            print("["+line[14]+"] location: ["+line[6]+"] year: ["+line[4]+"]")


findCountryDisasters("Canada")
