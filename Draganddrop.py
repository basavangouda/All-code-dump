from selenium import webdriver
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()

s=driver.find_element_by_id("draggable")
t=driver.find_element_by_id("droppable")

actions=ActionChains(driver)
actions.drag_and_drop(s,t).perform()

driver.refresh()
driver.switch_to.frame(1)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:/Users/Lenovo/Desktop/TDPL Agreement.docx")
time.sleep(5)

driver.close()