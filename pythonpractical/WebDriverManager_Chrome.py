
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


import pytest
import time
import unittest


class mytest(unittest.TestCase):
    @pytest.fixture(scope="session")
    def testbasic(self):

        self = webdriver.Chrome(ChromeDriverManager().install())
        self.implicitly_wait(6)
        self.get("https://store.xkcd.com/search")
        print(self.title)
        time.sleep(5)
        self.find_element_by_id('q').send_keys('xkcd book')

        time.sleep(6)
        self.find_element_by_id('q').submit()
        time.sleep(5)
        self.quit()
