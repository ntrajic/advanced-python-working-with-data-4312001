# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value


# TODO: The max() function finds the maximum value


# TODO: define a custom "key" function to extract a data field


# TODO: open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)

# define a custom "key" function to extract a data field
# this getmag(dataitem) will extract magnitude, and replace None with zero, and anyval with float
def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)
#


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data["metadata"]["title"])
print(len(data["features"]))               # data is table with rows "metadata",and columns "titels"

# max/min(table, key=f)-> f() is applied to extract specific title from the
# for each row there's one extracted title=magnitude, then we find min or max magitude for all rows

print(min(data["features"], key=getmag))   # key=getmag() is extracting MIN magnitued from data
print(max(data["features"], key=getmag))   # key=getmag() is extracting MAX magnitued from data
# NOTE: all other titles/columns for MIN magnitude, and MAX magnitude are printed

# OUT:
# $ python minmax.py 
# USGS All Earthquakes, Past Month
# 11745
# {'type': 'Feature', 'properties': {'mag': -1.31, 'place': '94km SE of King Salmon, Alaska', 'time': 1583824105680, 'updated': 1583950679450, 'tz': -540, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/av70876584', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/av70876584.geojson', 'felt': None, 'cdi': None, 'mmi': None, 'alert': None, 'status': 'reviewed', 'tsunami': 0, 'sig': 0, 'net': 'av', 'code': '70876584', 'ids': ',av70876584,', 'sources': ',av,', 'types': ',geoserve,origin,phase-data,', 'nst': 4, 'dmin': 0.04596, 'rms': 0.08, 'gap': 241, 'magType': 'ml', 'type': 'earthquake', 'title': 'M -1.3 - 94km SE of King Salmon, Alaska'}, 'geometry': {'type': 'Point', 'coordinates': [-155.3741667, 58.1711667, 1.55]}, 'id': 'av70876584'}
# {'type': 'Feature', 'properties': {'mag': 6.3, 'place': '298km NE of Raoul Island, New Zealand', 'time': 1584180077383, 'updated': 1584266633243, 'tz': -720, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008fl8', 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us60008fl8.geojson', 'felt': 3, 'cdi': 2.4, 'mmi': 0, 'alert': 'green', 'status': 'reviewed', 'tsunami': 1, 'sig': 611, 'net': 'us', 'code': '60008fl8', 'ids': ',us60008fl8,pt20074000,at00q76h61,', 'sources': ',us,pt,at,', 'types': ',associate,dyfi,geoserve,impact-link,losspager,moment-tensor,origin,phase-data,shakemap,', 'nst': None, 'dmin': 2.687, 'rms': 1.03, 'gap': 22, 'magType': 'mww', 'type': 'earthquake', 'title': 'M 6.3 - 298km NE of Raoul Island, New Zealand'}, 'geometry': {'type': 'Point', 'coordinates': [-175.6847, -27.4196, 10]}, 'id': 'us60008fl8'}