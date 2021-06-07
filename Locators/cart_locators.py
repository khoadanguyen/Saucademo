from selenium.webdriver.common.by import By


class CartLocators(object):
    BUTTON_CHECKOUT = (By.ID, 'checkout')
    BUTTON_CONTINUED_SHOPPING = (By.ID, 'continue-shopping')

    PART1 = "//*[@class='cart_item']["

    def LABEL_PRODUCT_TITLE(index):
        PART2 = "]//*[@class='inventory_item_name']"
        return (By.XPATH, (CartLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_DESCRIPTION(index):
        PART2 = "]//*[@class='inventory_item_desc']"
        return (By.XPATH, (CartLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_PRICE(index):
        PART2 = "]//*[@class='inventory_item_price']"
        return (By.XPATH, (CartLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_QUANTITY(index):
        PART2 = "]//*[@class='cart_quantity']"
        return (By.XPATH, (CartLocators.PART1 + str(index) + PART2))

    def BUTTON_REMOVE(index):
        PART2 = "]//*[contains(@class,'cart_button') and text()='Remove']"
        return (By.XPATH, (CartLocators.PART1 + str(index) + PART2))
