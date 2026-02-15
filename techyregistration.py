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
website_url="https://tech.sangamshrestha007.com.np/login"

#open the website as :
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
#time.sleep(10)


Sign_Up=driver.find_element(*(By.XPATH,"//button[normalize-space()='Sign Up']"))
Sign_Up.click()
time.sleep(5)

#find the form element by their xpath locator
firstName_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Sangam']"))
lastName_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Shrestha']"))
email_field=driver.find_element(*(By.XPATH,"//input[@placeholder='shr@test.com']"))
password_field=driver.find_element(*(By.XPATH,"//input[@name='password']"))
confirmPassword=driver.find_element(*(By.XPATH,"//input[@name='confirmPassword']"))
#fill the form element
firstName_field.send_keys("shree") 
time.sleep(3)
lastName_field.send_keys("Shrestha")
email_field.send_keys("shre@gamil.com")
time.sleep(2)
password_field.send_keys("HelloMe123@")
time.sleep(2)
confirmPassword.send_keys("HelloMe123@")
Verify_Email=driver.find_element(*(By.XPATH,"//button[@class='btn-primary flex items-center justify-center gap-2 mt-6']"))
Verify_Email.click()
time.sleep(10)

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
#print("xpath locator is success..")

 
