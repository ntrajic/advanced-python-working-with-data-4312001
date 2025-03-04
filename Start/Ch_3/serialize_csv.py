# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# TODO: Create the header and row structures for the data

# TODO: populate the rows with the resulting quake data

# TODO: write the results to the CSV file


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

# Create the header and row structures for the data
header = ["Place", "Magnitude", "Date", "Link"]
rows = []

# populate the rows with the resulting quake data
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"])/1000)
    rows.append([quake["properties"]["place"], quake["properties"]
                ["mag"], thedate, quake["properties"]["url"]])

# write the results to the CSV file
with open("largequakes.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)

# 
# $ python serialize_csv.py   # prerequisite is existance of largequakes.csv serialized data
# $ python deserialize.py 
# OUT:
# [{'place': '15km W of Petrolia, CA',
#   'magnitude': '5.21',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73355700'},
#  {'place': '246km S of Kangin, Indonesia',
#   'magnitude': '6.2',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008hzl'},
#  {'place': '6km NNE of Magna, Utah',
#   'magnitude': '5.7',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/uu60363602'},
#  {'place': '158km WSW of Lata, Solomon Islands',
#   'magnitude': '5.5',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008hml'},
#  {'place': '97km NNW of Sola, Vanuatu',
#   'magnitude': '6.1',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008hkg'},
#  {'place': '142km N of Tobelo, Indonesia',
#   'magnitude': '5.4',
#   'date': '2020-03-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008hkf'},
#  {'place': '172km E of Hihifo, Tonga',
#   'magnitude': '6',
#   'date': '2020-03-17',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008h76'},
#  {'place': '53km NNW of Tome, Chile',
#   'magnitude': '5.6',
#   'date': '2020-03-17',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008gzt'},
#  {'place': '195km SSE of Lata, Solomon Islands',
#   'magnitude': '5.1',
#   'date': '2020-03-15',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008g8y'},
#  {'place': "95km WNW of Bandar 'Abbas, Iran",
#   'magnitude': '5.3',
#   'date': '2020-03-15',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008g7m'},
#  {'place': '116km SW of Panenggoede, Indonesia',
#   'magnitude': '5.1',
#   'date': '2020-03-15',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008g6f'},
#  {'place': '25km SW of Villa Comaltitlan, Mexico',
#   'magnitude': '5.1',
#   'date': '2020-03-15',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008fuy'},
#  {'place': '298km NE of Raoul Island, New Zealand',
#   'magnitude': '6.3',
#   'date': '2020-03-14',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008fl8'},
#  {'place': '4km SE of Puerto Armuelles, Panama',
#   'magnitude': '5.1',
#   'date': '2020-03-13',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008euj'},
#  {'place': '86km ENE of Iquique, Chile',
#   'magnitude': '5.2',
#   'date': '2020-03-13',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008eru'},
#  {'place': '107km WSW of San Nicolas, Philippines',
#   'magnitude': '5.2',
#   'date': '2020-03-12',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008epc'},
#  {'place': '26km NNW of Nanao, Japan',
#   'magnitude': '5.3',
#   'date': '2020-03-12',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008egj'},
#  {'place': '111km SE of Neiafu, Tonga',
#   'magnitude': '5.3',
#   'date': '2020-03-12',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008e9x'},
#  {'place': '99km S of Wonosari, Indonesia',
#   'magnitude': '5.1',
#   'date': '2020-03-12',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008e67'},
#  {'place': '112km SE of Neiafu, Tonga',
#   'magnitude': '5.3',
#   'date': '2020-03-11',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008dwq'},
#  {'place': '70km S of Panguna, Papua New Guinea',
#   'magnitude': '5.3',
#   'date': '2020-03-11',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008dpf'},
#  {'place': "134km SE of L'Esperance Rock, New Zealand",
#   'magnitude': '5.3',
#   'date': '2020-03-11',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008dgf'},
#  {'place': '127km SW of Kuripan, Indonesia',
#   'magnitude': '5.5',
#   'date': '2020-03-10',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008d51'},
#  {'place': '88km NNE of San Pedro de Atacama, Chile',
#   'magnitude': '5.1',
#   'date': '2020-03-10',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008d4v'},
#  {'place': '209km NNW of Puerto Ayora, Ecuador',
#   'magnitude': '5.5',
#   'date': '2020-03-10',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008d3z'},
#  {'place': '145km ENE of Luring, China',
#   'magnitude': '5.3',
#   'date': '2020-03-09',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008clh'},
#  {'place': '156km NNE of Rumung, Micronesia',
#   'magnitude': '5.2',
#   'date': '2020-03-09',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008cdq'},
#  {'place': '69km W of Petrolia, CA',
#   'magnitude': '5.77',
#   'date': '2020-03-09',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73351710'},
#  {'place': '30km SSE of Canico, Portugal',
#   'magnitude': '5.2',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008brw'},
#  {'place': 'West Chile Rise',
#   'magnitude': '5.1',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008bmi'},
#  {'place': '294km WNW of Saumlaki, Indonesia',
#   'magnitude': '5.2',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008blz'},
#  {'place': '53km WSW of Port-Vila, Vanuatu',
#   'magnitude': '5.5',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008bj6'},
#  {'place': '71km SE of Estacion Coahuila, B.C., MX',
#   'magnitude': '5.49',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/ci38385946'},
#  {'place': '23km ESE of Buenos Aires, Costa Rica',
#   'magnitude': '5.2',
#   'date': '2020-03-07',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008bgr'},
#  {'place': 'Southwest Indian Ridge',
#   'magnitude': '5.9',
#   'date': '2020-03-06',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008ay3'},
#  {'place': 'Southern Mid-Atlantic Ridge',
#   'magnitude': '5.4',
#   'date': '2020-03-05',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008a9i'},
#  {'place': '168km ESE of Raoul Island, New Zealand',
#   'magnitude': '5.6',
#   'date': '2020-03-05',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008a7b'},
#  {'place': '161km ENE of Angoram, Papua New Guinea',
#   'magnitude': '5.2',
#   'date': '2020-03-05',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008a39'},
#  {'place': '39km S of Tinogasta, Argentina',
#   'magnitude': '5.5',
#   'date': '2020-03-05',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600089zt'},
#  {'place': '67km S of Bristol Island, South Sandwich Islands',
#   'magnitude': '5.1',
#   'date': '2020-03-04',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600089h2'},
#  {'place': '50km W of Amatignak Island, Alaska',
#   'magnitude': '5.1',
#   'date': '2020-03-03',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600088i8'},
#  {'place': '64km S of Bristol Island, South Sandwich Islands',
#   'magnitude': '5.1',
#   'date': '2020-03-02',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us6000885x'},
#  {'place': '53km WSW of Amatignak Island, Alaska',
#   'magnitude': '5.7',
#   'date': '2020-03-02',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600087lz'},
#  {'place': '5km NNE of Culasian, Philippines',
#   'magnitude': '5.3',
#   'date': '2020-03-01',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600087il'},
#  {'place': '158km N of Tobelo, Indonesia',
#   'magnitude': '5.3',
#   'date': '2020-02-29',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600086um'},
#  {'place': '135km ESE of Tadine, New Caledonia',
#   'magnitude': '5.1',
#   'date': '2020-02-29',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600086su'},
#  {'place': '103km SE of Neiafu, Tonga',
#   'magnitude': '5.3',
#   'date': '2020-02-29',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600086p0'},
#  {'place': '201km NW of Visokoi Island, South Georgia and the South Sandwich '
#            'Islands',
#   'magnitude': '5.1',
#   'date': '2020-02-28',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600086as'},
#  {'place': '43km WSW of Pagaralam, Indonesia',
#   'magnitude': '5.1',
#   'date': '2020-02-28',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us6000863e'},
#  {'place': '117km ESE of Neiafu, Tonga',
#   'magnitude': '5.7',
#   'date': '2020-02-28',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600085x5'},
#  {'place': 'Southern East Pacific Rise',
#   'magnitude': '5.4',
#   'date': '2020-02-27',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600085my'},
#  {'place': '179km S of Sarangani, Philippines',
#   'magnitude': '5.5',
#   'date': '2020-02-27',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600085g3'},
#  {'place': 'Southern Mid-Atlantic Ridge',
#   'magnitude': '5.3',
#   'date': '2020-02-27',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us6000859r'},
#  {'place': 'Southern Mid-Atlantic Ridge',
#   'magnitude': '5.1',
#   'date': '2020-02-27',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us60008535'},
#  {'place': '48km NNW of Saumlaki, Indonesia',
#   'magnitude': '5.9',
#   'date': '2020-02-26',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us600084gu'},
#  {'place': '109km WNW of Kirakira, Solomon Islands',
#   'magnitude': '5.2',
#   'date': '2020-02-25',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us6000848g'},
#  {'place': '50km NNW of Hualian, Taiwan',
#   'magnitude': '5.1',
#   'date': '2020-02-25',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007we1'},
#  {'place': '79km W of Santiago de Cao, Peru',
#   'magnitude': '5.2',
#   'date': '2020-02-25',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007w9l'},
#  {'place': '240km SE of Lambasa, Fiji',
#   'magnitude': '5.2',
#   'date': '2020-02-25',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007w8g'},
#  {'place': '83km ESE of Muara Siberut, Indonesia',
#   'magnitude': '5.2',
#   'date': '2020-02-24',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007w28'},
#  {'place': '24km SE of Saray, Turkey',
#   'magnitude': '6',
#   'date': '2020-02-23',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007v9g'},
#  {'place': "67km NE of Kuril'sk, Russia",
#   'magnitude': '5.2',
#   'date': '2020-02-23',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007v6u'},
#  {'place': '26km ESE of Saray, Turkey',
#   'magnitude': '5.8',
#   'date': '2020-02-23',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007v29'},
#  {'place': '141km SE of Modayag, Indonesia',
#   'magnitude': '5.1',
#   'date': '2020-02-23',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007v12'},
#  {'place': '135km SE of Modayag, Indonesia',
#   'magnitude': '5.3',
#   'date': '2020-02-23',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007v0d'},
#  {'place': 'West Chile Rise',
#   'magnitude': '5.5',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007uy4'},
#  {'place': '62km SSE of `Ohonua, Tonga',
#   'magnitude': '5.5',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007uvu'},
#  {'place': '40km SSE of `Ohonua, Tonga',
#   'magnitude': '5.2',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007uuu'},
#  {'place': '110km SSE of Pondaguitan, Philippines',
#   'magnitude': '5.2',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007usp'},
#  {'place': '114km SSE of Pondaguitan, Philippines',
#   'magnitude': '5.1',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007usm'},
#  {'place': '144km E of Chichi-shima, Japan',
#   'magnitude': '5.2',
#   'date': '2020-02-22',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007upz'},
#  {'place': '36km SSW of Amatignak Island, Alaska',
#   'magnitude': '5.2',
#   'date': '2020-02-21',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007u2w'},
#  {'place': '229km NW of Saumlaki, Indonesia',
#   'magnitude': '5.4',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007tt3'},
#  {'place': '153km ENE of Petropavlovsk-Kamchatskiy, Russia',
#   'magnitude': '5.8',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007trb'},
#  {'place': '286km NNE of Luring, China',
#   'magnitude': '5.1',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007tnv'},
#  {'place': '13km SE of Kalbay, Philippines',
#   'magnitude': '5.4',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007th0'},
#  {'place': 'South of the Kermadec Islands',
#   'magnitude': '5.1',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007tf0'},
#  {'place': '118km SE of Visokoi Island, South Georgia and the South Sandwich '
#            'Islands',
#   'magnitude': '5.1',
#   'date': '2020-02-20',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007tdi'},
#  {'place': '93km SSW of Merizo Village, Guam',
#   'magnitude': '5.1',
#   'date': '2020-02-19',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007t2i'},
#  {'place': 'North of Svalbard',
#   'magnitude': '5.2',
#   'date': '2020-02-18',
#   'link': 'https://earthquake.usgs.gov/earthquakes/eventpage/us70007s90'}]