# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a JSON file

import json
import datetime
import csv

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# 1 sort significant events
# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD


def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig


significantevents = sorted(data["features"], key=getsig, reverse=True)
significantevents = significantevents[:40]
significantevents.sort(key=lambda e: e["properties"]["time"], reverse=True)

header = ["Magnitude", "Place", "Felt Reports", "Date", "Link"]
rows = []

for event in significantevents:
    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([event["properties"]["mag"],
                event["properties"]["place"],
                0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                thedate,
                gmaplink])

with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)
print("file significantevents.csv created on HD.")
# ----------------------------------

def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6


# define a function to transform complex JSON to simpler JSON
def simplequake(q):
    return {
        "place": q["properties"]["place"],
        "mag":  q["properties"]["mag"],
        "link":  q["properties"]["url"],
        "date": str(datetime.date.fromtimestamp(
            int(q["properties"]["time"])/1000))
    }


# filter the data to only include large quakes
largequakes = list(filter(isbig, data["features"]))
# transform the data to a JSON format we want to save
largequakes = list(map(simplequake, largequakes))

# use the dumps() function to write json to a string
str = json.dumps(largequakes, sort_keys=True, indent=4)
print(str)

# use the dump() function to write json to a file
with open("largequakes.json", "w", encoding="utf-8") as outfile:
    json.dump(largequakes, outfile, sort_keys=True, indent=4)
