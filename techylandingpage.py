#import necessary modules form selenium
#using selector hub Xpath generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up the chrome driver using webdriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desired url:
website_url="https://test.techyversity.com"

#open the website as :
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
#time.sleep(10)

Send_Inquiry=driver.find_element(*(By.XPATH,"//a[normalize-space()='Send Inquiry']"))
Send_Inquiry.click()
time.sleep(5)

#find the form element by their xpath locator
fullname_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Enter your full name']"))
email_field=driver.find_element(*(By.XPATH,"//input[@placeholder='your@email.com']"))
#PhoneInputCountrySelect_field=driver.find_element(*(By.XPATH,"//select[@aria-label='Phone number country']"))
phone_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Enter phone number']"))
interestedCourseName_field=driver.find_element(*(By.XPATH,"//select[@name='intrestedCourseName']"))
message_field=driver.find_element(*(By.XPATH,"//textarea[@placeholder='Tell us more about your requirements...']"))

#fill the form element
fullname_field.send_keys("shree shrestha") 
time.sleep(3)
email_field.send_keys("shre@gamil.com")
time.sleep(2)

PhoneInputCountrySelect_field=driver.find_element(*(By.XPATH,"//select[@aria-label='Phone number country']"))
PhoneInputCountrySelect_field.click()
PhoneInputCountrySelect_field.send_keys("Nepal")
time.sleep(5)
phone_field.send_keys("9841029345")
time.sleep(2)
interestedCourseName_field.send_keys("devops engineering")
time.sleep(2)
message_field.send_keys("Hello")
time.sleep(2)

#appplication commands:
#1.Extract and print the website title
website_title=driver.title
print(f"Website title is:{website_title}")#to know actual title of the website that has been sued or visited
#2.Get the current url
current_url=driver.current_url 
print(f"current url is:{current_url}")
#get the page source
page_source=driver.page_source
#print(f"page source:",page_source)


#close the web driver instance
driver.quit()
print("xpath locator is success..")

 
