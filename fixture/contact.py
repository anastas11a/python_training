
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        self.open_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("ADD_NEW").click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.click_edit_contact_by_index(index)
        #edit fields
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.click_edit_contact_by_id(id)
        #edit fields
        self.fill_contact_form(contact)
        # submit contact editing
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def click_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='EDIT']")[index].click()

    def click_edit_contact_by_id(self, id):
        wd = self.app.wd
        row = wd.find_element_by_xpath("//input[@value='%s']/../.." % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='DELETE']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(5)
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='DELETE']").click()
        wd.switch_to_alert().accept()
        wd.implicitly_wait(5)
        self.contact_cache = None


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cell = element.find_elements_by_tag_name("td")
                firstname = cell[2].text
                lastname = cell[1].text
                address = cell[3].text
                all_emails = cell[4].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cell[5].text
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, id=id, all_phones_from_home_page = all_phones,
                                                  address=address, all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2, address = address, email1=email1, email2=email2, email3=email3)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone2=phone2)

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.select_contact_by_id(contact_id)
        self.select_group_by_id(group_id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='% s'])[2]" % group_id).click()
        wd.find_element_by_name("add").click()
        self.app.open_home_page()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % id).click()

    def open_contacts_in_group(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[@value='%s']" % group_id).click()

    def del_contact_from_group(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//*[@name='remove']").click()

    def view_all_contacts(self):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[2]").click()

