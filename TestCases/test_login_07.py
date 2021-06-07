import unittest
from Objects.account import Account
from Objects.checkout_sumary import CheckoutSummary
from Pages.cart_page import CartPage
from Pages.checkout_stepone_page import CheckoutStepOnePage
from Pages.checkout_steptwo_page import CheckoutStepTwoPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest


import sys

from TestData.test_data import TestData
from Utils.assertion import Assertion

sys.path.append('.')

class Login07(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        assertion = Assertion()
        products = TestData.getProductInfo_json()


        login_page = LoginPage(self.browser)
        login_page.login(Account('standard_user', 'secret_sauce'))

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

        checkout_stepone_page = CheckoutStepOnePage(self.browser)
        checkout_stepone_page.input_checkout_info('Dung', 'Truong', '123123')
        checkout_stepone_page.click_continue_button()

        checkout_steptwo_page = CheckoutStepTwoPage(self.browser)
        products2 = []

        for i in range(1,7):
            products2.append(checkout_steptwo_page.get_product_info(i))

        for index, expected_product in enumerate(products1, start=0):
            assertion.assert_product(expected_product, products2[index])

        expected_checkout_summary = CheckoutSummary('SauceCard #31337', 'FREE PONY EXPRESS DELIVERY!', 'Item total: $129.94', 'Tax: $10.40', 'Total: $140.34')

        assertion.assert_check_summary(expected_checkout_summary,checkout_steptwo_page.get_summary())
        # assert get_summary

        checkout_steptwo_page.click_finish()

    pass

if __name__ == "__main__":
    unittest.main()
