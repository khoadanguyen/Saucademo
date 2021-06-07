import unittest

import sys

from Pages import checkout_stepone_page
from Pages.checkout_stepone_page import CheckoutStepOnePage

sys.path.append('.')

from Objects.account import Account
from Objects.checkout_sumary import CheckoutSummary
from Pages.cart_page import CartPage
from Pages.checkout_steptwo_page import CheckoutStepTwoPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest
from TestData.test_data import TestData
from Utils.assertion import Assertion



class Login08(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        assertion = Assertion()
        products = TestData.getProductInfo_json()

        # step 1: login
        login_page = LoginPage(self.browser)
        login_page.login(Account('standard_user', 'secret_sauce'))

        # step 2: logginer.info('xxx')
        products_page = ProductsPage(self.browser)

        for index, expected_product in enumerate(products, start=1):
            assertion.assert_product(expected_product, products_page.get_product_info(index))

        for i in range(1,7):
            products_page.addtocart_button(i)
            products_page.get_shopping_cart_badge()
            # products_page.remove_product_button(i)
            products_page.get_product_info(i)

        products_page.click_shopping_cart_link()
        cart_page = CartPage(self.browser)
        products1 = []
        for i in range(1, 7):
            products1.append(cart_page.get_product_info(i))
            assertion.assert_product(products[i-1], cart_page.get_product_info(i))

        cart_page.click_checkout_product()
        #Question????
        checkout_stepone_page = CheckoutStepOnePage(self.browser)
        checkout_stepone_page.input_checkout_info('Khoa', 'Nguyen', '111111')
        checkout_stepone_page.click_continue_button()

        checkout_steptwo_page = CheckoutStepTwoPage(self.browser)
        products2 = []

        for i in range(0, 6):
            products2.append(checkout_steptwo_page.get_product_info(i+1))
            assertion.assert_product(products1[i], products2[i])

        expected_checkout_summary = CheckoutSummary('SauceCard #31337', 'FREE PONY EXPRESS DELIVERY!', 'Item total: $129.94', 'Tax: $10.40', 'Total: $140.34')

        assertion.assert_check_summary(expected_checkout_summary,checkout_steptwo_page.get_summary())
        # assert get_summary

        checkout_steptwo_page.click_finish()

    pass

if __name__ == "__main__":
    unittest.main()
