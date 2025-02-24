# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each
if __name__ == "__main__":
    ...
    # open the data file and load the JSON
    with open("../../30DayQuakes.json", "r", encoding="utf-8") as datafile:
        data = json.load(datafile)
    print(f"data: {data['metadata']}")
    # OUT: 
    # data: {'generated': 1584583554000, 'url': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson', 'title': 'USGS All Earthquakes, Past Month', 'status': 200, 'api': '1.8.1', 'count': 11745}

    # 1: How many quakes are there in total?
    # 1: We can just use the provided data, or we can use len() to get the length of the "features"
    print(f"Total quakes: {data['metadata']['count']}")  # Total quakes: 11745

    #2: How many quakes were felt by at least 100 people?
    # 2: This is a straightforward filtering process
    def feltreport(q):
        f = q["properties"]["felt"]
        return (f is not None and f >= 100)
    # class filter(
    # function: (_T@filter) -> Any,
    # iterable: Iterable[_T@filter],
    #     /
    # )        
    #        feltreport,       data
    # filter(function or None, iterable) --> filter object,   list(filter_object) : List[]
    #
    # Return an iterator yielding those items of iterable for which function(item)
    # is true. If function is None, return the items that are true.
    feltreports = list(filter(feltreport, data["features"]))
    print(f"Total quakes felt by at least 100 people: {len(feltreports)}") #OUT: Total quakes felt by at least 100 people: 28

    # 3: Print the name of the place whose quake was felt by the most people, with the # of reports
    # 3: We can use the max function here to find the maximum # of felt reports
    def getfelt(q):
        f = q["properties"]["felt"]
        if f is not None:
            return f
        return 0
    #

    mostfeltquake = max(data["features"], key=getfelt)
    print(
        f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")
        # Most felt reports: M 5.7 - 6km NNE of Magna, Utah, reports: 33091

    #4:
    sigevents = sorted(data["features"], key=getsig, reverse=True)
    print("The 10 most significant events were:")
    for i in range(0, 10):
        print(
            f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}")