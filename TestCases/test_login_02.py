import unittest
from selenium import webdriver

from Objects.account import Account

import sys
sys.path.append('.')

class Login02(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login(self):
        browser = self.browser

        account = Account('standard_user', 'secret_sauce')
        self.login_object(account)


    def login_object(self, account):
        browser = self.browser
        browser.get('https://www.saucedemo.com/')
        input_username = browser.find_element_by_id('user-name')
        input_username.send_keys(account.username)

        input_password = browser.find_element_by_id('password')
        input_password.send_keys(account.password)

        button_login = browser.find_element_by_id('login-button')
        button_login.click()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
