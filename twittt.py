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
user1 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/div'
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
# # if(driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')):
# driver.find_element(By.CLASS_NAME,'r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu').send_keys(username)
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,'css-901oao.r-1awozwy.r-jwli3a.r-6koalj.r-18u37iz.r-16y2uox.r-37j5jr.r-a023e6.r-b88u0q.r-1777fci.r-rjixqe.r-bcqeeo.r-q4m81j.r-qvutc0').click()
# time.sleep(2)

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
driver.get("https://twitter.com/DaveHsu")
# find the element where we have to
# enter the xpath
time.sleep(2)
followingNumber = driver.find_element(by='xpath',value=followingNum)
print('followingNum',followingNumber.text)
follwmeeee = followingNumber.text
time.sleep(2)

# new driver new url
driver.get("https://twitter.com/DaveHsu/following")
time.sleep(2)
# Determine the height of the viewport
viewport_height = driver.execute_script("return window.innerHeight")

# Determine the height of the entire document
document_height = driver.execute_script("return document.documentElement.scrollHeight")

# Calculate the number of scrolls needed
num_scrolls = document_height // viewport_height
# Capture elements after each scroll
captured_elements = []
full_captured_elements = []
fullaccount = []
faill = 0
iterator = 104
# with open("davhsu.txt", "r",encoding="utf-8") as file:
    # lines = file.readlines()
    # iterator = int(lines[3])  # Ind
with open("davhsu.txt", "a",encoding="utf-8") as file:
    # file.write('---------------------------------------')
    # file.write('\n')
    # file.write(' Accounts followed by DaveHsu')
    # file.write(follwmeeee)
    # file.write('\n')
    # file.write('---------------------------------------')
    # while len(captured_elements) < int(250):
    #     # if len(captured_elements) > 1: driver.refresh()
    #     # print('captured elements',len(captured_elements))
    #     driver.refresh()
    #     time.sleep(3)
    #     if(len(full_captured_elements) >= int(250)):driver.quit()
        # if len(captured_elements) > 1: 
        #     driver.close()
        #     time.sleep(5)
    try:
        for _ in range(num_scrolls):
            # Scroll down to the bottom
            driver.execute_script("window.scrollBy(0, arguments[0])", viewport_height)
            # Capture the elements
            elemnt = driver.find_element(
            by='xpath',
            value=followingDiv
            )
            time.sleep(1)
            accounts = elemnt.find_elements(By.CSS_SELECTOR, '.css-1dbjc4n.r-18u37iz')
            for e in accounts:
                if(e.text.startswith('@')):
                    if e.text in captured_elements:
                        continue
                    captured_elements.append(e.text)

            fullacc = elemnt.find_elements(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')
            # folowbt =elemnt.find_elements(By.CLASS_NAME,followBtn)

            # for e in folowbt:
            #     e.click()
            for e in fullacc:
                if isinstance(e, webdriver.remote.webelement.WebElement): 
                    time.sleep(2)
                    if e.text in fullaccount:
                        continue
                    fullaccount.append(e.text)
                    try:
                        follll =e.find_element(By.CLASS_NAME,followBtn)
                        if(follll): print('following')
                        # follll.click()
                        driver.execute_script("arguments[0].click();", follll)
                        if(iterator % 2 == 0):time.sleep(3)
                        time.sleep(3)
                        # if(e.text == 'follow'):e.click()
                        # print('\n\n\n','account', iterator,':',e.text,'\n','---------------------------------------')
                        file.write('\n')
                        file.write('account ')
                        file.write(str(iterator))
                        file.write(':')
                        file.write(e.text)
                        file.write('\n')
                        file.write('---------------------------------------')
                        iterator+=1
                        # lines = file.readlines()
                        # lines[3] = str(iterator)
                        faill = 0
                    except:
                        print('no follow btn')
                        faill+=1
                        if(faill == 44):
                            driver.refresh()
                            faill = 0
                            print('refresh')
                            time.sleep(3)
                        continue
            full_captured_elements.extend(captured_elements)
            print('captured elements',captured_elements)
            file.write('\n')
            file.write('---------------------------------------')
            file.write('\n')
            file.write('full accounts')
            file.write(str(full_captured_elements))
            # print('in accounts',e.text)
        #  print('fullAcc ',len(captured_elements),':',e.text)
# # Scroll down the page
    except:
        print('error')
        driver.quit()
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# following2 = elemnt.find_elements(By.CSS_SELECTOR, '.css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l')
# following.extend(following2)
#    toWrite = 'Account ',iterator,': '
#         f.write(toWrite)
#         f.write(e.text)
#         f.write('\n')
#         f.write('---------------------------------------')
#         f.write('\n')
num = 1
# print('captured elements',captured_elements)
# for e in  captured_elements:
    
#     # if(e.text.startswith('@')):
#     print(num,' acc:',e)
#     num+=1
driver.quit()     
# for e in following2:
    
#     if(e.text.startswith('@')):
#         print(num,' acc:',e.text)
#         num+=1



