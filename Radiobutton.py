from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

url="https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml"
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get(url)
driver.maximize_window()

#radio button
s=driver.find_elements_by_name("software")
print(len(s))
s1=driver.find_element_by_xpath("//*[@id='align']/span[4]/input").is_enabled()
print(s1)
s1=driver.find_element_by_xpath("//*[@id='align']/span[4]/input").is_selected()
print(s1)
time.sleep(5)
#explicit wait
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='align']/span[5]/input"))).click()
#driver.find_element_by_xpath("//*[@id='align']/span[4]/input").click()

try:
    WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.XPATH, "//*[@id='align']/span[4]/input']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='align']/span[4]/input']"))).click()
except TimeoutException as TT:
    isrunning = 0
    print("Exception has been thrown",str(TT))
    driver.close()

