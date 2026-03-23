from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.login_page import LoginPage


def test_valid_login():
    # Moved everything inside this function to check pytest functionaliy(just write pytest to call all the test functions automatically)
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    wait = WebDriverWait(driver, 10)

    login = LoginPage(driver)


    try:
        login.enterUsername("student")
        login.enterPassword("Password123")
        login.clickLogin()

        wait.until(EC.visibility_of_element_located(login.logoutBtn))

        if (
            "logged-in-successfully" in driver.current_url
            and login.isLogoutVisible()
            and "Logged In Successfully" in driver.page_source
        ):
            print("Login Successful")
        else:
            print("Login Failed")

    except:
        print("Login Failed")

    driver.quit()