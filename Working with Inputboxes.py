from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

url="https://www.myntra.com/"
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get(url)
driver.maximize_window()
#Number of search elements present on web page
X=driver.find_elements_by_class_name("desktop-searchBar")
print(len(X))

# How to get the status of the search the field
Y=driver.find_element_by_class_name("desktop-searchBar")
print(Y.is_enabled())
print(Y.is_displayed())

driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("T=shirts",Keys.ENTER)
time.sleep(5)

driver.close()
