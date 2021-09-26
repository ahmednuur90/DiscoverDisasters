# Reading an excel file using Python
import csv
import eel


eel.init('web')
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
csv_reader_object = csv.reader(f)


# Step 2: Make csv reader object

# csv_reader_object = csv.reader(f)


# Step 3: Loop through rows

@eel.expose
def findCountryDisasters(country):
    # f = open('DisasterDataSet.csv', encoding="utf8")
    f.seek(0)
    # print("Natural Disasters in country of: " + country)
    disasters = []
    for line in csv_reader_object:
        if line[COUNTRY] == country:
            disasters.append(line[DISASTER] + "," + line[LOCATION] + "," + line[YEAR])
            # print("[" + line[DISASTER] + "] location: [" + line[GEOLOCATION] + "] year: [" + line[YEAR] + "]")
    return disasters


@eel.expose
def findLatestCountryDisaster(country):
    f.seek(0)
    print("Natural Disasters in country of: " + country)
    for line in csv_reader_object:
        if line[COUNTRY] == country:
            # print("[" + line[DISASTER] + "] location: [" + line[GEOLOCATION] + "] year: [" + line[YEAR] + "]")
            return line[DISASTER] + "," + line[LOCATION] + "," + line[YEAR]
    return "No disaster found for specified country"


@eel.expose
def findLocationDisaters(location):
    f.seek(0)
    print("Natural Disasters in location of: " + location)
    for line in csv_reader_object:
        disasters = []
        if line[LOCATION] == location:
            disasters.append(line[DISASTER] + "," + line[LOCATION] + "," + line[YEAR])
            # print("[" + line[DISASTER] + "] country: [" + line[GEOLOCATION] + "] year: [" + line[YEAR] + "]")
    return disasters


@eel.expose
def findLatestLocationDisaster(location):
    f.seek(0)
    print("Natural Disasters in location of: " + location)
    for line in csv_reader_object:
        if line[LOCATION] == location:
            # print("[" + line[DISASTER] + "] location: [" + line[GEOLOCATION] + "] year: [" + line[YEAR] + "]")
            return line[DISASTER] + "," + line[COUNTRY] + "," + line[YEAR]
    return "No disaster found for specified location"


@eel.expose
def findMostCommonDisasterForLocation(location):
    disasterList = []  # keep track of unique disasters
    disasterCountList = []  # keep track of disaster counts
    f.seek(0)
    # print("Natural Disasters in country of: " + country)
    for line in csv_reader_object:  # go through rows in csv
        if line[LOCATION] == location:
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
    # print(max)
    if max == 0:
        return "No disaster found for specified location"
    return disasterList[disasterCountList.index(max)] + "," + str(max)


@eel.expose
def findMostCommonDisasterForCountry(country):
    disasterList = []  # keep track of unique disasters
    disasterCountList = []  # keep track of disaster counts
    f.seek(0)
    # print("Natural Disasters in country of: " + country)
    for line in csv_reader_object:  # go through rows in csv
        if line[COUNTRY] == country:
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
    # print(max)
    if max == 0:
        return "No disaster found for specified country"
    return disasterList[disasterCountList.index(max)] + "," + str(max)


eel.start('index.html')

# findLocationDisaters("Toronto")
print()
print(findCountryDisasters("Canada"))
print("Test: " + findMostCommonDisasterForCountry("Canada"))
print("Test: " + findMostCommonDisasterForCountry("Japan"))
print("Test: " + findMostCommonDisasterForCountry("Iraq"))
print("Test: " + findMostCommonDisasterForCountry("Afghanistan"))
print("Test: " + findMostCommonDisasterForCountry("Poland"))
print("Test Toronto: " + findMostCommonDisasterForLocation("Toronto"))

print(findLatestCountryDisaster("Canada"))
print(findLatestLocationDisaster("Toronto"))

print(findLatestCountryDisaster("cndeiucvn"))
print(findLatestLocationDisaster("cndeiucvn"))
print(findCountryDisasters("cndeiucvn"))
print(findLocationDisaters("cndeiucvn"))
print(findMostCommonDisasterForLocation("fbfvbd"))
print(findMostCommonDisasterForCountry("fbfvbd"))
