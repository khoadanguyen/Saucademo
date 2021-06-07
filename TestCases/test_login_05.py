import unittest
from Objects.account import Account
from Pages import checkout_stepone_page
from Pages.checkout_stepone_page import CheckoutStepOnePage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest

import sys

from TestData.test_data import TestData

sys.path.append('.')


def self(args):
    pass


class Login05(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_getAccount(self):
        print(TestData.getCheckoutInformation_txt())
        print(CheckoutStepOnePage.input_checkout_info(self))


    # def test_login(self):
    #     for username in TestData.getAccount():
    #         print(username)
    #         account = Account(username, 'secret_sauce')
    #         login_page = LoginPage(self.browser)
    #         login_page.login(account)
    #         self.assertEqual('Epic sadface: Username and password do not match any user in this service', login_page.get_error_message(),
    #                          'The actual result does not the same with the expected result.')
    #

    pass
if __name__ == "__main__":
    unittest.main()
