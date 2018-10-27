# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname", nickname="test nickname", title="test title",
                                   company="test company", address="test address", homephone="123", mobilephone="123", workphone="123", fax="123", email1="test email1", email2="test email2",
                                   email3="test email3", homepage="test homepage", address2="test address", phone2="1234", notes="test notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    old_contacts[0:1] == new_contacts


