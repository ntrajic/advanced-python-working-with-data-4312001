# Example file for Advanced Python: Working With Data by Joe Marini
# sorting data with the sorted() and sort() functions

import json


numbers = [42, 54, 19, 17, 23, 31, 16, 4]
names = ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "Stacy"]

# TODO: the sorted() function can be used to return a new list with sorted data
sorted_numbers = sorted(numbers); print(f"sorted copy, sorted_numbers: {sorted_numbers}")
sorted_names   = sorted(names);   print(f"sorted copy, sorted_names: {sorted_names}")


# TODO: alternately, you can use the list object's sort() method, which sorts the list in-place
numbers.sort(); print(f"in-place, numbers are sorted ASC: {numbers}")
names.sort();   print(f"in-place, names are sorted ASC: {names}")
names.sort(reverse=True);   print(f"in-place, names are sorted DISC: {names}")

# TODO: To sort custom objects, we can tell the sort function which property to use
# by specifying a key function

# open the data file and load the JSON
# with open("../../30DayQuakes.json", "r") as datafile:
#     data = json.load(datafile)


# def getmag(dataitem):
#     magnitude = dataitem["properties"]["mag"]
#     if (magnitude is None):
#         magnitude = 0
#     return float(magnitude)


# ------------------------------------------------------------------------------
# To sort custom objects, we can tell the sort function which property to use
# by specifying a key function, for e.g. getmag()
# ----------------------------------------------------------------------------

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)


data['features'].sort(key=getmag, reverse=True)   # sort by column/title == "mag" (magnitude)
for i in range(0, 10):
    print(data['features'][i]['properties']['place'])
#

# OUT:
#  python sorting.py 
# sorted copy, sorted_numbers: [4, 16, 17, 19, 23, 31, 42, 54]
# sorted copy, sorted_names: ['Addie', 'Bill', 'Jeff', 'Joe', 'Lukas', 'Stacy', 'Stephanie', 'Zach']
# in-place, numbers are sorted ASC: [4, 16, 17, 19, 23, 31, 42, 54]
# in-place, names are sorted ASC: ['Addie', 'Bill', 'Jeff', 'Joe', 'Lukas', 'Stacy', 'Stephanie', 'Zach']
# in-place, names are sorted DISC: ['Zach', 'Stephanie', 'Stacy', 'Lukas', 'Joe', 'Jeff', 'Bill', 'Addie']
# 298km NE of Raoul Island, New Zealand
# 246km S of Kangin, Indonesia
# 97km NNW of Sola, Vanuatu
# 172km E of Hihifo, Tonga
# 24km SE of Saray, Turkey
# Southwest Indian Ridge
# 48km NNW of Saumlaki, Indonesia
# 26km ESE of Saray, Turkey
# 153km ENE of Petropavlovsk-Kamchatskiy, Russia
# 69km W of Petrolia, CA