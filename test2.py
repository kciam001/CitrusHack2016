from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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

#select = driver.find_element_by_class_name("select2-results")
#for option in select.find_elements_by_tag_name('li'):
#    print("Text ", option.text)
#    if option.text == 'The Options I Am Looking For':
#        option.click()

#select.SelectByText("Winter 2017");
#select.Submit();

#text_box.send_keys(u'\ue007')
#drop_down = driver.find_element_by_class_name("select2-results-label")

#ActionChains(driver).move_to_element(drop_down).click(drop_down).perform()

#driver.find_element_by_class_name("select2-arrow").click()
#driver.find_element_by_class_name("form-button").click()
#html = str(f.read())

#parser = BeautifulSoup(html, 'html.parser')

#print parser.formtarget
