from selenium.webdriver.common.by import By

class CheckoutStepOneLocators(object):
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_ZIP_POSTAL_CODE = (By.ID, 'postal-code')
    BUTTON_CANCEL = (By.ID, 'cancel')
    BUTTON_CONTINUE = (By.ID, 'continue')
