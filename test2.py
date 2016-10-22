from bs4 import BeautifulSoup

import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

f = urllib.request.urlopen("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search")

driver = webdriver.Chrome()

driver.get("http://www.google.ca")

#text_box = driver.find_element_by_css_selector('#input')
#text_box.send_keys('hello')

text_box = driver.find_element_by_id("lst-ib")
text_box.send_keys('hello')

driver.find_element_by_name("btnG").click()

#html = str(f.read())

#parser = BeautifulSoup(html, 'html.parser')

#print parser.formtarget
