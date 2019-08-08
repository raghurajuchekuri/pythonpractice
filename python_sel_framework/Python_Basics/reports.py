from selenium import webdriver
import unittest
import HTMLTestRunner

class LoginTest(unittest.TestCase):

def setUp(self):   
    self.driver = webdriver.Chrome('C:/RaghuChekuri/SelmServer/chromedriver')
    self.driver.get("http://google.com/")

def testPythonScript(self):
    driver=self.driver
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.get_screenshot_as_file(../Screenshots/ss1.png)
    driver.find_element_by_xpath("(//a[contains(@href,'contact-us')])[1]").click()
    driver.find_element_by_name("name").send_keys("shubham")
    driver.find_element_by_id("contactemail").send_keys("shubham.xyz@abc.com")
    driver.find_element_by_css_selector("#contact_form > div:nth-child(3) > div:nth-child(3) > input").send_keys(
        "389198318312")
    driver.find_element_by_name("company").send_keys("myname")
    driver.get_screenshot_as_file(../Screenshots/contactus.png)
    print driver.title
    assert "Hello" in driver.title
    print "execution ends"

def testPythonFailScript(self):
    driver=self.driver
    driver.find_element_by_name("notExist").send_keys("done")

    def tearDown(self):
        driver = self.driver
        driver.quit();

if __name__ == "__main__":
    HTMLTestRunner.main()