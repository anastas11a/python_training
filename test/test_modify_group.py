from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test", header = 'test'))
    app.group.modify_first_group(Group(header="New header"))

def test_modify_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test", header = 'test', footer = 'test'))
    app.group.modify_first_group(Group(name="group name changed", header="group header changed", footer="group footer changed"))
