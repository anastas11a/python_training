from model.contact import Contact
from model.group import Group
import random

def test_add_contact_in_group(app, db):
    app.open_home_page()
    contact = db.get_contact_list()
    if len(contact) == 0:
        app.contact.create(Contact(firstname = "test firstname changed"))
    group = db.get_group_list()
    if len(group) == 0:
        app.group.create(Group(name="test"))
    contact_rand = random.choice(contact)
    group_rand = random.choice(group)
    app.contact.add_contact_to_group(contact_rand.id, group_rand.id)
    l = db.get_contacts_in_group(Group(id=group_rand.id))
    assert contact_rand in l


def test_del_contact_from_group(app, db):
    app.open_home_page()
    contact = db.get_contact_list()
    if len(contact) == 0:
        app.contact.create(Contact(firstname = "test firstname changed"))
    group = db.get_group_list()
    if len(group) == 0:
        app.group.create(Group(name="test"))
    group_rand = random.choice(group)
    app.contact.open_contacts_in_group(group_rand.id)
    contacts_in_group = db.get_contacts_in_group(Group(id=group_rand.id))
    if len(contacts_in_group) == 0:
        app.contact.view_all_contacts()
        contact_rand = random.choice(contact)
        app.contact.add_contact_to_group(contact_rand.id, group_rand.id)
        app.contact.open_contacts_in_group(group_rand.id)
        db.get_contacts_in_group(Group(id=group_rand.id))
    app.contact.del_contact_from_group()
    l = db.get_contacts_in_group(Group(id=group_rand.id))
    assert contact_rand.id not in l













