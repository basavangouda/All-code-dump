#aleart / Confirmation.
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(5)
x=driver.switch_to.alert
#x.accept()
x.dismiss()
driver.close()




