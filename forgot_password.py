from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class OrangeHRMTest:
    def __init__(self):
        # Initialize the WebDriver
        chromedriver_path = r'C:\Users\User\Desktop\workspace\PAT-25\Jay_selenium\chromedriver.exe'  # Replace with your actual path
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait with a 10-second timeout

    def visit_site(self, url):
        # Visit the provided URL
        self.driver.get(url)

    def click_forgot_password(self):
        # Wait for the 'Forgot your password?' link to be clickable and then click it
        forgot_password_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")))
        forgot_password_link.click()

    def reset_password(self, username):
        # Wait for the username input field, enter the username, and click the reset button
        username_field = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "oxd-input")))
        username_field.send_keys(username)

        reset_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        reset_button.click()

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


# Usage
if __name__ == "__main__":
    test = OrangeHRMTest()
    test.visit_site("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    test.click_forgot_password()
    test.reset_password("Admin")
    test.close_browser()
