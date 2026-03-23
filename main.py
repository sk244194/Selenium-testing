from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")

driver.find_element(By.ID,"submit").click()


# time.sleep(8)
# This time method is not preferred use implicit or explicit waits

wait = WebDriverWait(driver,10)

logout_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT,"Log out")))

assert "logged-in-successfully" in driver.current_url
# This will print error if something wrong otherwise nothing

assert logout_button.is_displayed(),"Logout not found"
# If wanted to print assertion error use it in try except block with -> except AssertionError as e:


# We prefere using POM(Page Object Model) because it improves readibility and maintainability by seperating locators and action from test_logic
# Check this by opening file from test folder

driver.quit()