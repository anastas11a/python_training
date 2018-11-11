from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, db):
    app.open_home_page()
    contact = db.get_contact_list()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test firstname changed"))
    group = db.get_group_list()
    if len(group) == 0:
        app.group.create(Group(name="test"))
    contact_rand = random.choice(contact)
    group_rand = random.choice(group)
    app.contact.add_contact_to_group(contact_rand.id, group_rand.id)
    assert contact_rand.id in db.get_contacts_in_group()










