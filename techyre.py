#import necessary modules
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#setup driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website_url = "https://tech.sangamshrestha007.com.np/login"
driver.get(website_url)
driver.maximize_window()
time.sleep(3)

#click Sign Up
driver.find_element(By.XPATH, "//button[normalize-space()='Sign Up']").click()
time.sleep(3)

#locate fields
firstName_field = driver.find_element(By.XPATH, "//input[@placeholder='Sangam']")
lastName_field = driver.find_element(By.XPATH, "//input[@placeholder='Shrestha']")
email_field = driver.find_element(By.XPATH, "//input[@placeholder='shr@test.com']")
password_field=driver.find_element(By.XPATH,"//input[@name='password']")
confirm_Password_field=driver.find_element(By.XPATH,"//input[@name='confirmPassword']")

# -------- RANDOM DATA GENERATORS -------- #

def generate_random_name():
    return ''.join(random.choices(string.ascii_letters, k=6))

def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{random_string}{random.randint(100,999)}@automation.com"

def generate_password():
    return "Test@" + str(random.randint(1000,9999))  # meets validation rules

#generate random data
first_name = generate_random_name()
last_name = generate_random_name()
email = generate_random_email()
password = generate_password()

#fill form
firstName_field.send_keys(first_name)
lastName_field.send_keys(last_name)
email_field.send_keys(email)
password_field.send_keys(password)
confirm_Password_field.send_keys(password)

# locate password eye icon
password_eye =driver.find_element(*(By.XPATH,"body > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > button:nth-child(3) > svg:nth-child(1) > path:nth-child(1)"))

password_eye.click()
time.sleep(2)


# driver.execute_script("arguments[0].setAttribute('type','text')", password_field)
# driver.execute_script("arguments[0].setAttribute('type','text')", confirm_Password_field)

time.sleep(5)

Verify_Email=driver.find_element(*(By.XPATH,"//button[@class='btn-primary flex items-center justify-center gap-2 mt-6']"))
Verify_Email.click()
time.sleep(10)

#print title and URL
print("Website title is:", driver.title)
print("Current URL is:", driver.current_url)

driver.quit()

