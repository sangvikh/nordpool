from concurrent.futures import thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Country to import
country = 'NO'

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")

# Step 1: Create a session and load the page
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/NO/Hourly/?view=table')

# Wait for the page to fully load
# Ugly code. Should use webdriver to wait until everything is loaded
time.sleep(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all('table')

# Step 3: Read tables with Pandas read_html()
dfs = pd.read_html(str(tables))

# Page contains two tables, with the second being price
# If page is not completely loaded, only one table appears
if len(tables) == 2:
    print(dfs[1])
    dfs[1].to_pickle('prices.pkl')
else:
    print("ERROR loading price data")

driver.close()
