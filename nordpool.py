# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Load pandas for parsing the data
import pandas as pd

# Establish chrome driver and go to report site URL
url = "https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/NO/Hourly/?view=table"
driver = webdriver.Chrome()
driver.get(url)

# Find the javascript table in the page
test = driver.find_element(by = By.CLASS_NAME, value = 'table-wrapper')
print(test)

#tmp = input("Scraping finished, press any key to quit...")
driver.close()