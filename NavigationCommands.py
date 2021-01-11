from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.youtube.com/")
print(driver.title)
time.sleep(5)
driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
driver.close()

