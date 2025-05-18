from selenium import webdriver
from bs4 import BeautifulSoup

URL = "https://www.techpowerup.com/gpu-specs/"

driver = webdriver.Firefox()

driver.get(URL)

driver.quit()
