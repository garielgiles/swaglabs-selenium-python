from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def go_to(self):
        self.driver.get(self.url)

    def take_screenshot(self):
        self.driver.save_screenshpt('../screenshots/test_login.png')
