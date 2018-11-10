from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test", lastname = "test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

