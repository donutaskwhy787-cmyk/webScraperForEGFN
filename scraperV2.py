from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

titles = ["type", "id"]
folder = os.path.dirname(os.path.abspath(__file__))
names = open(os.path.join(folder, "e.txt"), 'r')
id = names.readline()

df = pd.DataFrame(columns=titles)


options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
while id:
    
    driver.get("https://www.cbioportal.org/patient?sampleId=" + id +"&studyId=lgggbm_tcga_pub")

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.simple-table")))

    soup = BeautifulSoup(driver.page_source, "lxml")
    tables = soup.find_all("table", class_ = "simple-table table table-striped table-border-top")

    egfr = False
    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            data = row.find_all("td")
            vals = [tr.text for tr in data]
           
            for v in vals:
                if(v == "BGN"):
                    egfr = True
    if(egfr):
        tmp = ["amp", id]
        print("huh")
        df.loc[len(df)] = tmp
    else:
        tmp = ["normal", id]
        print("huh")
        df.loc[len(df)] = tmp
    
    id = names.readline()
driver.quit()
print(df)