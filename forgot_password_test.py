import pytest
from selenium.common.exceptions import TimeoutException
from forgot_password import OrangeHRMTest  # Assuming the class is saved in a file named orange_hrm_test.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def orange_hrm_test():
    """Fixture to initialize and close the OrangeHRMTest instance."""
    test_instance = OrangeHRMTest()
    yield test_instance
    test_instance.close_browser()

def test_visit_site(orange_hrm_test):
    """Test visiting the OrangeHRM site."""
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    orange_hrm_test.visit_site(url)
    assert "OrangeHRM" in orange_hrm_test.driver.title, "Failed to visit the OrangeHRM site."

def test_click_forgot_password(orange_hrm_test):
    """Test clicking the 'Forgot your password?' link."""
    orange_hrm_test.click_forgot_password()
    reset_password_element = orange_hrm_test.wait.until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Reset Password']"))
    )
    assert reset_password_element.is_displayed(), "Failed to navigate to the reset password page."

def test_reset_password(orange_hrm_test):
    """Test resetting the password."""
    username = "Admin"
    orange_hrm_test.reset_password(username)
    reset_password_confirmation = orange_hrm_test.wait.until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='Please contact HR admin in order to reset the password.']"))
    )
    assert reset_password_confirmation.is_displayed(), "Failed to reset the password or display confirmation."

def test_cleanup(orange_hrm_test):
    """Test closing the browser."""
    orange_hrm_test.close_browser()
    assert orange_hrm_test.driver.service.process is None, "Browser was not closed properly."
