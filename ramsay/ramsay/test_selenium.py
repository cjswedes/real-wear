from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

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
        # click all category in side bar menu
        for i in range(len(selenium.find_elements_by_css_selector('a.list-group-item'))):
            selenium.find_element_by_css_selector('a.list-group-item:nth-child('+str(i+1)+')').click()
 
    def test_viewdetails_clickable(self):
        sel = self.selenium
        sel.get("http://127.0.0.1:8000/categories/")

        for r in sel.find_elements_by_class_name('viewdetails'):
            sel.execute_script("arguments[0].scrollIntoView()", r)
            # TODO: scrolling to element and wait until r is clickable
            r.click()

    def test_addtocart_clickable(self):
        sel = self.selenium
        sel.get("http://127.0.0.1:8000/categories/")

        for r in sel.find_elements_by_css_selector('#addtocart'):
            sel.execute_script("arguments[0].scrollIntoView()", r)
            r.click()
    
    def test_cart_clickable(self):
        sel = self.selenium
        sel.get("http://127.0.0.1:8000/categories")
        sel.find_element_by_id('cart').click()

    def test_cart_quantity_and_total(self):
        sel = self.selenium
        sel.get("http://127.0.0.1:8000/categories")
        # TODO: find proper way of ensuring element is clickable.
        time.sleep(3) 
        add = sel.find_element_by_css_selector('#addtocart')
        add.click()
        time.sleep(1)
        add.click()
        time.sleep(1)
        add.click()
        time.sleep(1)
        sel.find_element_by_id('cart').click()
        time.sleep(1)
        q = int(sel.find_element_by_css_selector('.cart-row > div:nth-child(2) > div:nth-child(1)').text)
        p = float(sel.find_element_by_css_selector('.cart-row > div:nth-child(2) > div:nth-child(2)').text)
        s = sel.find_element_by_css_selector('.text-danger').text
        self.assertEquals(3, q, "quantity should be 3")
        self.assertEquals(s, "$"+str(p*q), "subtotal should be $3*8.41 = $25.23")