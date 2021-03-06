import tkinter as tk #For GUI stuff
from tkinter import *
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
import sys

from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

def initiate():
    global sched
    sched.add_job(executeFunc, id = 'job_0')
    sched.add_job(executeFunc, trigger='interval', minutes=30, id = 'job_1', max_instances=3)
    sched.start()

def executeFunc():
    #set/ask for class variables
    className = textBox1.get()
    classNumber = textBox2.get()
    quarterYear= textBox5.get() + ' ' + textBox6.get()
    callNumber = textBox3.get()
    if len(callNumber) is 0:
        callNumber = -1
    callNumber = int(callNumber)
    infoTotal = ""

    fromaddr = "expolozo2016@gmail.com"
    toaddr = textBox4.get()
    password = "EMAILMAILINGSERVICEFORSCHEDULEOFCLASSES123"
    
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Automated Email: {}".format(className + classNumber)

    body = "Do not reply to this email. This is an automated email. @Expolozo"
    msg.attach(MIMEText(body, 'plain'))
    
    #initialize callNumber to -1
    #only set callNumber when user wants to enter it
    #callNumber = 41651
    #whichQuarterYear = ...

    #initialize driver
    driver = webdriver.Chrome()
   ## driver.set_window_position(-2000, 0)

    #goto website and navigate to textbox
    driver.get("https://registrationssb.ucr.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
    driver.find_element_by_id("classSearchLink").click()
    driver.find_element_by_class_name("select2-arrow").click()

    #make file to read
    file = open('emailText.txt', 'w')

    #after file is created save its cwd
    filename = 'emailText.txt'
    attachment = open(os.getcwd() + "\\emailText.txt", "rb")
    
    #enter quarter
    text_box = driver.find_element_by_class_name("select2-input")
    text_box.send_keys(quarterYear)

    quarter = textBox5.get()
    quarter = quarter.capitalize()

    if(quarter == "Winter"):
        num_id = textBox6.get() + "10"
    elif(quarter == "Spring"):
        num_id = textBox6.get() + "20"
    elif(quarter == "Summer"):
        num_id = textBox6.get() + "30"
    else:
        num_id = textBox6.get() + "40"


    xpathID = "//*[@id='" + num_id + "']"
    #the infamous button clicking problem (idk how this code works)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpathID))
                                       )
    elementList = text_box.find_elements_by_xpath(xpathID)

    if len(elementList) is 0:
        file.write("elementList is empty\n")
        
    for i in elementList:
        i.click()
        break
        #if att is not "":
            #print(att)

    timeout = 5 # seconds


    #timed continue button click
    try:
        element_present = EC.presence_of_element_located((By.ID, "term-go"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load(1)\n")


    driver.find_element_by_id("term-go").click()


    #timed course box click
    try:
        element_present = EC.presence_of_element_located((By.ID, "term-go"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load\n")

    driver.find_element_by_id("s2id_txt_subjectcoursecombo").click()


    #timed course confirmation
    try:
        element_present = EC.presence_of_element_located((By.ID, "s2id_txt_subjectcoursecombo"))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load\n")

    text_box = driver.find_element_by_xpath("//*[@id='s2id_txt_subjectcoursecombo']/ul")
    ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(className + classNumber).perform()


    #CHECKS IF CLASS EXISTS
    time.sleep(1)
    if (driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li").text) in ["No Matches Found."]:
        messagebox.showerror("Error!","Class does not exist! :D Go Expolozo!")
        driver.close()
        sys.exit()
    #CONTINUE ONLY IF CLASS ACTUALLY EXISTS

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

    #Choice of fetching single class via callNumber or listing all class data

    #single class (callNumber)
    if(callNumber >= 0):
    ###########################################################################
    #for loop that finds all class information on each page and prints it to console
        i = 1 #helper that identifies class type (LEC, LAB, DISC)
        j = 0 #counter
        k = 1 #helper that identifies xpath to fine callNumber
        #iterates a total of how many classes there are
        for _ in range(numClassesFound):
            k = str(k)
            xpath0 = "//*[@id='table1']/tbody/tr[" + k + "]/td[6]/a"
            #click on section details
            driver.find_element_by_xpath(xpath0).click()
            time.sleep(1)
            #driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[6]/a").click()
            time.sleep(1)
            idCheck = driver.find_element_by_xpath("//*[@id='courseReferenceNumber']").text
            ##print (idCheck)

            if(int(idCheck) == callNumber):
                #convert '1' to string '1'
                i = str(i)
                #extract class type   
                xpath = "//*[@id='table1']/tbody/tr["+ i +"]/td[6]/span"
                ###print(driver.find_element_by_xpath(xpath).text)
                infoTotal += driver.find_element_by_xpath(xpath).text   
                ###print('\n') #newline for neatness
                infoTotal += ('\n')
                #click on enrollment info
                driver.find_element_by_id("enrollmentInfo").click() 
                time.sleep(1)
                #extract info of one class using xpath
                for element in driver.find_elements_by_xpath("//*[@id='classDetailsContentDetailsDiv']"):
                    ###print(element.text)
                    infoTotal += element.text
                        

                break

            #iterations
            i = int(i)+ 1
            k = int(k)+ 1
            j = j + 1

            time.sleep(1)
            ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
            #if this is the last class of the page then go to next page
            if(j % 10 == 0 and numPages > 0):
                driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()
                i = 1 #resets i


        #final exit of the windows
        time.sleep(1)
        ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()
    #############################################################################################################
      



    #all classes
    else:
        



        #for loop that finds all class information on each page and prints it to console
        i = 1 #helper that identifies class type (LEC, LAB, DISC)
        j = 0 #counter
        k = 1 #helper that selects each window
        
        #iterates a total of how many classes there are
        for _ in range(numClassesFound):
            #extract class type   
            #convert '1' to string '1'
            i = str(i)
            xpath = "//*[@id='table1']/tbody/tr["+ i +"]/td[6]/span"
            ###print(driver.find_element_by_xpath(xpath).text)
            infoTotal += driver.find_element_by_xpath(xpath).text
            k = str(k)
            xpath0 = "//*[@id='table1']/tbody/tr[" + k + "]/td[6]/a"
            #click on section details
            driver.find_element_by_xpath(xpath0).click()
            time.sleep(1)
            #driver.find_element_by_xpath("//*[@id='table1']/tbody/tr[1]/td[6]/a").click()
            time.sleep(1)
            #print call number
            idCheck = driver.find_element_by_xpath("//*[@id='courseReferenceNumber']").text
            ###print("Call Number: " + idCheck)
            infoTotal += ("\nCall Number:" + idCheck + "\n")
            #click on enrollment info
            driver.find_element_by_id("enrollmentInfo").click() 
            time.sleep(1)    


            #extract info of one class using xpath
            for element in driver.find_elements_by_xpath("//*[@id='classDetailsContentDetailsDiv']"):
                ###print(element.text)
                infoTotal += element.text

            ###print('\n') #newline for neatness
            infoTotal += ('\n')
            infoTotal += ('\n')

            
            ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()   
           

            #iterations
            i = int(i)+ 1 
            j = j + 1
            k = int(k) + 1
            #if this is the last class of the page then go to next page
            if(j % 10 == 0 and numPages > 0):
                time.sleep(1)
                ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
                driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()
                i = 1 #resets i
                k = 1


        #final exit of the windows
        time.sleep(1)
        ActionChains(driver).move_to_element_with_offset(text_box,0,0).send_keys(Keys.ESCAPE).perform()
        driver.find_element_by_xpath("//*[@id='searchResultsTable']/div[2]/div/button[3]").click()


    if(infoTotal != ""):
        file.write(infoTotal+"\n")
    else:
        messagebox.showerror("Error","Sorry, something went wrong. Either you call number was incorrect or the class is full.")

  
    file.close()

    if len(infoTotal) is not 0:
    
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachement; filename= %s" % filename)

        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    
    driver.quit()

def close_window():
    global sched
    #sched.remove_job('job_0')
    sched.remove_job('job_1')
    sched.shutdown(wait=True)
    app.destroy()


app = Tk()
app.title('Expolozo!')
app.resizable(width=False, height=False)
app.geometry("400x400")

go = tk.Button(bg = 'black', text='Go', fg = 'white', command = initiate)
go.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
go.place(relx=0.5, rely=0.3, anchor=CENTER)

go = tk.Button(bg = 'black', text='QUIT', fg = 'white', command = close_window)
go.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
go.place(relx=0.5, rely=0.7, anchor=CENTER)

textBox1 = tk.Entry()
textBox1.grid(row=0, column=0, sticky=tk.W+tk.N)
textBox1.place(relx=0, rely=0, anchor=NW)

textBox2 = tk.Entry()
textBox2.grid(row=0, column=0, sticky=tk.E+tk.N)
textBox2.place(relx=1, rely=0, anchor=NE)

textBox3 = tk.Entry()
textBox3.grid(row=0, column=0, sticky=tk.W+tk.S)
textBox3.place(relx=0, rely=1, anchor=SW)

textBox4 = tk.Entry()
textBox4.grid(row=0, column=0, sticky=tk.S)
textBox4.place(relx=1, rely=1, anchor=SE)

textBox5 = tk.Entry()
textBox5.grid(row=0, column=0, sticky=tk.E)
textBox5.place(relx=0.15, rely=0.5, anchor=W)

textBox6 = tk.Entry()
textBox6.grid(row=0, column=0, sticky=tk.SE)
textBox6.place(relx=0.85, rely=0.5, anchor=E)

label1 = tk.Label(text="Class Name(Eg: Phys, CS, BIOL)", fg= 'black')
label1.place(relx=0.01, rely=0.05, anchor=NW)

label2 = tk.Label(text="Class Number(Eg: 040A, 10, 001)", fg='black')
label2.place(relx=0.99, rely=0.05, anchor=NE)

label3 = tk.Label(text="Call Number(-1 if no call number)", fg='black')
label3.place(relx=0.001, rely=0.95, anchor=SW)

label4 = tk.Label(text="Email", fg='black')
label4.place(relx=0.99, rely=0.95, anchor=SE)

label5 = tk.Label(text="Quarter", fg='black')
label5.place(relx=0.01, rely=0.5, anchor=W)

label6 = tk.Label(text="YEAR", fg='black')
label6.place(relx=0.97, rely=0.5, anchor=E)


app.mainloop()

