from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url="https://www.ironspider.ca/forms/checkradio.htm"
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get(url)
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='Content']/div[1]/blockquote[1]/form/input[1]").click()
x=driver.find_element_by_xpath("//*[@id='Content']/div[1]/blockquote[1]/form/input[1]").is_selected()
print(x)
driver.refresh()
driver.close()