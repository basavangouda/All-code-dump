from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

#Capturing all the cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#adding new cookies
cookie={'name':'mycookie','value':'12344555'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(cookies)
print(len(cookies))

#deleting cookies
driver.delete_cookie('mycookie')
time.sleep(3)
cookies=driver.get_cookies()
print(len(cookies))

#delet all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(cookies)
print(len(cookies))