from urllib.request import urlopen
import datefinder
from datetime import datetime

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://data.norges-bank.no/api/data/EXR/B.EUR.NOK.SP?format=sdmx-json&lastNObservations=1&locale=en"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
#print(data_json)

# Latest EURNOK price
eurnok = list(data_json["data"]["dataSets"][0]["series"]["0:0:0:0"]["observations"].values())[-1]
# Convert to float
eurnok = float(eurnok[0])
print(eurnok)

# Get date of latest entry
date = data_json["data"]["structure"]["dimensions"]["observation"]
date = date[-1]["values"]
date = str(date)

# Use datefinder to find last date in string
date = list(datefinder.find_dates(date))
print(len)
print(date[-1])