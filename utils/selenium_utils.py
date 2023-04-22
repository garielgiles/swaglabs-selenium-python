from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()

    return driver


def close_browser(driver):
    driver.quit()
