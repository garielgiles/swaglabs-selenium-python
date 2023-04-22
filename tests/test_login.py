from pages.login_page import LoginPage
from utils.selenium_utils import open_browser, close_browser

# Defining the driver variable as a global variable
driver = None
page = None


def setup():
    global driver
    driver = open_browser()
    global page
    page = LoginPage(driver)


def teardown():
    global driver
    close_browser(driver)
