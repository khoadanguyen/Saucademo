import unittest
from Objects.account import Account
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest

import sys
sys.path.append('.')

class Login03(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login(self):
        account = Account('locked_out_user', 'secret_sauce')
        login_page = LoginPage(self.browser)

        # 3 ways to reduce the code
        login_page.login(account)
        self.assertEqual('Epic sadface: Sorry, this user has been locked out...', login_page.get_error_message(),
                         'The actual result does not the same with the expected result.')

    def test_login(self):
        account = Account('standard_user', 'secret_sauce')
        login_page = LoginPage(self.browser)

        # 3 ways to reduce the code
        login_page.login(account)

        products_page = ProductsPage(self.browser)
        self.assertTrue(products_page.does_product_header_exist(), 'The Products title does not exist.')


        # login_page.login(Account('standard_user', 'secret_sauce'))
        # (LoginPage(self.browser)).login(Account('standard_user', 'secret_sauce'))

if __name__ == "__main__":
    unittest.main()
