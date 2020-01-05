from selenium import webdriver
from getpass import getpass
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


usr=input("Enter your username or email: ")
pwd=getpass("Enter your password: ")
send_to=input('Your message: ')
subject=input('Subject: ')
message=input('Message: ')


time.sleep(1)

#Open browser and then open Gmail 'About' page
browser=webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://www.google.com/intl/en-GB/gmail/about/')

time.sleep(2)

#Find and click the 'Sign In' button
signin = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/ul[1]/li[2]/a')
signin.location_once_scrolled_into_view
signin.click()

time.sleep(2)

#Enters the input email ID
enter_email=wait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
#enter_email=browser.find_element_by_xpath('//*[@id="identifierId"]')
enter_email.send_keys(usr)

time.sleep(2)

#Find and click the 'Next' button
next_btn=browser.find_element_by_class_name('RveJvd snByac')
next_btn.click()

time.sleep(2)

#Locate the password box and enter valid password
enter_password=browser.find_element_by_class_name('whsOnd zHQkBf')
enter_password.send_keys(pwd)

time.sleep(2)

#Locate and click the 'Next' button
next_btn2=browser.find_element_by_class_name('RveJvd snByac')
next_btn2.click()

time.sleep(2)

#Locate and click the 'Compose' button
compose=browser.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
compose.click()

#Locate and click the 'To' field
to=browser.find_element_by_xpath('//*[@id=":rd"]')
to.click()
to.send_keys(send_to)

#Locate and click the 'Subject' field
enter_sub=browser.find_element_by_xpath('//*[@id=":qv"]')
enter_sub.click()
enter_sub(subject)

#Locate and click message box
mssg=browser.find_element_by_xpath('//*[@id=":s0"]')
mssg_sub.click()
mssg(message)

#Locate and click send button
send=browser.find_element_by_xpath('//*[@id=":ql"]')
send.click()

