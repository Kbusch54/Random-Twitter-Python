from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
inputUser = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
user ='kdb22222'
username = 'kdb22222'
passwrd = '2012201994'
nextBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
followingNum ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span'
inputPass ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
followingDiv = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div'
followBtn = 'css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-15ysp7h.r-4wgw6l.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr'
logInBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
tweetBtn ='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
user1 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div'
textBox = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div'
# create instance of Chrome webdriver
driver = webdriver.Chrome() 
driver.get("https://twitter.com/login")
    # adjust the sleep time according to your internet speed
time.sleep(2)
# find the element where we have to 
# enter the xpath
# driver.find_element.__getattribute__
# fill the number or mail
driver.find_element(
    by='xpath', value=inputUser).send_keys(user)
# find the element next button 
# request using xpath 
# clicking on that element 
driver.find_element(
    by='xpath',
    value=nextBtn).click()

# adjust the sleep time according to your internet speed
time.sleep(2)

# find the element where we have to 
# enter the xpath
# fill the password
driver.find_element(
    by='xpath',value=inputPass).send_keys(passwrd)
# find the element login button
# request using xpath
# clicking on that element
driver.find_element(by='xpath',value=logInBtn).click()
# adjust the sleep time according to your internet speed
time.sleep(2)

driver.find_element(by='xpath',value=tweetBtn).click()
time.sleep(2)
driver.find_element(by='xpath',value=textBox).send_keys('Hello World part 2')
time.sleep(2)
tweetButton = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'
driver.find_element(by='xpath',value=tweetButton).click()
time.sleep(2)
driver.close()