from pages.login_page import LoginPage
from utils.selenium_utils import open_browser, close_browser

# Defining variables as a global variable
driver = None
page = None
username = "standard_user"
password = "secret_sauce"


def setup():
    global driver
    driver = open_browser()
    global page
    page = LoginPage(driver)


def teardown():
    global driver
    close_browser(driver)


def test_login():
    page.go_to()

    page.input_username().send_keys(username)
    page.input_password().send_keys(password)

