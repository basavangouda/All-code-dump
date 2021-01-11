from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
fp=webdriver.FirefoxProfile()


fp.set_preference("browser.helperApps.neverAsk.saveToDisk","text/pdf/word/application")
fp.set_preference("browser.download.manager.showWhenStarting", False)


'''ChromeOptions=Options()
prefs={"download.dafault_dictionary" :"\\C:\\Users\\Lenovo\\Desktop\\"}'''
#ChromeOptions.add_experimental_option("prefs",prefs)

#driver=webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\DRIVERS\geckodriver.exe")


driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(5)
#word document
driver.find_element_by_id("textbox").send_keys('textbook')
driver.find_element_by_id("createTxt").click()
time.sleep(5)

driver.find_element_by_xpath("//a[@id='link-to-download']").click()

driver.refresh()
#PDF document
driver.find_element_by_id("pdfbox").send_keys('textbook')
driver.find_element_by_id("createPdf").click()
time.sleep(5)

driver.find_element_by_id("pdf-link-to-download").click()

driver.close()
