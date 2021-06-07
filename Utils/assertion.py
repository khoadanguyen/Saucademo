import unittest

class Assertion(unittest.TestCase):
    def assert_check_summary(self, expected_checkout_summary, actual_checkout_summary):
        self.assertEqual(expected_checkout_summary.paymentInfo, actual_checkout_summary.paymentInfo)
        self.assertEqual(expected_checkout_summary.shippingInfo, actual_checkout_summary.shippingInfo)
        self.assertEqual(expected_checkout_summary.subTotal, actual_checkout_summary.subTotal)
        self.assertEqual(expected_checkout_summary.tax, actual_checkout_summary.tax)
        self.assertEqual(expected_checkout_summary.total, actual_checkout_summary.total)

    def assert_product(self, expected_product, actual_product):
        self.assertEqual(expected_product.title, actual_product.title)
        self.assertEqual(expected_product.description, actual_product.description)
        self.assertEqual(expected_product.price, actual_product.price)
        self.assertEqual(expected_product.quantity, actual_product.quantity)
