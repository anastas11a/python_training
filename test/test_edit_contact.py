from model.contact import Contact
from random import randrange

def test_edit_first_contact(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test firstname changed"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="test firstname changed", middlename="test middlename changed", lastname="test lastname changed")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
