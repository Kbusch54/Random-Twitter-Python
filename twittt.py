from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytz
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv


import os
dotenv_path = './.env'
load_dotenv(dotenv_path=dotenv_path)
user = os.getenv('TWITTER_USER')
username = os.getenv('TWITTER_USERNAME')
passwrd = os.getenv('TWITTER_PASSWORD')
doubled = set()
all_accounts = {}
inDb = set()
url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')



class Account:
    def __init__(self, account, username, description):
        self.account = account
        self.username = username
        self.description = description
        self.followed_by = []

    def add_follower(self, follower):
        if follower not in self.followed_by:
            self.followed_by.append(follower)

    def get_info(self):
        return {
            'account': self.account,
            'username': self.username,
            'description': self.description,
            'followed_by': self.followed_by
        }
    


user = os.getenv('TWITTER_USER')
username = os.getenv('TWITTER_USERNAME')
passwrd = os.getenv('TWITTER_PASSWORD')
doubled = set()
all_accounts = {}
inDb = set()
url: str = os.getenv('SUPABASE_URL')
key: str = os.getenv('SUPABASE_KEY')
print('url',url)

dbUser='postgres'
dbPassword='C12veEutvfQzE2y9'
dbPort="5432"
dbHost = 'db.utvsxgfogcixgkztnvxo.supabase.co'
dbdDatabase='postgres'
def print_all_accounts(accounts_dict):
    for account in accounts_dict.values():
        info = account.get_info()
        print(f"Account: {info['account']}")
        print(f"Username: {info['username']}")
        print(f"Description: {info['description']}")
        print(f"Followed by: {', '.join(info['followed_by'])}")
        print('-------')
inputUser = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'

nextBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
followingNum ='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[1]/a/span[1]/span'
inputPass ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
followingDiv = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div'
followBtn = 'css-18t94o4.css-1dbjc4n.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-15ysp7h.r-4wgw6l.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr'
logInBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
user1 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div'
listBtn ='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div/div[3]/div/a'
nextBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
inputPass ='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
logInBtn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
tweetBtn ='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a'
nameInput='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/label/div/div[2]/div/input'
descriptionBox = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[3]/label/div/div[2]/div/textarea'
searchPeopleBox = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div/div/div/label/div[2]/div[1]/input'
textBox = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div'

addBtnList = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/span/span'
usedSerachPeople = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div/div/div/label/div[3]/div'

doneLisatBtn="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span"
listNextBtn = '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/span/span'
doubled = set()
all_accounts = {}
inDb = set()
supabase: Client = create_client(url, key)

def get_All_Tracked():
    try:
        accounts = supabase.table('Tracking').select("account").execute()
        return accounts
    except (Exception) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        if(accounts):
            print("PostgreSQL connection is closed")
def get_all_accounts():
    try:
        accounts = supabase.table('Followed').select("*").execute()
        
        return accounts.data
    except (Exception) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        if(accounts):
            print("PostgreSQL connection is closed")

def update_last_num(amt):
    try:
        supabase.table('sign').update({
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'new_amount': amt
        }).eq('id', 2).execute()
    except (Exception) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        if(amt):
            print("Added to Database")
def update_or_insert(account, username, description, followed_by):
    try:
        if account in inDb:
            supabase.table('Followed').update({
                'followed_by': followed_by,
                'updated_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }).eq('account', account).execute()
        else:
            supabase.table('Followed').insert({
                'account': account,
                'username': username,
                'description': description,
                'followed_by': followed_by,
                'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }).execute()
    except (Exception) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        if(account):
            print("PostgreSQL connection is closed and completed")

def twitter_log_in():
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
    return driver

def get_following(driver,trackers):
    for tracked in trackers:
        # new driver new url
        url = f"https://twitter.com/{tracked}/following"
        driver.get(url)
        time.sleep(2)
        # Determine the height of the viewport
        viewport_height = driver.execute_script("return window.innerHeight")

        # Determine the height of the entire document
        document_height = driver.execute_script("return document.documentElement.scrollHeight")

        # Calculate the number of scrolls needed
        num_scrolls = document_height // viewport_height
    
        # with open("davhsu.txt", "r",encoding="utf-8") as file:
            # lines = file.readlines()
            # iterator = int(lines[3])  # Ind
    
        try:
            seen = set()
            for _ in range(num_scrolls):
                time.sleep(1)
                # Scroll down to the bottom
                driver.execute_script("window.scrollBy(0, arguments[0])", viewport_height)
                # Capture the elements
                elemnt = driver.find_element(
                by='xpath',
                value=followingDiv
                )
                # accounts = elemnt.find_elements(By.CSS_SELECTOR, '.css-1dbjc4n.r-18u37iz')
                fullacc = elemnt.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
                time.sleep(1)
                for e in fullacc:
                    if isinstance(e, webdriver.remote.webelement.WebElement): 
                        try:
                            usernameForAcc = e.text[0:e.text.find('@')]
                            accountName = e.text[e.text.find('@'):e.text.find('Follow')-1]
                            if accountName in seen or accountName == '':
                                continue
                            description = e.text[e.text.find('Follow'):].replace('Follow\n','',1)
                            if description == '' or description == 'Follow':
                                seen.add(accountName)
                                continue
                            if accountName in doubled:
                                print('doubled maybe', accountName)
                                acc = all_accounts[accountName]
                                acc.add_follower(tracked)
                                all_accounts[accountName] = acc
                            else:
                                acc = Account(accountName, usernameForAcc, description)
                                acc.add_follower(tracked)
                                all_accounts[accountName] = acc
                            seen.add(accountName)
                            doubled.add(accountName)
                        except Exception as e:
                            # print('error FOR BOBBY JONES')
                            continue  
        except:
            print('complete')
            driver.quit()
            break
def add_accounts_to_db():
    for account in all_accounts.values():
        username = account.username
        description = account.description
        followed_by = account.followed_by
        accounts = account.account
        update_or_insert(accounts, username, description, followed_by)
    global length
    update_last_num(len(all_accounts)-length)
# accounts = get_all_accounts()
# for account in accounts:
#     acc = Account(account['account'], account['username'], account['description'])
#     acc.followed_by = account['followed_by']
#     all_accounts[account['account']] = acc
#     doubled.add(account.accountName)
#     inDb.add(account.accountName)

def add_list(usersToAdd):
    driver = twitter_log_in()
    time.sleep(2)
    # get_following(driver,tracking)
    driver.get("https://twitter.com/"+user+"/lists")
    time.sleep(2)
    driver.find_element(by='xpath',value=listBtn).click()
    time.sleep(2)
    eastern = pytz.timezone('US/Eastern')
    eastern_time = datetime.now(eastern)
    # Define the Eastern Time Zone
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in Eastern Time Zone
    eastern_time = datetime.now(eastern)

    # Format the time in 'HH:MM AM/PM' format
    hour_am_pm = eastern_time.strftime('%I:%M %p')
    print(hour_am_pm)
    print(datetime.now().strftime("%Y-%m-%d %H:%M")+hour_am_pm)
    driver.find_element(by='xpath',value=nameInput).send_keys('Joes list '+datetime.now().strftime("%m-%d ")+hour_am_pm)
    driver.find_element(by='xpath',value=descriptionBox).send_keys('Twitter list to follow for joe '+datetime.now().strftime("%Y-%m-%d %H:%M"))
    time.sleep(2)
    driver.find_element(by='xpath',value=listNextBtn).click()
    time.sleep(2)
    for users in usersToAdd:
        driver.find_element(by='xpath',value=searchPeopleBox).send_keys(users)
        time.sleep(3)
        addMe = driver.find_element( by=By.XPATH,value=addBtnList)
        driver.execute_script("arguments[0].click();", addMe)
        time.sleep(3)
        driver.find_element(by='xpath',value=usedSerachPeople).click()
        time.sleep(2)
    driver.find_element(by='xpath',value=doneLisatBtn).click()
    driver.close() 
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
length = 0
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
def start_process():
    accounts = get_all_accounts()
    global length
    for account in accounts:
        acc = Account(account['account'], account['username'], account['description'])
        acc.followed_by = account['followed_by']
        all_accounts[account['account']] = acc
        doubled.add(account['account'])
        inDb.add(account['account'])
    length = len(all_accounts)
    trackers = get_All_Tracked()
    tracking = []
    for tracked in trackers.data:
        tracking.append(tracked['account'])
    if(len(tracking) == 0):
        print('No accounts to track')
        exit()
    print(tracking)
    driver = twitter_log_in()
    time.sleep(2)
    get_following(driver,tracking)
    driver.quit()
    add_accounts_to_db()
    print('done')
start_process()



thingToTweet = 'My Name is JoJOBot @JKendzicky I am here to please you \n Check this out: https://www.youtube.com/watch?v=9bZkp7q19f0 \n Whoops I meant this \n Site: https://twitt-creep-eee.vercel.app/'
tweet = tweetThis(thingToTweet)
print(tweet)
