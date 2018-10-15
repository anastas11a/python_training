from model.contact import Contact

def test_edit_first_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="test firstname changed", middlename="test middlename changed", lastname="test lastname changed", nickname="test nickname changed", title="test title changed",
                                   company="test company changed", address="test address changed", homephone="123 changed", mobilephone="123 changed", workphone="123", fax="123 changed", email1="test email1 changed", email2="test email2 changed",
                                   email3="test email3 changed", homepage="test homepage changed", address2="test address changed", phone2="test phone home changed", notes="test notes changed"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0:1] == new_contacts