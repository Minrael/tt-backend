class SeleniumTests(SeleniumTestCase):
  def test_main(self):
  self.webdriver.find_element_by_xpath().click()
  elem = self.webdriver.find_element_by_id('blog-create-blog-button')
  assert elem is not None

  
