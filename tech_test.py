#import necessary modules form selenium
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up the chrome driver using webdriver manager
def test_google_search():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://www.google.com/")
    #driver.maximize_window()
    # time.sleep(5)

    # search_box=driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    # search_box.send_keys("consultancy bhaktapur")
    # search_box.send_keys(Keys.RETURN)
    # time.sleep(7)

    # #click on the first available link and go to home menu
    # #first_link = driver.find_element(By.XPATH, "//h3[contains(text(), 'MindRisers')]")


    # first_link=driver.find_element(*(By.XPATH,"//div[@class='YzSd aTI8gc']"))
    # first_link.click()
    # time.sleep(5)
    # print("pytest demo succeed....")
    
    search_box = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']"))
    )
    search_box.send_keys("techyversity.com")
    search_box.send_keys(Keys.RETURN)

    print("If there is a CAPTCHA, please solve it in the browser now...")
    time.sleep(30)  # Give yourself time to solve the CAPTCHA

    # Save page source for debugging
    with open("page_after_captcha.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    
     # Wait for the search results container to appear
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Try a more generic XPath for the first result link
    first_link = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='search']//a/h3"))
    )
    first_link.click()
    time.sleep(5)
    print("pytest demo succeed....")