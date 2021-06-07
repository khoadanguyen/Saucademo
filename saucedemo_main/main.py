import unittest
from selenium import webdriver


class Login(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_login(self):
        browser = self.browser

        self.login('standard_user', 'secret_sauce')

        productsTitle = browser.find_element_by_xpath("//span[text()='Products']")

        self.assertTrue(productsTitle.is_displayed(), 'The Products title does not exist.')

        self.login('locked_out_user', 'secret_sauce')
        self.login('problem_user', 'secret_sauce')
        self.login('performance_glitch_user', 'secret_sauce')

    def login(self, username, password):
        browser = self.browser
        browser.get('https://www.saucedemo.com/')
        input_username = browser.find_element_by_id('user-name')
        input_username.send_keys(username)

        input_password = browser.find_element_by_id('password')
        input_password.send_keys(password)

        button_login = browser.find_element_by_id('login-button')
        button_login.click()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
