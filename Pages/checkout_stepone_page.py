import sys

sys.path.append('.')


from Locators.checkout_stepone_locators import CheckoutStepOneLocators
from Pages.base_page import BasePage


class CheckoutStepOnePage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def input_checkout_info(self, firstname, lastname, zipcode):
        self.send_keys(CheckoutStepOneLocators.INPUT_FIRSTNAME, firstname)
        self.send_keys(CheckoutStepOneLocators.INPUT_LASTNAME, lastname)
        self.send_keys(CheckoutStepOneLocators.INPUT_ZIP_POSTAL_CODE, zipcode)

    def click_continue_button(self):
        self.click(CheckoutStepOneLocators.BUTTON_CONTINUE)

    def click_cancel_button(self):
        self.click(CheckoutStepOneLocators.BUTTON_CANCEL)
