import os
import sys

sys.path.append(".")
import unittest

from Utils.HTMLTestRunner import *
from TestCases.test_login_01 import Login01
from TestCases.test_login_02 import Login02
from TestCases.test_login_03 import Login03
from TestCases.test_login_04 import Login04

# get all tests from Login class
login1 = unittest.TestLoader().loadTestsFromTestCase(Login01)
login2 = unittest.TestLoader().loadTestsFromTestCase(Login02)
login3 = unittest.TestLoader().loadTestsFromTestCase(Login03)
login4 = unittest.TestLoader().loadTestsFromTestCase(Login04)

# get the directory path to output report file
dir = os.getcwd()

# create a test suite
test_suite = unittest.TestSuite([login1, login2, login3, login4])

# open the report file
outfile = open(dir + "/Reports/TestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(stream=outfile, title='Sauce Demo Test Report', description='Acceptance Tests')

# run the suite using HTMLTestRunner
runner.run(test_suite)
outfile.close()
