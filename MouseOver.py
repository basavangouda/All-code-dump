from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
#MouseOver
'''
driver.get("https://www.toolsqa.com/selenium-webdriver/mouse-hover-action/")
time.sleep(5)
driver.maximize_window()
sw=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[4]/a[1]/span[1]/span[1]")
al=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/span[1]/span[1]")
wd=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[4]/ul[1]/li[2]/a[1]/span[1]/span[1]")
fm=driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/header[1]/nav[1]/ul[1]/li[4]/ul[1]/li[3]/a[1]/span[1]/span[1]")

actions=ActionChains(driver)
actions.move_to_element(sw).move_to_element(al).move_to_element(wd).move_to_element(fm).click().perform()
time.sleep(5)'''

#Doubleclick
'''driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
e=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

actions=ActionChains(driver)
actions.double_click(e).perform()
driver.close()'''

#Rightclick
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
e=driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

actions=ActionChains(driver)
time.sleep(5)
actions.context_click(e).perform()
time.sleep(3)
driver.close()