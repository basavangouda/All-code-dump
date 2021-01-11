from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("file:///C:/Users/Lenovo/Desktop/table.html")
driver.maximize_window()

rows=len(driver.find_elements_by_xpath("//tbody/tr"))
col=len(driver.find_elements_by_xpath("//tbody/tr/td"))
print(rows,col)


for r in range(1,rows+1):
    for c in range(1,col+1):
        value=driver.find_element_by_xpath("//tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="  ")
    print()

"""try:
            values = driver.find_element_by_xpath("(//tbody/tr[" + str(r) + "]/td[" + str(c) + "])").text
        except Exception:
            print("Hi")
            print(values, end="     ")
    print() """


