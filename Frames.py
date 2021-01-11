from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
time.sleep(3)
driver.find_element_by_link_text("org.openqa.selenium.cli").click()
time.sleep(5)

driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame("classFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(5)
driver.switch_to.default_content()
driver.refresh()
time.sleep(5)
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Action").click()
time.sleep(3)
driver.close()