from bs4 import BeautifulSoup
import requests
import pandas as pd
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.cbioportal.org/study/clinicalData?id=lgggbm_tcga_pub")

time.sleep(3)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, "lxml")

print(soup.prettify)