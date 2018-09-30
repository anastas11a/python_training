# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(firstname="test firstname", middlename="test middlename", lastname="test lastname", nickname="test nickname", title="test title",
                            company="test company", address="test address", homephone="123", mobilephone="123", workphone="123", fax="123", email1="test email1", email2="test email2",
                            email3="test email3", homepage="test homepage", address2="test address", phone2="test phone home", notes="test notes"))
        app.logout()

if __name__ == "__main__":
    unittest.main()
