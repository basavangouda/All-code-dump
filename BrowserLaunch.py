from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.youtube.com/")
print(driver.title)
driver.close()

driver=webdriver.Firefox(executable_path="C:\DRIVERS\geckodriver.exe")
driver.get("https://www.youtube.com/")
print(driver.title)
driver.close()

print(" Hello Enjoy cheyandi")
driver=webdriver.Edge(executable_path="D:\Software\Drivers\platform-tools_r30.0.4-windows\msedgedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/")
print(driver.title)
driver.close()