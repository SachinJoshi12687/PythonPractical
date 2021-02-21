from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time
import unittest


class mytest(unittest.TestCase):

    def testbasic(self):

        self = webdriver.Chrome(ChromeDriverManager().install())
        self.implicitly_wait(5)
        driver.get("https://www.amazon.in/")
        print(driver.title)
        time.sleep(5)
        print("hello this is pass")
        driver.quit()
