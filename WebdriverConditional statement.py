from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.youtube.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)
#driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys("Good Morning")
#driver.find_element_by_xpath("//input[@id='search']").send_keys("Good Morning")
x=driver.find_element_by_xpath("//input[@id='search']")
print(x.is_displayed())
print(x.is_enabled())
print(x.is_selected())
time.sleep(5)
driver.close()