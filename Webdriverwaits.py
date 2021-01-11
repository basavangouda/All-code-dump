from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#Implicit wait
'''driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@id='email']").send_keys("bgowda.tyss@gmail.com")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("abc9741090584@J")
driver.find_element_by_name("login").click()
driver.quit()'''

#explicit wait
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get('https://www.expedia.co.in/')
driver.maximize_window()
driver.find_element_by_xpath("//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/figure[1]/div[3]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/figure[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").send_keys("SFO")

time.sleep(5)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/figure[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]").send_keys("BOS")
driver.find_element_by_xpath("//button[@id='d1-btn']").send_keys("14/11/2020")
#driver.find_element_by_xpath("//*[@id='d2-btn']").send_keys("20-11-2020")
time.sleep(10)

C="//button[@class='uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary']"
#using Java script exicutor
#element = driver.find_element_by_xpath(C)
#driver.execute_script("arguments[0].click();", element)
wait=WebDriverWait(driver,10)
e=wait.until(EC.element_to_be_clickable((By.XPATH,C)))
driver.execute_script("arguments[0].click();", e)












