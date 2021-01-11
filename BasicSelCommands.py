from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.youtube.com/")
#To fetch the webpage title
print(driver.title)

#How to get the current Url
print(driver.current_url)
time.sleep(5)
driver.close()