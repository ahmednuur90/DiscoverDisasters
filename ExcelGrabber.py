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


def findMostCommonDisasterForLocation(location):
    print()


def findMostCommonDisasterForCountry(country):
    disasterList = []  # keep track of unique disasters
    disasterCountList = []  # keep track of disaster counts
    f = open('DisasterDataSet.csv', encoding="utf8")
    csv_reader_object = csv.reader(f)
    # print("Natural Disasters in country of: " + country)
    for line in csv_reader_object:  # go through rows in csv
        if line[1] == country:
            found = False  # variable to track if disaster is found in disasterList
            for i in range(len(disasterList)):
                if line[DISASTER] == disasterList[i]:  # if disaster from csv is found in disaster list, increment count
                    disasterCountList[i] += 1
                    found = True
            if not found:  # if not found, add to list
                disasterList.append(line[DISASTER])
                disasterCountList.append(1)
    # finding most common disaster
    max = 0
    for count in disasterCountList:  # finding the most common disaster
        if max < count:
            max = count
    print(max)
    return disasterList[disasterCountList.index(max)]


#findLocationDisaters("Toronto")
print()
#findCountryDisasters("Canada")
print("Test: "+findMostCommonDisasterForCountry("Canada"))
print("Test: "+findMostCommonDisasterForCountry("Japan"))
print("Test: "+findMostCommonDisasterForCountry("Iraq"))
print("Test: "+findMostCommonDisasterForCountry("Afghanistan"))
print("Test: "+findMostCommonDisasterForCountry("Poland"))

findCountryDisasters("Mexico")