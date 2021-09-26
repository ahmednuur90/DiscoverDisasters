# Reading an excel file using Python
import csv

# codes for convenience
COUNTRY = 1
COUNTRYCODE = 2
WARDCODE = 3
YEAR = 4
GEOID = 5
GEOLOCATION = 6
LEVEL = 7
LOCATION = 11
DISASTER = 14
DISASTERID = 15
LATITUDE = 16
LONGITUDE = 17

f = open('DisasterDataSet.csv', encoding="utf8")

# Step 2: Make csv reader object

# csv_reader_object = csv.reader(f)


# Step 3: Loop through rows

def findCountryDisasters(country):
    f = open('DisasterDataSet.csv', encoding="utf8")
    csv_reader_object = csv.reader(f)
    print("Natural Disasters in country of: " + country)
    for line in csv_reader_object:
        if line[1] == country:
            print("[" + line[14] + "] location: [" + line[6] + "] year: [" + line[4] + "]")


def findLocationDisaters(location):
    f = open('DisasterDataSet.csv', encoding="utf8")
    csv_reader_object = csv.reader(f)
    print("Natural Disasters in location of: " + location)
    for line in csv_reader_object:
        if line[6] == location:
            print("[" + line[14] + "] country: [" + line[1] + "] year: [" + line[4] + "]")


findLocationDisaters("Toronto")
print()
findCountryDisasters("Canada")
