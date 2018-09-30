# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname", nickname="test nickname", title="test title",
                                   company="test company", address="test address", homephone="123", mobilephone="123", workphone="123", fax="123", email1="test email1", email2="test email2",
                                   email3="test email3", homepage="test homepage", address2="test address", phone2="test phone home", notes="test notes"))
        app.session.logout()

if __name__ == "__main__":
    unittest.main()
