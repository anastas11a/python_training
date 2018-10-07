from model.group import Group

def test_modify_group_name(app):
    app.open_home_page()
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    app.open_home_page()
    app.group.modify_first_group(Group(header="New header"))

def test_modify_all_fields(app):
    app.open_home_page()
    app.group.modify_first_group(Group(name="group name changed", header="group header changed", footer="group footer changed"))
