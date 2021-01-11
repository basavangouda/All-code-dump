from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

url="https://www.globalsqa.com/demo-site/select-dropdown-menu/"
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get(url)
driver.maximize_window()
#number of links
links=driver.find_elements_by_tag_name('a')
print(len(links))
#print all links
for link in links:
    print(link.text)

#click on any link usink linked text
driver.find_element_by_link_text("Home").click()

time.sleep(5)

driver.refresh()

#using partial linked text
driver.find_element_by_partial_link_text("Global").click()

driver.close()

