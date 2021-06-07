from Locators.products_locators import ProductsLocators
from Objects.product import Product
from Pages.base_page import BasePage

import sys
sys.path.append('.')


class ProductsPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def does_product_header_exist(self):
        return self.is_displayed(ProductsLocators.LABEL_PRODUCTS)

    def addtocart_button(self, index):
        self.click(ProductsLocators.BUTTON_ADDTOCARD(index))

    def remove_product_button(self, index):
        self.click(ProductsLocators.BUTTON_REMOVE(index))

    def get_product_info(self, index):
        title = self.get_text(ProductsLocators.LABEL_PRODUCT_TITLE(index))
        description = self.get_text(ProductsLocators.LABEL_PRODUCT_DESCRIPTION(index))
        price = self.get_text(ProductsLocators.LABEL_PRODUCT_PRICE(index))
        return Product(title, description, price)

    def get_shopping_cart_badge(self):
        return self.get_text(ProductsLocators.LABEL_SHOPPING_CART_BADGE)

    def click_shopping_cart_link(self):
        self.click(ProductsLocators.LINK_SHOPPING_CART)
