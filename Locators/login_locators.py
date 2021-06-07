from selenium.webdriver.common.by import By

class LoginLocators(object):
    """A class for login page locators. All login page locators should come here"""
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.ID, 'login-button')
    LABEL_ERROR = (By.XPATH, "//h3[@data-test='error']")
