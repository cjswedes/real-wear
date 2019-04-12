
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MySeleniumTests(LiveServerTestCase):
    def setUp(self):
        # Firefox latest geckodriver not working with 66.0.2
        # Using Chromedriver 73.0.3683.103 
        self.selenium = webdriver.Chrome()
        super(MySeleniumTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumTests, self).tearDown()

    def test_categories_clickable(self):
        selenium = self.selenium
        #Opening the link we want to test
        print(
            '%s%s' % (self.live_server_url,  "/admin/")
        )
        selenium.get(
            '%s%s' % ("http://127.0.0.1:8000",  "/categories/")
        )
        
        # Category side bar menu
        # @Yu-lin, all failed. I dont believe these are proper css selector?
        '''
        self.assertTrue(selenium.find_elements_by_css_selector('#prodlist'))
        self.assertTrue(selenium.find_elements_by_css_selector('#craft'))
        self.assertTrue(selenium.find_elements_by_css_selector('#tool'))
        self.assertTrue(selenium.find_elements_by_css_selector('#agricultural'))
        self.assertTrue(selenium.find_elements_by_css_selector('#textile'))
        self.assertTrue(selenium.find_elements_by_css_selector('#grocery'))
        self.assertTrue(selenium.find_elements_by_css_selector('#foodways'))
        self.assertTrue(selenium.find_elements_by_css_selector('#footwear'))
        '''
        
        viewall = selenium.find_element_by_css_selector('a.list-group-item:nth-child(1)').click()
        craft = selenium.find_element_by_css_selector('a.list-group-item:nth-child(2)').click()
        argi = selenium.find_element_by_css_selector('a.list-group-item:nth-child(3)').click()
        tool = selenium.find_element_by_css_selector('a.list-group-item:nth-child(4)').click()
        textile = selenium.find_element_by_css_selector('a.list-group-item:nth-child(5)').click()
        grocery = selenium.find_element_by_css_selector('a.list-group-item:nth-child(6)').click()
        foodway = selenium.find_element_by_css_selector('a.list-group-item:nth-child(7)').click()
        ftware = selenium.find_element_by_css_selector('a.list-group-item:nth-child(8)').click()

    # def test_addtocart(self):
        # sel = self.selenium
        # self.assertTrue(sel.find_elements_by_css_selector('.show'))