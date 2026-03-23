from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    usernameInput = (By.ID, "username")
    passwordInput = (By.ID, "password")
    submitBtn = (By.ID, "submit")
    logoutBtn = (By.LINK_TEXT, "Log out")

    def enterUsername(self, username):
        self.driver.find_element(*self.usernameInput).send_keys(username)
        # * is used here to parse -> it removes outbracket so it will not be ((BY.ID, "... ")) 

    def enterPassword(self, password):
        self.driver.find_element(*self.passwordInput).send_keys(password)


# Needed to create this because now we are not writing login in test_login.py
    def login(self,username,password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLogin()

    def clickLogin(self):
        self.driver.find_element(*self.submitBtn).click()

    def isLogoutVisible(self):
        return self.driver.find_element(*self.logoutBtn).is_displayed()