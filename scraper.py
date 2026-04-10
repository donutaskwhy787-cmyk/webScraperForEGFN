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
driver.get("https://www.cbioportal.org/patient?studyId=lgggbm_tcga_pub&caseId=TCGA-06-0125")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.simple-table")))

page_source = driver.page_source

soup = BeautifulSoup(page_source, "lxml")

tablery = soup.find_all("table", class_ = "simple-table table table-striped table-border-top")
tabler = tablery[1]
headers = tabler.find_all("th")
titles = []

for i in headers:
    title = i.text
    titles.append(title)

df = pd.DataFrame(columns=titles)

rows = tabler.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    df.loc[len(df)] = row
print(df)
driver.quit()
