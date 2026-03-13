#import necessary modules form selenium
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.techyversitylogin_page import LoginPage
# from pages.techydashboard_page import  TechyDashboardPage
from pages.studentprofile_page import StudentprofilePage
#set up the chrome driver using webdriver manager
@pytest.fixture()
def driver():

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
def test_login(driver):
    login_page=LoginPage(driver)#object of loginpage class
    login_page.open_page("https://portal.techyversity.com/login") #Calls a method from LoginPage to open the login page URL in the browser.
    login_page.enter_email("shristighuluu@gmail.com")#Calls the enter_email method from LoginPage to type "TestQA" in the email field.
    time.sleep(2)
    login_page.enter_password("Newpassword@123")#Calls the enter_password method from LoginPage to type "password" in the password field.
    time.sleep(2)
    login_page.click_sign_in()#Calls the click_sign_in method from LoginPage to click the sign in button.
    time.sleep(5)
    print("Login test  successful.")
    
#redirect to dashboard page
# def test_techy_dashboard_page(driver):
#     # techy_dashboard_page=TechyDashboardPage(driver)
#     # techy_dashboard_page.open_dashboard_page("https://portal.techyversity.com/student/browse")
#     # time.sleep(5)
#     login_page=LoginPage(driver)#object of loginpage class
#     login_page.open_page("https://portal.techyversity.com/login") #Calls a method from LoginPage to open the login page URL in the browser.
#     login_page.enter_email("shristighuluu@gmail.com")#Calls the enter_email method from LoginPage to type "TestQA" in the email field.
#     time.sleep(2)
#     login_page.enter_password("Tryme@123")#Calls the enter_password method from LoginPage to type "password" in the password field.
#     time.sleep(2)
#     login_page.click_sign_in()#Calls the click_sign_in method from LoginPage to click the sign in button.
#     time.sleep(5)
    # print("Techy Dashboard page opened successfully after login.")
    # print("Current URL:", driver.current_url)
    


def test_Student_Profile_Page(driver):
    Student_profile_page=StudentprofilePage(driver)
    Student_profile_page.open_page("https://portal.techyversity.com/student/profile")
    time.sleep(5)
    # First, login with the user
    login_page=LoginPage(driver)#object of loginpage class
    # login_page.open_page("https://portal.techyversity.com/login") #Calls a method from LoginPage to open the login page URL in the browser.
    login_page.enter_email("shristighuluu@gmail.com")#Calls the enter_email method from LoginPage to type "TestQA" in the email field.
    time.sleep(2)
    login_page.enter_password("Newpassword@123")#Calls the enter_password method from LoginPage to type "password" in the password field.
    time.sleep(2)
    login_page.click_sign_in()#Calls the click_sign_in method from LoginPage to click the sign in button.
    time.sleep(5)
    
    # Now navigate to the student profile page after login
    # Student_profile_page=StudentprofilePage(driver)
    Student_profile_page.open_page("https://portal.techyversity.com/student/profile")
    time.sleep(5)
    
    # Click on "Change Password" button first
    Student_profile_page.click_change_password()
    time.sleep(2)
    
    Student_profile_page.enter_current_password("Newpassword@123")
    time.sleep(2)
    Student_profile_page.enter_new_password("Newpassword@12345")
    time.sleep(2)
    Student_profile_page.enter_confirm_new_password("Newpassword@12345")
    time.sleep(2)
    Student_profile_page.click_update_password()
    time.sleep(5)
    print("Student Profile page updated successfully.")
    
    
    #PS C:\Users\Dell\Desktop\QApython\pom> python -m pytest test_run.py -v -s
    