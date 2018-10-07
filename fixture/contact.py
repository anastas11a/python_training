from selenium.webdriver.support.ui import Select
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        self.open_contact_page()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
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
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("ADD_NEW").click()

    def edit_first_contact(self):
        wd = self.app.wd
        # select first contact
        self.select_first_contact()
        #click edit
        wd.find_element_by_xpath("//img[@alt='EDIT']").click()
        #edit fields
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("firstname changed")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("middlename changed")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("lastname changed")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nickname changed")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title changed")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("company changed")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("address changed")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("homephone changed")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("mobilephone changed")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("workphone changed")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("fax changed")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("email1 changed")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("email2 changed")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("email3 changed")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("homepage changed")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("1")
        wd.find_element_by_xpath("//option[@value='3']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("JANUARY")
        wd.find_element_by_xpath("//option[@value='February']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1995")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("1")
        wd.find_element_by_xpath("(//option[@value='5'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("FEBRUARY")
        wd.find_element_by_xpath("(//option[@value='February'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1990")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("address2 changed")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("phone2 changed")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("notes2 changed")
        # submit contact editing
        wd.find_element_by_name("update").click()


    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='DELETE']").click()
        wd.switch_to_alert().accept()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()




