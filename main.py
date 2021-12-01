import os
import selenium
from selenium import webdriver

import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

#driver = webdriver.Chrome('/home/user/Web_scrapping/chromedriver')

search_url="https://mausam.imd.gov.in/thiruvananthapuram/"

i=0
service = []
drivers = []
# No of Instances.
while i < 2:
    service.append(Service(ChromeDriverManager().install()))
    drivers.append(webdriver.Chrome(service=service[i]))
    drivers[i].maximize_window()
    drivers[i].get(search_url)
    drivers[i].find_element_by_link_text('DATA SUPPLY').click()
    i+=1


# s=Service(ChromeDriverManager().install())
# d=Service(ChromeDriverManager().install())
#
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver2 = webdriver.Chrome(service=d)
# driver2.maximize_window()



# driver.get(search_url)
# driver2.get(search_url)



#Scroll to the end of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)

# elem = driver.find_element_by_link_text('DATA SUPPLY').click()
# elem2 = driver2.find_element_by_link_text('DATA SUPPLY').click()

# elem.send_keys("selenium test")
# time.sleep(5)
# driver.find_element_by_id("search_button").click()
time.sleep(5)





