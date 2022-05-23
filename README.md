# Nordpool webscraper
Grabs prices from nordpool website using selenium and chrome

## Requirements
* Chrome 101.0.4951.67
* Chromedriver: https://chromedriver.chromium.org/
* Selenium
````
pip install -U selenium
````
* Beautiful soup
````
pip install beautifulsoup4
````

## How to use
* run nordpool.py to get the latest prices from nordpool. Data is saves as .json
* pickleRick.py can access the json file and read the data fields