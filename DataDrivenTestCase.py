from Selenium import XLutilities
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

path="C:\\Users\\Lenovo\\Desktop\\PythonPractice\\XYZ.xlsx"
rows=XLutilities.getRowCount(path,"Sheet3")

for r in range(2,rows+1):
    username=XLutilities.ReadData(path,"Sheet3",r,1)
    password=XLutilities.ReadData(path,'Sheet3',r,2)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath("//i[contains(text(),'Login')]").click()
    time.sleep(10)
    driver.find_element_by_xpath("//i[contains(text(),'Logout')]").click()
    time.sleep(10)


    if driver.title == "The Internet":
        print('test passed')
        XLutilities.WriteData(path,"Sheet3",r,3,"Test Passed")
    else:
        print('Test Failed')
        XLutilities.WriteData(path,"Sheet3",r,3,'Test Failed')



