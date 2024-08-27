import pytest
from validate_title_options import ShankarHeadlessBrowsing


@pytest.fixture(scope="module")
def browser():
    # Initialize the ShankarHeadlessBrowsing instance
    web_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    shankar_browser = ShankarHeadlessBrowsing(web_url)

    # Navigate to the home page
    assert shankar_browser.home_page(), "Failed to load the home page"

    yield shankar_browser

    # Shutdown the browser after tests are done
    shankar_browser.shutdown()


def test_login(browser):
    # Validate the username input box is present and enabled
    assert browser.validate_username_input_box(), "Username input box is not present or enabled"

    # Perform the login
    assert browser.login(), "Login failed"

    # Validate the page title
    assert browser.validate_page_title(), "Page title after login is incorrect"


def test_navigate_to_admin_page(browser):
    # Navigate to the Admin page
    assert browser.navigate_to_admin_page(), "Failed to navigate to the Admin page"

    # Validate the Admin page options
    assert browser.validate_admin_page_options(), "Admin page options validation failed"
