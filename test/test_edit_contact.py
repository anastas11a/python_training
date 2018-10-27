from model.contact import Contact
from random import randrange

def test_edit_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test firstname changed"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="test firstname changed", middlename="test middlename changed", lastname="test lastname changed", nickname="test nickname changed", title="test title changed",
                                   company="test company changed", address="test address changed", homephone="4321", mobilephone="4321", workphone="4321", fax="123 changed", email1="test email1 changed", email2="test email2 changed",
                                   email3="test email3 changed", homepage="test homepage changed", address2="test address changed", phone2="4321", notes="test notes changed")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    old_contacts[index:index+1] == new_contacts