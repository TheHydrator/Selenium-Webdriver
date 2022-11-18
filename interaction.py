import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# global driver

s = Service(r'C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)

url =("https://secure-retreat-92358.herokuapp.com/")
driver.get(url)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "MediaWiki")
# all_portals.click()
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("abba")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("abba")
email = driver.find_element(By.NAME, "email")
email.send_keys("abbadabba@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Apple")
# search.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()