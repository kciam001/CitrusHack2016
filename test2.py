from bs4 import BeautifulSoup

import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#f = urllib.request.urlopen("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

driver = webdriver.Chrome()

driver.get("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

year = input("What year do you want to search a class for?\n")

quarter = input("What quarter do you want to search a class for?\n")

quarter = quarter.capitalize()

search_id = quarter + ' ' + year

driver.find_element_by_class_name("select2-arrow").click()

print(search_id)

##driver.find_element_by_id("select2-result-label-2").click()

##text_box = driver.find_element_by_class_name("select2-search")
##text_box.send_keys(search_id)

#driver.find_element_by_name("btnG").click()

#html = str(f.read())

#parser = BeautifulSoup(html, 'html.parser')

#print parser.formtarget
