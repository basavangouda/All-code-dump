from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

#1st Approach by pixel
driver.execute_script("window.scrollTo(0,100)")

time.sleep(5)
#second Approach

target=driver.find_element_by_xpath("//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[10]/div[1]/span[1]/span[1]/span[1]")
driver.execute_script("arguments[0].scrollIntoView();",target)

#3rd approach

driver.execute_script("window.scrollTo(0,document.body.scrollHight);")

driver.close()



