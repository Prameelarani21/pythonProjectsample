from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    username=(By.XPATH,"//input[@name='username']")
    password=(By.XPATH,"//input[@name='password']")
    login=(By.XPATH,"//button[@type='submit']")

    def getusername(self):
        return self.driver.find_element(*LoginPage.username)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password)


    def getlogin(self):
        return self.driver.find_element(*LoginPage.login)

