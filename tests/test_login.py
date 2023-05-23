import time
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


def test_login_successful():
    page.go_to()

    page.username_field().send_keys(username)
    page.password_field().send_keys(password)

    page.login_button().click()

    page.products_title().is_displayed()

    time.sleep(5)


def test_login_unsuccessful():
    page.go_to()

    page.username_field().send_keys("incorrect user")
    page.password_field().send_keys(password)

    page.login_button().click()

    time.sleep(5)
