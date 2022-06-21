from urllib.request import urlopen
import datefinder
from datetime import datetime
import jsonpath_ng

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://data.norges-bank.no/api/data/EXR/B.EUR.NOK.SP?format=sdmx-json&lastNObservations=1&locale=en"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
json_data = json.loads(response.read())

# print the json response
#print(json_data)

# Latest EURNOK price
eurnok = list(json_data["data"]["dataSets"][0]["series"]["0:0:0:0"]["observations"].values())[-1]
# Convert to float
eurnok = float(eurnok[0])
print(eurnok)

# Get date of latest entry
def gettime(data, index):
    data = data.split(",")
    return data[index*4]

# Read date from json strucure
# Values are not working correctly, cannot access "start" time etc.
date = json_data["data"]["structure"]["dimensions"]["observation"]
date = date[-1]["values"]
date = str(date)

#date = date.split(",")
#print(len(date))
#print(date)

# Use datefinder to find last date in string
date = list(datefinder.find_dates(date))
print(date[-1])
print("\n\n\n")

#print(json_data["data"]["structure"]["dimensions"]["observation"][0].values())
jsonpath_expr = jsonpath_ng.parse('data.structure.dimensions.observation[0].values[0].start')
val = [match.value for match in jsonpath_expr.find(json_data)]
print(val)