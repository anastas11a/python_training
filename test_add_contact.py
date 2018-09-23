# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("LOGOUT").click()

    def create_contact(self, wd):
        # init contact creation
        wd.find_element_by_link_text("ADD_NEW").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("test firstname")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("test middlename")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("test lastname")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("test nickname")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("test title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("test company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("test address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("123")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("123")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("123")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("123")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("test email1")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("test email2")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("test email3")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("test homepage")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='1']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("JANUARY")
        wd.find_element_by_xpath("//option[@value='January']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("(//option[@value='1'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("FEBRUARY")
        wd.find_element_by_xpath("(//option[@value='February'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2000")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("test address")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("test phone home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("test notes")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='LOGIN']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
