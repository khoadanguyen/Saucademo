from Objects.product import Product
from Pages.base_page import BasePage
from Locators.cart_locators import CartLocators

import sys
sys.path.append('.')


class CartPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def get_product_info(self, index):
        title = self.get_text(CartLocators.LABEL_PRODUCT_TITLE(index))
        description = self.get_text(CartLocators.LABEL_PRODUCT_DESCRIPTION(index))
        price = self.get_text(CartLocators.LABEL_PRODUCT_PRICE(index))
        quantity = self.get_text(CartLocators.LABEL_PRODUCT_QUANTITY(index))
        return Product(title, description, price, quantity)

    def click_remove_product(self, index):
        self.click(CartLocators.BUTTON_REMOVE(index))

    def click_checkout_product(self):
        self.click(CartLocators.BUTTON_CHECKOUT)

    def click_continued_shopping(self):
        self.click(CartLocators.BUTTON_CONTINUED_SHOPPING)
