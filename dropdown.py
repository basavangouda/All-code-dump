from allure_commons.model2 import Attachment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
import allure
import pytest

url="https://www.globalsqa.com/demo-site/select-dropdown-menu/"
driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver.get(url)
driver.maximize_window()
e=driver.find_element_by_xpath("//*[@id='post-2646']/div[2]/div/div/div/p/selec")
allure.attach(driver.get_screenshot_as_png(),name="fail",attachment_type=Attachment.PNG)
drop=Select(e)
time.sleep(5)
drop.select_by_visible_text("India")
time.sleep(2)
drop.select_by_index(10)
time.sleep(4)
drop.select_by_value("ASM")

print(len(drop.options))

all_option=drop.options

for option in all_option:
    print(option.text)

driver.close()