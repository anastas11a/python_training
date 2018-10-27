# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_numbers(maxlen):
    symbols = string.digits
    return ([random.choice(symbols) for i in range(maxlen)])

testdata = [
    Contact(firstname=random_string("fistname", 10), middlename=random_string("middlename", 5), lastname=random_string("lastname", 15),
            nickname=random_string("nickname", 7), title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 15), homephone=random_numbers(7),
            mobilephone=random_numbers(7), workphone=random_numbers(10),
            fax=random_string("fax", 10), email1=random_string("email1", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage=random_string("homepage", 10), address2=random_string("address2", 10), phone2=random_numbers(7),
            notes=random_string("notes", 10))
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)



