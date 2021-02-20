from selenium import werbdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
print(driver.title)
time.sleep(5)
driver.quit()
