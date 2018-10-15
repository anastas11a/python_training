from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = app.group.get_group_list()
    group = Group(name="test")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.contact.count()
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test", header = 'test'))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)
#    old_groups[0:1] == new_groups

#def test_modify_all_fields(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name = "test", header = 'test', footer = 'test'))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(name="group name changed", header="group header changed", footer="group footer changed"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups)  == len(new_groups)
#    old_groups[0:1] == new_groups
