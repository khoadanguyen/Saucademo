import os
import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        browser_name = self.get_browser(self)
        self.browser = self.start_browser(browser_name)
        self.browser.maximize_window()

    @classmethod
    def tearDown(self):
        try:
            self.browser.close()
        except Exception:
            self.browser.quit()
            pass

    def start_browser(name='chrome'):
        """
        browsers，"firefox", "chrome", "ie", "phantomjs"
        """
        try:
            if name.lower() == 'firefox' or name.lower() == 'ff':
                return webdriver.Firefox()
            elif name.lower() == 'chrome':
                return webdriver.Chrome()
            elif name.lower() == 'edge':
                return webdriver.MicrosoftEdge()
            elif name.lower() == 'phantomjs':
                return webdriver.PhantomJS()
            else:
                return webdriver.Chrome()
        except Exception as msg:
            print("message: %s" % str(msg))

    def get_browser(self):
        try:
            return os.environ['BROWSER']
        except KeyError:
            return 'chrome'

