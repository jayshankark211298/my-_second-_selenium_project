from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ShankarHeadlessBrowsing:
    username = "Admin"
    password = "admin123"

    def __init__(self, web_url):
        self.url = web_url
        chromedriver_path = r'C:\Users\User\Desktop\workspace\PAT-25\Jay_selenium\chromedriver.exe'  # Replace with your actual path
        self.driver = webdriver.Chrome(service=Service(chromedriver_path))
        self.wait = WebDriverWait(self.driver, 10)

    def home_page(self):
        self.driver.get(self.url)
        sleep(3)
        return self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def shutdown(self):
        self.driver.quit()

    def validate_username_input_box(self):
        try:
            username_input_box = self.driver.find_element(By.NAME, value="username")
            return username_input_box.is_displayed() and username_input_box.is_enabled()
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def login(self):
        try:
            username_input_box = self.driver.find_element(By.NAME, value="username")
            password_input_box = self.driver.find_element(By.NAME, value="password")
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

            username_input_box.send_keys(self.username)
            password_input_box.send_keys(self.password)
            login_button.click()

            sleep(3)
            return self.driver.current_url != "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        except Exception as e:
            print(f"An error occurred during login: {e}")
            return False

    def navigate_to_admin_page(self):
        try:
            admin_menu = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")
            admin_menu.click()
            sleep(3)  # Wait for the page to load
            return self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        except Exception as e:
            print(f"An error occurred while navigating to the Admin page: {e}")
            return False

    def validate_page_title(self):
        try:
            expected_title = "OrangeHRM"
            actual_title = self.driver.title
            if actual_title == expected_title:
                print("Page title is correct: OrangeHRM")
                return True
            else:
                print(f"Page title is incorrect. Expected: {expected_title}, Got: {actual_title}")
                return False
        except Exception as e:
            print(f"An error occurred while validating the page title: {e}")
            return False

    def validate_admin_page_options(self):
        try:
            options = [
                "User Management",
                "Job",
                "Organization",
                "Qualifications",
                "Nationalities",
                "Corporate Banking",
                "Configuration"
            ]
            for option in options:
                # Adjust the XPath if needed to match the actual structure of the page
                menu_option = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul")
                if not menu_option.is_displayed():
                    print(f"Option '{option}' is NOT displayed.")
                    return False
            print("All options are displayed correctly.")
            return True
        except Exception as e:
            print(f"An error occurred while validating admin options: {e}")
            return False

if __name__ == "__main__":
    test = ShankarHeadlessBrowsing("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    if test.home_page():
        print("Home page accessed successfully.")

        if test.validate_username_input_box():
            print("Username input box is present and enabled.")

            if test.login():
                print("Login successful.")

                if test.navigate_to_admin_page():
                    print("Navigated to Admin page successfully.")

                    if test.validate_page_title():
                        print("Page title is validated successfully.")

                        if test.validate_admin_page_options():
                            print("Admin page options are validated successfully.")
                        else:
                            print("Admin page options validation failed.")
                    else:
                        print("Page title validation failed.")
                else:
                    print("Failed to navigate to Admin page.")
            else:
                print("Login failed.")
        else:
            print("Username input box not found.")
    else:
        print("Failed to access home page.")

    test.shutdown()
