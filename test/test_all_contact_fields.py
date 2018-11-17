import re
from random import randrange
from model.contact import Contact

def test_all_fields_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_phone_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_email_page(contact_from_edit_page)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def test_ui_matches_db(app, db):
    contact_from_db = db.get_contact_list()
    contact_from_home_page = app.contact.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)
    emails_phones_from_db = []
    emails_phones_from_ui = []
    for contact_db in contact_from_db:
        all_phones_from_home_page = merge_phones_like_on_phone_page(contact_db)
        all_emails_from_home_page = merge_emails_like_on_email_page(contact_db)
        emails_phones_from_db.append(all_phones_from_home_page)
        emails_phones_from_db.append(all_emails_from_home_page)
    for contact_ui in contact_from_home_page:
        emails_phones_from_ui.append(contact_ui.all_phones_from_home_page)
        emails_phones_from_ui.append(contact_ui.all_emails_from_home_page)
    assert sorted(emails_phones_from_db) == sorted(emails_phones_from_ui)


def merge_phones_like_on_phone_page(contact):
    return "\n".join(filter(lambda y: y != "",
                            map(lambda x: clear(x),
                                filter(lambda z: z is not None,
               [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))

def merge_emails_like_on_email_page(contact):
    return "\n".join(filter(lambda y: y != "",
                            map(lambda x: clear(x),
                                filter(lambda z: z is not None,
                                       [contact.email1, contact.email2, contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)

