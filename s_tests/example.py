import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestChatList(unittest.TestCase):

  def test_list(self):
    self.driver = webdriver.Chrome("C:/home/maria/Projects/tt-backend/driverChrom/chromedriver.exe")
    self.driver.get("http://127.0.0.1:3000")
    elem = driver.find_element_by_xpath('//*[@id="linkChat"]').click()

#assert "Python" in driver.title
#elem = driver.find_element_by_name("")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
