from concurrent.futures import thread
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Create a session and load the page
driver = webdriver.Chrome()
driver.get('https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/NO/Hourly/?view=table')

# Wait for the page to fully load
#WebDriverWait wait = new WebDriverWait(driver, numberOfSeconds);    
#WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'table-wrapper'), 'EUR/MWh'))
time.sleep(5)

# Step 2: Parse HTML code and grab tables with Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all('table')

# Step 3: Read tables with Pandas read_html()
dfs = pd.read_html(str(tables))

print(f'Total tables: {len(dfs)}')
print(dfs[1])

driver.close()