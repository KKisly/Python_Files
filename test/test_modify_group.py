from model.group import Group
from random import randrange

def test_test_modify_group_name(app):
    #app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New Name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_test_modify_group_header(app):
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.group.retrun_to_groups_page()
    #app.session.logout()