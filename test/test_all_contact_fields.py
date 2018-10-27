import re
from random import randrange

def test_all_fields_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_phone_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_email_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname


def merge_phones_like_on_phone_page(contact):
    return "\n".join(filter(lambda x: x != "",
    map(lambda x: clear(x),
        filter(lambda x: x is not None,
               [contact.homephone, contact.workphone, contact.mobilephone, contact.phone2]))))

def merge_emails_like_on_email_page(contact):
    return "\n".join([contact.email1, contact.email2, contact.email3])

def clear(s):
    return re.sub("[() -]", "", s)

