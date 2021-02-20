from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import time


class mytest():
  
  
  def testbasic(self):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in/")
    print(driver.title)
    time.sleep(5)
    driver.quit()
