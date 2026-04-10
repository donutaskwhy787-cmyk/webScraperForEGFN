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
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
titles = []
driver = webdriver.Chrome(options=options)
driver.get("https://www.cbioportal.org/patient?studyId=lgggbm_tcga_pub&caseId=TCGA-06-0125")

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.simple-table")))

page_source = driver.page_source

soup = BeautifulSoup(page_source, "lxml")

tablery = soup.find_all("table", class_ = "simple-table table table-striped table-border-top")
tabler = tablery[1]
headers = tabler.find_all("th")


for i in headers:
    title = i.text
    titles.append(title)

titles = ["type", "id"]
df = pd.DataFrame(columns=titles)
driver.quit()




#ok uhm this is the second part right here ------------------- where like we get the data and not the header
folder = os.path.dirname(os.path.abspath(__file__))
names = open(os.path.join(folder, "e.txt"), 'r')
id = names.readline()
while id:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    titles = []
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.cbioportal.org/patient?sampleId=" + id +"&studyId=lgggbm_tcga_pub")
    

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.simple-table")))

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "lxml")

    tablery = soup.find_all("table", class_ = "simple-table table table-striped table-border-top")
    print(len(tablery))
    if(len(tablery) > 1):
        tabler = tablery[0]
    else:
        tabler = tablery[0]

    rows = tabler.find_all("tr")
    for i in rows[1:]:    
        data = i.find_all("td")
        row = [tr.text for tr in data]
        row.append(id)
        for idkman in row:
            if(idkman == "EGFN"):
                bob = ["amp", id]
                df.add(bob)
        

    id = names.readline()
    driver.quit

print(df)
names.close()
