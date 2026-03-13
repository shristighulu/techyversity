#simple login page
from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.email_textbox=(By.XPATH,"//input[@placeholder='you@example.com']")
        self.password_textbox=(By.XPATH,"//input[@placeholder='••••••••']")
        self.sigin_button=(By.XPATH,"//button[normalize-space()='Sign In']")
    def open_page(self,url):
        self.driver.get(url)
    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)
    def click_sign_in(self):
        self.driver.find_element(*self.sigin_button).click()