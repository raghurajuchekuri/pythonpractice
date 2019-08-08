from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, imaplib
from time import sleep
import HtmlTestRunner

user = "raghuc"
pwd = "new123#"
driver = webdriver.Chrome('C:/RaghuChekuri/SelmServer/chromedriver')
driver.maximize_window()
time.sleep(5)
driver.get("http://sandbox8.avangate.local/admin/")
#assert "Facebook" in driver.title
elem = driver.find_element_by_id("username")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

sleep(5)


#driver.close()
