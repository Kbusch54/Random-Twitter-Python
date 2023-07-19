import datetime
import re
from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    print("I'm inside hello_there()",name)
    now = datetime.datetime.now()
    formatted_now = now.strftime("%a, %d %b, %y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
inputUser = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
user ='kdb22222'
username = 'kdb22222'
passwrd = '2012201994'
listBtn ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/a'
nextBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
inputPass ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
logInBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
tweetBtn ='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
searchPeopleBox = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div/div/div/label/div[2]/div[2]/div/span'
addBtnList = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]'
doneLisatBtn="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span"
listNextBtn = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span'
nameInput = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/label/div/div[2]/div/input'
descriptionBox = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/label/div/div[2]/div/textarea'
textBox = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div'
def logIn_Credentials(cred_user,cred_password):
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
        by='xpath', value=inputUser).send_keys(cred_user)
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
        by='xpath',value=inputPass).send_keys(cred_password)
    # find the element login button
    # request using xpath
    # clicking on that element
    driver.find_element(by='xpath',value=logInBtn).click()
    # adjust the sleep time according to your internet speed
    time.sleep(2)

    driver.find_element(by='xpath',value=tweetBtn).click()
    time.sleep(2)
    return driver
def logIn():
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
    return driver
def tweetThis(tweet):
    print("I'm inside tweetThis()",tweet)
    driver = logIn()
    time.sleep(5)
    driver.find_element(by='xpath',value=textBox).send_keys(tweet)
    time.sleep(2)
    tweetButton = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]'
    driver.find_element(by='xpath',value=tweetButton).click()
    time.sleep(2)
    driver.close()
    return "Tweeted: "+tweet
def followList(list):
    driver = logIn()
    for user in list:
        driver.get("https://twitter.com/"+user)
        time.sleep(2)
        followBtn = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div'
        driver.find_element(by='xpath',value=followBtn).click()
        time.sleep(2)
@app.route("/api/tweets/<path:tweetToSend>")
def tweets(tweetToSend):
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
  
    tweet = tweetThis(tweetToSend)
    print(tweet)
    return f'Tweeted: {tweetToSend}'

@app.route("/api/follow/<path:followList>")
def create_tweet(followList):
    print("I'm inside create_tweet()",followList)
    return f'Tweet: {followList}'
@app.route("/api/createList/<path:list>")
def create_list(list):
    driver = logIn()
    driver.get("https://twitter.com/"+user+"/lists")
    time.sleep(2)
    driver.find_element(by='xpath',value=listBtn).click()
    time.sleep(2)
    driver.find_element(by='xpath',value=nameInput).send_keys('test')
    driver.find_element(by='xpath',value=descriptionBox).send_keys('test description')
    driver.find_element(by='xpath',value=listNextBtn).click()
    time.sleep(2)
    driver.find_element(by='xpath',value=doneLisatBtn).click()
    driver.close()

    print("I'm inside create_list()",list)
    return f'Tweet: {list}',driver
