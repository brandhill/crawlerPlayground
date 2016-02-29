# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class AgodaCrawler(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.agoda.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_agoda_crawler(self):
        driver = self.driver
        driver.get(self.base_url + "/zh-tw/index.html?type=1&device=c&network=g&adid=71362113032&rand=12134790519668366478&expid=4557709&adpos=1t1&site_id=1618671;&tag=5b307967-f548-4147-81f5-d6be9ffc4bf5&url=http://www.agoda.com/zh-tw/index.html&gclid=COailLOr1scCFY6SvQod6DsPLA&cklg=1")
        driver.find_element_by_id("SearchInput").clear()
        driver.find_element_by_id("SearchInput").send_keys(u"東京")
        driver.find_element_by_id("search-submit").click()
        driver.find_element_by_link_text(u"下一頁").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def getTitle(self):
        return "dummyTitle"

    def getToken(self):
        return "dummyToken"

if __name__ == "__main__":
    unittest.main()
