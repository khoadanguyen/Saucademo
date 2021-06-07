from Locators.checkout_steptwo_locators import CheckoutStepTwoLocators
from Objects.checkout_sumary import CheckoutSummary
from Objects.product import Product
from Pages.base_page import BasePage

import sys
sys.path.append('.')


class CheckoutStepTwoPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def get_product_info(self, index):
        title = self.get_text(CheckoutStepTwoLocators.LABEL_PRODUCT_TITLE(index))
        description = self.get_text(CheckoutStepTwoLocators.LABEL_PRODUCT_DESCRIPTION(index))
        price = self.get_text(CheckoutStepTwoLocators.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CheckoutStepTwoLocators.LABEL_PRODUCT_QUANTITY(index))
        return Product(title, description, price, quantity)

    def click_finish(self):
        self.click(CheckoutStepTwoLocators.BUTTON_FINISH)

    def click_cancel(self):
        self.click(CheckoutStepTwoLocators.BUTTON_CANCEL)

    def get_summary(self):
        payment_info = self.get_text(CheckoutStepTwoLocators.LABEL_PAYMENT_INFO)
        shipping_info = self.get_text(CheckoutStepTwoLocators.LABEL_SHIPPING_INFO)
        sub_total = self.get_text(CheckoutStepTwoLocators.LABEL_SUBTOTAL)
        tax = self.get_text(CheckoutStepTwoLocators.LABEL_TAX)
        total = self.get_text(CheckoutStepTwoLocators.LABEL_TOTAL)
        return CheckoutSummary(payment_info, shipping_info, sub_total, tax, total)

