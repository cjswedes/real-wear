
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(MySeleniumTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumTests, self).tearDown()

    def test_productList(self):
        selenium = self.selenium
        #Opening the link we want to test
        print(
            '%s%s' % (self.live_server_url,  "/admin/")
        )
        selenium.get(
            '%s%s' % ("http://127.0.0.1:8000",  "/categories/")
        )
        
        self.assertTrue(selenium.find_elements_by_css_selector('#prodlist'))
        self.assertTrue(selenium.find_elements_by_css_selector('#craft'))
        self.assertTrue(selenium.find_elements_by_css_selector('#tool'))
        self.assertTrue(selenium.find_elements_by_css_selector('#agricultural'))
        self.assertTrue(selenium.find_elements_by_css_selector('#textile'))
        self.assertTrue(selenium.find_elements_by_css_selector('#grocery'))
        self.assertTrue(selenium.find_elements_by_css_selector('#foodways'))
        self.assertTrue(selenium.find_elements_by_css_selector('#footwear'))