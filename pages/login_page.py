from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def go_to(self):
        self.driver.get(self.url)

    def take_screenshot(self):
        self.driver.save_screenshot('../screenshots/test_login.png')

    def input_username(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='user-name']")

    def input_password(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='password']")

    def input_login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='login-button']")

    def div_epic_sadface_username_required(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class$='error']")

    def h3_error(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

    def button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[class='error-button']")
