import time
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

#1
driver.save_screenshot('basava.jpj')
driver.refresh()
driver.get_screenshot_as_file("xyz.png")
driver.get_screenshot_as_png()