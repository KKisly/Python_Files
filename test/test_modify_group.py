from model.group import Group

def test_test_modify_group_name(app):
    #app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group(name="New Name")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    #app.group.retrun_to_groups_page()
    #app.session.logout()


def test_test_modify_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    #app.group.retrun_to_groups_page()
    #app.session.logout()