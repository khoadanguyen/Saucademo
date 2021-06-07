import unittest
from Objects.account import Account
from Pages.login_page import LoginPage
from TestCases.base_test import BaseTest
from TestData.test_data import TestData

import sys
sys.path.append('.')

class Login04(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login(self):
        account = Account(TestData.USERNAME, TestData.PASSWORD)
        login_page = LoginPage(self.browser)
        login_page.login(account)

        # login_page.verify_login_success()
        # login_page.verify_login_unsuccess()


if __name__ == "__main__":
    unittest.main()
