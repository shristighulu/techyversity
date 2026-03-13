 #import necessary modules form selenium
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set up the chrome driver using webdriver manager
@pytest.fixture()
def driver():

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
    
@pytest.mark.parametrize("Email_Address,password", [("TestQA@gmail.com", "password"), ("user1", "password1"), ("shristighuluu@gmail.com", "testpass")])
def test_login(driver,Email_Address,password):
    driver.get(" https://portal.techyversity.com/login")
    Email_Address_field=driver.find_element(*(By.XPATH,"//input[@placeholder='you@example.com']"))
    password_field=driver.find_element(*(By.XPATH,"//input[@placeholder='••••••••']"))
    Sign_In_button=driver.find_element(*(By.XPATH,"//button[normalize-space()='Sign In']"))
    Email_Address_field.send_keys(Email_Address)
    password_field.send_keys(password)
    Sign_In_button.click()
    time.sleep(5)
   
    #
    try:
        #check if an alert is present
        alert=driver.switch_to.alert
        alert_text=alert.text
        assert "Invalid username or password" in alert_text
        print(f"Invalid username or password for {Email_Address}")
    
    except:
        #if no alert then login successful
        time.sleep(5)
        page_source=driver.page_source
        assert "Welcome to the Dashboard" in page_source, f"Login failed for {Email_Address}, no welcome message found"
        print(f"Login is successful for {Email_Address}")