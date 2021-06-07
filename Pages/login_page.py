from Pages.base_page import BasePage
from Locators.login_locators import LoginLocators
from TestData.test_data import TestData

import sys
sys.path.append('.')

class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.get(TestData.BASE_URL)

    def login(self, account):
        self.send_keys(LoginLocators.INPUT_USERNAME, account.username)
        self.send_keys(LoginLocators.INPUT_PASSWORD, account.password)
        self.click(LoginLocators.BUTTON_LOGIN)

    def get_error_message(self):
        return self.get_text(LoginLocators.LABEL_ERROR)
