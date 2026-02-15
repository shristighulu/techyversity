#import necessary modules form selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set up the chrome driver using webdriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desired url:
website_url="https://test.techyversity.com/"

#open the website as :
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(10)

#extract the website title
website_title=driver.title
print(f" Website Title:{website_title}")




#close ythe webdriver instance 
driver.quit()