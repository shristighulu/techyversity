 #import necessary modules form selenium
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time

#set up the chrome driver using webdriver manager
@pytest.fixture()
def driver():

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
@pytest.mark.parametrize("Email_Address,password", [("TestQA@gmail.com", "password"),("shristighuluu@gmail.com", "Newpassword@123")])
def test_login(driver,Email_Address,password):
    driver.get("https://portal.techyversity.com/login")
    Email_Address_field=driver.find_element(*(By.XPATH,"//input[@placeholder='you@example.com']"))
    password_field=driver.find_element(*(By.XPATH,"//input[@placeholder='••••••••']"))
    Sign_In_button=driver.find_element(*(By.XPATH,"//button[normalize-space()='Sign In']"))
    Email_Address_field.send_keys(Email_Address)
    password_field.send_keys(password)
    Sign_In_button.click()
    time.sleep(2)
    Profile=driver.find_element(*(By.XPATH,"//*[@id='root']/div/div[2]/nav/div/a[4]/span"))
    Profile.click()
    time.sleep(5)
    #calculate the height of the page using javascripts
    page_height=driver.execute_script("return document.body.scrollHeight")
    #scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

