from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time

import urllib.request

className = "MATH"
classNumber = "146B"

driver = webdriver.Chrome()

driver.get("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
driver.find_element_by_id("classSearchLink").click()
driver.find_element_by_class_name("select2-arrow").click()

text_box = driver.find_element_by_class_name("select2-input")
text_box.send_keys('Winter 2017')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='201710']"))
                                   )
elementList = text_box.find_elements_by_xpath("//*[@id='201710']")

if len(elementList) is 0:
    print("elementList is empty")
    
for i in elementList:
    i.click()
    break
    #if att is not "":
        #print(att)

timeout = 5 # seconds

try:
    element_present = EC.presence_of_element_located((By.ID, "term-go"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print ("Timed out waiting for page to load(1)")



driver.find_element_by_id("term-go").click()

try:
    element_present = EC.presence_of_element_located((By.ID, "term-go"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print ("Timed out waiting for page to load(2)")

driver.find_element_by_id("s2id_txt_subjectcoursecombo").click()

try:
    element_present = EC.presence_of_element_located((By.ID, "s2id_txt_subjectcoursecombo"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print ("Timed out waiting for page to load(3)")

text_box = driver.find_element_by_xpath("//*[@id='s2id_txt_subjectcoursecombo']/ul")
ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(className + classNumber).perform()



time.sleep(1)
text_box = driver.find_element_by_xpath("//*[@id='s2id_txt_subjectcoursecombo']/ul")
ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.TAB).perform()

driver.find_element_by_id("chk_open_only").click()
driver.find_element_by_id("search-go").click()
time.sleep(1)

driver.find_element_by_class_name("section-details-link").click()
time.sleep(1)
driver.find_element_by_id("enrollmentInfo").click()




for elem in driver.find_elements_by_xpath("//*[@id='classDetailsContentDetailsDiv']"):
    print (elem.text)


print(driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[6]/span").text)

    

#ActionChains(driver).move_to_element_with_offset(text_box,0,0).click().perform()




#text_box.send_keys('CS 100')

#print("Expolozo: ", uL.get_attribute('name'))


#text_box.send_keys(Keys.ENTER)

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
