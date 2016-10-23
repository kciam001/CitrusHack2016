from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import sys 
import urllib.request


#set/ask for class variables
className = "MATH"
classNumber = "009C"
#whichQuarter = ...

#initialize driver
driver = webdriver.Chrome()

#goto website and navigate to textbox
driver.get("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
driver.find_element_by_id("classSearchLink").click()
driver.find_element_by_class_name("select2-arrow").click()

#enter quarter
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
    print ("Timed out waiting for page to load")

driver.find_element_by_id("s2id_txt_subjectcoursecombo").click()

try:
    element_present = EC.presence_of_element_located((By.ID, "s2id_txt_subjectcoursecombo"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print ("Timed out waiting for page to load")


text_box = driver.find_element_by_xpath("//*[@id='s2id_txt_subjectcoursecombo']/ul")
ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(className + classNumber).perform()

time.sleep(1)
text_box = driver.find_element_by_xpath("//*[@id='s2id_txt_subjectcoursecombo']/ul")
ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.TAB).perform()

time.sleep(1)

driver.find_element_by_id("chk_open_only").click()
driver.find_element_by_id("search-go").click()
time.sleep(1)


#find out how many classes are found
numClassesFound = driver.find_element_by_xpath("//*[@id='results-terms']/div/h3/span/span").text

#check if number of classes is one or two digits
#if the class is single digit
if(numClassesFound[1] == ' '):
    numClassesFound = int(numClassesFound[0])
#else the class is 2 digits    
else:
    numClassesFound = numClassesFound[0] + numClassesFound[1]

#cast to integer
numClassesFound = int(numClassesFound)
#calculate number of pages
numPages = int(numClassesFound / 10) + 1




#for loop that finds all class information on each page and prints it to console
i = 1 #helper that identifies class type (LEC, LAB, DISC)
j = 0 #counter

#iterates a total of how many classes there are
for _ in range(numClassesFound):
    #if this is the first class of the page  
    if(j % 10 == 0): 
        #click on section details
        driver.find_element_by_class_name("section-details-link").click()  
        time.sleep(1)
        #click on enrollment info
        driver.find_element_by_id("enrollmentInfo").click() 
        time.sleep(1)
        
    #convert '1' to string '1'
    i = str(i) 
    
    #extract info of one class using xpath
    for element in driver.find_elements_by_xpath("//*[@id='classDetailsContentDetailsDiv']"):
        print(element.text)
        
    #extract class type   
    xpath = "//*[@id='table1']/tbody/tr["+ i +"]/td[6]/span"
    print(driver.find_element_by_xpath(xpath).text)
    
    print('\n') #newline for neatness

    #iterations
    i = int(i)+ 1 
    j = j + 1

    #if this is the last class of the page then go to next page
    if(j % 10 == 0 and numPages > 0):
        time.sleep(1)
        ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()
        i = 1 #resets i


#final exit of the windows
time.sleep(1)
ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()













#driver.find_element_by_xpath("/html/body/div[45]/div[1]/a").click()


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
