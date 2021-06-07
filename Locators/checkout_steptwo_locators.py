from selenium.webdriver.common.by import By

class CheckoutStepTwoLocators(object):
    BUTTON_FINISH = (By.ID, 'finish')
    BUTTON_CANCEL = (By.ID, 'cancel')
    LABEL_PAYMENT_INFO = (By.XPATH, "//div[@class='summary_value_label'][1]")
    LABEL_SHIPPING_INFO = (By.XPATH, "//div[@class='summary_value_label'][2]")
    LABEL_SUBTOTAL = (By.CLASS_NAME, 'summary_subtotal_label')
    LABEL_TAX = (By.CLASS_NAME, 'summary_tax_label')
    LABEL_TOTAL = (By.CLASS_NAME, 'summary_total_label')

    PART1 = "//*[@class='cart_item']["

    def LABEL_PRODUCT_TITLE(index):
        PART2 = "]//*[@class='inventory_item_name']"
        return (By.XPATH, (CheckoutStepTwoLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_DESCRIPTION(index):
        PART2 = "]//*[@class='inventory_item_desc']"
        return (By.XPATH, (CheckoutStepTwoLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_PRICE(index):
        PART2 = "]//*[@class='inventory_item_price']"
        return (By.XPATH, (CheckoutStepTwoLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_QUANTITY(index):
        PART2 = "]//*[@class='cart_quantity']"
        return (By.XPATH, (CheckoutStepTwoLocators.PART1 + str(index) + PART2))
