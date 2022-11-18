import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'C:\Development\chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = "https://www.python.org/"
# url_1= "https://www.amazon.in/Launched-Bassbuds-Wireless-Headphone-Playtime/dp/B0BC1WNLFT/ref=sr_1_11_sspa?crid=ZAO7OK97I72H&keywords=realme%2Bbuds&qid=1668343341&qu=eyJxc2MiOiI1LjIzIiwicXNhIjoiNC43NyIsInFzcCI6IjQuMTIifQ%3D%3D&sprefix=realme%2Bcbuds%2Caps%2C201&sr=8-11-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1"

driver.get(url)
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_time:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_names[n].text,
    }
print(events)


# driver.close()
driver.quit()
