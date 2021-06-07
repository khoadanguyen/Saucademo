from Objects.account import Account
from Objects.product import Product
from Objects.information import Information
from Utils.utility import Utility
import sys

sys.path.append(".")

class TestData:
    BASE_URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    ACCOUNT_DATA_FILE_TXT = 'TestData/account.txt'
    CHECKOUTINFORM_DATA_FILE_TXT = 'TestData/checkoutinformation.txt'
    ACCOUNT_DATA_FILE_CSV = 'TestData/account.csv'
    INFO_PRODUCT_DATA_FILE_JSON = 'TestData/products.json'

    def getAccount_txt():
        return Utility.read_txt(TestData.ACCOUNT_DATA_FILE_TXT, '\n')

    def getCheckoutInformation_txt():
         return Utility.read_txt(TestData.CHECKOUTINFORM_DATA_FILE_TXT, '\n')

    def getAccount_csv():
        data = []
        for d in Utility.read_csv(TestData.ACCOUNT_DATA_FILE_CSV):
            account = Account(d[0].split('|')[0].strip(), d[0].split('|')[1].strip())
            data.append(account)

        return data

    def getProductInfo_json():
        products = []
        for item in Utility.read_json(TestData.INFO_PRODUCT_DATA_FILE_JSON)['products']:
            product = Product(item['name'], item['desc'], item['price'])
            products.append(product)
        return products



    