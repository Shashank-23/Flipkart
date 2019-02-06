from selenium.webdriver.common.by import By
from Test_Utilities.Framework_Utility import frameworkUtility

class LoginPage(frameworkUtility):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def login(self,email,password):
        self.driver.find_element(By.XPATH, "//a[@href='/sign_in']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, "user_email").send_keys(email="")
        self.driver.find_element(By.ID, "user_password").send_keys(password="")