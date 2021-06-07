import unittest
from Objects.account import Account
from Pages.cart_page import CartPage
from Pages.checkout_stepone_page import CheckoutStepOnePage
from Pages.checkout_steptwo_page import CheckoutStepTwoPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest

import sys

from TestData.test_data import TestData

sys.path.append('.')

class Login05(BaseTest):

    @classmethod
    def setUp(self):
        super().setUp()

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product(self):
        # step 1: Login
        login_page = LoginPage(self.browser)
        login_page.login(Account('standard_user', 'secret_sauce'))

        # step 2: Compare data with JSON file
        products_page = ProductsPage(self.browser)
        products = TestData.getInfoProduct_json()
        for index, expected_product in enumerate(products, start=1):
            self.assertEqual(expected_product.title, products_page.get_product_info(index).title)
            self.assertEqual(expected_product.description, products_page.get_product_info(index).description)
            self.assertEqual(expected_product.price, products_page.get_product_info(index).price)

        # step 3: Add Products to cart
        for i in range(1, 7):
            products_page.addtocart_button(i)

            # Get Badge icon & product info
            products_page.get_shooping_cart_badge()
            products_page.get_product_info(i)

        # step 4: Click Shopping Cart icon
        products_page.click_shopping_cart_link()

        # step 5: Get Product Info on Cart Page
        cart_page = CartPage(self.browser)
        products1 = []

        for i in range(1, 7):
            products1.append(cart_page.get_product_info(i))


        for index, expected_product in enumerate(products, start=1):
            self.assertEqual(expected_product.title, cart_page.get_product_info(index).title)
            self.assertEqual(expected_product.description, cart_page.get_product_info(index).description)
            self.assertEqual(expected_product.price, cart_page.get_product_info(index).price)
            self.assertEqual(expected_product.quantity, cart_page.get_product_info(index).quantity)

        cart_page.click_checkout_product()

        # step 6: Fill in Checkout form
        checkout_stepone_page = CheckoutStepOnePage(self.browser)
        checkout_stepone_page.input_checkout_info("Khoa", "abc", "123")
        checkout_stepone_page.click_continue()

        # step 7:
        checkout_steptwo_page = CheckoutStepTwoPage(self.browser)
        product2 = []
        for i in range (1, 7):
            product2.append(checkout_steptwo_page.get_product_info(i))

        for index, expected_product in enumerate(products1, start=0):
            self.assertEqual(expected_product.title, product2[i].title)
            self.assertEqual(expected_product.description, product2[i].description)
            self.assertEqual(expected_product.price, product2[i].price)
            self.assertEqual(expected_product.quantity, product2[i].quantity)

        checkout_steptwo_page.click_finish_product()
        pass


if __name__ == "__main__":
    unittest.main()