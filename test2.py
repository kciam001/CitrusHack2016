from bs4 import BeautifulSoup

import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = urllib.request.urlopen("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

driver = webdriver.Chrome()

driver.get("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
driver.find_element_by_id("classSearchLink").click()
driver.find_element_by_class_name("select2-arrow").click()

text_box = driver.find_element_by_class_name("select2-input")
text_box.send_keys('Winter 2017')

#html = str(f.read())

#parser = BeautifulSoup(html, 'html.parser')

#print parser.formtarget
