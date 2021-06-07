from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage(object):
    """This is the parent page"""

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 60
        self.browser.implicitly_wait(60)
        self.browser.maximize_window()
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    def get(self, url):
        message = "Navigate to the url '{}'"
        logging.info(message.format(url))
        self.browser.get(url)

    def send_keys(self, by_locator, text):
        message = "Enter value '{}' into the element with locator '{}'"
        logging.info(message.format(text, ','.join(by_locator)))

        element = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(by_locator))
        element.clear()
        return element.send_keys(text)

    def click(self, by_locator):
        message = "Click on the element with locator '{}'"
        logging.info(message.format(','.join(by_locator)))
        WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

    def is_displayed(self, by_locator):
        message = "Check the element with the locator '{}' is displayed or not"
        logging.info(message.format(','.join(by_locator)))
        try:
            element = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False

    def get_text(self, by_locator):
        try:
            element = WebDriverWait(self.browser, self.timeout).until(EC.visibility_of_element_located(by_locator))
            message = "Get text '{}' from the element with the locator '{}'"
            _text = element.text
            logging.info(message.format(_text, ','.join(by_locator)))
            return _text
        except:
            return None
