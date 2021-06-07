from selenium.webdriver.common.by import By

class ProductsLocators(object):
    """A class for products page locators. All products page locators should come here"""
    LABEL_PRODUCTS = (By.XPATH, "//span[text()='Products']")
    PART1 = "//*[@class='inventory_item']["
    LABEL_SHOPPING_CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    LINK_SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart_link')

    def LABEL_PRODUCT_TITLE(index):
        PART2 = "]//*[@class='inventory_item_name']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_DESCRIPTION(index):
        PART2 = "]//*[@class='inventory_item_desc']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_PRICE(index):
        PART2 = "]//*[@class='inventory_item_price']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))

    def BUTTON_ADDTOCARD(index):
        PART2 = "]//*[contains(@class,'btn_inventory') and text()='Add to cart']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))

    def BUTTON_REMOVE(index):
        PART2 = "]//*[contains(@class,'btn_inventory') and text()='Remove']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))

    def LABEL_PRODUCT_IMAGE(index):
        PART2 = "]//img[@class='inventory_item_img']"
        return (By.XPATH, (ProductsLocators.PART1 + str(index) + PART2))


