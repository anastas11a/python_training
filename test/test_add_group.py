# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
        app.open_home_page()
        app.group.create(Group(name="test", header="test", footer="test"))

def test_add_empty_group(app):
        app.open_home_page()
        app.group.create(Group(name="", header="", footer=""))


if __name__ == "__main__":
    unittest.main()