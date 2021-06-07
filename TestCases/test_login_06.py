import unittest
from Objects.account import Account
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest

import sys

from TestData.test_data import TestData

sys.path.append('.')

class Login06(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login(self):
        for account in TestData.getAccount_csv():
            login_page = LoginPage(self.browser)
            login_page.login(account)
        #        self.assertEqual('Epic sadface: Username and password do not match any user in this service', login_page.get_error_message(),
        #                         'The actual result does not the same with the expected result.')

        pass
if __name__ == "__main__":
    unittest.main()
