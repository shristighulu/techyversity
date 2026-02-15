#import necessary modules form selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set up the chrome driver using webdriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desired url:
website_url="https://techyversity.com/"

#open the website as :
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(10)

#calculate the height of the page using javascripts
page_height = driver.execute_script("return document.documentElement.scrollHeight")

#page_height=driver.execute_script("return documemt.body.scrollHeight;")

#scroll down the page using the scripts
scroll_speed=100
scroll_iterations=int(page_height/scroll_speed)

#loop to perform the iteration
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(1)

#extract the website title
website_title=driver.title
print(f" Website Title:{website_title}")

#close ythe webdriver instance 
driver.quit()