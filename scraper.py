from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
driver.get("https://www.cbioportal.org/study/clinicalData?id=lgggbm_tcga_pub")

time.sleep(.4)

driver.quit()
page_source = driver.page_source
soup = BeautifulSoup(page_source, "lxml")

table = soup.find("table", class_ = "simple-table table table-striped table-border-top")
headers = table.find_all("th")
titles = []

for i in headers:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns=titles)
print(df)
