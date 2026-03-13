#profile page for student profile
from selenium.webdriver.common.by import By
class StudentprofilePage:
    def __init__(self,driver):
        self.driver=driver
        self.change_password_link=(By.XPATH,"//button[normalize-space()='Change Password']")
        self.current_password_textbox=(By.XPATH,"//input[@placeholder='Enter current password']")
        self.new_password_textbox=(By.XPATH,"//input[@placeholder='Enter new password']")
        self.confirm_new_password_textbox=(By.XPATH,"//input[@placeholder='Confirm new password']")
        self.Update_Password_button=(By.XPATH,"//button[normalize-space()='Update Password']")
    def open_page(self,url):
        self.driver.get(url)
    def click_change_password(self):
        self.driver.find_element(*self.change_password_link).click()    
    def enter_current_password(self,password):
        self.driver.find_element(*self.current_password_textbox).send_keys(password)
    def enter_new_password(self,password):
        self.driver.find_element(*self.new_password_textbox).send_keys(password)
    def enter_confirm_new_password(self,password):
        self.driver.find_element(*self.confirm_new_password_textbox).send_keys(password)
    def click_update_password(self):
        self.driver.find_element(*self.Update_Password_button).click()
        